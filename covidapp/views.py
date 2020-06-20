from django.db.models import Count
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
import json
from twilio.rest import Client
import requests
import tweepy
import datetime, time
TWITTER_APP_KEY = "LH8wFfPPmviZAkEEpUtSSfuii"
TWITTER_APP_SECRET = "G3N1LjBuLEW6weUcQD62p5jilBljigpGxxCH7XoNRX3HkTy2qI"
TWITTER_KEY = "914138843305017345-UIABECEEIPnlc77nggLsULx8RSsKwY2"
TWITTER_SECRET = "jLfGaWV2QVtASlfCtFJXgB55n8VLPwIr0Y7thlWGvIjqE"

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

###################################################################


def send_welcome():
    from .models import UserDetails
    list1 = []
    qw = UserDetails.objects.values('phoneno').annotate(the_count=Count('phoneno'))
    qw = list(qw)
    for key in qw:
        list1.append(key['phoneno'])

    account_sid = 'ACc1eb16ac09628f63b82b3b240d52c9b5'
    auth_token = 'ec68d3148f22e1e3dfab35c43110af1f'
    client = Client(account_sid, auth_token)
    string = '*Welcome to WhatsCovid Project*\nGet Latest Updates on *Coronavirus*'
    for nu in list1:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=string,
            to='whatsapp:+91' + str(nu),
        )
        print('whatsapp:+91' + str(nu))
        print(message.sid)




    return render(request, 'admin.html',context)
@login_required
def join(request):
    from .models import UserDetails
    user = request.user
    cuser = ''
    deletetoggle = 0
    if user.is_authenticated:
        email = user.email
        cuser = UserDetails.objects.get(emailid=email)
        print(cuser.phoneno)

    context = {
            'currentuser':cuser,

    }
    return render(request,'join.html',context)
@login_required
def delete(request):
    from .models import UserDetails
    user = request.user
    cuser = ''
    if user.is_authenticated:
        email = user.email
        cuser = UserDetails.objects.get(emailid=email)
        print(cuser.phoneno)
        if UserDetails.objects.filter(emailid=user.email).exists():
            UserDetails.objects.filter(emailid=user.email).delete()
    context = {
            'currentuser':cuser,
    }
    return redirect('/dashboard/')

@login_required
def dashboard(request):
    from .models import UserDetails
    user = request.user
    if request.method == 'POST':
        phone = request.POST["phonec"]
        state = request.POST["statedata"]
        if UserDetails.objects.filter(emailid=user.email).exists():
            return redirect('/joined/')
            pass
        else:
            object = UserDetails()
            object.state = state
            object.phoneno = phone
            object.emailid = user.email
            object.save()
            print(user.email,phone,state)
            return redirect('/joined/')
    if UserDetails.objects.filter(emailid=user.email).exists():
        deletetoggle = 1
    else:
        deletetoggle = 0
    print(deletetoggle)
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4),
        'delete': deletetoggle,
    })


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')

def check(request):
    from .models import UserDetails
    for a in UserDetails.objects.all().values_list('phoneno'):
        pass

    return HttpResponse('')

