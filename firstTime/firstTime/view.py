
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

data={
    'title':'Home Page ',
    'data' : 'Haaram Zadha',
    'number' : [10,20,30,40,50],
    'list' : ['aniket','golu','parasram','nirmala'],
    'student_details' : [
        {'name' : 'aniket','phone' : 80207357357},
        {'name' : 'golu','phone' : 80207357357},
    ]
}

def aboutUs(request) :
     return HttpResponse("Welcome Aniket")

def homePage(request) :
     return render(request,"index.html",data)

def course(request) :
    return HttpResponse("Hello Welcome to new Course")

def courseDetails(request,courseId) :
    return HttpResponse(courseId)