from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    if not "submissions" in request.session:
        request.session['submissions'] = 0
    return render(request,'surveyApp/index.html')

def process(request):
    error=False
    if request.POST['name']=="":
        error=True
        messages.info(request, "Name cannot be empty")
    if request.POST['location']=="None":
        error=True
        messages.info(request, "Location cannot be empty")
    if request.POST['language']=="None":
        error=True
        messages.info(request, "Language cannot be empty")
    if error:
        return redirect('/')
    else:
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['submissions'] += 1
        return redirect ('/result')

def result(request):
    context={
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
    }
    messages.success(request, "Thanks for submitting this form! You have submitted this form {} times now.".format(request.session['submissions']))
    return render(request,'surveyApp/result.html', context)

def goBack(request):
    # request.session.clear()
    return redirect('/')