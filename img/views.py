from django.shortcuts import render
from django.http import  JsonResponse
from .forms import UploadImage


# Create your views here.


# 图片上传接口
def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        response_data = {
            "status": False,
            "msg": "Image format error!",
            "path": ""
        }
        form = UploadImage(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            response_data['status'] = True
            response_data['msg'] = "Image upload successfully"
            entry = form.save()
            response_data['path'] = entry.image.url
        return JsonResponse(response_data)
