from fastapi import FastAPI
from routes import inventory, sales, chatbot, alerts, insights, ranking  

app = FastAPI()

app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(chatbot.router)
app.include_router(alerts.router)
app.include_router(insights.router)
app.include_router(ranking.router)  
