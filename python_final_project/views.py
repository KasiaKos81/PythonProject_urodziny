from flask.views import MethodView
from flask import Blueprint

users_blueprint = Blueprint("users_blueprint", __name__)

class UsersView(MethodView):
    def get(self):
        return "Get all flights"

flights_view = UsersView.as_view("flights_view")

users_blueprint.add_url_rule("/v1/flights", view_func=flights_view, methods=["GET"])