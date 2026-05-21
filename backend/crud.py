from sqlalchemy.orm import Session
from sqlalchemy import extract, func

import models


def get_yoy_emissions(db: Session):
    """
    Year-over-Year emissions grouped by year and scope
    """

    results = (
        db.query(
            extract(
                'year',
                models.EmissionRecord.created_at
            ).label("year"),

            models.EmissionRecord.scope,

            func.sum(
                models.EmissionRecord.emissions
            ).label("total")
        )
        .group_by(
            extract(
                'year',
                models.EmissionRecord.created_at
            ),
            models.EmissionRecord.scope
        )
        .all()
    )

    data = {}

    for year, scope, total in results:

        year = str(int(year))

        if year not in data:
            data[year] = {}

        data[year][scope] = round(total or 0, 2)

    return data


def get_hotspots(db: Session):
    """
    Top emission categories
    """

    results = (
        db.query(
            models.EmissionRecord.category,

            func.sum(
                models.EmissionRecord.emissions
            ).label("total")
        )
        .group_by(
            models.EmissionRecord.category
        )
        .order_by(
            func.sum(
                models.EmissionRecord.emissions
            ).desc()
        )
        .all()
    )

    return {
        category: round(total or 0, 2)
        for category, total in results
    }


def get_emission_intensity(db):

    records = db.query(models.EmissionRecord).all()

    scope1 = 0
    scope2 = 0
    scope3 = 0

    for record in records:

        if record.scope == "Scope 1":
            scope1 += float(record.emissions or 0)

        elif record.scope == "Scope 2":
            scope2 += float(record.emissions or 0)

        elif record.scope == "Scope 3":
            scope3 += float(record.emissions or 0)

    total = scope1 + scope2 + scope3

    production_metric = 100000000

    intensity = round(total / production_metric, 2)

    return {

        "total": round(total, 2),

        "scope1": round(scope1, 2),

        "scope2": round(scope2, 2),

        "scope3": round(scope3, 2),

        "intensity": intensity
    }


def get_monthly_trends(db):

    results = (
        db.query(
            extract('month', models.EmissionRecord.created_at),
            func.sum(models.EmissionRecord.emissions)
        )
        .group_by(
            extract('month', models.EmissionRecord.created_at)
        )
        .all()
    )

    return {
        str(int(month)): float(total)
        for month, total in results
    }


