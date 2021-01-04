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
    return render(request, 'dramarama/index.html')

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



    # **[경고] 이 코드는 절대로 실행되선 안됩니다. 주석 풀지 마세요.
    DRAMADATA_DIR = 'dramarama/static/data/dramadata.csv'
    with open(DRAMADATA_DIR, newline='', encoding='utf-8') as drama_csv:
        reader = csv.DictReader(drama_csv)
        for row in reader:
            Drama.objects.create(
                value = row['value'],
                title = row['title'],
                channel = row['channel'],
                info_url = row['information']
            )

    FORM_DIR = 'dramarama/static/data/formdata.csv'
    with open(FORM_DIR, newline='', encoding='utf-8') as form_csv:
        reader = csv.DictReader(form_csv)
        for row in reader:
            date_list = row['date'].split('. ')

            physicaltrouble_val = row['physicaltrouble']
            if row['physicaltrouble'] == "예":
                physicaltrouble_val = True
            elif row['physicaltrouble'] == "아니오":
                physicaltrouble_val = False

            mentaltrouble_val = row['mentaltrouble_val']
            if row['mentaltrouble'] == "예":
                mentaltrouble_val = True
            elif row['mentaltrouble'] == "아니오":
                mentaltrouble_val = False

            Survey.objects.create(
                date = date(int(date_list[0]), int(date_list[1]), int(date_list[2])),
                age = row['age'],
                gender = row['gender'],
                personality = row['personality'],
                activity = True if row['activity']=="예" else False,
                job = row['job'],
                interested = row['interested'],
                school = True if row['school'] =="예" else False,
                work = True if row['work'] =="예" else False,
                abode = row['abode'],
                siblings = row['siblings'],
                family = row['family'],
                livealone = True if row['livealone'] =="예" else False,
                major = row['major'],
                homeeconomy = row['homeeconomy'],
                havedate = True if row['havedate'] =="예" else False,
                physicaltrouble = physicaltrouble_val,
                mentaltrouble = mentaltrouble_val,
                prefergenre = row['prefergenre'],
                preferchannel = row['preferchannel'],
                watchingtime = row['watchingtime'],
                used = row['used'],
                way = row['way'],
                first = row['first'],
                second = row['second'],
                third = row['third']
            )

    context = {'Drama':sol.solution(input_form)}

    return render(request, 'dramarama/result.html', context)