from django.apps import AppConfig
from ultralytics import YOLO

class BasketballtrainerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basketballtrainer'

    model = YOLO(model="./models/hubert.pt")
