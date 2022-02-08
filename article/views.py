from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from article.models import Blog, Micro_blog, Tags, Categories, Pages
from .convert import markdown2html


# 网站首页
def index_page(request):
    return render(request, "index.html")


# 404页面
def page_not_found(request, *args, **argv):
    return render(request, "404.html")


# 分类页
def category_page(request):
    return render(request, "index.html")


# 标签页
def tags_page(request):
    return render(request, "index.html")


# 微博页
def micro_blog_page(request):
    return render(request, "weibo.html")


# 关于页面
def about_page(request):
    about = Pages.objects.values_list(
        "html_text", "markdown_text", "updated"
    ).filter(name='about')
    if about.exists():
        html_text, markdown_text, updated = about[0]
        # 如果没有更新则更新数据
        if not updated:
            html_text = markdown2html(markdown_text, template=True, standalone=True)
            model = Pages.objects.filter(name='about')[0]
            model.html_text = html_text
            model.updated = True
            model.save()
        return HttpResponse(html_text)
    else:
        return HttpResponse("<h1>Page not found</h1")


# 博客文章页
def blog_article_page(request):
    title = request.GET.get("title")
    content = Blog.objects.values_list("html_text", "markdown_text", "updated").filter(
        title=title)
    if content:
        html_text, markdown_text, updated = content[0]
        if not updated:
            model = Blog.objects.filter(title=title)[0]
            html_text = markdown2html(markdown_text=markdown_text, template=True, standalone=True)
            model.html_text = html_text
            model.updated = True
            model.save()
        # 记录访客数
        model = Blog.objects.filter(title=title)[0]
        model.visits += 1
        model.save()
        return HttpResponse(html_text)
    else:
        return HttpResponse("404 Not found")


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
        items = Blog.objects
        # 特定的分类
        category = request.GET.get("category")
        # 特定的标签
        tags = request.GET.get("tag")
        # 分类
        if category:
            items = items.filter(category__name=category)
        if tags:
            items = items.filter(tags__name=tags)
        # 现在数量
        items = items.values_list("title", "pubdate", "abstract").order_by('-pubdate')[(page - 1) * 10: 10 * page]
        for i in items:
            title, date, text = i
            response_data['data'].append(
                {"title": title, "date": date, "text": text}
            )
        return JsonResponse(response_data)
    else:
        items = Micro_blog.objects.values_list(
            "pubdate", "updated", "markdown_text", "html_text"
        ).order_by('-pubdate')[(page - 1) * 10: 10 * page]
        for item in items:
            pubdate, updated, markdown_text, html_text = item
            if not updated:
                model = Micro_blog.objects.filter(pubdate=pubdate)[0]
                html_text = markdown2html(markdown_text=markdown_text)
                model.html_text = html_text
                model.updated = True
                model.save()
            response_data['data'].append({'date': pubdate, 'text': html_text})
        return JsonResponse(response_data)


def api_pages(request):
    name = request.GET.get("name")
    item = Pages.objects.values_list(
        "text_type", "updated", "html_text", "markdown_text"
    ).filter(name=name)
    if item.exists():
        text_type, updated, html_text, markdown_text = item[0]
        if text_type == 'html':
            return HttpResponse(html_text)
        if not updated:
            model = Pages.objects.filter(name=name)[0]
            html_text = markdown2html(markdown_text=markdown_text, template=True, standalone=True)
            model.html_text = html_text
            model.updated = True
            model.save()
            return HttpResponse(html_text)
    else:
        return HttpResponse("Not found")


# 获取categories
def api_categories(request):
    # 构建响应JSON
    response_data = {
        "status": True,
        "msg": "",
        "data": [],
    }
    categories = Categories.objects.values("name")
    for i in categories:
        i = i['name']
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
    tags = Tags.objects.values("name")
    for i in tags:
        i = i['name']
        response_data['data'].append(i)
    return JsonResponse(response_data)

