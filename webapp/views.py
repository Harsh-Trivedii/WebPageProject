from django.shortcuts import render
from datetime import datetime
from webapp import forms
from webapp.models import UserDataModel

# Create your views here.
def homepage_view(request):
    return render(request,'webapp/main.html')


def currentdatetime_view(request):
    date=datetime.now()
    quote="A day without laughter is a day wasted. - Charlie Chaplin"
    context={
        'date':date,
        'quote':quote,
    }
    return render(request,'webapp/date.html',context)

def userdata_view(request):
    error_message = ""
    if request.method == 'POST':
        form = forms.UserDataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            UserDataModel.objects.create(name=name, email=email)
            context = {
                'name': name,
                'email': email,
            }
            return render(request, 'webapp/formdata.html', context) #to display data directly without saving in database
        else:
            error_message = 'Please submit correct data'
    else:
        form = forms.UserDataForm()

    context = {
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'webapp/form.html', context)


def saveduserdata_view(request):
    users = UserDataModel.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'webapp/saveduserdata.html', context)