from django.shortcuts import render
from event.models import *
from django.core.mail import EmailMessage
from .forms import EmailForm
from django.conf import settings



def login(request):
	msg=""
	if request.method=="POST":
		p_emailid=request.POST["emailid"]
		p_password=request.POST["password"]
		
		if RegisterDetails.objects.filter(emailid=p_emailid,password=p_password).exists():

			request.session["emailid"]=p_emailid
			return render(request,"home2.html")
		else:
			msg="Invalid Login Details"
	return render(request,"login.html",{"msg":msg})



def login1(request):
	msg=""
	if request.method=="POST":
		p_emailid=request.POST["emailid"]
		p_password=request.POST["password"]
		
		if RegisterDetails1.objects.filter(emailid=p_emailid,password=p_password).exists():

			request.session["emailid"]=p_emailid
			return render(request,"home1.html")
		else:
			msg="Invalid Login Details"
	return render(request,"login1.html",{"msg":msg})



def changepasswordA(request):
	msg=""
	if request.method=="POST":
		currentpassword=request.POST["currentpassword"]
		newpassword=request.POST["newpassword"]
		confirmnewpassword=request.POST["confirmnewpassword"]
		p_emailid=request.session["emailid"]
		if newpassword==confirmnewpassword:
			if RegisterDetails.objects.filter(emailid=p_emailid,password=currentpassword).exists():
				RegisterDetails.objects.filter(emailid=p_emailid,password=currentpassword).update(password=newpassword)
				msg="Password Changed Successfully "

			else:
				msg="Invalid Password"
		else:
			msg="New Password And Confirm New Password Must Same"
	return render(request,"changepasswordA.html",{"msg":msg})



def changepassword(request):
	msg=""
	if request.method=="POST":
		currentpassword=request.POST["currentpassword"]
		newpassword=request.POST["newpassword"]
		confirmnewpassword=request.POST["confirmnewpassword"]
		p_emailid=request.session["emailid"]
		if newpassword==confirmnewpassword:
			if RegisterDetails1.objects.filter(emailid=p_emailid,password=currentpassword).exists():
				RegisterDetails1.objects.filter(emailid=p_emailid,password=currentpassword).update(password=newpassword)
				msg="Password Changed Successfully "

			else:
				msg="Invalid Password"
		else:
			msg="New Password And Confirm New Password Must Same"
	return render(request,"changepassword.html",{"msg":msg})



def register(request):
	msg=""
	if request.method=="POST":
		rd=RegisterDetails()
		rd.fullname=request.POST["fullname"]
		rd.address=request.POST["address"]
		rd.mobilenumber=request.POST["mobilenumber"]
		rd.emailid=request.POST["emailid"]
		rd.password=request.POST["password"]
		rd.save()
		msg="Registerd Successfully"
	return render(request,"register.html",{"msg":msg})



def register1(request):
	msg=""
	if request.method=="POST":
		rd=RegisterDetails1()
		rd.fullname=request.POST["fullname"]
		rd.address=request.POST["address"]
		rd.mobilenumber=request.POST["mobilenumber"]
		rd.emailid=request.POST["emailid"]
		rd.password=request.POST["password"]
		rd.save()
		msg="Registerd Successfully"
	return render(request,"register1.html",{"msg":msg})



def food(request):
	msg=""
	if request.method=="POST":
		fd=FoodDetails()
		fd.food=request.POST["food"]
		fd.plates=request.POST["plates"]
		fd.save()
		msg="Registerd Successfully"
	return render(request,"food.html",{"msg":msg})



def registerdata(request):
	msg=""
	if request.method=="POST":
		rid=request.POST["rid"]
		RegisterDetails.objects.filter(id=rid).delete()
		msg="Record Deleted Successfully"
	data=RegisterDetails.objects.all()
	return render(request,"registerdata.html",{"data":data, "msg":msg})



def registerdata1(request):
	msg=""
	if request.method=="POST":
		rid=request.POST["rid"]
		RegisterDetails1.objects.filter(id=rid).delete()
		msg="Record Deleted Successfully"
	data=RegisterDetails1.objects.all()
	return render(request,"registerdata1.html",{"data":data, "msg":msg})



