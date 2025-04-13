from django.shortcuts import render
import random
import string

def generator(request):
    password=""
    length=8

    if request.method =='POST' :
        length = int(request.POST.get('length', 8))
        use_uppercase = request.POST.get('uppercase') == 'on'
        use_lowercase = request.POST.get('lowercase') == 'on'
        use_digits = request.POST.get('digits') == 'on'
        use_special = request.POST.get('special') == 'on'

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        if characters:
            password = "".join(random.choice(characters) for i in range(length))
        else:
            password = "Please select at least one option."

    if not password:
         password = "Please fill the options."

    return render(request, 'generator/index.html', {'password': password})
