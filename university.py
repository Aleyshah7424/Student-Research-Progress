class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.research_projects = []

    def add_student(self, student):
        self.students.append(student)

    def add_research_project(self, project):
        self.research_projects.append(project)