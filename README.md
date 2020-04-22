
## Flask base


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
pip install Flask flask_sqlalchemy flask_login flask_redis flask_httpauth flask_login pymysql -i https://pypi.doubanio.com/simple 
```

