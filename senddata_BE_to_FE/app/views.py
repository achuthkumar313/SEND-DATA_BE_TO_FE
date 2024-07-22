from django.shortcuts import render

# Create your views here.
def send_data (request):
    context={'name':'Achuth Kumar','age':23,'Gender':'Male'}
    return render(request,'send_data.html',context)