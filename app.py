import os
from bottle import error, route, run, template
from data import get_data


@route("/")
def index():
    data = get_data("combined_data.json")
    return template("index", data=data)


@error(404)
def error404(error):
    return "Nothing here, sorry!"


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8000, reloader=True, debug=True)