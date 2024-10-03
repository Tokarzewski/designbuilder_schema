from _typeshed import Incomplete
from designbuilder_schema.core import DBJSON as DBJSON
from designbuilder_schema.utils import load_file_to_dict as load_file_to_dict

def get_filepaths(directory, extension: str = '.json'): ...

models_folder: str
json_filepaths: Incomplete

def test_validate_dbjson(filepath) -> None: ...
