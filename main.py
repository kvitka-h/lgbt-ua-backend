import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import content, actions

app = FastAPI(
    title="LGBT+ Ukrainian Community in Germany API",
    description="Бекенд для інформаційно-комунікаційної платформи підтримки українців.",
    version="1.0.0"
)

# НАЛАШТУВАННЯ CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутерів
app.include_router(content.router)
app.include_router(actions.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to LGBT+ UA Support API",
        "documentation": "/docs",
        "supported_languages": ["ua", "en", "de"]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)