from pydantic import Field, field_validator, PrivateAttr
from typing import Union, List
from designbuilder_schema.base import BaseModel
import pandas as pd

class Tables(BaseModel):
    Table: list # Union[List["Tables"], List["TableOfTables"]]

    @field_validator("Table")
    def map_to_specific_class(cls, tables):
        """XYZ: This is the only method I know for recasting Table
           TODO: Find a different method for recasting so that the 
           Table __getattr__ is still accessible"""
        mapped_tables = []
        for table in tables:
            #match table.get("@name"):
                #case "TableOfTables":
                #    mapped_tables.append(TableOfTables(**table))
                #case "EditFormats":
                #    mapped_tables.append(EditFormats(**table))
                #case _:
            mapped_tables.append(Table(**table))
        return mapped_tables

    @staticmethod
    def get_table_by_name(self, name: str) -> "Table":
        table_names = {table.name: index for index, table in enumerate(self.Table)}
        index = table_names[name]
        return self.Table[index]

class Table(BaseModel):
    name: str = Field(alias="@name")
    numberOfFields: int = Field(alias="@numberOfFields")
    Category: Union[str, list, None] = Field(default=None)
    FieldName: list[str]
    Row: list[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        for field in self.FieldName:
            self.__annotations__[field] = List[str]

    @property
    def __class__(self):
        # This is a trick to make the IDE recognize dynamic attributes
        class _DynamicTable(type(self)):
            pass
        for field in self.FieldName:
            setattr(_DynamicTable, field, property(lambda self, f=field: self.__getattr__(f)))
        return _DynamicTable

    @field_validator('Row', mode="before")
    def ensure_row_list(cls, v):
        if isinstance(v, str):
            return [v]
        return v

    def to_dataframe(self) -> pd.DataFrame:
        def parse_row(row: str) -> list:
            parts = row.split(' #')
            return [parts[0].lstrip('#')] + parts[1:]

        processed_rows = [parse_row(row) for row in self.Row]
        return pd.DataFrame(processed_rows, columns=self.FieldName)

    def read_dataframe(self, dataframe: pd.DataFrame) -> None:
        """Updates the Table instance from a DataFrame."""
        def compose_row(row) -> str:
            return '#' + str(row[0]) + ' #' + ' #'.join(str(item) for item in row[1:])
        
        composed_row = [compose_row(row[1:]) for row in dataframe.itertuples()]
        self.Row = composed_row

    def __getattr__(self, name):
        if name in self.FieldName:
            return self.to_dataframe()[name].tolist()
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")