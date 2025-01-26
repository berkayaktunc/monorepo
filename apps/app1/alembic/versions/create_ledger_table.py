"""create ledger table

Revision ID: 001_create_ledger_table
Revises: 
Create Date: 2024-01-21 01:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '001_create_ledger_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'ledger_entries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('operation', sa.String(), nullable=False),
        sa.Column('amount', sa.Integer(), nullable=False),
        sa.Column('nonce', sa.String(), nullable=False),
        sa.Column('owner_id', sa.String(), nullable=False),
        sa.Column('created_on', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nonce')
    )

def downgrade():
    op.drop_table('ledger_entries') 