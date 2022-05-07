<div align="center">    
  <h1>E-Commerce com Vue e Django 🛒</h1>
  <br>    
  <div align="center">    
    <a href="#sobre">Sobre</a> | 
    <a href="#tecnologias">Tecnologias</a> | 
    <a href="#run">Rodando o projeto</a>      
  </div>  
</div>

<a id="sobre"></a>

Teste de realizar a regra de negocio do serviço do E-Commerce em django, essa aplicação faz parte do ecossistema que ira atuar junto com o Frontend.

O serviço utiliza autenticação simples via Token, serviços da Cloudinary para o upload de imagens, o Stripe para pagamentos e outros recursos.

<div align="center">    
  <strong>Tela de uma requisição JSON de cursos</strong>    
  <img src="./.github/media/app-api.png" />    
  <a id="tecnologias"></a>    
</div> 
    
## :computer: Tecnologias    
 O projeto foi desenvolvido usando as tecnologias:    
    
<div align="center">    
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />    
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" />    
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />    
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" />    
</div>

<a id="run"></a>

## :running: Rodando o projeto

### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `< Docker/ Python>`
- Você tem uma máquina `< Windows / Linux / Mac >`.
- Você possui um `< Editor de código ou IDE / Gerenciador de banco de dados >`.

## ☕ Pequena ajuda

Preencha o arquivo `.env.example` com as informações cobradas e depois renomeie para `.env`.

```env
# APP

SECRET_KEY=
DEBUG=
HOSTS=

# POSTGRES
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# PGADMIN
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=

# STRIPE
STRIPE_API_KEY=
ENDPOINT_SECRET=

# Cloudinary
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=


```

## Serviços necessários antes de rodar a aplicação:

Lembre-se de pegar as suas chaves de API nos serviços da **[Cloudinary](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjl49bn4oX3AhXPQUgAHdW8AFAYABAAGgJjZQ&ohost=www.google.com&cid=CAASJeRoZficLapyBYRC5pWQ6cgFAKUh-DeA2yIPtwULbUZEPsb5Evg&sig=AOD64_3SQrHCVZaf9Ts2mVKRuoGkzAm4Dw&q&adurl&ved=2ahUKEwid3c7n4oX3AhWArJUCHbZRAH4Q0Qx6BAgDEAE)** e do **[Stripe](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwijlrD54oX3AhUvQUgAHQb7CAsYABAAGgJjZQ&ohost=www.google.com&cid=CAASJeRopwqWu91WWsvPhM4UKeVdBrRdLP22hWD2ajMnUqih0kZrdnc&sig=AOD64_0Ww0E5pwd2EtlWshd1Y1RIipL_mg&q&adurl&ved=2ahUKEwiutan54oX3AhUNjZUCHaMFAqsQ0Qx6BAgDEAE).**

## Se lembre de ter o Docker :ocean:

### UM comando só:

```bash
$ docker-compose up web
```

### Manualmente:

Crie um banco de dados com o docker-compose

```bash
$ docker-compose up
```

Crie a sua pasta de venvs:

```bash
$ python -m venv venv && source ./venv/bin/activate
```

Agora realize as migrações necessárias:

```bash
$ python manage.py makemigrations && python manage.py migrate
```

E por fim, rode o aplicativo:

```bash
$ python manage.py runserver
```

#### _Sinta-se livre para colaborar, toda ajuda é bem vinda ;)_

 <br/>
