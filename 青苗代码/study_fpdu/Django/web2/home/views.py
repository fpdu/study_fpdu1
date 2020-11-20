from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(r):
    return HttpResponse('HELLO WORLD')

def req_info(r):
    res = r.path
    print(res)
    return HttpResponse('关于请求对象')