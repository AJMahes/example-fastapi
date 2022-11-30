"""add content post table

Revision ID: 3518f5d90f82
Revises: 4476fa61e3c0
Create Date: 2022-11-25 16:19:24.264611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3518f5d90f82'
down_revision = '4476fa61e3c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
