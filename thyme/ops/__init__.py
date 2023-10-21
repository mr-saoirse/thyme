from .io import *
from .codetools import *


def get_types():
    pass


def save_type(code):
    my_type = eval(code)

    path = my_type.get_path()

    with open(path, "w") as f:
        f.write(code)


def build_ops_index():
    pass
