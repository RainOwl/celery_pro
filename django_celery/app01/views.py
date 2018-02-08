from django.shortcuts import render,HttpResponse
from app01 import tasks
from celery.result import AsyncResult

# Create your views here.

def index(request):
    r = tasks.add.delay(1,55)
    print('r-->',r)
    #return HttpResponse(r.get())
    
    return HttpResponse(r.task_id)


def celery_res(request):
    res_id = '7d65df6c-92a4-49df-b3f9-4681c8988f56'
    res = AsyncResult(id=res_id)
    return HttpResponse(res.get())
