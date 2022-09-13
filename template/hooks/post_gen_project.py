import shutil
import logging
import os
from subprocess import Popen

from pytablewriter import MarkdownTableWriter
from lume_model.utils import variables_from_yaml
from lume_model.variables import Variable, ArrayVariable, TableVariable, ScalarVariable, ImageVariable
import logging


logger = logging.getLogger(__name__)


def get_var_type(variable: Variable):

    type_str = None
    if isinstance(variable, (ArrayVariable,)):
        type_str = "array"

    elif isinstance(variable, (ScalarVariable,)):
        type_str = "scalar"

    elif isinstance(variable, (ImageVariable,)):
        type_str = "image"

    elif isinstance(variable, (TableVariable,)):
        type_str = "table"

    else:
        raise ValueError("Variable type not found: %s", variable.__name__)

    return type_str


class LUMEModelVariableProcessor():
    """Class used for processing LUME-model variables into template content and
    organized step by step.

    Attributes:
        filename (str): Filename to load with variable spec.
        input_variables (dict): Dictionary of input variable name : variable
        output_variables (dict): Dictionary of input variable name : variable

    """


    def __init__(self, filename: str) -> None:
        """
        Args:
            filename (str): Filename from which to load LUME-model variables.
        """
        self.filename = filename
        self.input_variables = None
        self.output_variables = None

        try:
            with open(filename, "r") as f:
                self.input_variables, self.output_variables = variables_from_yaml(f)

        except Exception as e:
            logger.exception(e)
            raise e

    def build_variable_table(self):
        input_table = None
        output_table=None

        input_var_matrix = [[var.name, get_var_type(var), var.default] for var in self.input_variables.values()]

        if len(self.input_variables) > 0:

            if len(self.input_variables) == 1:
                var = list(self.input_variables.values())[0]
                output_var_matrix = [var.name, get_var_type(var), var.default]
            
            else:
                output_var_matrix = [[var.name, get_var_type(var), var.default] for var in self.input_variables.values()]


            input_variable_table_writer =  MarkdownTableWriter(
            table_name="input_variables",
            headers=["variable name", "type", "default"],
            value_matrix=input_var_matrix,
            )

            input_table = input_variable_table_writer.dumps()

        if len(self.output_variables) > 0:

            if len(self.output_variables) == 1:
                var = list(self.output_variables.values())[0]
                output_var_matrix = [var.name, get_var_type(var)]
            
            else:
                output_var_matrix = [[var.name, get_var_type(var)] for var in self.output_variables.values()]


            output_variable_table_writer =  MarkdownTableWriter(
                table_name="output_variables",
                headers=["variable_name", "type"],
                value_matrix=output_var_matrix,
            )

            output_table = output_variable_table_writer.dumps()

        return input_table, output_table


# YAML configuration
#####################
cwd = os.getcwd()

# get absolute path
lume_model_config_yaml = os.path.abspath("{{ cookiecutter.model_config_file }}")

# move model config file to files
if not os.path.isfile(lume_model_config_yaml):
    logger.error("No such file %s", lume_model_config_yaml)
    raise FileNotFoundError(lume_model_config_yaml)

# Add variable file to /files subdir
yaml_dest =  f"{cwd}/{{ cookiecutter.package }}/files/variables.yml"
shutil.copy(lume_model_config_yaml, yaml_dest)


# compose readme variable tables
processor = LUMEModelVariableProcessor(lume_model_config_yaml)
input_table, output_table = processor.build_variable_table()


# compose readme variable tables
logger.info("Placing input/output variable tables in README.")
with open(f'{cwd}/README.md', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('<<INPUT_VARIABLES>>', input_table)
filedata = filedata.replace('<<OUTPUT_VARIABLES>>', output_table)

# Write the file out again
with open(f'{cwd}/README.md', 'w') as file:
  file.write(filedata)

logger.info("Finished placing input/output tables in README.")


# initialize git
git_proc = Popen(["git", "init", str(cwd)])
git_proc.wait()
git_add_proc = Popen(["git", "add", "."])
git_add_proc.wait()
git_commit_proc = Popen(["git", "commit", "-a", "-m", "Initial Cookiecutter commit."])
git_commit_proc.wait()

# versioneer
versioneer_proc = Popen(["versioneer", "install", str(cwd)])