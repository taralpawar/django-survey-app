from django.shortcuts import render, HttpResponse, redirect
from .models import Survey
from django.contrib import messages
# Create your views here.


def homepage(request):
    if request.method == 'POST':
        service = request.POST['servicequality']
        food = request.POST['foodquality']
        speed = request.POST['speed']
        value = request.POST['value']
        email = request.POST['email']
        comment = request.POST['comment']

        newsurvey = Survey(foodquality=food, servicequality=service,
                           speed=speed, value=value, email=email, comment=comment)

        newsurvey.save()
        #messages.success(request, 'Thank You for your response')
        return redirect('thankyou/')

    else:
        return render(request, 'usersurvey/homepage.html')


def thankyou(request):
    return render(request, 'usersurvey/thank.html')


def summary(request):
    allsurvey = Survey.objects.all()

    foodex = 0
    foodgood = 0
    foodavg = 0
    foodunsat = 0
    serveex = 0
    servegood = 0
    serveavg = 0
    serveunsat = 0
    speedex = 0
    speedgood = 0
    speedavg = 0
    speedunsat = 0
    valex = 0
    valgood = 0
    valavg = 0
    valunsat = 0

    for survey in allsurvey:
        if survey.foodquality == 'Excellent':
            foodex += 1
        elif survey.foodquality == 'Good':
            foodgood += 1
        elif survey.foodquality == 'Average':
            foodavg += 1
        elif survey.foodquality == 'Unsatisfied':
            foodunsat += 1

        if survey.servicequality == 'Excellent':
            serveex += 1
        elif survey.servicequality == 'Good':
            servegood += 1
        elif survey.servicequality == 'Average':
            serveavg += 1
        elif survey.servicequality == 'Unsatisfied':
            serveunsat += 1

        if survey.speed == 'Excellent':
            speedex += 1
        elif survey.speed == 'Good':
            speedgood += 1
        elif survey.speed == 'Average':
            speedavg += 1
        elif survey.speed == 'Unsatisfied':
            speedunsat += 1

        if survey.value == 'Excellent':
            valex += 1
        elif survey.value == 'Good':
            valgood += 1
        elif survey.value == 'Average':
            valavg += 1
        elif survey.value == 'Unsatisfied':
            valunsat += 1
    if len(allsurvey) > 0:
        foodexp = (foodex*100)/len(allsurvey)
        serveexp = (serveex*100)/len(allsurvey)
        valexp = (valex*100)/len(allsurvey)
        speedexp = (speedex*100)/len(allsurvey)
    else:
        foodexp = 0
        serveexp = 0
        valexp = 0
        speedexp = 0

    return render(request, 'usersurvey/summary.html', {'allsurvey': allsurvey, 'foodpercent': foodexp, 'servepercent': serveexp,
                                                       'valpercent': valexp, 'speedpercent': speedexp})


def deletesurvey(request, id):
    survey = Survey.objects.get(id=id)
    survey.delete()

    messages.success(request, "Survey deleted successfully")
    return redirect('/summary')
