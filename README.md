# lista-ser347

## Objetivos:

1) Criar um repositório com alguns arquivos de código fonte da lista 
de exercícios 06. 

2) Enviar o link desse repositório para os professores da disciplina, 
com um resumo da sequência de comandos git utilizados.

## Instruções 1: Repositório

* Antes de iniciar é preciso ter uma conta no gitHub 
* Certifique-se que o git está instalado, caso não tenha instalado, instruções para instalação em: https://ser-347.github.io/variados/git_comandos.html

* Defina um pasta na máquina local para onde deseja copiar o repositório 

**Observação**: Alguns comandos são exclusivos para o  Windows

## Sequência de comandos utilizados

**1ª Etapa:** fazendo uma copia do repositório remoto na máquina local

comando: git clone

* O comando git clone foi utilizado para copiar o repositório remoto na máquina local

git clone https://github.com/AnielliRosane/lista-ser347


**2ª Etapa:**  Alterando o diretorio corrente

comando: cd 

* O comando cd altera o diretório corrente para a pasta lista-ser347

cd lista-ser347

**3ª Etapa:** Modificando o arquivo README do repositório

Utilizou-se o *Notepad++* para alterar o arquivo README.md

com o comando: *git status* podemos verificar o status do repositório

**4ª Etapa:** Registrando - incluir o arquivo no repositório

comando: git add

git add README.md

**5ª Etapa:** Confirmando a modificação

comando: git commit 

git commit -m "Primeira versão do arquivo README.md"

**6ª Etapa:** Sincronizando -  máquina local e repositório remoto

O comando garante que a copia local esteja realmente atualizada com a remota

comando: git pull

**7ª Etapa:** Sincronizando -  repositório remoto e máquina local

comando: git push

**Obs:** nesta etapa temos que lembrar do usuário e senha do GitHub


## Instruções 2: Arquivos de código

Adicionando os exercicios 02 e 04 da lista de exercícios 06

nome dos arquivos: 

* exercicio-2

* exercicio-4

**Sequência de comandos**

* git add

* git commit

* git pull *(importante ter certeza que está sincronizado)*

* git push

## Considerações

Neste arquivo está a explicado sequência de comandos git utilizados para construção de uma repositório remoto e virtual, 
bem como, os códigos para adicionar os arquivos de código fonte.
