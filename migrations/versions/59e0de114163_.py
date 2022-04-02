"""empty message

Revision ID: 59e0de114163
Revises: 2788587df353
Create Date: 2022-04-01 19:07:44.089536

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '59e0de114163'
down_revision = '2788587df353'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_projects_last_updated', table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('abstract', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('project_link', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prospectus_description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prospectus_link', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prospectus_secondary_file', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cp_courses', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('keywords', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('feature', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hsr_review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['logins.id'], name='projects_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='projects_pkey')
    )
    op.create_index('ix_projects_last_updated', 'projects', ['last_updated'], unique=False)
    # ### end Alembic commands ###
