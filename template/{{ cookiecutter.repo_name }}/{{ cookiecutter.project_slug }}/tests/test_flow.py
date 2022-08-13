from {{ cookiecutter.project_slug }}.flow import flow


def test_flow_execution():
    # This will require defaults for all parameters
    flow.run()
