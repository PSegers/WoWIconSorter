
from flask import Flask, render_template, request
import models

app = Flask(__name__)


# set FLASK_APP=main_app

CSV_DATA = None


@app.route("/", methods=["GET", "POST"])
def color_picker():
    color = request.form.get("color")
    if not color:
        image_files = []

    else:
        image_files = app.color_sorter.rank_sort(color)[:2000]

    return render_template("main_template.html", image_files=image_files, color=color)


if __name__ == "__main__":
    color_sorter = models.ColorSorter()
    app.color_sorter = color_sorter
    app.run(debug=True)
