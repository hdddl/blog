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
            "album": {}
        }
        cnt = 1
        for i in album_object:
            context["album"][str(cnt)] = i['name']
            cnt = cnt + 1
        return render(request, 'upload.html', context=context)
    else:
        context = {
            "direct_Link": "",
            "Markdown_Link": "",
            "HTML_Link": "",
        }
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            imageUrl = HOST + "/media" + entry.image.url  # 获取直链
            imageName = entry.image.name.split("/")[-1]  # 获取图片名称
            imageName = imageName.split(".")[0]
            context["direct_Link"] = imageUrl
            context["Markdown_Link"] = "![%s](%s)" % (imageName, imageUrl)
            context["HTML_Link"] = "<img src=\"%s\" alt=\"%s\">" % (imageUrl, imageName)
            if "direct" in request.headers:
                return JsonResponse({"status": True, "path": entry.image.url})
        return render(request=request, template_name="uploadSuccess.html", context=context)
