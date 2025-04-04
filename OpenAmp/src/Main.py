#external imports which are necessary for this script.
from flask import render_template, Flask, request, redirect


class MainApp:
    app = Flask(__name__)
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///OpenAmp.db"
    #db.init_app(app)


if __name__ == '__main__':
    mainapp = MainApp
    mainapp.app.run(debug=True)