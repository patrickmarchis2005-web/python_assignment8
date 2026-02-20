from src.repository.repo_memory import *
from src.repository.repo_text import *
from src.repository.repo_binary import *


class GradeService:
    def __init__(self, repo):
        self._repo = repo
        self._data = self._repo.data

    def add(self, grade: Grade):
        try:
            self._repo.add(grade)
        except InvalidGradeError:
            raise InvalidGradeError
        except IDNotFoundError:
            raise IDNotFoundError

    def remove_discipline(self, discipline_id: int):
        try:
            self._repo.remove_discipline(discipline_id)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def remove_student(self, student_id: int):
        try:
            self._repo.remove_student(student_id)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def remove_grade(self, student_grade: Grade):
        try:
            self._repo.remove_grade(student_grade)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidGradeError:
            raise InvalidGradeError
        except IDNotFoundError:
            raise IDNotFoundError
        except GradeNotFoundError:
            raise GradeNotFoundError

    def find_grades(self, stud_id: int, discipline_id: int) -> list:
        try:
            lst = self._repo.find_grades(stud_id, discipline_id)
            return lst
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def update_grade(self, new_grade: int, actual_grade: Grade):
        try:
            self._repo.update_grade(new_grade, actual_grade)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidGradeError:
            raise InvalidGradeError
        except IDNotFoundError:
            raise IDNotFoundError
        except GradeNotFoundError:
            raise GradeNotFoundError

    def get_all(self):
        return self._repo.data

    def load(self):
        try:
            self._repo.load()
        except AttributeError:
            raise AttributeError

    def data(self):
        return self._data


