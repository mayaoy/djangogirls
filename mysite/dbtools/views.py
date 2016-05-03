from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from .models import Job


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })

def home(request):
    job_list = Job.objects.all()
    return render(request, 'home.html', {
        'job_list': job_list,
    })

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'job.html', {
        'job': job,
    })  

def demo(request):
    return render(request, 'demo.html', {
        'current_time': datetime.now(),
    })

def index(request):
    job_list = Job.objects.all()
    # output = job_list[0].depiction
    # return HttpResponse(output)
    return render(request, 'index.html', {
        'job_list': job_list,
    })