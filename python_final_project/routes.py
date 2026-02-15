from flask import Blueprint, render_template

my_blueprint = Blueprint("my_blueprint", __name__)

base_url = "https://api.aviationstack.com"

@my_blueprint.route(base_url + "/v1/airplanes", methods=["GET", "POST"])
def index():
    pass


