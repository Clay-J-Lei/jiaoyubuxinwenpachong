import datetime
import json
from django.shortcuts import render,HttpResponse
from app.models import GetData
# Create your views here.

def day_get(d):
    for i in range(1,15):
        oneday = datetime.timedelta(days=i)
        day = d - oneday
        date_to = datetime.datetime(day.year,day.month,day.day)

        yield str(date_to)[0:10]

def Get(request):
    d = datetime.datetime.now()
    date = day_get(d)
    data = {}
    for i in date:
        data[i] = len(GetData.objects.filter(add_time=i))

    return HttpResponse(json.dumps(data))

def Index(request):
    pass
    return render(request,'index/index.html',locals())