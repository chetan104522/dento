from django.shortcuts import render
from django.core.mail import send_mail
# from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        #send email
        send_mail(
            'message_name', # subject
            'message', # message
            'message_email', # from email
            ['chetan.patel12796@gmail.com'], # To email
        )

        return render(request,'contact.html',{'message_name':message_name})
    else:    
        return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})

def pricing(request):
    return render(request,'pricing.html',{})   

def blog_details(request):
    return render(request,'blog-details.html',{}) 

def blog(request):
    return render(request,'blog.html',{})     

def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_date = request.POST['your-date']
        your_scheldule = request.POST['your-scheldule']
        your_message = request.POST['your-message']
        return render(request,'appointment.html',{ 
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_date': your_date,
            'your_scheldule': your_scheldule,
            'your_message': your_message })    
    else:
        return render(request,'home.html',{})