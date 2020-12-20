from django.shortcuts import render
from quiz_app.models import quizDB

# Create your views here.

def login(request):
	return render(request, 'login.html')

#def startquiz(request):
#    uname = int(request.GET["username"])
#    return render(request, 'startquiz.html', {'name':uname})
	
def startquiz(request):
    return render(request, 'startquiz.html')

def quizpage(request):
    questions = quizDB.objects.all()
    return render(request, 'quizpage.html', {'questions':questions})


	
	
