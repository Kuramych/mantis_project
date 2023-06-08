from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_new = app.project.get_project_list()
    if app.project.get_project_list() == 0:
        app.project.add_project(Project(name="test", status="development", view_state="public",
                                        description="fsvcsvsv"))
    app.project.add_project(Project(name="ss", status="development", view_state="public",
                                    description="fsvcsvsv"))
    new_len = app.project.get_project_list()
    assert old_new+1 == new_len
    #assert app.session.is_logged_in_as("administrator")