import copy
import os 

from prefect import Flow, task
from prefect import Parameter

from lume_services.services.scheduling.prefect.results import DBResult
from lume_services.tasks import configure_services, SaveDBResult, LoadDBResult, LoadFile, SaveFile
from prefect.storage import Module

from {{ cookiecutter.project_slug }}.model import {{ cookiecutter.model_class }}
from {{ cookiecutter.project_slug }} import INPUT_VARIABLES, OUTPUT_VARIABLES





@task(log_stdout=True)
def format_input_vars(**input_variable_parameter_dict):
    """Assumes input_var_rep is a dict mapping var_name to value. The input variables 
    have already been instantiated, so here we assign their values.

    """
    # use deepcopy because model references INPUT_VARIABLES/OUTPUT_VARIABLES
    input_variables = copy.deepcopy(INPUT_VARIABLES)

    for var_name in INPUT_VARIABLES:
        input_variables[var_name].value = input_variable_parameter_dict[var_name]

    return input_variables


@task(log_stdout=True)
def preprocessing_task():
    ...



@task(log_stdout=True)
def format_file(results):
    ...





@task(log_stdout=True)
def predict(formatted_input_vars, settings):

    model = {{ cookiecutter.model_class }}(**settings)

    return model.execute(formatted_input_vars)


with Flow(
        "{{ cookiecutter.repo_name }}",
        storage=Module(__name__)
    ) as flow:

    # Configure services must run if using LUME-services
    # see https://slaclab.github.io/lume-services/workflows/#configuring-flows-for-use-with-lume-services
    configure_services()


    # Set up input variables 
    input_variable_parameter_dict = {
        var_name: Parameter(var_name, default=var.default) for var, var_name in INPUT_VARIABLES.items()
    }


    # add misc other variables
    output_filename = Parameter("filename")


    # MOVE TO LUME-SERVICES
    formatted_input_vars = format_input_vars(**input_variable_parameter_dict)


    # This is where preprocessing would be applied
    # formatted_input_vars = preprocessing_task()


   # db_result = LoadDBResult().run(
   #     previous_flow_run_id,
   #     attribute="outputs",
   #     attribute_index=["output1"],
   #     results_db_service=results_db_service,
   # )



    # MOVE TO LUME-SERVICES
    formatted_input_vars = format_input_vars(**input_variable_parameter_dict)


    model_settings = Parameter("model_settings", default=None)

    # Define any extra parameters here...

    # Define flow DAG
    # Can expand this for extended functionality
    formatted_input_vars = format_input_vars(**input_variable_parameter_dict)
    model_output = model_predict(formatted_input_vars, model_settings)
    store_db_results(model_output)
    store_result_artifact(model_output)


def get_flow():
    return flow
