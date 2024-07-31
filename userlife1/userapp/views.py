from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render, redirect
# myapp/views.py
from django.contrib import messages
from .models import userprofile



def createuserProfile(request):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        DOB = request.POST.get('DOB')
        bio = request.POST.get('bio')
        skills = request.POST.get('skills')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        p = userprofile(fullname=fullname, DOB=DOB,bio=bio,skills=skills,email=email,phone=phone)
        p.save()

    return render(request, 'userprofile.html')


def listdetails(request):
    values = userprofile.objects.all()
    paginator = Paginator(values, 3)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'printvalues.html', {'values': values, 'page': page})

def updatedetails(request, p_id):
    p=userprofile.objects.get(id=p_id)
    if request.method=='POST':
        fullname = request.POST.get('fullname')
        DOB = request.POST.get('DOB')
        bio = request.POST.get('bio')
        skills = request.POST.get('skills')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        p.fullname=fullname
        p.DOB=DOB
        p.bio = bio
        p.skills = skills
        p.email = email
        p.phone = phone
        p.save()
        return redirect('details')
    return render(request, 'updatevalues.html', {'p':p})

def deletedetails(request,p_id):
    p = userprofile.objects.get(id=p_id)
    p.delete()
    return redirect('details')
    return render(request, 'printvalues.html', {'p': p})