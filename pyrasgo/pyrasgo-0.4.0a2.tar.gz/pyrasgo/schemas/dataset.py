from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from pyrasgo.schemas import dw_table as dw_table_schemas
from pyrasgo.schemas import dataset_column as dataset_column_schemas


class Dataset(BaseModel):
    """
    Contract to return from get by id endpoints
    """
    id: int
    name: Optional[str]
    description: Optional[str]
    status: Optional[str]

    owner_id: Optional[int] = Field(alias='ownerId')
    organization_id: int = Field(alias='organizationId')
    dw_table_id: Optional[int] = Field(alias='dwTableId')
    dw_operation_set_id: Optional[int] = Field(alias='dwOperationSetId')

    columns: Optional[List[dataset_column_schemas.DatasetColumn]]
    dw_table: Optional[dw_table_schemas.DataTableWithColumns] = Field(alias='dataTable')
    consumer_count: int = Field(alias='consumerCount')

    attributes: Optional[dict]
    tags: Optional[List[str]]

    create_timestamp: datetime = Field(alias='createTimestamp')
    create_author: int = Field(alias='createdBy')
    update_timestamp: datetime = Field(alias='updateTimestamp')
    update_author: int = Field(alias='updatedBy')

    class Config:
        allow_population_by_field_name = True


class DatasetBulk(BaseModel):
    """
    Contract to return from get list endpoints
    """
    id: int
    name: Optional[str]
    description: Optional[str]

    owner_id: Optional[int] = Field(alias='ownerId')
    organization_id: int = Field(alias='organizationId')

    dw_table_id: Optional[int] = Field(alias='dwTableId')
    dw_table: Optional[dw_table_schemas.DataTable] = Field(alias='dataTable')

    dw_operation_set_id: Optional[int] = Field(alias='dwOperationSetId')

    dataset_dependencies: List[int] = Field(alias='datasetDependencies')

    column_count: int = Field(alias='columnCount')
    consumer_count: int = Field(alias='consumerCount')

    create_timestamp: datetime = Field(alias='createTimestamp')
    create_author: int = Field(alias='createdBy')
    update_timestamp: datetime = Field(alias='updateTimestamp')
    update_author: int = Field(alias='updatedBy')

    class Config:
        allow_population_by_field_name = True


class DatasetCreate(BaseModel):
    """
    Contract to accept in post endpoints
    """
    name: str
    description: Optional[str]
    status: Optional[str]
    dw_table_id: Optional[int] = Field(alias='dwTableId')
    dw_operation_set_id: Optional[int] = Field(alias='dwOperationSetId')

    class Config:
        allow_population_by_field_name = True


class DatasetUpdate(BaseModel):
    """
    Contract to accept in put endpoints
    """
    name: Optional[str]
    description: Optional[str]
    status: Optional[str]
    owner_id: Optional[int] = Field(alias='ownerId')
    dw_table_id: Optional[int] = Field(alias='dwTableId')
    dataset_columns: Optional[List[dataset_column_schemas.DatasetColumnUpdateById]]

    class Config:
        allow_population_by_field_name = True
