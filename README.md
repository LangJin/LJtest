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