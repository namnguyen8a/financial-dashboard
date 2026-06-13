import uvicorn
import yfinance as yf
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/companies/{ticker}")
def get_ticker(ticker: str):
    ticker_info = yf.Ticker(ticker)
    return {"Ticker": ticker_info.info}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000) #reload=True)