from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = b'ajdsnkajsnaslknc/'

@app.route('/')
def dashboard():
    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template("OOP's Terms Glossary.html")

app.run(port=4996)