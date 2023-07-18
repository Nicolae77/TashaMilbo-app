# Deployment


Login to `gcloud`
```sh
gcloud auth application-default login
```

To deploy app to GCP App Engine
```sh
gcloud app deploy
```
To run the django app in gloud
```sh
gcloud app browse
```

Start proxy for DB in order to develop from local and connect to cloud DB
Open a terminal and run the proxy server
```sh
.\cloud-sql-proxy django-e-commerce-392411:europe-west4:django-e-commerce-db
```
Open a second terminal and run the Django app
```sh
python manage.py runserver
```

---

In caz de eroare 
The proxy has encountered a terminal error: unable to start: [django-e-commerce-392411:europe-west4:django-e-commerce-db] Unable to mount socket: listen tcp 127.0.0.1:5432: bind: An attempt was made to access a socket in a way forbidden by its access permissions.

IP = 127.0.0.1
[PORT] = 5432


```sh
netstat -ano | findstr :[PORT]
```

returns 
```sh
  TCP    0.0.0.0:5432           0.0.0.0:0              LISTENING       5772
  TCP    [::]:5432              [::]:0                 LISTENING       5772
```
Process ID (PID) = 5772

to stop the process

```sh
taskkill /PID [PID] /F
```



Local development in Windows might need these into `requirements.txt`

```txt
pypiwin32==223
pywin32==306
pywinpty==2.0.10
```