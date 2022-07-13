从刚开始接触博客到现在用过`WordPress`这种有特别多插件的博客也用过`Hexo`这种静态博客，虽然功能很全也蛮好看的，但是总有一点地方不太满意，比如有时候并不想那么长的博客，想要添加一个微博的功能，修改那些主题很麻烦，所以就想写一个自己的博客，完全的定制化。

### 技术栈

**后端**：Django

**数据库**：MySQL

**前端**：Tailwind CSS

**Markdown渲染**：Pandoc

## Feature

- [x] 支持Markdown语法，支持Latex公式，支持代码高亮，支持Mermaid绘图
- [x] 博客详情页单页展示，沉浸式阅读体验
- [x] 支持发表微博
- [x] 移动端适配
- [x] 集成简易图床，支持网页上传于命令行上传
- [x] 支持Typora插件上传图片
- [x] 支持通过Docker安装
- [ ] 支持黑夜模式

## 通过Docker安装

下载源码

```sh
git clone https://github.com/hdddl/SimbleBlog.git	# 下载源码
```

编辑配置文件

```shell
cd SimbleBlog 
vim ./blog/env.py
```

`HOST`为网站名称，`SECRET_KEY`可以随便填写最好复杂一些，database可以参考django官网上面的填法，这里默认使用`sqlite3`也提供了`MySQL`的模板

```python
HOST = "HOST"

SECRET_KEY = "SECRET"

DATABASES = {
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST',
        'PORT': 'PORT',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    },
    "default": {
        'ENGINE': "django.db.backends.sqlite3",
        'NAME': 'blog.sqlite3',
    }
}

DEBUG = True
```
通过Docker构建
```shell
sudo docker-compose up
```
数据库迁移
```shell
sudo docker-compose exec blog python manage.py migrate
```
创建 super user
```shell
sudo docker-compose exec blog python manage.py createsuperuser
```

现在就可以在`13248`端口访问博客了
