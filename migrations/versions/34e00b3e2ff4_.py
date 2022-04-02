"""empty message

Revision ID: 34e00b3e2ff4
Revises: 58fd931f65c9
Create Date: 2022-03-31 15:05:34.922547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34e00b3e2ff4'
down_revision = '58fd931f65c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_projects', 'additional_information')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_projects', sa.Column('additional_information', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
