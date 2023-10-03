from django.apps import AppConfig
from ultralytics import YOLO

class BasketballConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basketball'

    detection_model = YOLO(model="./models/hubert.pt")
    pose_model = YOLO(model="./models/orville.pt")
