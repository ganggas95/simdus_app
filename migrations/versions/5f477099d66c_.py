"""empty message

Revision ID: 5f477099d66c
Revises: 
Create Date: 2018-08-17 06:24:20.020845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f477099d66c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_alamat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dusun', sa.String(length=100), nullable=True),
    sa.Column('desa', sa.String(length=100), nullable=True),
    sa.Column('kec', sa.String(length=100), nullable=True),
    sa.Column('kab', sa.String(length=200), nullable=True),
    sa.Column('prov', sa.String(length=200), nullable=True),
    sa.Column('rt_rw', sa.String(length=4), nullable=True),
    sa.Column('kode_pos', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_keluarga',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('no_kk', sa.String(length=45), nullable=True),
    sa.Column('nama_kk', sa.String(length=45), nullable=True),
    sa.Column('id_alamat', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_alamat'], ['tb_alamat.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_keluarga')
    op.drop_table('tb_alamat')
    # ### end Alembic commands ###
