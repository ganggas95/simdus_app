from flask import (
    render_template,
    request,
    redirect,
    url_for)
from flask_login import login_user, logout_user
from app.helpers import BaseView
from .models import LoginForm, User


class AuthView(BaseView):
    def dispatch_request(self):
        form = LoginForm(request.form)
        if request.method == 'GET':
            return render_template(
                self.template_name,
                form=form)
        user = User.get_username(form.username.data)
        print(user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(
                url_for('dashboard_bp.dashboard_page')
            )
        return redirect(url_for('auth_bp.auth_view'))


class LogoutView(BaseView):
    def dispatch_request(self):
        logout_user()
        return redirect(
            url_for('auth_bp.auth_view')
        )
