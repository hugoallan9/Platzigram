from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Oh, hi! Current server time is {now}".format(now=str(now)))

def sorted(request):
    nums = sorted([int(i) for i in request.GET['numbers'].split(",")])
    data = {
        'status': 'ok',
        'numbers': nums,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def say_hi(request, name, age):
    if age <12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hello, {}! Welcome to Platzigram".format(name)
    return HttpResponse(message)