

from ast import Pass
import re
from typing import ParamSpecArgs
from django.shortcuts import render

def aniket123(request) :
    return render(request,"index.html")


def form(request) :
    try:
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        print(n1+n2)
        
    except:
        pass
    return render(request,"form.html")