from pydantic import field_validator, field_serializer
from typing import Union, Any, List
from designbuilder_schema.base import BaseModel
import pandas as pd


class Tables(BaseModel):
    Table: List["Table"]

    @staticmethod
    def get_table_by_name(self, name: str) -> "Table":
        table_names = {table.name: index for index, table in enumerate(self.Table)}
        index = table_names[name]
        return self.Table[index]


class TableItem(BaseModel):
    FieldName: List[str]
    Row: List[Any]

    def __getattr__(self, name):
        if name in self.FieldName:
            i = self.FieldName.index(name)
            return self.Row[i]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __setattr__(self, name, value):
        if name in self.__dict__:
            super().__setattr__(name, value)
        elif name in self.FieldName:
            index = self.FieldName.index(name)
            self.Row[index] = value
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )


class Table(BaseModel):
    name: str
    numberOfFields: int
    Category: Union[str, List, None] = None
    FieldName: List[str]
    Row: List[List[Any]] = None

    @field_validator("Row", mode="before")
    def parse_rows(cls, value):
        def parse_row(row: str) -> list:
            parts = row.split(" #")
            return [parts[0].lstrip("#")] + parts[1:]

        if value is None:
            return [None]
        elif isinstance(value, str):
            return [parse_row(value)]
        else:
            return [parse_row(row) for row in value]

    @field_serializer("Row")
    def serialize_rows(self, row: List[Any]) -> List[str]:
        if row is None:
            return None
        else:
            return ["#" + " #".join(str(x) for x in item) for item in row]

    def __getitem__(self, index):
        if index >= len(self.Row):
            raise IndexError("Table index out of range")
        return TableItem(FieldName=self.FieldName, Row=self.Row[index])

    def __getattr__(self, name):
        if name in self.FieldName:
            fieldname_index = self.FieldName.index(name)
            return [row[fieldname_index] for row in self.Row]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __setattr__(self, name, value):
        if name in self.__dict__:
            super().__setattr__(name, value)
        elif name in self.FieldName:
            field_index = self.FieldName.index(name)
            if isinstance(value, list) and len(value) == len(self.Row):
                for i, row in enumerate(self.Row):
                    row[field_index] = value[i]
            else:
                raise ValueError(f"Value must be a list with {len(self.Row)} elements")
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.Row, columns=self.FieldName)

    def from_dataframe(self, dataframe: pd.DataFrame) -> None:
        def compose_row(row) -> str:
            return "#" + str(row[0]) + " #" + " #".join(str(item) for item in row[1:])

        self.Row = [compose_row(row[1:]) for row in dataframe.itertuples()]
