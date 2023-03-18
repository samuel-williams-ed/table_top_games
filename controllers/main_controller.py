from flask import render_template, redirect, request
from flask import Blueprint

# models
# from models.inventory_holding import Inventory_holding

# repositories
# import repositories.inventory_repository as invent_rep


# instead of shop_blueprint
home_blueprint = Blueprint("shops", __name__)

@home_blueprint.route("/")
def home():
    return render_template("index.html")

@home_blueprint.route("/test/scenario_test")
def testPage():
    return render_template("test/scenario_test.html")

@home_blueprint.route("/Codex_Eldar")
def codex():
    return render_template("eldar/codex.html")

