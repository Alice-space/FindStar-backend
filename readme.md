# 521 来自宇宙的告白 （后端）
[521 来自宇宙的告白](http://find-star.xgb.phy.pku.edu.cn/)

## 初始化配置
```shell
cd /path/to/project
cp config/config.example.ini config/config.ini
```
编辑 config.ini 文件
```shell
poetry install --no-dev -E mysql -E asgi
poetry shell
python manage.py makemigrations
python manage.py migrate
python manage.py compilemessages
```

## 导入数据
```shell
poetry shell
python import_data.py
python import_data2.py
```

## supervisor 配置
```conf
[fcgi-program:find-star]
socket=tcp://localhost:10804
command=/path/to/bin/daphne -v 0 --fd 0 --proxy-headers star.asgi:application
directory=/path/to/FindStar-backend/
autorestart=true
startsecs=3
startretries=3
stdout_logfile=/paht/to/log/find-star.out.log
redirect_stderr=true
stdout_logfile_maxbytes=2MB
user=root
priority=999
numprocs=2
process_name=%(program_name)s_%(process_num)02d
```

## nginx 配置
```nginx
    location ~ ^/(graphql|admin) {
        proxy_pass http://127.0.0.1:10804;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static {
        alias /path/to/FindStar-backend/assets;
        expires      12h;
        error_log /dev/null;
        access_log off;
    }
    location /media/media {
        alias /path/to/FindStar-backend/media/;
        expires      30d;
        error_log /dev/null;
        access_log off;
    }
```