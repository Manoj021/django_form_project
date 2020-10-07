from django.shortcuts import render
from django.http import HttpResponse
from .models import from_details
from .personForm import PersonForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('form is getting saved')
            p = form.save(commit=False)
            print("came into is valid")
            p.save()
            return HttpResponse("data submitted successfully")
    return render(request, 'Form/home.html')


def success(request):
    return render(request, '<h1>success<h1>')
