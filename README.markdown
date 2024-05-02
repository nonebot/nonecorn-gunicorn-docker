#  nonecorn with  gunicorn for process manegement

### usage
```bash
docker run --name py -v /apppath:/app -v /logpath:/log nonecorn-gunicorn-docker:python3.10-slim
```

### config: use environ args

- bind, default= "0.0.0.0"
- port, default= 9000
- wsgi_app, default= "main:app"
- timeout, default= 30
- workers, default= 1
- worker_class, default= "hypercorn.workers.HypercornUvloopWorker"
- worker_connections, default= 10000
- loglevel, default= "debug"
- access_log_format, default= '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"')
- errorlog, default= "/log/error.log"
- websocket_max_message_size
- websocket_ping_interval
