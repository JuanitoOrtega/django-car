## Exportar datos de la base de datos a json
```Shell
python manage.py dumpdata cars.Car --output=data.json
```

## Importar datos
```Shell
python manage.py loaddata data.json
```