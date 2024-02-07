import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, timedelta


app = FastAPI()

# Setup Jinja2 templates location
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def show_time(request: Request):
    """
    Show the current time in Moscow timezone.
    """
    # Moscow timezone
    moscow_timezone = timezone(timedelta(hours=3))
    current_time = datetime.now(moscow_timezone).strftime("%H:%M:%S")

    # Pass the current time to the template
    return templates.TemplateResponse(
        "index.html", {"request": request, "current_time": current_time}
    )


if __name__ == "__main__":
    import uvicorn

    # Run the app with Uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
    )