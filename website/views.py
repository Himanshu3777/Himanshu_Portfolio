from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pickdata

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')


def submit_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        if(name and email and message):
            Pickdata.objects.create(name=name, email=email, message=message); # sara dat name email etc models ke variable se match hona chahiye
            return redirect("contact")
        else:
            return HttpResponse("plase provided all data");
    return redirect('contact') # contact yah urls.py me contact url ka nam hai contact


    def messages_view(request):
    try:
        # कोशिश करें data fetch करने की
        data = Pickdata.objects.all().order_by('-id')
        return render(request, 'messages.html', {'data': data})
    except Exception as e:
        # अगर कोई error आता है, तो उसे पूरा print करके दिखा दें
        error_details = traceback.format_exc()
        return HttpResponse(f"<h1>❌ Server Error Details</h1><pre>{error_details}</pre>", status=500)
