from flask import redirect, request, render_template
from sqlalchemy import text

import Main
from common.model.Models import db, Users
import common.services.Crudhelper as Crudhelper 

class Loginservice:
    def __init__(self):
        self.exec_user = text('SELECT * FROM Users')
        self.app = Main.MainApp
    def login(self):
        if request.method == 'POST':
            self.app.Username = request.form['Username']
            Password = request.form['Password']
            find_users = Users.query.filter_by(username=self.app.Username).first()
            if find_users is not None:
                self.app.Username_role = find_users.role
            self.app.Username_id = Crudhelper.username_to_id(self.app.Username)
            match request.form['button']:
                case 'login':
                    try:
                        if find_users.password == Password and find_users.role == 'user':
                            return redirect('/')

                        elif find_users.password == Password and find_users.role == 'admin':
                            return redirect('/admin/')
                        else:
                            return 'wrong password or access denied...'





                    except AttributeError:
                        return 'wrong login...'
                    except Exception as e:
                        return str(e)
                case 'register':
                    users = db.session.execute(self.exec_user)
                    for i in users:
                        if i[1] == self.app.Username:
                            return f'username {i[1]} exists!'
                    if self.app.Username and Password == '':
                        return redirect('/login')
                    else:
                        add_user = Users(username=self.app.Username,
                                             password=Password,
                                             role='user')
                        db.session.add(add_user)
                        db.session.commit()
                        return redirect('/login')
        else:
            return render_template('login.html')
