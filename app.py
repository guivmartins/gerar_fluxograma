# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from ProcFluxograma import gerar_fluxograma
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("excel_file")
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            gerar_fluxograma(filepath)
            return redirect(url_for("index"))
    return render_template("index.html")
