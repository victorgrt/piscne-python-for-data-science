import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """Generates random id. Used to generate student id."""
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    """STUDENT DATACLASS
    Using fields for attributes to have default values
    and various behavior.
    """
    name:       str = field(init=True)
    surname:    str = field(init=True)
    active :    bool =field(default = True)
    login:      str = field(init=False)
    id :        str = field(init=False, default = generate_id())

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()