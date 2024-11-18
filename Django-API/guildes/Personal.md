
## Apos baixar e configrar o asdf rodar o comando para ajudar
```bash
    sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev tk-dev
```
### instalar plugin python
```bash
    asdf plugin add python
```

### instalar versão especifica do python
```bash
    asdf install python 3.12.6
```
### Agora podemos sertar a versão por projeto do python
```bash
    asdf local python 3.12.6
```
### Ou globalmente
```bash
    asdf global python 3.12.6
```
### Instalar o pipenv
```bash
    pip install pipenv
```

## Comandos mais utilizados

### Docker
```bash
    docker compose up 
```
caso de algum problema tente rodar o comando abaixo
```bash
    service docker start
```
### Pipenv
```bash
    pipenv shell
```
## Default users

### PG-admin

- User: `admin@user.com`
- Password: `secret`

### server
- admin: `postgres`
- password: `root`

### superuser
- username: `victorVilela`
- email: `victor@gmail.com`
- password: `1598`

