"""your message

Revision ID: 451d4b6a74ea
Revises: 0e12555d4c52
Create Date: 2023-06-26 09:52:28.559970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '451d4b6a74ea'
down_revision = '0e12555d4c52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
