
## informações do docker
#### docker info 
## Verifica se tem o grupo docker
##### cat /etc/group | grep docker
## Cria groupo do Docker
##### groupadd docker
## verifica se o usuario atual faz parte do grupo
groups #USER 
## adiciona usuario ao grupo 
useradd $USER docker  ou usando (usermod -aG docker  $USER docker)
## lista as imagens existentes na estação 
docker images
## lista as imagens 
docker images ou docker image ls
## busca imagens de acordo com onome 
docker search nome_da_imagem
## faz download da imagem
docker pull nome_da_imagem
## run shell em um conteiner ja instalado por exemplo ubuntu
docker run -it ubuntu bash





