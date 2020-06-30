from django.shortcuts import render
from django.http  import HttpResponse
import random

# Create your views here.
#function for routing the urls
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    thePassword = ''

    #Extending the lowercase alphabets to the uppercase alphabets in
    #thesame list variable called characters
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    #Extending both lower and uppercase alphabets into
    if request.GET.get('special'):
        characters.extend(list('!@#$*;(^%'))

    #Adding numbers to the list
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))




    #Function looping through the passwords
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request,'generator/password.html', {'pass':thePassword})



