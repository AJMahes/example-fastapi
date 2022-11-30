"""create post table

Revision ID: 4476fa61e3c0
Revises: 
Create Date: 2022-11-25 16:08:25.016107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4476fa61e3c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
