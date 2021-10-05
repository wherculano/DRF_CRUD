### CRUD usando DRF (Django Rest Framework)

Para rodar este projeto, será necessário criar um ambiente virtual:
Os comandos abaixo foram usados em uma distro Linux.
```
$ python -m venv venv
```
Ativar este ambiente:
```
$ source venv/bin/activate
```
Com o ambiente virtual ativo, instalar as bibliotecas necessarias:
```
$ python -m pip install -r requirements.txt
```

Para rodar o sistema primeiro devemos criar os "migratios"
```
$ python manage.py makemigrations
```
Após isso devemos de fato migrar os dados:
```
$ python manage.py migrate
````
E para subir o sistema basta digitar:
```
$ python manage.py runserver
```


E para acessar as rotas, os seguintes endpoints podem ser usados (após *http://127.0.0.1:8000/*) :

1. getAluno/    
    - lista os alunos cadastrados o sistema
2. postAluno/    
    - possibilita cadastrar novos alunos
3. putAluno/<str:pk>/
    - possibilita atualizar um aluno passando seu ID
4. delAluno/<str:pk>/
    - possibilita excluir um aluno passando seu ID
    