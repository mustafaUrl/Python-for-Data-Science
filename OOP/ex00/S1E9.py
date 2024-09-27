from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Character Class"""

    def __init__(self, first_name:str, is_alive:bool = True):
        """Your docstring for __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
    @abstractmethod
    def die(self):
        """Your docstring for die method"""
        pass
    

class Stark(Character):
    """Your docstring for  Stark Class"""

    

    def die(self):
        """Your docstring for die method"""
        self.is_alive = False