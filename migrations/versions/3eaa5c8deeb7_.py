"""empty message

Revision ID: 3eaa5c8deeb7
Revises: 59e0de114163
Create Date: 2022-04-01 19:19:13.693951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eaa5c8deeb7'
down_revision = '59e0de114163'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_projects', sa.Column('project_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_projects', 'project_link')
    # ### end Alembic commands ###