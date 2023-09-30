
# Web Scraping y Aplicacion Web con Flask
En el siguiente Proyecto vamos a realizar un ejemplo de como realizar un scrapping a la pagina web de alibaba utiliando Selenium y mostrando los datos recompilados en una aplicacion web realizada con Flask


## Requisitos

- Python 3.8
- Bibliotecas Python (instalables "mediante pip install -r requirements.txt")
- Google Chrome (o el navegador de tu elección) para Selenium

## Uso
 
__Ejecutar el Scraping__

Para ejecutar el scraper y recopilar datos desde Alibaba:

```bash
python web_scraping/scraping_script.py
```

Esto iniciará el proceso de scraping y almacenará los datos en una base de datos MongoDB.


__Iniciar la Aplicación Web__

Para poner en marcha la aplicación web con Flask:

```bash
python web_app/app.py
```
## Ejemplo

- En el directorio web_app/templates, se encuentra un archivo index.html que tiene la estructura de la página web donde se muestran los productos. 
Personaliza este archivo según tus necesidades.

## Problemas

- El ejemplo de scraping actual esta diseñado para paginas web que cuenten con informacion que contienen información en su página principal. Además, en el repositorio se incluye un código que se enfoca en el scraping de una página web como Reddit. Sin embargo, surgió un problema al intentar automatizar el proceso de inicio de sesión o acceso a la plataforma por medio de Selenium.
## 🚀 About Me
Mi nombre es Daniel Velasco soy Ing. en Telecomunicaciones, desarrollando una maestria en Ciberseguridad y programador freelancer fullstack.

Si tienes alguna pregunta, comentario o incluso la resoluion al problema de automatizacion no dudes en ponerte en contacto conmigo
- desteban.velpi@gmail.com
## Authors

- [@Daniel Velasco](https://github.com/DanEsteban)


