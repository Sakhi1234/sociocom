from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.formsprofile import UpdateForm
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def profileupd(request):
    inp = UpdateForm(request.POST or None)
    if request.method == 'POST' and inp.is_valid():
        username=inp.cleaned_data['username']
        email = inp.cleaned_data['email']
        location = inp.cleaned_data['location']
        about_me = inp.cleaned_data['about_me']
        er=Profile.objects.filter(email=email)[0]
        if location:
            er.location=location
        if about_me:
            er.about_me=about_me
        if request.FILES:
            image = request.FILES['image']
            er.image = image
        er.save()
        return redirect("profile",username=username)
        
    else:
        return render(request, "updateprofile.html", {'form':inp})