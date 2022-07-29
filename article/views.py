from django.shortcuts import render
from urllib.parse import quote
from django.http import HttpResponse
from article.models import Blog, Micro_blog, Tags, Categories, Pages


# 网站首页
def index_page(request):
    # get categories data
    categories = []
    for i in Categories.objects.values("name"):
        metadata = {
            "url": "?category=" + quote(i['name']),
            "name": i['name']
        }
        categories.append(metadata)
    # get tags data
    tags = []
    for i in Tags.objects.values("name"):
        metadata = {
            "url": "?tag=" + quote(i['name']),
            "name": i['name']
        }
        tags.append(metadata)

    # get blog
    blogs = []
    blog_object = Blog.objects
    get_category = request.GET.get("category")
    get_tag = request.GET.get("tag")
    get_page = request.GET.get('page')
    if not get_page or not get_page.isdigit():
        get_page = 1
    get_page = int(get_page)
    if not request.user.is_authenticated:   # 对未登入用户隐藏私密文章与博客
        blog_object = blog_object.filter(public=True)
    if get_category:  # filter category
        blog_object = blog_object.filter(category__name=get_category)
    if get_tag:  # filter tag
        blog_object = blog_object.filter(tags__name=get_tag)
    blog_object = blog_object.values_list("title", "pubdate", "abstract").order_by("-pubdate")[
                  (get_page - 1) * 10: 10 * get_page]
    for i in blog_object:
        title, date, abstract = i
        metadata = {
            "title": title,
            "date": date,
            "abstract": abstract,
            "url": "/blog?title=" + quote(title)
        }
        blogs.append(metadata)
    context = {
        "tags": tags,
        "categories": categories,
        "blogs": blogs,
        "page": {
            "previous": 1 if get_page <= 1 else get_page - 1,
            "next": get_page + 1
        }
    }
    return render(request, "index.html", context=context)


# 微博页
def micro_blog_page(request):
    micro_blogs = []
    get_page = request.GET.get('page')
    if not get_page or not get_page.isdigit():
        get_page = 1
    get_page = int(get_page)
    micro_blog_object = Micro_blog.objects
    if not request.user.is_authenticated:   # 对未登入用户隐藏私密文章与博客
        micro_blog_object = micro_blog_object.filter(public=True)
    micro_blog_object = micro_blog_object.values_list("html_text", "pubdate").order_by("-pubdate")[
                        (get_page - 1) * 10: 10 * get_page]
    for i in micro_blog_object:
        text, pubdate = i
        metadata = {
            "text": text,
            "date": pubdate
        }
        micro_blogs.append(metadata)
    context = {
        "microBlogs": micro_blogs,
        "page": {
            "previous": 1 if get_page <= 1 else get_page - 1,
            "next": get_page + 1
        }
    }

    return render(request, "weibo.html", context=context)


# 404页面
def page_not_found(request, *args, **argv):
    return render(request, "404.html")


# 分类页
def category_page(request):
    return render(request, "index.html")


# 标签页
def tags_page(request):
    return render(request, "index.html")


# 关于页面
def about_page(request):
    about = Pages.objects.values_list("html_text").filter(title='about')
    if about.exists():
        html_text = about[0]
        return HttpResponse(html_text)
    else:
        return HttpResponse("<h1>Page not found</h1")


# 博客文章页
def blog_article_page(request):
    title = request.GET.get("title")
    blog_object = Blog.objects
    if not request.user.is_authenticated:   # 对未登入用户隐藏私密文章与博客
        blog_object = blog_object.filter(public=True)
    content = blog_object.filter(title=title)
    if content:
        # 记录访客数
        model = Blog.objects.filter(title=title)[0]
        html_text = model.html_text
        model.visits += 1
        model.save()
        return HttpResponse(html_text)
    else:
        return HttpResponse("404 Not found")


# 返回特殊自创页面
def api_pages(request):
    name = request.GET.get("name")
    item = Pages.objects.values_list("html_text").filter(title=name)
    if item.exists():
        html_text = item[0]
        return HttpResponse(html_text)
    else:
        return HttpResponse("Not found")
