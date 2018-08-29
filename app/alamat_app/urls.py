from .blueprint import (
    alamat_bp,
    api_alamat_bp,
    api_alamat)
from .views import (
    AlamatView,
    AddAlamatView,
    EditAlamatView)
from .api import alamat_ns


alamat_bp.add_url_rule(
    '/admin/alamat',
    view_func=AlamatView.as_view(
        'alamat_view',
        'alamat.html'
    )
)
alamat_bp.add_url_rule(
    '/admin/alamat/add',
    view_func=AddAlamatView.as_view(
        'add_alamat_view',
        'tambah_alamat.html'
    ),
    methods=['GET', 'POST']
)
alamat_bp.add_url_rule(
    '/admin/alamat/<int:id_alamat>/detail',
    view_func=EditAlamatView.as_view(
        'edit_alamat_view',
        'edit_alamat.html'
    ),
    methods=['GET', 'POST']
)

api_alamat.add_namespace(alamat_ns)
