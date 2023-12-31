"""create users table

Revision ID: b0834bfca742
Revises: 
Create Date: 2023-11-01 10:56:00.599772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0834bfca742'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
