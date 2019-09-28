from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage, User
from first_app.forms import FormName

# Create your views here.


def index(req):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_rec": webpages_list}
    # my_dict = {"insert_me": "Hello, i am views.py"}
    return render(req, "app/index.html", context=date_dict)
def help(req):
    return render(req, "app/help.html")
def noPage(req):
    return render(req, "app/error.html")
def users(req):
    users_list = User.objects.order_by('first_name')
    user_dict = {"users": users_list}
    return render(req, "app/users.html", context=user_dict)
def forms(req):
    form = FormName()

    if req.method == 'POST':
        form = FormName(req.POST)
        if form.is_valid(): 
            print('VALIDATION SUCCESS!')
            print(form.cleaned_data['name'])

    return render(req, "app/forms.html", {'form': form})
