from flask import Flask, render_template, abort

import data as data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html", directions=data.get_directions(), tours=data.get_tours()
    )


@app.route("/from/<direction>")
def from_direction(direction):
    direction = data.get_direction_info(direction)

    if not direction:
        abort(404)

    return render_template(
        "from_direction.html",
        directions=data.get_directions(),
        direction=direction,
        tours=data.get_tours(direction=direction),
    )


@app.route("/tours/<tour_id>")
def tour(tour_id):
    tour = data.get_tour(tour_id)

    if not tour:
        abort(404)

    return render_template("tour.html", directions=data.get_directions(), tour=tour)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="404"), 404


if __name__ == "__main__":
    app.run()
