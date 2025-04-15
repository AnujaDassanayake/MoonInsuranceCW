from fastapi import FastAPI
from .schemas import Notification

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Notification Service is running"}

@app.post("/notify/")
def send_notification(notification: Notification):
    # Simulate sending a notification (print/log)
    print(f"🔔 Notification Received: {notification.message}")
    return {"status": "success", "detail": "Notification received"}
