from flask import Flask, render_template, request
import os
import re

from topsis.topsis import topsis
from email_utils import send_email

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        # ---------- VALIDATIONS ----------
        if not is_valid_email(email):
            return "Invalid Email Format"

        weights_list = weights.split(",")
        impacts_list = impacts.split(",")

        if len(weights_list) != len(impacts_list):
            return "Number of weights must equal number of impacts"

        for i in impacts_list:
            if i not in ["+", "-"]:
                return "Impacts must be + or - only"

        # ---------- FILE HANDLING ----------
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(RESULT_FOLDER, "result.csv")

        file.save(input_path)

        # ---------- RUN TOPSIS ----------
        topsis(input_path, weights, impacts, output_path)

        # ---------- SEND EMAIL ----------
        send_email(email, output_path)

        return render_template("success.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
