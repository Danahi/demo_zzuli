from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/product/", methods=["GET","POST"])
def show_product():

    if request.method == "POST":
        info = request.form["product_name"]
        return render_template("product.html", product_name = info)

    return render_template("product.html")

app.run("127.0.0.1", port=80, debug=True)