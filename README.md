
## Flask base

- 详细解析flask的安装和使用
- 对于Flask的扩展包并且实际配置于代码中
- 结合《深入理解Flask(JackStouffer)》一书对flask框架各方面应用都有涉及

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
token认证模式如下：在请求header中加入token

JWT(json web token) on branch jwtAuth

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