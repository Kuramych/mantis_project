from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def init_project(self):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Manage").click()
        wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def change_field_value_with_visible_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            Select(wd.find_element("name", field_name)).select_by_visible_text(text)

    def fill_form_project(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value_with_visible_value("status", project.status)
        self.change_field_value_with_visible_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def submit_project(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()

    def add_project(self, project):
        self.init_project()
        self.fill_form_project(project)
        self.submit_project()

    def select_project_by_index(self):
        wd = self.app.wd

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        rows1 = wd.find_elements(By.CSS_SELECTOR, "tr.row-1")
        rows2 = wd.find_elements(By.CSS_SELECTOR, "tr.row-2")
        rows1.extend(rows2)
        return len(rows1)

    def delete_project(self):
        wd = self.app.wd
        self.open_project_page()
        rows1 = wd.find_elements(By.CSS_SELECTOR, "tr.row-1")
        rows2 = wd.find_elements(By.CSS_SELECTOR, "tr.row-2")
        rows1.extend(rows2)
        first_row = rows1[0]
        cells = first_row.find_elements(By.TAG_NAME, "td")
        click_project = cells[0].find_element(By.TAG_NAME, "a")
        click_project.click()
        self.submit_delete_project(wd)
        self.submit_delete_project(wd)

    def submit_delete_project(self, wd):
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()






