# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_file
import os
from ProcFluxograma import gerar_fluxograma

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".xlsx"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            output_files = gerar_fluxograma(filepath)

            return render_template("index.html", files=output_files)

    return render_template("index.html", files=None)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
