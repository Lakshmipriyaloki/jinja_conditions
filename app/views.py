from django.shortcuts import render

# Create your views here.
def jinja_conditions(request):
    d={'name':'nani','num':20}
    d1={'a':1,'b':5,'c':3}
    return render(request,'jinja_conditions.html',context=d1)