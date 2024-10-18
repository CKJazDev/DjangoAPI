from django.shortcuts import render

#Create yoyr views here:
def login_views(request):
    template_name = "auth-login.html"
    
    return render(request, template_name)
