from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'hobana studio',
        'npm' : '2306217304',
        'name': 'Clara Aurelia Setiady',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)