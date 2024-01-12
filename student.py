from university import University

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.research_progress = {}

    def update_research_progress(self, project, status, details=""):
        self.research_progress[project] = {"status": status, "details": details}