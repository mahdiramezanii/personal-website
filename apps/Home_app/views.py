from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .models import *
from django.http import JsonResponse
class HomeView(View):

    def get(self,request):
        context={}

        information=Information.objects.all().last()
        eduction=Eduction.objects.all()
        working=Working.objects.all()
        maharat=Maharat.objects.all()
        work_sample=work_samples.objects.all()

        context["information"]=information
        context["eduction"]=eduction
        context["working"]=working
        context["maharat"]=maharat
        context["work_sample"]=work_sample




        return render(request,"Home_app/Home.html",context)


    def post(self,request):

        name=request.POST.get("name")
        email=request.POST.get("email")
        text=request.POST.get("text")


        print(name)
        print(email)
        print(text)

        if name and email and text:

            Coutact_us.objects.create(name=name,email=email,text=text)

            return JsonResponse({"response":"پیام شما ارسال شد"})

        else:
            return redirect("Home_app:Home")