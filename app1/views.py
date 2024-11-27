from django.shortcuts import render

# Create your views here.
#render HtML page
def vamsi(request):
    return render(request,'h1.html')#html file name with extenction