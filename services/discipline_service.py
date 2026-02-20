from src.repository.repo_memory import *
from src.repository.repo_text import *
from src.repository.repo_binary import *


class DisciplineService:
    def __init__(self, repo):
        self._repo = repo
        self._data = self._repo.data

    def add(self, discipline: Discipline):
        try:
            self._repo.add(discipline)
        except InvalidNameError:
            raise InvalidNameError
        except DuplicateIDError:
            raise DuplicateIDError

    def remove(self, discipline_id: int):
        try:
            self._repo.remove(discipline_id)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def find_id(self, discipline_id: int):
        try:
            discipline = self._repo.find_id(discipline_id)
            return discipline
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except IDNotFoundError:
            raise IDNotFoundError

    def find_name(self, discipline_name: str) -> list:
        try:
            list_disciplines = self._repo.find_name(discipline_name)
            return list_disciplines
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidNameError:
            raise InvalidNameError
        except NameNotFoundError:
            raise NameNotFoundError

    def update_name(self, discipline_id: int, new_name: str):
        try:
            self._repo.update_name(discipline_id, new_name)
        except EmptyRepositoryError:
            raise EmptyRepositoryError
        except InvalidNameError:
            raise InvalidNameError
        except IDNotFoundError:
            raise IDNotFoundError

    def get_all(self):
        return self._repo.data

    def load(self):
        try:
            self._repo.load()
        except AttributeError:
            raise AttributeError

    def data(self):
        return self._data


