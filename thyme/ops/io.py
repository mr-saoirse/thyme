from pathlib import Path
import thyme

# namespace
# from glob import glob
# glob(namespace_path('one')+"/**")


def namespace_path(ns):
    """
    given a namespace such as "one" resolves the full path to the namespace under the thyme library


    """
    return f"{Path(thyme.__file__).parent}/types/ns/{ns}/"
