# LJtest浪晋的测试小讲堂
基于Flask实现的一个前后端分离的项目

自动生成requirements文件
```
pip freeze >requirements.txt
```
自动安装requirements里的包
```
pip install -r requirements.txt
```


错误页面
```python
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

为了解决最新版本的谷歌浏览器不让我去读取cookies的问题。
我只能弃用了session的处理方式。
增加了redis赖代替session.
当前代码是测谈网的后端。
搭建环境需要python3+MySQL5.7+Redis+gunicorn。
前端环境需要使用tomcat另行搭建。

如今这个项目，是真的前后端分离了。
我觉得按现在的节奏做下去，
下一步我是不是就得考虑上nginx了？负载均衡？
然后分布式？集群?
天知道，我本来只想做一个demo的。
