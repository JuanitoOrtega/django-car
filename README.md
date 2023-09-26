## Exportar datos de la base de datos a json
```shell
python manage.py dumpdata cars.Car --output=data.json
```

## Importar datos
```shell
python manage.py loaddata data.json
```

## Exportar datos de la base de datos
```shell
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json
```

http://localhost:8000/accounts/facebook/login/callback/