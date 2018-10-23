# volatile-db-components

Proyect to test volatile databases with docker & python

## Getting Started

```
git clone git@github.com:agrojas/volatile-db-components.git
cd volatile-db-components
```
### Prerequisites

What things you need to install the software and how to install them

```
docker
python3
virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
 python3 -m venv venv
```

```
 . venv/bin/activate
```

```
pip install -r requirements.txt
```

### Use

```
$ python3 app.py

Image_list [<Image: 'mysql:5.6'>]
$ docker run -v {'path/config/mysql': {'bind': '/docker-entrypoint-initdb.d', 'mode': 'rw'}} -e {'MYSQL_ROOT_PASSWORD': 'mysql'} -p {'33061': '3306'}--name some-mysql -d mysql:5.6 
<Container: 8e1a9c0685>

```

```
python3 get.py
GET container
8e1a9c0685
some-mysql
exited
[Container Logs----->]
```


```
python3 stop.py
STOP container
<Container: 8e1a9c0685>
```
