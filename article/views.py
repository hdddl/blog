from django.shortcuts import render
from django.http import JsonResponse
from article.models import blog, micro_blog


# 网站首页
def index(request):
    return render(request, "index.html")


# 获取文章目录，默认一页为10条。
def api_content(request):
    # 获取文章类型，博客或者是微博
    content_type = request.GET.get("type")
    # 获取页面，默认一页10条
    page = request.GET.get("page")
    # 构建响应JSON
    response_data = {
        "status": False,
        "msg": "",
        "data": []
    }
    # 验证类型参数是否正确
    if content_type != "blog" and content_type != "micro_blog":
        response_data['msg'] = "parameter type worry"
        return JsonResponse(response_data)
    # 验证page页面参数是否错误
    if page.isdigit() and int(page) > 0:
        page = int(page)
    else:
        response_data['msg'] = "parameter page worry"
        return JsonResponse(response_data)
    # 修改响应状态
    response_data['status'] = True
    if content_type == "blog":
        items = blog.objects.values_list("title", "pubdate", "abstract")
        # 特定的分类
        category = request.GET.get("category")
        # 特定的标签
        tags = request.GET.get("tag")
        # 分类
        if category:
            items = items.filter(category=category)
        if tags:
            items = items.filter(tags=tags)
        # 现在数量
        items = items[(page - 1) * 10: 10 * page]
        for i in items:
            title, date, text = i
            response_data['data'].append(
                {"title": title, "date": date, "text": text}
            )
        return JsonResponse(response_data)
    else:
        items = micro_blog.objects.values_list("pubdate", "content")[(page - 1) * 15: 10 * page]
        for i in items:
            date, text = i
            response_data['data'].append(
                {"date": date, "text": text}
            )
        return JsonResponse(response_data)


# 获取文章正文API
def api_blog(request):
    # 获取文章标题
    title = request.GET.get("title")
    # 构建响应JSON
    response_data = {
        "status": False,
        "msg": "",
        "data": []
    }
    item = blog.objects.values_list("content").filter(title=title)
    if item.exists():
        response_data['status'] = True
        response_data['data'].append({"text": item[0][0]})
        return JsonResponse(response_data)
    else:
        response_data['msg'] = "article is not find"
        return JsonResponse(response_data)


# 获取categories
def api_categories(request):
    # 构建响应JSON
    response_data = {
        "status": True,
        "msg": "",
        "data": [],
    }
    categories = blog.objects.values("category")
    for i in categories:
        i = i['category']
        if i not in response_data['data']:
            response_data['data'].append(i)
    return JsonResponse(response_data)


# 获取tags
def api_tags(request):
    # 构建响应JSON
    response_data = {
        "status": True,
        "msg": "",
        "data": [],
    }
    tags = blog.objects.values("tags")
    for i in tags:
        i = i['tags'].split(',')
        for j in i:
            if j not in response_data['data']:
                response_data['data'].append(j)
    return JsonResponse(response_data)
