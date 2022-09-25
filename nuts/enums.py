from enum import Enum

class LoadedStatus(Enum):
    NONE = 0
    CAMERA_LOADED = 1
    CAMERA_USED = 2

class NutClasses(Enum):
    HOLE = 0
    DARK_DARK_GREY = 1
    HALF = 2
    CRACK = 3
    GOUGE = 4
    HUSK = 5
    GOOD = 6
    WHILE_LIGHT_GREY = 7
    