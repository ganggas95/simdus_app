from .blueprint import dashboard_bp
from .views import DashboardView


dashboard_bp.add_url_rule(
    '/admin/dashboard',
    view_func=DashboardView.as_view(
        'dashboard_page',
        'dashboard.html'
    ),
    methods=['GET']
)
