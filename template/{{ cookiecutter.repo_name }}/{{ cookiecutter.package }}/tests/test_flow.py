from {{ cookiecutter.package }}.flow import flow, output_variables


def test_flow_execution():
    # mark success on success of evaluate task
    flow.set_reference_tasks([output_variables])

    # Running without passing parameters require defaults for all parameters
    flow.run()

    # check success of flow
    assert flow_run.is_successful()
