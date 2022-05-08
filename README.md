# Desafio-dev

## Executando a aplicação
- Build do container:
```shell
docker-compose build

cp .env.template .env
```
- Execução do container:
```shell
docker-compose up
```
## Banco de dados
- Configuração do banco de dados:
```shell
docker exec -t -i desafio-dev_web_1 bash 
# acessar o container

cd desafio_dev/ 
# acessar o diretório desafio_dev

python manage.py migrate 
# executar migrações no banco de dados
```
- Criando/importando informações necessárias:
```shell
docker exec -t -i desafio-dev_web_1 bash 
# acessar o container

cd desafio_dev/ 
# acessar o diretório desafio_dev

python manage.py createsuperuser 
# criar um super usuário para acessar o admin do Django

python manage.py loaddata cnab/fixtures/transaction_types.json
# carregar dados referentes aos tipos de transação
```

## URLs importantes
### Admin - Django
Interface para gerenciamento dos dados da aplicação:
> Acessar com super usuário criado
```
http://localhost:8000/admin/
```

### Importação de arquivos
URL para importação de arquivos CNAB
```
http://localhost:8000/cnab/upload-file/
```

### Operações
URL para exibição de lista de operações importadas por loja
> Para cada loja é gerado um [slug](https://pt.wikipedia.org/wiki/Slug_%28programa%C3%A7%C3%A3o%29), portanto, é necessário informá-lo na URL também
```
http://localhost:8000/cnab/operations/slug-da-loja/
```