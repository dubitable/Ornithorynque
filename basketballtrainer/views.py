import json, re, base64
from PIL import Image
from io import BytesIO
from . import apps
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request: HttpRequest):
    if request.method != "POST": return HttpResponseBadRequest()

    body = json.loads(request.body)
    b64 = re.sub('^data:image/.+;base64,', '', body['image'])

    image = Image.open(BytesIO(base64.b64decode(b64)))
    result = apps.BasketballtrainerConfig.model(source=image)[0]

    boxes, names, speed = result.boxes.xyxy.tolist(), result.names, result.speed
    return JsonResponse({"boxes": boxes, "names": names, "speeds": speed})
