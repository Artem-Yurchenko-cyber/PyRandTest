from flask import Flask, render_template, request, redirect, url_for
from modules.generator import generate_sequence
from modules.tests import tun_all_tests, run_selected_test

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_seq = ""
    test_results = None

    if request.method == "POST":
        if "generate" in request.form:
            method = request.form.get("method")
            length = int(request.from.get("length"))
            seed = request



if __name__ == "__main__":
    app.run(debug=True)
