from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_inf = app.project.get_project_list()
    old_project = len(old_project_inf)
    project = Project(name="hhggffgvvvvnhfdvfdhhg", status="development")
    if app.project.get_project_len_list() == 0:
        app.project.add_project(Project(name="test", status="development", view_state="public",
                                        description="fsvcsvsv"))
    app.project.add_project(project)
    new_project_inf = app.project.get_project_list()
    new_project = len(new_project_inf)
    assert old_project+1 == new_project
    old_project_inf.append(project)
    assert sorted(old_project_inf) == sorted(new_project_inf)
