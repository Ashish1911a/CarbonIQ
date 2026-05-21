# CarbonIQ – ESG Analytics Platform

CarbonIQ is a full-stack ESG analytics dashboard that enables organizations to upload carbon emissions Excel data and visualize sustainability insights through interactive dashboards and analytics.

---

# Features

- Excel Upload System
- Scope 1 / Scope 2 / Scope 3 Emissions Tracking
- KPI Dashboard
- Year-over-Year Emissions Charts
- Emission Hotspot Analysis
- Monthly Emission Trends
- Responsive ESG Dashboard
- FastAPI Backend
- React + Tailwind Frontend
- Recharts Data Visualization
- Docker Support

---

# Tech Stack

## Frontend
- React.js
- Tailwind CSS
- Framer Motion
- Recharts
- Axios

## Backend
- FastAPI
- SQLAlchemy
- Pandas
- SQLite

---

# Folder Structure

```bash
CarbonIQ/
│
├── backend/
│   ├── app.py
│   ├── crud.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│
├── Dockerfile
├── README.md

Backend Setup
cd backend

pip install -r requirements.txt

uvicorn app:app --reload

Backend runs on:

http://localhost:8000
Frontend Setup
cd frontend

npm install

npm run dev

Frontend runs on:

http://localhost:5173


API Endpoints
Method	Endpoint	Description
POST	/upload-excel	Upload Excel File
GET	/analytics/yoy	YoY Emissions
GET	/analytics/hotspots	Emission Hotspots
GET	/analytics/intensity	KPI Metrics
GET	/analytics/monthly-trends	Monthly Trends
Excel Upload

Supported sheets:

Scope 1
Scope 2
Scope 3

The uploaded data is automatically parsed and stored in the database.

Docker Run
docker build -t carboniq .

docker run -p 8000:8000 carboniq


