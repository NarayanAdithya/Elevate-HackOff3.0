"""empty message

Revision ID: c1c05294a00d
Revises: fa3f8c9bf9d8
Create Date: 2020-12-13 10:42:39.938177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1c05294a00d'
down_revision = 'fa3f8c9bf9d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_name', sa.String(length=150), nullable=True),
    sa.Column('patient_key', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patient_patient_key'), 'patient', ['patient_key'], unique=True)
    op.create_index(op.f('ix_patient_time'), 'patient', ['time'], unique=False)
    op.drop_index('ix_post_patient_key', table_name='post')
    op.drop_index('ix_post_time', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('patient_name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('patient_key', sa.INTEGER(), nullable=True),
    sa.Column('time', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_time', 'post', ['time'], unique=False)
    op.create_index('ix_post_patient_key', 'post', ['patient_key'], unique=1)
    op.drop_index(op.f('ix_patient_time'), table_name='patient')
    op.drop_index(op.f('ix_patient_patient_key'), table_name='patient')
    op.drop_table('patient')
    # ### end Alembic commands ###