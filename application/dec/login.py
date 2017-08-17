from flask_login import LoginManager
login_manager = LoginManager()
from ..models.user import User

# user = dict({'xm':{"mz":"xm","age":10,"address":"sz"},'xf':{"mz":"xf","age":14,"address":"sh"}})
# user = User('afaf')

@login_manager.user_loader
def load_user(user_id):
    print('load user...{}'.format(user_id))
    return None


