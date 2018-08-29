from app.create_app import login_manager
from app.user_app.models import User


@login_manager.user_loader
def user_loader(user):
    return User.get_by_id(user)
