

class Project:
    def __init__(self, name=None, status=None, view_state=None, description=None):
        self.name = name
        self.status = status
        self.view_state = view_state
        self.description = description

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.name, self.status, self.view_state, self.description)

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status