# from django.http import HttpResponse
from django.shortcuts import render


def reverse_it(request):
    return render(request, 'first.html')
