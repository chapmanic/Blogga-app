"""add username column

Revision ID: 1368379e0c0c
Revises: fb2cb98241ec
Create Date: 2024-01-06 13:19:53.399118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1368379e0c0c'
down_revision = 'fb2cb98241ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=100), nullable=True))
        batch_op.create_unique_constraint('usernames', ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###