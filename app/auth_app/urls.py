from .blueprint import auth_bp
from .views import AuthView, LogoutView


auth_bp.add_url_rule('/login',
                     view_func=AuthView.as_view(
                         'auth_view',
                         'login.html'
                     ), methods=['GET', 'POST'])
auth_bp.add_url_rule('/logout',
                     view_func=LogoutView.as_view(
                         'logout_view',
                         None
                     ))
