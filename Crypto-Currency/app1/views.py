import email
from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader
from django import template
# from .models import profile
from django.contrib.auth import authenticate, login as dj_login
# from django.contrib.auth.models import User
from django.conf import settings
from django.forms.utils import ErrorList
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
import json





# Create your views here.

###########################################################
     #Landing Page views
###########################################################
def index(request):
     return render(request, 'index.html', {})

def about(request):
     return render(request, 'about.html', {})

def started(request):
     return render(request, 'started.html', {}) 

def faq(request):
     return render(request, 'faq.html', {})      

def affiliate(request):
     return render(request, 'affiliate.html', {})         

def contact(request):
     return render(request, 'contact.html', {})

def signup(request):
     msg     = ''
     success = False
     
     if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            # profile.objects.create(user=user)
            

            msg     = 'User created - please login.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
     else:
        form = SignUpForm()
     return render(request, 'signup.html', {"form": form, "msg" : msg, "success" : success })



def login(request):
     form = LoginForm(request.POST or None)
     msg = None

     if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect("/dashboard")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    
     return render(request, 'login.html', {"form": form, "msg" : msg})          


##################################################################

          #Dashboard Views

##################################################################



@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "main.html")


@login_required(login_url="/login/")
def depositHistory(request):
    return render(request, "deposit.html")



@login_required(login_url="/login/")
def earnings(request):
    return render(request, "earnings.html")



@login_required(login_url="/login/")
def investments(request):
    return render(request, "my-investments.html")




@login_required(login_url="/login/")
def purchasePlan(request):
    return render(request, "purchase-plan.html")

@login_required(login_url="/login/")
def withdraw(request):
    msg = ""

    if request.method == "POST":
        updatedebit = DebitEditForm(instance=request.user,
        data=request.POST)
        if updatedebit.is_valid():
            updatedebit.save()
            msg = 'Request Submitted Successfully'
            updatedebit = DebitEditForm()
        else:
            updatedebit= DebitEditForm()
            msg = 'Invalid Details'

    else:
        updatedebit = DebitEditForm()
    
    return render(request, "withdraw.html", {'debit':updatedebit, 'msg':msg})

# def calculate_amount():
#     amount = (1/5900)*200

#     print(amount)





#############################################################################

#### pulling live data from coinmarketcap. 
#  signup on their site and get your api key and place it in the string below
# note: there are 2 apis the first for bitcoin n d second for ethereum but u 
# #will use the same api key

#############################################################################

def get_crypto_data():
    
   

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'id':'1',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
  

    # my api key
    'X-CMC_PRO_API_KEY': '439a6f18-ad33-459b-84e9-16b5f51c81bc',

    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']['1']['quote']['USD']['price']

        print(data)
        
        return round(data, 4)


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_crypto_data_eth():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'id':'1027',   
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    
    # my api key
    'X-CMC_PRO_API_KEY': '439a6f18-ad33-459b-84e9-16b5f51c81bc',

    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']['1027']['quote']['USD']['price']

        print(data)
        # print()
        return data


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


@login_required(login_url="/login/")
def fundAccount(request):
    msg = ""

    if request.method == "POST":
        updatecredit = creditEditForm(instance=request.user,
        data=request.POST)
        if updatecredit.is_valid():
            updatecredit.save()
            msg = ''
            updatecredit = creditEditForm()
        else:
            updatecredit= creditEditForm()
            msg = 'Invalid Details'

    else:
        updatecredit = creditEditForm()
    


   
    if request.user.fund_method == 'BTC':
        btc_data = get_crypto_data()
        btc_data = round((1/btc_data)* float(request.user.fund_amount), 8)
        
    else:
        btc_data = None
    
    if request.user.fund_method == 'ETH':
        eth_data = get_crypto_data_eth()
        print(type(eth_data))
        eth_data = round((1/eth_data)* float(request.user.fund_amount), 8)
        
    else:
        eth_data = None

    return render(request, "fund-account.html", {'credit':updatecredit, "msg": msg, 'data':btc_data, 'eth_data':eth_data })




####################################################################

          #Error page Catcher

####################################################################

# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template = request.path.split('/')[-1]
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( 'page-404.html' )
#         return HttpResponse(html_template.render(context, request))

#     except:
    
#         html_template = loader.get_template( 'page-500.html' )
#         return HttpResponse(html_template.render(context, request))
