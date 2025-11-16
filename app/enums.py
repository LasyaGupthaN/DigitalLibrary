from enum import Enum

class GenreEnum(str, Enum):
    fiction = "fiction"
    nonfiction = "nonfiction"
    fantasy = "fantasy"
    biography = "biography"
    science = "science"


class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"