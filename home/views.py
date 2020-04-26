from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        contex = {
        'isim': 'Tahir',
        }
    else:
        contex = {
        'isim': 'Yabancı',
        }

    return render(request, 'home.html', contex)
