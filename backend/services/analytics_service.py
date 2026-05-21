from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from models import EmissionRecord, BusinessMetric


def get_yoy_emissions(db: Session):

    results = (
        db.query(
            extract('year', EmissionRecord.created_at).label("year"),
            EmissionRecord.scope,
            func.sum(EmissionRecord.emissions).label("total")
        )
        .group_by(
            extract('year', EmissionRecord.created_at),
            EmissionRecord.scope
        )
        .all()
    )

    data = {}

    for row in results:

        year = str(int(row.year))

        if year not in data:
            data[year] = {}

        data[year][row.scope.lower()] = round(row.total, 2)

    return data



def get_hotspots(db: Session):

    results = (
        db.query(
            EmissionRecord.activity,
            func.sum(EmissionRecord.emissions).label("total")
        )
        .group_by(EmissionRecord.activity)
        .order_by(func.sum(EmissionRecord.emissions).desc())
        .all()
    )

    total_emissions = sum(r.total for r in results)

    hotspot_data = {}

    for row in results:

        percentage = (
            row.total / total_emissions
        ) * 100 if total_emissions else 0

        hotspot_data[row.activity] = round(percentage, 2)

    return hotspot_data



def get_emission_intensity(db: Session):

    total_emissions = (
        db.query(
            func.sum(EmissionRecord.emissions)
        ).scalar()
    )

    metric = (
        db.query(BusinessMetric)
        .order_by(BusinessMetric.metric_date.desc())
        .first()
    )

    if not metric or metric.metric_value == 0:
        return {
            "intensity": 0
        }

    intensity = total_emissions / metric.metric_value

    return {
        "total_emissions": round(total_emissions, 2),
        "metric_name": metric.metric_name,
        "metric_value": metric.metric_value,
        "intensity": round(intensity, 2)
    }



def get_monthly_trends(db: Session):

    results = (
        db.query(
            extract('month', EmissionRecord.created_at).label("month"),
            func.sum(EmissionRecord.emissions).label("total")
        )
        .group_by(
            extract('month', EmissionRecord.created_at)
        )
        .order_by(
            extract('month', EmissionRecord.created_at)
        )
        .all()
    )

    trend_data = {}

    for row in results:

        trend_data[int(row.month)] = round(row.total, 2)

    return trend_data