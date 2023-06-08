from model.project import Project
import time

def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.delete_project()
    time.sleep(5)
    #assert app.session.is_logged_in_as("administrator")