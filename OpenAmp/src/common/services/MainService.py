from flask import redirect, request, render_template
from sqlalchemy import text

import Main
from common.model.Models import db, Users, Playlists, Songs
import common.services.Crudhelper as Crudhelper 

class Mainservice:
    def __init__(self):
        self.exec_user = text('SELECT * FROM Users')
        self.app = Main.MainApp
    def Mainpage(self):
        return render_template('main.html', username=self.app.Username,
                               Username_role=self.app.Username_role)