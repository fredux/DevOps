import subprocess

ip = input('IP INICIAL: ').split('.')
ip_final = input('IP FINAL: ').split('.')
print('Processando...\n')

#if __name__ == "__main__":
#    principal(ip)
ativos = []
inativos =[]
qtd_ativos = 0
qtd_inativos = 0

for i in range(int(ip[3]),int(ip_final[3])+1):
    # mudar a ultima parte do ip para o numero como string
    ip[3] = str(i)
    # criar o texto que representa o ip
    res =subprocess.run(['ping', '-n', '1', '-w', '5', ip_formatado], shell=True)
    print(res)
    print(".", end="")
    if res.returncode == 0:
       qtd_ativos+=1
       ativos.append(ip_formatado)
    else:
       qtd_inativos+=1
       inativos.append(ip_formatado)
print("\n")       
print("-"*80)
print(f"Ativos: {qtd_ativos}  {ativos} \n")
print(f"Inativos: {qtd_inativos} {inativos} \n")
