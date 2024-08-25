import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.jinja")

if __name__ == '__main__':
     uvicorn.run(
                "main:app",
                host='0.0.0.0',
                port=8000,
                workers=1,
                log_level='info',
                reload=True,
            )
