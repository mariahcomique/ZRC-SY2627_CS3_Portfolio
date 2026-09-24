class Student:

  def __init__(self, name: str):
    self.name = name


class Course:

  def __init__(self, course_name: str):
    self.course_name = course_name
    self.students = []  # Holds the list of Student objects

  def add_student(self, student: Student):
    """Appends a Student object to the course's list."""
    self.students.append(student)