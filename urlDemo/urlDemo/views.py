

from ast import Pass
import re
from typing import ParamSpecArgs
from django.shortcuts import render

def aniket123(request) :
    return render(request,"index.html")


def form(request) :
    sum=0
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        sum=n1+n2
        
    except:
        pass
    return render(request,"form.html",{'output':sum})