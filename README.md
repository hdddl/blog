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

## 开始使用

#### 1. 直接安装

首先安装`Mysql`数据库

```shell
sudo apt install mysql
```

安装`Pandoc`用于`Markdown`渲染

```shell
sudo apt install pandoc
```

下载源码安装

```shell
git clone https://github.com/hdddl/SimbleBlog.git	# 下载源码
cd SimbleBlog
pip3 install -r requirements.txt		# 安装Django
```

安装`Nginx`进行反向代理

```shell
sudo apt install nginx
```

配置`Nginx`

```

```

#### 2. 通过Docker安装

