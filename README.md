# 執行celery
```bash=
celery -A tasks worker -l info --concurrency=16
celery -A tasks flower --address=0.0.0.0 --port=5566
```
