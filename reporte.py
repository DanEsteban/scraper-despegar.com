from flask import Flask, render_template
from mongo import MongoConnection
import atexit

app = Flask(__name__)

# Configura la conexión a la base de datos MongoDB
db_client = MongoConnection().client
db = db_client.get_database('alibaba')
col = db.get_collection('products')

@app.route('/')
def index():
    # Consulta todos los documentos en la colección 'products'
    products_data = col.find({})

    # Renderiza una plantilla HTML para mostrar los datos
    return render_template('index.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True)