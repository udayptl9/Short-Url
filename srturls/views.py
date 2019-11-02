from django.shortcuts import render
from .models import Urls
# Create your views here.
def home(request):
    urls = Urls.objects.all()
    context = {'urls': urls}
    if request.method == "POST":
        title = request.POST['title']
        fullurl = request.POST['fullurl']
        newUrl = Urls(title = title, fullurl = fullurl, creater = request.user)
        newUrl.save()
    return render(request, 'srturls/index.html', context)

def showurl(request, id):
    url = Urls.objects.get(id = id)
    context = {'url': url}
    return render(request, 'srturls/shorturl.html', context)