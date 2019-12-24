from django.shortcuts import render
from .models import Album


def song(request):
    songs=Album.objects.all()
    list = {'songs':songs}
    return render(request,'song/song.html',list)
def home(request):
    songs=Album.objects.all()
    list={'songs':songs}
    return render(request,'home.html',list)
def songplay(request,slug):
    songs=Album.objects.get(slug=slug)
    return render(request,'play/play.html',{'songs':songs})




