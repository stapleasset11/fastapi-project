"""add content column to posts table

Revision ID: 244115466029
Revises: 78b6c592ace2
Create Date: 2024-04-17 10:16:33.830984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '244115466029'
down_revision: Union[str, None] = '78b6c592ace2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
