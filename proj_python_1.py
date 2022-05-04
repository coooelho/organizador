''' PROJETO PYTHON 1
DESCRIÇÃO: Escrever um programa que crie duas pastas e organize os arquivos nessas pastas de acordo com sua extensão
NOME: Luis coelho
VERSÃO: 0.0.1
DATA: 03/05/2022

'''

#Primeiramente temos que entrar na pasta na qual esses arquivos estão, para isso vamos fazer uma pedido para o OS

import os

#pasta = '/home/luis/ufrgs/pasta'
pasta = '.'
arquivo = os.scandir(pasta)

#for arquivo in arquivo:
#   print(arquivo.name)


#Agora que vimos que os arquivos estão na pasta, vamos criar as pastas para organiza-los
if os.path.exists('.'):
    print('Pasta já existe')
else:
    os.mkdir('documentos')


if os.path.exists('.'):
    print('Pasta já existe')
else:
    os.mkdir('planilhas')


#Enviando os arquivos para as pastas
if arquivo == '.doc':
    shutil.move(arquivo, './documentos')
elif arquivo == 'xls':
    shutil.move(arquivo, './planilhas')