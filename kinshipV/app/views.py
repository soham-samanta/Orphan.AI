from django.shortcuts import render
from django.http import HttpResponse
# from ml.runner
# Create your views here.

def index(req):
    return render(req,'index.html')

def landpage(req):
    return render(req,'landing.html')

def formpageP(req):
    return render(req,'formParent.html')
def formpageC(req):
    return render(req,'formChild.html')