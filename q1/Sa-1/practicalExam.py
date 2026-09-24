class AssignmentSubmission:
    def __init__(self, student_name: str , student_id: str, assignment_title: str, due_date: str, grade: float = 0.0, is_submitted: bool = False):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__submitted_files: list[str] = []
        self.__grade = grade
        self.__is_submitted = is_submitted

    def view_files(self):
        return self.__submitted_files

    def assign_grade(self, assign_grade: float = 0.0):
        if not self.__submitted_files:
            print(f"[WARNING] Cannot grade. No assignment submitted for {self.student_name}")
            return

        self.__grade = assign_grade
        self.__is_submitted = True
        print(f"The grade {assign_grade:g} officially assigned to {self.student_name}")

    def add_file(self, filename: str):
        if filename in self.__submitted_files:
            print(f"[WARNING] {self.student_name} has already submitted {filename}.")
        else:
            self.__submitted_files.append(filename)
            print(f"[SUCCESS] {self.student_name} attached: {filename}. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename: str):
        if self.__is_submitted:
            print(f"[WARNING] {self.student_name} cannot remove files. Assignment already graded.")
        elif filename not in self.__submitted_files:
            print(f"[WARNING] {self.student_name} has not submitted {filename}.")
        else:
            self.__submitted_files.remove(filename)
            print(f"[SUCCESS] {self.student_name} removed: {filename}. Total files: {len(self.__submitted_files)}")


    def status_report(self):
        if not self.__submitted_files:
            return f"Id: {self.student_id} | Name: {self.student_name} | Status: Missing | Grade: Not graded"

        grade_str = f"{self.__grade:g}" if self.__grade != 0.0 else "Not Graded"
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: Submitted {self.__submitted_files} | Grade: {grade_str}"



print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List --- ")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") 
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") 
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) 
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.status_report())
print(student2.status_report())
print(student3.status_report())
print(student4.status_report())
print(student5.status_report())

                       









#sir im so gonna fail comsci bye hahahahah HELP 
