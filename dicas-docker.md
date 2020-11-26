
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
docker run nome_da_imagem
## mostra os container que estao em atividade
docker ps
## mostra os container que estao em atividade e os que estão parados
docker ps-a
## Remover um container
docker rm id_ou_apelido
## Colocar apelidos nos containers 
docker run --name ubuntinho ubuntu
## Informações de uso de Hardware do containe 
docker stats id_ou_apelido
## mapear porta do container
### Estamos informando que a porta 8080 no Host é aberta e deve ser mapeada na porta 80 do container
docker run -it -p 8080:80 ubuntu
docker run -it -p 8080:80 nginx





