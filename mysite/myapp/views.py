from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
    
        for link in soup.find_all('a'):
            
            link_address = link.get('href')
            
            if link_address is None or link_address == 'None':
                continue
            else:
                link_text = link.string
                link_address = f'{site}{link_address}' if link_address.startswith('/') else link_address
                Link.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    
    return render(request, 'myapp/result.html',{'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')

