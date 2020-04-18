from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('<b> Hoş Geldiniz <b/>')


def user(request):
    return HttpResponse('<b> Hoş Geldiniz Kullanıcılar<b/>')


def testler(request):
    return HttpResponse('<b>Test Sayfasına Hoş Geldiniz<b/>')
