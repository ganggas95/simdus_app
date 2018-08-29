from sqlalchemy import (
    or_, and_
)
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    SelectField)
from app.create_app import db, ma


class Provinsi(db.Model):
    __tablename__ = 'tb_prov'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(45))


class Kab(db.Model):
    __tablename__ = 'tb_kab'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(45))
    id_prov = db.Column(
        db.Integer,
        db.ForeignKey('tb_prov.id', ondelete='cascade'))
    prov = db.relationship(
        'Provinsi',
        foreign_keys=id_prov,
        backref=db.backref('prov_kab')
    )

    @staticmethod
    def get_by_prov(prov_id, search=''):
        return Kab.query.filter(
            and_(
                Kab.id_prov == prov_id,
                or_(
                    Kab.nama.like('%{}%'.format(search))
                )
            )
        ).all()


class Kec(db.Model):
    __tablename__ = 'tb_kec'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(45))
    id_kab = db.Column(
        db.Integer,
        db.ForeignKey('tb_kab.id', ondelete='cascade'))
    kab = db.relationship(
        'Kab',
        foreign_keys=id_kab,
        backref=db.backref('kab_kec')
    )

    @staticmethod
    def get_by_kab(kab_id, search=''):
        return Kec.query.filter(
            and_(
                Kec.id_kab == kab_id,
                or_(
                    Kec.nama.like('%{}%'.format(search))
                )
            )
        ).all()


class KecSchema(ma.ModelSchema):
    class Meta:
        model = Kec


class Desa(db.Model):
    __tablename__ = 'tb_desa'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(45))
    id_kec = db.Column(
        db.Integer,
        db.ForeignKey('tb_kec.id', ondelete='cascade'))
    kec = db.relationship(
        'Kec',
        foreign_keys=id_kec,
        backref=db.backref('kec_desa')
    )

    @staticmethod
    def get_by_kec(kec_id, search=''):
        return Desa.query.filter(
            and_(
                Desa.id_kec == kec_id,
                or_(
                    Desa.nama.like('%{}%'.format(search))
                )
            )
        ).all()


class DesaSchema(ma.ModelSchema):
    class Meta:
        model = Desa


class Dusun(db.Model):
    __tablename__ = 'tb_dusun'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(45))
    id_desa = db.Column(
        db.Integer,
        db.ForeignKey('tb_desa.id', ondelete='cascade'))
    desa = db.relationship(
        'Desa',
        foreign_keys=id_desa,
        backref=db.backref('desa_dusun')
    )

    @staticmethod
    def get_by_desa(desa_id, search=''):
        return Dusun.query.filter(
            and_(
                Dusun.id_desa == desa_id,
                or_(
                    Dusun.nama.like('%{}%'.format(search))
                )
            )
        ).all()


class DusunSchema(ma.ModelSchema):
    class Meta:
        model = Dusun


class Alamat(db.Model):
    __tablename__ = 'tb_alamat'
    id = db.Column(db.Integer, primary_key=True)
    id_dusun = db.Column(
        db.Integer,
        db.ForeignKey('tb_dusun.id', ondelete='cascade'))
    dusun = db.relationship(
        'Dusun',
        foreign_keys=id_dusun,
        backref=db.backref('dusun_alamat')
    )
    rt_rw = db.Column(db.String(4))
    kode_pos = db.Column(db.String(5))

    def desa(self):
        if self.dusun:
            return self.dusun.desa
        return None

    def kec(self):
        if self.dusun and self.dusun.desa:
            return self.dusun.desa.kec
        return None

    def kab(self):
        if self.dusun and self.dusun.desa and self.dusun.desa.kec:
            return self.dusun.desa.kec.kab
        return None

    def prov(self):
        if self.dusun and self.dusun.desa \
            and self.dusun.desa.kec \
                and self.dusun.desa.kec.kab:
            return self.dusun.desa.kec.kab.prov
        return None

    def get_all(search='', page=1):
        return Alamat.query.join(
            Dusun,
            Alamat.id_dusun == Dusun.id
        ).join(
            Desa,
            Dusun.id_desa == Desa.id
        ).join(
            Kec,
            Desa.id_kec == Kec.id
        ).filter(
            or_(
                Dusun.nama.like('%{}%'.format(search)),
                Desa.nama.like('%{}%'.format(search)),
                Kec.nama.like('%{}%'.format(search))
            )
        ).paginate(page, per_page=10)


class AlamatForm(FlaskForm):
    prov = SelectField(
        'Provinsi',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "disabled": True,
            "placeholder": "Pilih Provinsi"
        }
    )
    kab = SelectField(
        'Kabupaten',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control select2",
            "placeholder": "Pilih Kabupaten"
        }
    )
    kec = SelectField(
        'Kecamatan',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control select2",
            "placeholder": "Pilih Kecamatan"
        }
    )
    desa = SelectField(
        'Desa',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control select2",
            "placeholder": "Pilih Desa"
        }
    )
    dusun = SelectField(
        'Dusun',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control select2",
            "placeholder": "Pilih Dusun"
        }
    )
    rt_rw = StringField(
        'RT/RW',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "required": True,
            "placeholder": "RT/RW"
        }
    )
    kode_pos = StringField(
        'Kode Pos',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "required": True,
            "placeholder": "Kode Pos"
        }
    )

    def init_choices(self):
        prov = Provinsi.query.all()
        kab = Kab.query.all()
        kec = []
        self.prov.choices = [(p.id, p.nama) for p in prov]
        self.kab.choices = [(k.id, k.nama) for k in kab]
        self.kec.choices = [(k.id, k.nama) for k in kec]
        self.desa.choices = []
        self.dusun.choices = []
