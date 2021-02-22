from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
import csv
import pandas as pd
from dramarama.models import Drama, Survey
from datetime import date

from dramarama import main_solution as sol


@method_decorator(csrf_exempt)
def index(request):
    return render(request, 'dramarama/cover.html')

@method_decorator(csrf_exempt)
def form(request):
    request.session['input'] = {}  # init session
    request.session['result'] = {} 
    request.session.modified = True
    return render(request, 'dramarama/form.html')

@method_decorator(csrf_exempt)
def answer(request):
    input_ = request.session.get('input')
    for el in input_.keys():
        input_[el] = ', '.join(input_[el])
    context = {'answer':input_}
    return render(request, 'dramarama/answer.html', context)

@method_decorator(csrf_exempt)
def result(request):
    input_form = dict(request.POST)
    request.session['input'] = input_form

    context = {'Drama':sol.solution(input_form)}

    return render(request, 'dramarama/result.html', context)

@method_decorator(csrf_exempt)
def survey(request):
    return render(request, 'dramarama/survey.html')

@method_decorator(csrf_exempt)
def submitSurvey(request):
    item_names = ['age', 'gender', 'personality', 'activity', 'job', 'interested',
                 'school', 'work', 'abode', 'siblings', 'family', 'livealone', 'major', 'homeeconomy',
                 'havedate', 'physicaltrouble', 'mentaltrouble', 'prefergenre', 'preferchannel',
                 'watchingtime', 'used', 'way', 'first', 'second', 'third']
    items = {}
    for item_name in item_names:
        items[item_name] = request.POST[item_name]



    return render(request, 'dramarama/cover.html')