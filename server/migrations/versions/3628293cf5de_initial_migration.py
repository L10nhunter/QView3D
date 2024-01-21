"""Initial migration

Revision ID: 3628293cf5de
Revises: 
Create Date: 2024-01-20 18:04:33.580013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3628293cf5de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.create_table('printer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('port', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'), 
    )
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('printer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['printer_id'], ['printer.id'], ),
    sa.PrimaryKeyConstraint('id'), 
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    op.drop_table('printer')
    # ### end Alembic commands ###
