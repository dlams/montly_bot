from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, Integer, String

# metadata = MetaData()

# object_lines = Table(
#     'object_lines', metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("qty", Integer, nullable=False),
#     Column("orderid", String(255)),
# )


# def start_mappers():
#     lines_mapper = mapper(func.foo, object_lines)