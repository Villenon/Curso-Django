from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>A soma de {} + {} = {}</h1>' .format(num1, num2, soma))