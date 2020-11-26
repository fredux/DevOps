## install phpMyAdmin
apt install phpmyadmin
## Cria um arquivo do virtual host no diretorio /etc/nginx/sites-available por exemplo
sudo vi /etc/nginx/sites-available/phpmyadmin.local
## adicione as seguintes linhas
server {
    listen 80;
   # listen [::]:80 default_server ipv6only=on;

    root /usr/share/phpmyadmin;
    index index.php index.html index.htm;

    server_name phpmyadmin.local;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri /index.php =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
## Salve o arquivo e crie um link simbólico
sudo ln -s /etc/nginx/sites-available/phpmyadmin.local /etc/nginx/sites-enabled/

## Edite o arquivo hosts
sudo vi /etc/hosts

## Adicione a linha
127.0.1.1       phpmyadmin.local

## Restarta os servicos
sudo systemctl restart nginx
sudo systemctl restart  php7.4-fpm.service

## No navegador entre com o endereço
phpmyadmin.local





