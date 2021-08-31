
## Informações do docker
#### docker info 
## Verifica se tem o grupo docker
##### cat /etc/group | grep docker
## Cria groupo do Docker
##### groupadd docker
## Verifica se o usuario atual faz parte do grupo
groups #USER 
## Adiciona usuario ao grupo 
useradd $USER docker  ou usando (usermod -aG docker  $USER docker)
## Lista as imagens existentes na estação 
docker images
## Lista as imagens 
docker images ou docker image ls
## Busca imagens de acordo com onome 
docker search nome_da_imagem
## Faz download da imagem
docker pull nome_da_imagem
## Run shell em um conteiner ja instalado por exemplo ubuntu
docker run -it ubuntu bash
# Rodar uma imagem
docker run nome_da_imagem
# Executar um comando sem precisar esta dentro do container
docker exec -it id_ou_apelido comando
## Mostra os container que estao em atividade
docker ps
docker ps -a  (mostra todos inclusive os que já foramo encerrados)
docker ps -a -q (mostra os id do container)
## Mostra os container que estao em atividade e os que estão parados
docker ps-a
## Remover um container
docker rm id_ou_apelido
docker rm $(docker ps -a -q) -f (remove todos container)
## Colocar apelidos nos containers 
docker run --name ubuntinho ubuntu
## Informações de uso de Hardware do containe 
docker stats id_ou_apelido
## Mapear porta do container
### Estamos informando que a porta 8080 no Host é aberta e deve ser mapeada na porta 80 do container
docker run -it -p 8080:80 ubuntu
docker run -it -p 8080:80 nginx
## Criar container que auto destroi ao encerrar a sessão
docker run -it --rm -p 8080:80 nginx /bin/bash
## Remove imagens
docker rmi image_id_1 image_id_2 image_id_n





