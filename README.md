# dz15_celery_beat



```bash
    ./manage.py migrate
```


```bash
    celery -A core worker --loglevel=INFO
```



```bash
    celery -A core beat -l INFO
```




