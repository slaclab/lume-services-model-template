import copy
from lume_model.models import BaseModel
from {{ cookiecutter.project_slug }} import INPUT_VARIABLES, OUTPUT_VARIABLES

class {{ cookiecutter.model_class }}(BaseModel):

    input_variables = copy.deepcopy(INPUT_VARIABLES)
    output_variables = copy.deepcopy(OUTPUT_VARIABLES)

    ...

    def evaluate():

        ... 