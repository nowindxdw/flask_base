
## Flask base

详细解析flask的安装和使用,对于Flask的扩展包并且实际配置于代码中.

结合《深入理解Flask(JackStouffer)》一书对flask框架各方面应用都有涉及

包括以下实践：
- 1.虚环境构建
- 2.flask框架搭建
- 3.使用Flask_login用户登录认证（也对restful的JWT的token认证方式有HttpAuth包实践）
- 4.Jinja模板和渲染
- 5.用户身份鉴权比较复杂，不建议套用Flask principal包，而是借鉴其思想：
- 对用户id绑定不同的身份对象（role)，每个身份对象包含操作所赋予的权限(permission)
- 在需要权限判定的地方调用鉴权函数完成。(todo)
- 6.使用Nosql数据库包括redis和mongo;数据库选择应根据业务特点灵活使用。
- 7.构建Restful的API  Flask-restful
- 8.使用Celery+RabbitMQ配置异步队列，并配置Flower监控，实现监控用户登录和登出发送消息(todo)
- 9.常用Flask扩展  Flask-cache
- 10.编写一个Flask扩展并添加到应用（此处使用视频扩展作例子）(todo)
- 11.测试Flask应用（单元测试）使用assert语句组合（unittest库）+用户界面测试（selenium)
使用coverage库查看测试覆盖率，最后测试驱动开发的实践（TDD)(todo)
- 12.代码部署
jenkins根据github代码推送自动构建并使用nginx+uWsgi并打包在Docker的方式部署
该方法适用于各个云服务器或私有化部署(todo)


###1 virtual env
1.Install ENV
```bash
pip install virtualenv  -i https://pypi.doubanio.com/simple 
```
if error  do `pip install --upgrade pip`  then try

2.Create venv

if your envname = {{venv_name}} 
```bash
virtualenv {{venv_name}}
```
use python3:
```bash
virtualenv -p /usr/bin/python3.5 env3.5
```
not with system site packages:
```bash
virtualenv --no-site-packages {{venv_name}}
```
3.Enter venv:
```bash
source {{venv_name}}/bin/activate
```

```bash
pip list  //show package installed
pip install // install new packages
```
make requirements.txt
```bash
pip freeze > requirements.txt
```

4.Exit venv
```bash
deactivate
```


###2 Build Flask APP


use pip install below  package or `pip install -r requirements.txt  -i https://pypi.doubanio.com/simple `
install latest version Flask :
```bash
pip install Flask flask_sqlalchemy flask_login flask_redis flask_httpauth flask_login flask_wtf  pymysql -i https://pypi.doubanio.com/simple 
```


###3 user auth
HTTPBaisic
在restful设计中，用户认证模式通常使用json web token，而不会使用传统的HTTP Basic认证（传入账号密码）
token认证模式如下：
在请求header中Authorization加入token(JWT(json web token) on branch jwt_auth)


#### structure

|.env35                         #virtual env

|---apps                        # app main files 
    
|   |---file                    # application for url path /file/*

|   |---user                    # application for url path /user/* 
     
|   |---static                  # static folder for templates use

|   |---templates               # jinja2 html templates

|   |---utils                   # customer utils for public useage

|   |---__init__.py             # init app for db, blueprint etc.

|   |---log.py                  # print runtime log

|   |---setting.py              # system setting not changable

|---test                        # folder for put unitest case

|---config.py                   # all config should in here

|---requirements.txt            # env package list

|---run.py                      # start file 