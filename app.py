from flask import Flask, render_template, abort

import data as data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.j2",
        tours=data.get_tours(),
        menu_departures=data.get_menu_departures(),
    )


@app.route("/from/<direction>/")
def from_direction(direction):
    tours=data.get_tours(direction=direction),

    if not direction:
        abort(404)

    return render_template(
        "from_direction.j2",
        direction=direction,
        tours=data.get_tours(direction=direction),
        menu_departures=data.get_menu_departures(),
    )


@app.route("/tours/<tour_id>/")
def tour(tour_id):
    tour = data.get_tour(tour_id)

    if not tour:
        abort(404)

    return render_template(
        "tour.j2",
        tour=tour,
        menu_departures=data.get_menu_departures(),
    )


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "404.j2", title="404", menu_departures=data.get_menu_departures()
        ),
        404,
    )


if __name__ == "__main__":
    app.run()
