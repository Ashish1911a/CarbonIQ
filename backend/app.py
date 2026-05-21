from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import pandas as pd
from datetime import datetime
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base, SessionLocal
import models

from crud import (
    get_yoy_emissions,
    get_hotspots,
    get_emission_intensity,
    get_monthly_trends
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def safe_float(value):

    if pd.isna(value):
        return 0.0

    try:
        return float(value)

    except:
        return 0.0

@app.post("/upload-excel")
async def upload_excel(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    all_sheets = pd.read_excel(
        file_path,
        sheet_name=None
    )

    records = []

    for sheet_name, df in all_sheets.items():

        df.columns = [
            str(col).strip()
            for col in df.columns
        ]

        for _, row in df.iterrows():

            record = None

            if sheet_name == "Scope 1":

                record = models.EmissionRecord(

                    scope="Scope 1",

                    category=str(
                        row.get("Section", "General")
                    ),

                    activity=str(
                        row.get("Material", "Unknown")
                    ),

                    quantity=safe_float(
                        row.get("Q1 Quantity")
                    ),

                    unit=str(
                        row.get("Unit of Material", "")
                    ),

                    emission_factor=safe_float(
                        row.get("Emission Factor")
                    ),

                    emissions=safe_float(
                        row.get("GHG Emission (tCO2)")
                    ),

                    reporting_period=str(
                        row.get("Year/Timeline", "2025")
                    ),

                    location=str(
                        row.get("Location (Plant)", "India")
                    ),

                    source=str(
                        row.get(
                            "Data Source for Emission Factor",
                            "Excel Upload"
                        )
                    ),

                    created_at=datetime.utcnow()
                )

            elif sheet_name == "Scope 2":

                record = models.EmissionRecord(

                    scope="Scope 2",

                    category=str(
                        row.get("Section/Process", "General")
                    ),

                    activity=str(
                        row.get("Energy Type", "Unknown")
                    ),

                    quantity=safe_float(
                        row.get("Energy Consumed")
                    ),

                    unit=str(
                        row.get("Unit", "")
                    ),

                    emission_factor=safe_float(
                        row.get("Emission Factor (tCO₂/unit)")
                    ),

                    emissions=safe_float(
                        row.get("Scope 2 Emissions (tCO₂)")
                    ),

                    reporting_period=str(
                        row.get("Quarter", "2025")
                    ),

                    location=str(
                        row.get("Location (Plant)", "India")
                    ),

                    source=str(
                        row.get(
                            "Grid Emission Factor Source",
                            "Excel Upload"
                        )
                    ),

                    created_at=datetime.utcnow()
                )

            elif sheet_name == "Scope 3":

                record = models.EmissionRecord(

                    scope="Scope 3",

                    category=str(
                        row.get("Scope 3 Category", "General")
                    ),

                    activity=str(
                        row.get(
                            "Activity Description",
                            "Unknown"
                        )
                    ),

                    quantity=safe_float(
                        row.get("Quantity")
                    ),

                    unit=str(
                        row.get("Unit of Activity", "")
                    ),

                    emission_factor=safe_float(
                        row.get(
                            "Emission Factor (tCO2/unit)"
                        )
                    ),

                    emissions=safe_float(
                        row.get(
                            "Scope 3 Emissions (tCO2)"
                        )
                    ),

                    reporting_period=str(
                        row.get("Quarter", "2025")
                    ),

                    location="India",

                    source=str(
                        row.get(
                            "Emission Factor Source",
                            "Excel Upload"
                        )
                    ),

                    created_at=datetime.utcnow()
                )

            if record:
                records.append(record)

    db.bulk_save_objects(records)

    db.commit()

    return {
        "message": "Carbon Emissions API Running",
        "records_inserted": len(records)
    }

@app.get("/analytics/yoy")
def yoy_analytics(
    db: Session = Depends(get_db)
):
    return get_yoy_emissions(db)


@app.get("/analytics/hotspots")
def hotspots(
    db: Session = Depends(get_db)
):
    return get_hotspots(db)


@app.get("/analytics/intensity")
def intensity(
    db: Session = Depends(get_db)
):
    return get_emission_intensity(db)


@app.get("/analytics/monthly-trends")
def monthly_trends(
    db: Session = Depends(get_db)
):
    return get_monthly_trends(db)

