import json, re, base64
from PIL import Image
from io import BytesIO

from ultralytics import YOLO
from . import apps
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def load_image(request: HttpRequest):
    body = json.loads(request.body)
    b64 = re.sub('^data:image/.+;base64,', '', body['image'])
    return Image.open(BytesIO(base64.b64decode(b64)))

def export_image(image: Image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def get_results(result):
        return {
        "predictions": json.loads(result.tojson()),
        "annotated": export_image(Image.fromarray(result.plot()[..., ::-1]))
    }


def predict(request: HttpRequest, model: YOLO):
    if request.method != "POST": return HttpResponseBadRequest()

    try: image = load_image(request)
    except: return HttpResponseBadRequest()

    result = model(source=image, verbose=False)[0]
    return JsonResponse(get_results(result), safe=False)

@csrf_exempt
def detect(request: HttpRequest): return predict(request, apps.BasketballtrainerConfig.detection_model)

@csrf_exempt
def pose(request: HttpRequest): return predict(request, apps.BasketballtrainerConfig.pose_model)