def searchregister(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			rid=request.POST["rid"]
			SaveDetails.objects.filter(id=rid).delete()
			msg="Record deleted"
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=SaveDetails.objects.filter(mobilenumber=value)
			elif searchby==2:
				data=SaveDetails.objects.filter(fullname__contains=value)

			if data.exists():
				pass;
			else:
				msg="Record Not Found"
	return render(request,"searchregister.html",{ "data":data, "msg":msg})



def searchregisters(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			rid=request.POST["rid"]
			SaveDetails.objects.filter(id=rid).delete()
			msg="Record deleted"
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=SaveDetails.objects.filter(mobilenumber=value)
			
			if data.exists():
				pass;
			else:
				msg="Record Not Found"
	return render(request,"searchregisters.html",{ "data":data, "msg":msg})



def halldetails(request):
	msg=""
	if request.method=="POST":
		hd=HallDetails()
		hd.venue=request.POST["venue"]
		hd.contactnumber=request.POST["contactnumber"]
		hd.save()
		msg="Hall Details Enterd Successfully"
	return render(request,"halldetails.html",{"msg":msg})



def savehalldetails(request):
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		HallDetails.objects.filter(id=sid).delete()
		msg="Record Deleted Successfully"
	data=HallDetails.objects.all()
	return render(request,"savehalldetails.html",{"data":data, "msg":msg})





def searchhall(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			sid=request.POST["sid"]
			HallDetails.objects.filter(id=sid).delete()
			msg="Record deleted"
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=HallDetails.objects.filter(contactnumber=value)
			elif searchby==2:
				data=HallDetails.objects.filter(functionhallname=value)
			elif searchby==3:
				data=HallDetails.objects.filter(managername=value)
			if data.exists():
				pass;
			else:
				msg="Record(s) Not Found"
	return render(request,"searchhall.html",{ "data":data, "msg":msg})



def chairdetails(request):
	msg=""
	if request.method=="POST":
		cd=ChairDetails()
		cd.stagechair=request.POST["stagechair"]
		cd.scquantity=request.POST["scquantity"]
		cd.chairtype=request.POST["scquantity"]
		cd.quantity=request.POST["quantity"]
		cd.save()
		msg="Registerd Successfully"
	return render(request,"chairdetails.html",{"msg":msg})



def savefood(request):
	msg=""
	if request.method=="POST":
		fid=request.POST["fid"]
		FoodDetails.objects.filter(id=fid).delete()
		msg="Record Deleted Successfully"
	data=FoodDetails.objects.all()
	return render(request,"savefood.html",{"data":data, "msg":msg})



def savechair(request):
	msg=""
	if request.method=="POST":
		cid=request.POST["cid"]
		ChairDetails.objects.filter(id=cid).delete()
		msg="Record Deleted Successfully"
	data=ChairDetails.objects.all()
	return render(request,"savechair.html",{"data":data, "msg":msg})



def decorationtype(request):
	msg=""
	if request.method=="POST":
		dd=DecorationDetails()
		dd.theme=request.POST["theme"]
		dd.eventtype=request.POST["eventtype"]
		dd.celebrationspot=request.POST["celebrationspot"]
		dd.save()
		msg="Registerd Successfully"
	return render(request,"decorationtype.html",{"msg":msg})



def savedecoration(request):
	msg=""
	if request.method=="POST":
		did=request.POST["did"]
		DecorationDetails.objects.filter(id=did).delete()
		msg="Record Deleted Successfully"
	data=DecorationDetails.objects.all()
	return render(request,"savedecoration.html",{"data":data, "msg":msg})



def completeregister(request):
	msg=""
	if request.method=="POST":
		sd=SaveDetails()
		sd.fullname=request.POST["fullname"]
		sd.mobilenumber=request.POST["mobilenumber"]
		sd.quantity=request.POST["quantity"]
		sd.food=request.POST["food"]
		sd.plates=request.POST["plates"]
		sd.venue=request.POST["venue"]
		sd.theme=request.POST["theme"]
		sd.eventtype=request.POST["eventtype"]
		sd.date=request.POST["date"]
		sd.save()
		msg="Registerd Successfully"
	return render(request,"completeregister.html",{"msg":msg})



def saveall(request):
	msg=""
	if request.method=="POST":
		aid=request.POST["aid"]
		SaveDetails.objects.filter(id=aid).delete()
		msg="Record Deleted Successfully"
	data=SaveDetails.objects.all()
	return render(request,"saveall.html",{"data":data, "msg":msg})



def nav(request):
	return render(request,"nav.html")



def home1(request):
	return render(request,"home1.html")



def imghall(request):
	return render(request,"imghall.html")



def imgfood(request):
	return render(request,"imgfood.html")



def imgtheme(request):
	return render(request,"imgtheme.html")



def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            user_mail = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            receiver_mail = form.cleaned_data['receiver_mail']
            subject = form.cleaned_data['subject']
            email_text = form.cleaned_data['email_text']

            email = EmailMessage(
                subject=subject,
                body=email_text,
                from_email=user_mail,
                to=[receiver_mail]
            )
            email.send()
            return render(request, 'success.html', {'receiver_mail': receiver_mail})
    else:
        form = EmailForm()

    return render(request, 'send_email_view.html', {'form': form})



def home2(request):
	return render(request,"home2.html")


# Create your views here.