from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):
    if request.session.get('hit') and request.session.get('hit') == 4:
        blocked = True
    else:
        blocked = False
    return render(request, 'The_Site/index.html', {'blocked': blocked})

def send_info(request):
    if not request.session.get('hit'):
        request.session['hit'] = 1
    if request.session.get('hit') and request.session.get('hit') < 4:
        request.session['hit'] += 1

    massage = f"""=====================================
    Имя:\t{request.POST['name']}
    Телефон:\t{request.POST['phoneNumber']}
====================================="""
    send_mail('Hello',
              massage,
              'gr801821@gmail.com',  # отправитель
              ['vadim.yanchenko.2003@mail.ru'],  # получатель
              fail_silently=False)
    return redirect('/')


def calculator(request):
    values = {'square': None, 'texture': None, 'perimeter': None, 'niche': None, 'light': None, 'pipes': None, 'lines': None, 'fly_ceiling': None}
    for i in values.keys():
        if request.POST[i] == "":
            values[i]=0
            continue
        values[i] = int(request.POST[i])
    print(100//2.4)
    s = values['square'] * values['texture'] + values['perimeter'] * 10 + 200 * values['niche'] + 10 * values['light'] + 5 * values['pipes'] + 80 * values['lines'] + 50 * values['fly_ceiling']
    return JsonResponse({'amount': f"Цена - {s} р."}, status=200)
