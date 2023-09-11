
from django.contrib.auth.decorators import login_required
from .models import Salesforce
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from .models import Salesforce
import requests
from django.conf import settings


# Create your views here.
# views.py
from django.shortcuts import redirect, render
import requests
def home(request):
    return render(request,'home.html')
def salesforce_oauth(request):
   
    client_id = '3MVG9pRzvMkjMb6m2CZ6aOjuqpJQtMvUUwGxk2O_1_tVErvarMU3zPhz436fIwhs4zh_Iee00u503jAWRfWyC'
    client_secret = '9284C44F17C26FF14503E055C70A6BD085E2E4AEAFE595CC07E7274201A28BB8'
    redirect_uri = 'http://localhost:8000/callback/ ' 
    
   
    auth_url = f'https://login.salesforce.com/services/oauth2/authorize?' \
               f'client_id={client_id}&response_type=code&redirect_uri={redirect_uri}'
    
    return redirect(auth_url)
@login_required
def welcome(request):
    return render(request, 'welcome.html')

""""def callback(request):
    if 'code' in request.GET:
     
        code = request.GET['code']

        
        token_url = 'https://login.salesforce.com/services/oauth2/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': '3MVG9pRzvMkjMb6m2CZ6aOjuqpLBAuvvCUuf89b6njNCpBipT1iwY_yqU3z8amWVkNbceMtbjAeJ9Mtt5UQTF',
            'client_secret': '4619438C6213A1699A78FD6BAB62641172D1F5A77F37EE85B9D22ACFC752B100',
            'redirect_uri': 'http://localhost:8000/callback/ ' 
        }

        response = requests.post(token_url, data=data)
        token_data = response.json()

      
        token = Salesforce(
            access_token=token_data['access_token'],
            refresh_token=token_data['refresh_token'],
            instance_url=token_data['instance_url'],
            user=request.user  
        )
        token.save()

        return redirect('welcome')
    else:
      
        return render(request, 'error.html')"""



"""def callback(request):
    if 'code' in request.GET:
        # Retrieve the code from the Salesforce OAuth response
        code = request.GET['code']
        
        # Exchange the code for an access token
     

        return render (request,'welcome.html')
       
    else:
        # Handle OAuth error
        return render(request, 'error.html', {'message': 'OAuth error'})"""


"""def callback(request):
    if 'code' in request.GET:
        code = request.GET['code']

       

        return render (request,'welcome.html')
    else:
        # Handle OAuth error
        return render(request, 'error.html', {'message': 'OAuth error'})"""
def callback(request):
    if 'code' in request.GET:
        code = request.GET['code']

        token_url = 'https://login.salesforce.com/services/oauth2/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'client_secret': settings.SALESFORCE_CLIENT_SECRET,
            'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
        }

        response = requests.post(token_url, data=data)
        token_data = response.json()

        # Check if the user is authenticated
        if not isinstance(request.user, AnonymousUser):
            # Store the obtained tokens in your app's database
            token = Salesforce(
                user=request.user,
                access_token=token_data['access_token'],
                refresh_token=token_data['refresh_token'],
                instance_url=token_data['instance_url'],
            )
            token.save()

        return redirect('welcome')
    else:
        # Handle OAuth error
        return render(request, 'error.html', {'message': 'OAuth error'})
