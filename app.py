from flask import Flask, render_template, request, send_file
import os
from ProcFluxograma import gerar_fluxograma

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "Nenhum arquivo enviado", 400
        file = request.files["file"]
        if file.filename == "":
            return "Nenhum arquivo selecionado", 400

        filepath = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        gerar_fluxograma(filepath)

        return render_template(
            "index.html",
            image_file="static/fluxograma.png",
            pdf_file="static/fluxograma.pdf",
            svg_file="static/fluxograma.svg",
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
