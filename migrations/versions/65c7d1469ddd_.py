"""empty message

Revision ID: 65c7d1469ddd
Revises: c80089d43cd6
Create Date: 2020-10-19 13:50:00.494757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c7d1469ddd'
down_revision = 'c80089d43cd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('venues', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'seeking_talent')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###