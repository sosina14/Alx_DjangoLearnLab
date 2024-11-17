server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
