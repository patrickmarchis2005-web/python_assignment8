from src.repository.repo_memory import *
from src.repository.repo_text import *
from src.repository.repo_binary import *


class StudentService:
    def __init__(self, repo):
        self._repo = repo
        # self._data = self._repo.data()

    def add(self, student: Student):
        try:
            self._repo.add(student)
        except InvalidNameError:
            raise InvalidNameError
        except DuplicateIDError:
            raise DuplicateIDError

    def remove(self, student_id: int):
        try:
            self._repo.remove(student_id)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def find_id(self, stud_id: int) -> Student:
        try:
            student = self._repo.find_id(stud_id)
            return student
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def find_name(self, student_name: str) -> list:
        try:
            lst = self._repo.find_name(student_name)
            return lst
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidNameError:
            raise InvalidNameError
        except NameNotFoundError:
            raise NameNotFoundError

    def update_name(self, new_name: str, student_id: int):
        try:
            self._repo.update_name(new_name, student_id)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidNameError:
            raise InvalidNameError
        except IDNotFoundError:
            raise IDNotFoundError

    def get_all(self) -> dict:
        return self._repo.data

    def load(self):
        try:
            self._repo.load()
        except AttributeError:
            raise AttributeError

    # def data(self):
    #     return self._data


