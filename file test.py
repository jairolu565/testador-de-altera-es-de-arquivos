import chunk
import hashlib
from time import sleep 
from difflib import SequenceMatcher
import shutil
import smtplib
import os
import sys


while True:
    def hash_file(filename1,filename2):
        h1 = hashlib.sha1()
        h2 = hashlib.sha1()

        with open(filename1, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read (1024)
                h1.update (chunk)
        with open(filename2, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read (1024)
                h2.update (chunk)
        return h1.hexdigest(),h2.hexdigest()
    msg1,msg2 = hash_file('A:\\Arquivos\\Documents\\aula8.pptx','A:\\Arquivos\\Documents\\copia\\aula8.pptx')
    print(msg1+"\t"+msg2)
    razao = (SequenceMatcher(None,msg1,msg2).ratio())*100
    if razao == 100:
        print('A RAZAO ENTRE OS ARQUIVOS É DE ', razao, '%')
        print('TESTANDO ALTERAÇÕES NO ARQUIVO NOVAMENTE EM 10 SEGUNDOS')
        print('\n')
    else:
        print('OS ARQUIVOS SÃO DIVERGENTES E O E-MAIL SERÁ ENVIADO')
        servidor=smtplib.SMTP('smtp-mail.outlook.com', 587)
        servidor.ehlo()

        servidor.starttls()


        sender="pyenviar@outlook.com"
        receivers=["pyreceber@outlook.com"]
        subject="PLANILHA DIARIA"
        msg="segue anexa planilha diaria"
        
     
        servidor.login("pyenviar@outlook.com","ravenclaw13")
        servidor.sendmail(sender,receivers,subject,msg)
        servidor.quit()
        print('TESTANDO ALTERAÇÕES NO ARQUIVO NOVAMENTE EM 10 SEGUNDOS')
        print('\n')
        src_path = r'C:\\Users\\admin\\Documents\\testeee\\ONU.txt'
        dst_path = r'C:\\Users\\admin\\Documents\\testeee2\\ONU.txt'
        shutil.copy(src_path, dst_path)
        print('Arquivo atualizado. Aguardando uma nova alteração.')
        print('\n')
    sleep(10)
    
            