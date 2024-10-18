from django.shortcuts import render

#Create yoyr views here:
def home_views(request):
    template_name = "login.html"
    
    return render(request, template_name)