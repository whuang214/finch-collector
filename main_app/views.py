from django.shortcuts import render

# home controller
def home(request):
    # format is render(request, template_name, context)
    # request is the request object
    # template_name is the path to the template
    # context is optional (data you want to pass to the template)
    return render(request, 'home.html')