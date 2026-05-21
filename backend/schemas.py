from pydantic import BaseModel
from datetime import date
from typing import Optional


class EmissionRecordCreate(BaseModel):
    activity: str
    quantity: float
    unit: str
    activity_date: date
    scope: str


class EmissionRecordResponse(BaseModel):
    id: int
    activity: str
    quantity: float
    unit: str
    activity_date: date
    emissions: float
    scope: str

    class Config:
        from_attributes = True


class EmissionFactorResponse(BaseModel):
    id: int
    activity: str
    scope: str
    factor_value: float
    valid_from: date
    valid_to: date

    class Config:
        from_attributes = True


class AnalyticsResponse(BaseModel):
    total_emissions: float
    total_records: int
    average_emissions: float
    