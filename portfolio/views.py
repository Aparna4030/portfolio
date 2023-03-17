from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from . models import *

def first(request):
    return render(request,'indexx.html')

def indexx(request):
    return render(request,'indexx.html')

def portfo(request):
    return render(request,'portfo.html')

def portforeg(request):
    return render(request,'portforeg.html')
    
def portforeg(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        uemail=request.POST.get('uemail')
        upassword=request.POST.get('upassword')
        uabout=request.POST.get('uabout')
        log=usereg(uname=uname,uemail=uemail,upassword=upassword,uabout=uabout)
        log.save()
        return redirect(portfologg)
    return render(request,'portforeg.html')


def portfologg(request):
    uemail = request.POST.get('uemail')
    upassword = request.POST.get('upassword')
    if uemail == 'admin@gmail.com' and upassword =='admin':
        request.session['logindetail'] = uemail
        request.session['admin'] ='admin'
        return render(request,'adminlogin.html')

    elif usereg.objects.filter(uemail=uemail,upassword=upassword).exists():
        request.session.flush()
        userre=usereg.objects.get(uemail=request.POST['uemail'],upassword=upassword)
        if userre.upassword == request.POST['upassword']:
            request.session.flush()
            request.session['uid'] = userre.id
            request.session['uname'] = userre.uname
            request.session['uemail'] = userre.uemail
            request.session['user'] = 'user'
            return render(request,'userlogin.html')
    else:
            return render(request, 'portfolog.html', {'status': 'failed'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(indexx)

def adminlogin(request):
    return render(request,'adminlogin.html')

def userlogin(request):
    return render(request,'userlogin.html')

def personaldet(request):
    return render(request,'personaldet.html')

def persodet(request):
    tosession=request.session['uid']
    if request.method=='POST':
        uname=request.POST.get('uname')
        udob=request.POST.get('udob')
        ucontact=request.POST.get('ucontact')
        uemail=request.POST.get('uemail')
        uaddress=request.POST.get('uaddress')
        uabout=request.POST.get('uabout')
        log=personaldetails(uname=uname,udob=udob,ucontact=ucontact,uemail=uemail,uaddress=uaddress,uabout=uabout,tosession=tosession)
        log.save()
        return redirect(edudet)
    return render(request,'personaldet.html')
    

def educationdet(request):
    return render(request,'educationdet.html')

def edudet(request):
    tosession=request.session['uid']
    if request.method=='POST':
        upostgraduate=request.POST.get('upostgraduate')
        uundergraduate=request.POST.get('uundergraduate')
        uhighersecondary=request.POST.get('uhighersecondary')
        uhighschool=request.POST.get('uhighschool')
        log=educationdetails(upostgraduate=upostgraduate,uundergraduate=uundergraduate,uhighersecondary=uhighersecondary,uhighschool=uhighschool,tosession=tosession)
        log.save()
        return redirect(ski)
    return render(request,'educationdet.html')

def skills(request):
    return render(request,'skills.html')

def ski(request):
    tosession=request.session['uid']
    if request.method=='POST':
        uskill1=request.POST.get('uskill1')
        uskill2=request.POST.get('uskill2')
        uskill3=request.POST.get('uskill3')
        uskill4=request.POST.get('uskill4')
        log=skillset(uskill1=uskill1,uskill2=uskill2,uskill3=uskill3,uskill4=uskill4,tosession=tosession)
        log.save()
        return redirect(achieve)
    return render(request,'skills.html')

def achievements(request):
    return render(request,'achievements.html')

def achieve(request):
    tosession=request.session['uid']
    if request.method=='POST':
        uachievement1=request.POST.get('uachievement1')
        uachievement2=request.POST.get('uachievement2')
        uachievement3=request.POST.get('uachievement3')
        log=achievement(uachievement1=uachievement1,uachievement2=uachievement2,uachievement3=uachievement3,tosession=tosession)
        log.save()
        return redirect(exp)
    return render(request,'achievements.html')

def experience(request):
    return render(request,'experience.html')

def exp(request):
    tosession=request.session['uid']
    if request.method=='POST':
        uexp1=request.POST.get('uexp1')
        uexp2=request.POST.get('uexp2')
        uexp3=request.POST.get('uexp3')
        log=experien(uexp1=uexp1,uexp2=uexp2,uexp3=uexp3,tosession=tosession)
        log.save()
        return redirect(ref)
    return render(request,'experience.html')

def references(request):
    return render(request,'references.html')

def ref(request):
    tosession=request.session['uid']
    if request.method=='POST':
        uref1=request.POST.get('uref1')
        uref2=request.POST.get('uref2')
        log=referen(uref1=uref1,uref2=uref2,tosession=tosession)
        log.save()
    return render(request,'references.html')

# def pview(request):
#     return render(request,'resumeview.html')

def pview(request):
    tem=request.session['uid']
    ab=achievement.objects.get(tosession=tem)
    abc=educationdetails.objects.get(tosession=tem)
    abd=experien.objects.get(tosession=tem)
    abe=personaldetails.objects.get(tosession=tem)
    abf=referen.objects.get(tosession=tem)
    abg=skillset.objects.get(tosession=tem)
    return render(request,'resumeview.html',{'result':ab,'result1':abc,'result2':abd,'result3':abe,'result4':abf,'result5':abg})
    