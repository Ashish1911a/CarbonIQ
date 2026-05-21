from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from database import Base
from datetime import datetime


class EmissionFactor(Base):
    __tablename__ = "emission_factors"

    id = Column(Integer, primary_key=True, index=True)

    activity = Column(String, nullable=False)
    scope = Column(String, nullable=False)

    unit = Column(String, nullable=False)

    factor_value = Column(Float, nullable=False)

    source = Column(String, nullable=False)

    valid_from = Column(Date, nullable=False)
    valid_to = Column(Date, nullable=False)

class EmissionRecord(Base):
    __tablename__ = "emission_records"

    id = Column(Integer, primary_key=True, index=True)

    scope = Column(String, nullable=False)

    category = Column(String, nullable=False)

    activity = Column(String, nullable=False)

    quantity = Column(Float, nullable=False)

    unit = Column(String, nullable=False)

    emission_factor = Column(Float, nullable=False)

    emissions = Column(Float, nullable=False)

    reporting_period = Column(String, nullable=False)

    location = Column(String, nullable=False)

    source = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    emission_record_id = Column(Integer, nullable=False)

    old_value = Column(Float, nullable=False)

    new_value = Column(Float, nullable=False)

    reason = Column(String, nullable=False)

    changed_at = Column(DateTime, default=datetime.utcnow)

class BusinessMetric(Base):
    __tablename__ = "business_metrics"

    id = Column(Integer, primary_key=True, index=True)

    metric_name = Column(String, nullable=False)

    metric_value = Column(Float, nullable=False)

    metric_date = Column(Date, nullable=False)
