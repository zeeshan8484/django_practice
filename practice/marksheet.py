from typing import Dict, List


class Marksheet:
    def __init__(self, student_name: str, roll_number: str, marks: Dict[str, int]):
        self.student_name = student_name
        self.roll_number = roll_number
        self.marks = marks

    def total_marks(self) -> int:
        return sum(self.marks.values())

    def total_subjects(self) -> int:
        return len(self.marks)

    def percentage(self) -> float:
        if not self.marks:
            return 0.0
        total = self.total_marks()
        maximum = self.total_subjects() * 100
        return round((total / maximum) * 100, 2)

    def grade(self) -> str:
        percent = self.percentage()

        if percent >= 90:
            return "A+"
        elif percent >= 80:
            return "A"
        elif percent >= 70:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 50:
            return "D"
        else:
            return "F"

    def result(self) -> Dict[str, object]:
        return {
            "student_name": self.student_name,
            "roll_number": self.roll_number,
            "marks": self.marks,
            "total_marks": self.total_marks(),
            "percentage": self.percentage(),
            "grade": self.grade(),
        }


# Example usage
if __name__ == "__main__":
    student_marks = {
        "Math": 85,
        "Science": 90,
        "English": 78,
        "Computer": 95,
    }

    sheet = Marksheet("John Doe", "101", student_marks)
    print(sheet.result())
