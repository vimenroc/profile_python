from flask import Blueprint, render_template

vistas = Blueprint('vistas', __name__)

@vistas.route('/')
def home():
  #return "h";
  return render_template("home.html")


@vistas.route('/about')
def about():
  #return "h";
  return render_template("pages/about.html")