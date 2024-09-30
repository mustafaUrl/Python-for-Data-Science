import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """ Generate a random id. """
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str = field(metadata={"help": "The name of the student."})
    surname: str = field(metadata={"help": "The surname of the student."})
    active: bool = field(default=True, metadata={"help": "The status of the student."})  # Keep active in repr
    login: str = field(init=False, metadata={"help": "The login of the student."})  # Keep login in repr
    id: str = field(default_factory=generate_id, metadata={"help": "The id of the student."})

    def __post_init__(self):
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"  # Generate login after initialization
