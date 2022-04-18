from abc import ABC, abstractmethod


class DatabaseRequests(ABC):
    @abstractmethod
    def add_note(self):
        pass
    
    @abstractmethod
    def del_note(self):
        pass

    @abstractmethod
    def get_note(self):
        pass
