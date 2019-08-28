# todoapp

## Getting started

First, create new virtual environment and activate, of course:

```console
$  git clone https://github.com/andreytsykh/todoapp.git
$  cd todoapp
$  virtualenv venv
$  source venv/bin/activate
```
Then install requirements:

```console
(venv) $ pip install -r requirements.txt
```
For run app:

```console
$ flask init-db
$ flask run
```

API description

POST /                 request body {lists : [{field:value, ...}, {field:value, ...}]}
POST /list_id/tasks    request body {task: {filed:value, ...}}
DELETE tasks/task_id 
PATCH tasks/task_id    request body {field : value}
PATCH tasks/tack_id/finish

