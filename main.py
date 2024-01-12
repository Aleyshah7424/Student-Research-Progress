from university import University
from student import Student
from researchproject import ResearchProject

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