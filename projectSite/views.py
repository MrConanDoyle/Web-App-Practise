from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    'variable' : "Site Connected!!!",
    'name' : "Adnan Habib",
    'projectName': "Event Manager"
  }
  return render(request, "index.html", context)
  # return HttpResponse("Hello, My first Project.")

def userFunc(request):
  return HttpResponse("Getting User Info!!!")