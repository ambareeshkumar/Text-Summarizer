from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from TextSummarizer.pipeline.Prediction_Pipeline import PredictionPipeline
import uvicorn

MIN_TEXT_LENGTH = 128
MAX_TEXT_LENGTH = 1024

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="templates"), name="static")

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        input_text = request.text
        from typing import Optional
    

        if len(input_text) < MIN_TEXT_LENGTH:
            return {"message": f'Input text must be at least {MIN_TEXT_LENGTH} characters'}
        elif len(input_text) > MAX_TEXT_LENGTH:
            return {"message": f'Input text must be at most {MAX_TEXT_LENGTH} characters'}
        
        model = PredictionPipeline()
        summary = model.predict(input_text)
        return {"summary": summary}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)