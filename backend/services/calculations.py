from sqlalchemy.orm import Session
from models import EmissionFactor


def get_emission_factor(
    db: Session,
    activity: str,
    scope: str
):
    """
    Fetch emission factor from database
    """

    factor = (
        db.query(EmissionFactor)
        .filter(
            EmissionFactor.activity == activity,
            EmissionFactor.scope == scope
        )
        .first()
    )

    return factor


def calculate_emissions(
    db: Session,
    activity: str,
    quantity: float,
    scope: str
):
    """
    Calculate total emissions

    Formula:
    emissions = quantity × factor_value
    """

    factor = get_emission_factor(
        db=db,
        activity=activity,
        scope=scope
    )

    if not factor:
        raise ValueError(
            f"No emission factor found for {activity} ({scope})"
        )

    emissions = quantity * factor.factor_value

    return {
        "activity": activity,
        "scope": scope,
        "quantity": quantity,
        "emission_factor": factor.factor_value,
        "emissions": round(emissions, 2)
    }


def calculate_total_emissions(records):
    """
    Calculate total emissions from multiple records
    """

    total = sum(record.emissions for record in records)

    return round(total, 2)


def calculate_average_emissions(records):
    """
    Calculate average emissions
    """

    if not records:
        return 0

    average = sum(
        record.emissions for record in records
    ) / len(records)

    return round(average, 2)


def emissions_by_scope(records):
    """
    Group emissions by scope
    """

    scope_totals = {}

    for record in records:

        if record.scope not in scope_totals:
            scope_totals[record.scope] = 0

        scope_totals[record.scope] += record.emissions

    return scope_totals