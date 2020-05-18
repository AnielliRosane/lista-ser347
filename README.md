# lista-ser347

# lista-ser347

## Objetivo:
Exercício 03. Crie um repositório com alguns arquivos de código fonte da lista 
de exercícios 06 e envie o link desse repositório para os professores da disciplina, 
com um resumo da sequência de comandos git utilizados.

## Instruções

* Antes de iniciar é preciso ter uma conta no gitHub 
* Certifique-se que o git está instalado, caso não instruções para instalação em: https://ser-347.github.io/variados/git_comandos.html

* Defina um pasta na máquina local para onde deseja copiar o repositório 

**Observação**: Algunas comandos são exclusivos para o  Windows

## Sequência de comandos utilizados

**1ª Etapa:** fazendo uma copia do repositório remoto na máquina local

comando: git clone

* O comando git clone foi utilizado para copiar o repositório remoto na máquina local

git clone https://github.com/AnielliRosane/lista-ser347


**2ª Etapa:**  Alterando o diretorio corrente

comando: cd 

* O comando cd altera o diretório corrente pata a pasta lista-ser347

cd lista-ser347

**3ª Etapa:** Modificar o arquivo README do repositório

Utilizou-se o *Notepad++* para alterar o arquivo README.md

com o comando: *git status* podemos verificar o status do repositório

4ª Etapa: Registar - incluir o arquivo no repositório

comando: git add

git add README.md

**5ªEtapa:** Confirmar a modificação

comando: git commit 

git commit -m "Primeira versão do arquivo README.md"

**6ªEtapa:** Sincronização -  maquina local e repositório remoto
O comando garante que a copia local esteja realmenre atualziada com a remota

comando: git pull

**7ªEtapa:** Sincronização -  repositório remoto e maquina local

comando: git push

**Obs:** nesta etapa temos que lembrar do usuário e senha do GitHub