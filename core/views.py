from django.shortcuts import render, HttpResponse

def hello(request, nome):
    return HttpResponse(f"<h1>Olá, {nome}</h1>")
