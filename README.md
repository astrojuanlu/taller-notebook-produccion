# Taller: De notebook a modelo en producción

## Resumen

1. Crear una biblioteca Python con el código reutilizable correspondiente al proyecto
   y probar que funciona desde un intérprete de Python
2. Crear una aplicación web usando FastAPI que haga uso de ese código
   y probar que funciona desde Gitpod
3. Desplegar la aplicación web en Railway

## Referencias

- https://github.com/astrojuanlu/ie-mbd-advanced-python/

## Enlaces

- https://fastapi.tiangolo.com/
- https://www.gitpod.io/
- https://voila.readthedocs.io/
- https://shiny.rstudio.com/py/
- https://railway.app/?referralCode=VO2J82 (afiliado)

## Instrucciones

```
python -m venv .venv
source .venv/bin/activate
pip install -U pip pip-tools
pip-compile
pip install -r requirements.txt
pip install flit
mkdir library && cd library
flit init
pip install black
```
