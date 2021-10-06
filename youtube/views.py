from django.shortcuts import redirect, render
from django.http import HttpResponse

from pytube import YouTube


# Index
def index(request):
    if(request.method == 'POST'):
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_lowest_resolution()
        print(stream)

        
        
        stream.download('~/Downloads')

        # stream.download()
        context = {
            'title':video.title,
            'img':video.thumbnail_url,
            'views':video.views,
            'length':video.length,
            'rating':video.rating,
        }

        
        return render(request,'youtube/video.html',context)

    else:
        return render(request,'youtube/index.html')
    
