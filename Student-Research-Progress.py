class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.research_projects = []

    def add_student(self, student):
        self.students.append(student)

    def add_research_project(self, project):
        self.research_projects.append(project)

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.research_progress = {}

    def update_research_progress(self, project, status, details=""):
        self.research_progress[project] = {"status": status, "details": details}

class ResearchProject:
    def __init__(self, title, description):
        self.title = title
        self.description = description

# Example Usage:
university = University("Research University")

student1 = Student("2023001", "Ali")
student2 = Student("2023002", "Alishah")

research_project1 = ResearchProject("Machine Learning in Healthcare", "Exploring applications of ML in healthcare")
research_project2 = ResearchProject("Renewable Energy Technologies", "Investigating advancements in renewable energy")

university.add_student(student1)
university.add_student(student2)

university.add_research_project(research_project1)
university.add_research_project(research_project2)

# Update research progress
student1.update_research_progress(research_project1, "In Progress", "Healthcare Study")
student2.update_research_progress(research_project2, "Not Started")

# Access research progress
print(f"Research progress for {student1.name} on {research_project1.title}: {student1.research_progress[research_project1]}")
print(f"Research progress for {student2.name} on {research_project2.title}: {student2.research_progress[research_project2]}")