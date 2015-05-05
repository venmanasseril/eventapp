from django.http import HttpResponse
from eventapp.models import User
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
#from django.core.urlresolvers import reverse
#
def index(request):
    context = {}

    return render(request, 'eventapp/index.html', context)


def register(request):
    context = {}
    return render(request, 'eventapp/register.html', context)


def login_success(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            context = {}
            return render(request, 'eventapp/login_success.html', context)
        else:
            return HttpResponse("User Not Active")  # Return a 'disabled account' error message
    else:
        return HttpResponse("Invalid user")
        # Return an 'invalid login' error message.


def update(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.mobile = request.POST['mobil']
        user.save()

        # cursor = connection.cursor()

        # cursor.execute("UPDATE auth_user SET first_name = '%s', last_name = '%s', email = '%s' WHERE username = '%s'" % (first_name,last_name,email,username))

        return render_to_response('eventapp/update.html', {'user': User.objects.get(id=request.user.id)},
                                  context_instance=RequestContext(request))

        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        #row = cursor.fetchone()

        #return row

    return render_to_response('eventapp/login_success.html', {'user': request.user}, context_instance=RequestContext(request))
    # return render(request,'eventapp/loginProfile.html',context)


def edit(request):
    context = {}
    return render(request, 'eventapp/edit_success.html', context)


#def update(request):
#    context = {}
#    return render(request, 'eventapp/update.html', context)


def regis_success(request):
    fname = request.POST.get("username")
    email = request.POST.get("email")
    pasword = request.POST.get("password")
    mobil =request.POST.get("mobil")
    user = User.objects.create_user(username=fname, email=email,mobil=mobil, password=pasword)
    user.save()
    context = {}

    return render(request, 'eventapp/success.html', context)
    # return HttpResponse("You're Logged In User_id%s." % user_id)
    #
    # def results(request, user_id):
    #    response = "You're looking at the results of user %s."
    #    return HttpResponse(response % user_id)