from fastapi import FastAPI
from livef1 import get_season

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Render LiveF1 test server running"}

@app.get("/season/{year}")
def season_data(year: int):
    try:
        season = get_season(year)
        return {"success": True, "data": season}
    except Exception as e:
        return {"success": False, "error": str(e)}
