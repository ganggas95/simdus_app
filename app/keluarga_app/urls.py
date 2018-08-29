from .blueprint import kk_bp
from .views import KeluargaView


kk_bp.add_url_rule(
    '/admin/keluarga',
    view_func=KeluargaView.as_view(
        'keluarga_view',
        'keluarga.html'
    ),
    methods=['GET', 'POST']
)
