import pandas as pd
from database import SessionLocal
from models import EmissionFactor

db = SessionLocal()

df = pd.read_excel("data/ghg_factors.xlsx")

for _, row in df.iterrows():

    factor = EmissionFactor(
        activity=row["Activity"],
        scope=row["Scope"],
        unit=row["Unit"],
        factor_value=row["Factor"],
    )

    db.add(factor)

db.commit()