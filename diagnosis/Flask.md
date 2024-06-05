WSGI

WERKZEUG

Jinja2





执行 flask run 命令时，Flask 会使用内置的开发服务器来运行程序。这个服务器默认监听本地机的 5000 端口

内置的开发服务器只能用于开发时使用，部署上线的时候要换用性能更好的生产服务器

 Flask 默认会假设你把程序存储在名为 app.py 或 wsgi.py 的文件中。如果你使用了其他名称，就要设置系统环境变量 FLASK_APP 来告诉 Flask 你要启动哪个程序

FLASK_DEBUG 用来开启调试模式（debug mode）。调试模式开启后，当程序出错，浏览器页面上会显示错误信息；代码出现变动后，程序会自动重载。

为了不用每次打开新的终端会话都要设置环境变量，我们安装用来自动导入系统环境变量的 python-dotenv：

Flask 版本是 2.3 或更高版本，则可以直接使用 --debug 命令行选项来开启调试模式

返回值作为响应的主体，默认会被浏览器作为 HTML 格式解析

一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现

我们也可以在 URL 里定义变量部分

```python
@app.route('/user/<name>')
def user_page(name):
    return 'User page'
```

















