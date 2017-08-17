from flask_login import LoginManager
login_manager = LoginManager()

user = dict({'xm':{"mz":"xm","age":10,"address":"sz"},'xf':{"mz":"xf","age":14,"address":"sh"}})

@login_manager.user_loader
def load_user(user_id):
    return user.get(user_id)


