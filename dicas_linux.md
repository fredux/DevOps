## Como usar chave para autenticar em servidor ssh
https://salsa.debian.org/kretcheu/tutoriais/-/blob/master/copiar.chave.md

## Recuperar senha root
## Comandos systemctl
SYSTEMD
A partir do Ubuntu 15.04, o Upstart será preterido em favor do Systemd. Com o Systemd para gerenciar os serviços, podemos fazer o seguinte:

systemctl start SERVICE- Use-o para iniciar um serviço. Não persiste após a reinicialização

systemctl stop SERVICE- Use-o para interromper um serviço. Não persiste após a reinicialização

systemctl restart SERVICE - Use-o para reiniciar um serviço

systemctl reload SERVICE - Se o serviço suportar, ele recarregará os arquivos de configuração relacionados a ele sem interromper nenhum processo que esteja usando o serviço.

systemctl status SERVICE- Mostra o status de um serviço. Informa se um serviço está em execução no momento.

systemctl enable SERVICE- Liga o serviço, na próxima reinicialização ou no próximo evento de inicialização. Persiste após a reinicialização.

systemctl disable SERVICE- Desativa o serviço na próxima reinicialização ou no próximo evento de parada. Persiste após a reinicialização.

systemctl is-enabled SERVICE - Verifique se um serviço está atualmente configurado para iniciar ou não na próxima reinicialização.

systemctl is-active SERVICE - Verifique se um serviço está ativo no momento.

systemctl show SERVICE - Mostre todas as informações sobre o serviço.

sudo systemctl mask SERVICE- Desabilite completamente um serviço vinculando-o a /dev/null; você não pode iniciar o serviço manualmente ou habilitá-lo.

sudo systemctl unmask SERVICE- Remove o link /dev/nulle restaura a capacidade de ativar e / ou iniciar manualmente o serviço.

## *Encontrar a localização de um ou mais rquivos executáveis*
which file1 file2 filen
## Encontra todas as rotas de localização do executável
which -a arquivo  


## editar uma arquivo sem editor usando o shell
cat > nome_do_arquivo.txt <<EOF



