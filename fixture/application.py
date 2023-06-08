from selenium import webdriver
from fixture.session import Session_helper
from fixture.project import ProjectHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = Session_helper(self)
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20")

    def destroy(self):
        self.wd.quit()
