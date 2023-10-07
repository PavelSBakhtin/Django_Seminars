from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Data
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='./log/logger.log',
                    filemode='a', format='%(levelname)s %(message)s')


def seminar5(request):
    logger.info(f'{request} request received')
    return HttpResponse('<h1>Seminar5</h1>')


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


def home_page(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SalaryForm()
    return render(request, 'home_page.html', {'form': form})
