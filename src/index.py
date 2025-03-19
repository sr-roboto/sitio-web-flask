from flask import Flask, render_template

# Creación de la aplicación Flask
app = Flask(__name__, static_folder="public/static", template_folder="public/template")

# Rutas de la aplicación
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
