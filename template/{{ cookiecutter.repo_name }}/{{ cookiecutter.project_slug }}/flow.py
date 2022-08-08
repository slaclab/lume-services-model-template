from prefect import Flow, task
from prefect import Parameter

from lume_services.services.scheduling.prefect.results import DBResult
from prefect.storage import Module
import os

from {{ cookiecutter.project_slug }}.model import {{ cookiecutter.model_class }}
from {{ cookiecutter.project_slug }} import INPUT_VARIABLES, OUTPUT_VARIABLES, service_container

import copy


@task(log_stdout=True)
def format_input_vars(**input_variable_parameter_dict):
    """Assumes input_var_rep is a dict mapping var_name to value. The input variables 
    have already been instantiated, so here we assign their values.

    """
    input_variables = copy.deepcopy(INPUT_VARIABLES)

    for var_name in INPUT_VARIABLES:
        input_variables[var_name].value = input_variable_parameter_dict[var_name]

    return input_variables


@task(log_stdout=True)
def predict(formatted_input_vars, settings):

    model = {{ cookiecutter.model_class }}(**settings)

    return model.execute(formatted_input_vars)


with Flow(
        {{ cookiecutter.repo_name }},
        storage=Module(__name__)
    ) as flow:


    # Configure LUME-services services



    input_variable_parameter_dict = {
        var_name: Parameter(var_name, default=var.default) for var, var_name in INPUT_VARIABLES.items()
    }


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
