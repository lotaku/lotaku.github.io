Title: Pelican 学习笔记
Subtitle:包括主题配置和插件使用等
Slug:pelican-learn
Date: 2014-10-06 10:20
Category: Tools

### 学习材料
官方文档：http://docs.getpelican.com/en/3.3.0/
### 介绍
可以在github上搭建一个全静态化的博客网站.

###安装等准备工作
http://docs.getpelican.com/en/3.3.0/getting_started.html

###pelican theme tool
http://docs.getpelican.com/en/3.3.0/pelican-themes.html

###开启/停止本地web服务器：
```bash
alias myblogst='cd ~/app/myblog/ &&./develop_server.sh start'
alias myblogsp='cd ~/app/myblog/ &&./develop_server.sh stop'
```
创建一个新的博客项目：

### 进入新建的目录，比如myblog目录

```bash
$pelican-quickstart
```

### 同步网站：(同步方法在执行pelican命令时可选)
```bash

make rsync_upload
其他命令：
升级pelican：$ pip install --upgrade pelican
```
###网站配置文件：pelicanconf.py
```bash

不使用content文件夹下的子目录做分类标志：USE_FOLDER_AS_CATEGORY=False
文章摘要长度：SUMMARY_MAX_LENGTH
设置提取文件名元数据的正则表达式：FILENAME_METADATA
是否在主目录显示page：DISPLAY_PAGES_ON_MENU
```
###工具

Fabric :对一些pelican命令的封装 方便使用（我再也不用使用./bashrc的别名来执行pelican的命令，虽然还是很好用的）

```bash
fab安装：pip install Fabric
fab常用命令：
生成网站：fab build
重新生成网站：fab regenerate
启动web服务器：fab serve
开启ssh:fab publish
```

Make:也是一些pelican命令的封装

```bash
生成网站：make html
重新生成网站：make regenerate
启动web服务器：make serve
重新生成网站并且再次启动web服务器：make devserver
```

### 设置评论：disqus
1. 注册并登录 http://disqus.com/

2. 添加新的网站
```bash

Site name ：{任意名字}
Choose your unique Disqus URL: {lotaku}.disqus.com
#lotaku是短域名，要记住的！在pelicanconf.py的配置中要用到。
进入Admin > Settings > Advanced,将以下域名添加到 Trusted Domains

lotaku.github.io #我的博客域名
127.0.0.1        #本地调试域名
localhost        #本地调试域名
打开博客项目根目录下的配置文件

#pelicanconf.py 添加:
SITEURL = 'http://lotaku.github.io'
#如果要在本地调试测试显示disqus,修改SITEURL
#SITEURL = 'http://127.0.0.1:8000'
THEME =u'/home/l/app/myblog3/mytheme/pelican-elegant-1.3'
DISQUS_SITENAME = u'lotaku'
```

### 主题设置

使用中的主题：[pelican-elegant-1.3](http://oncrashreboot.com/elegant-best-pelican-theme-features)

### 使用记录
```bash
#在pelicanconf.py 中添加,以下代码，主题的搜索等功能需要

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
```

###备份整个博客
```bash
alias myblogbackup_to_dropbox='cp -r ~/app/myblog/* ~/Dropbox/myblog/'
```