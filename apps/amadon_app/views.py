# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total' in request.session:
        pass
    else:
        request.session['total'] = 0
        request.session['count'] = 0
    return render(request, 'amadon_app/index.html')

def add(request):
    if request.method == 'POST':
        request.session['cost'] = float(request.POST['cost'])*float(request.POST['amount'])
        request.session['total'] += float(request.POST['cost'])*float(request.POST['amount'])
        request.session['count'] += int(request.POST['amount'])
        return redirect('/confirm')   

def confirm(request):
    return render(request, 'amadon_app/confirm.html', {'total': request.session['total']})

def clear(request):
    request.session.flush()
    return redirect ('/')
# Create your views here.
