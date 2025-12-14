from flask import Flask, render_template, request
from datetime import datetime
import uuid

app = Flask(__name__)

reports = []

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        desc = request.form.get("desc")

        report_id = str(uuid.uuid4())[:6].upper()

        report = {
            "id": report_id,
            "location": "India",
            "desc": desc,
            "status": "Pending",
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        reports.append(report)
        message = f"Report submitted successfully. Your ID is {report_id}"

    return render_template("index.html", message=message)


@app.route("/track", methods=["POST"])
def track():
    rid = request.form.get("rid").upper()
    result = None

    for r in reports:
        if r["id"] == rid:
            result = r
            break

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
