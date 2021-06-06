"""empty message

Revision ID: 94641e67dcd5
Revises: 7c97d7939c01
Create Date: 2021-06-05 16:49:25.857944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94641e67dcd5'
down_revision = '7c97d7939c01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dept', sa.String(), nullable=True),
    sa.Column('empname', sa.String(), nullable=True),
    sa.Column('empnid', sa.String(), nullable=True),
    sa.Column('empnuid', sa.String(), nullable=True),
    sa.Column('groups', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empm')
    # ### end Alembic commands ###
