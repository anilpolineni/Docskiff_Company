from django.shortcuts import render,redirect

from .forms import UserRegisterForm,ItemForm

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from.models import Items


# Create your views here.


def home(request):
	return render(request,'products/home.html')


def register(request):
	if request.method =="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'succssfully registred..!')
			return redirect('login')
	else:
		form=UserRegisterForm()
		return render(request,'products/register.html',{'form':form})

@login_required
def additem(request):
	if request.method=="POST":
		form=ItemForm(request.POST)
		if form.is_valid():
			pro=form.save(commit=False)
			pro.user=request.user
			pro.save()
			item=form.cleaned_data.get('name')
			messages.success(request,"%s  is successfully Added..!"%(item))
		return redirect('showitems')
	else:
		form=ItemForm()
		return render(request,'products/additem.html',{'form':form})

@login_required
def showitems(request):
	user = User.objects.get(id=request.user.id)
	data=Items.objects.filter(user=user)
	context={'data':data}
	return render(request,'products/showitems.html',context)