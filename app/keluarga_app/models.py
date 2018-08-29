from sqlalchemy import (
    func, or_, and_)
from app.create_app import db


class Keluarga(db.Model):
    __tablename__ = 'tb_keluarga'

    id = db.Column(db.Integer, primary_key=True)
    no_kk = db.Column(db.String(45))
    nama_kk = db.Column(db.String(45))
    id_alamat = db.Column(
        db.Integer,
        db.ForeignKey('tb_alamat.id', ondelete='cascade'))
    alamat = db.relationship(
        'Alamat',
        foreign_keys=id_alamat,
        backref=db.backref('keluarga_alamat')
    )

    @staticmethod
    def get_all(page=1, search=''):
        return Keluarga.query.filter(
            or_(
                Keluarga.nama_kk.like('%{}%'.format(search)),
                Keluarga.no_kk.like('%{}%'.format(search))
            )
        ).paginate(page, per_page=10)
