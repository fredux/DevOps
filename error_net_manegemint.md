Erro  Linux Mint 
Erro ao tentar abrir configuração de redes no linux mint
m-connection-editor: CRYPTO/Crypto.c:258: init_openssl_crypto: Assertiva “lib” falhou.
Abortado (imagem do núcleo gravada)

A solução? No Terminal entre com o seguinte comando:
sudo ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/libcrypto.so.6
