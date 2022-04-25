from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from img.models import Album
from img.forms import UploadImage
from blog.env import HOST


# Create your views here.


# 图片上传接口
@login_required(login_url='/admin')
def upload(request):
    if request.method == 'GET':
        album_object = Album.objects.values("name")
        context = {
            "album": {

            }
        }
        cnt = 1
        for i in album_object:
            context["album"][str(cnt)] = i['name']
            cnt = cnt+1
        return render(request, 'upload.html', context=context)
    else:
        response_data = {
            "status": False,
            "msg": "Image format error!",
            "path": ""
        }
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            response_data['status'] = True
            response_data['msg'] = "Image upload successfully"
            entry = form.save()
            response_data['path'] = HOST + "/media" + entry.image.url
        return JsonResponse(response_data)
