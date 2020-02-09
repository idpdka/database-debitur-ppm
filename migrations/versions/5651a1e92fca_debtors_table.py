"""debtors table

Revision ID: 5651a1e92fca
Revises: a3a8f9f3040d
Create Date: 2020-02-09 13:48:22.433912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5651a1e92fca'
down_revision = 'a3a8f9f3040d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('debtor', sa.Column('legality', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('debtor', 'legality')
    # ### end Alembic commands ###