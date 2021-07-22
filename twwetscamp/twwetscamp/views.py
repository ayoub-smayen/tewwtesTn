
from django.shortcuts import render
from django.contrib.auth import get_user_model
User=get_user_model()
#views


def mymusic(request):
    return render(request,"mumusic.html")


def photo_uploader(request):
    return render(request,"phot_uploader.html")


def photo_uploader2(request):
    return render(request,"image_gallery.html")

def search_user(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = User.objects.filter(username__contains=query_name)
            #user = qs.order_by("?").first()
            #return (user, None)
            #results = Product.objects.filter(name__contains=query_name)
            return render(request, 'search-user.html', {"results":results})

    return render(request, 'pages/home.html')