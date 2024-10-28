import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

record = []


@app.get("/status")
def status():
    systems_list = list(systems.keys())
    pick = random.choice(systems_list)
    record.append(pick)
    return {"damaged_system": pick}


@app.get("/repair-bay", response_class=HTMLResponse)
def repair_bay():
    system = ''
    if record:
        pick = record[-1]
        system = systems.get(pick)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
    <div class="anchor-point">{system}</div>
    </body>
    </html>
    """
    return html


@app.post("/teapot", status_code=418)
def teapot():
    return {"message": "I'm a teapot"}


@app.get("/phase-change-diagram")
def phase_change_diagram(pressure: float = 10):
    svl_m = 4061.224489795918
    specific_volume_liquid = (pressure-0.05+(svl_m*0.00105))/svl_m

    svv_m = -0.3317053656259897
    specific_volume_vapor = (pressure-10+(svv_m*0.0035))/svv_m
    return {
        "specific_volume_liquid": round(specific_volume_liquid, 4),
        "specific_volume_vapor": round(specific_volume_vapor, 4)
    }