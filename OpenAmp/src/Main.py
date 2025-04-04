#external imports which are necessary for this script.
from flask import render_template, Flask, request, redirect
#local imports which are part of this script
from common.model.Models import Users, db
from common.services import loginService, MainService
class MainApp:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Openamp.db"
    db.init_app(app)
    Username = ''
    Username_role = ''
    Username_id = 0

    @app.route('/', methods = ['POST', 'GET'])
    def index():
        return render_template("main.html")
    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        loginsrv = loginService.Loginservice()
        return loginsrv.login()


if __name__ == '__main__':
    app = MainApp
    app.app.run(debug=True)