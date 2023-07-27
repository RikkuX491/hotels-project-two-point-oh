"""Create hotels, customers, and reviews tables

Revision ID: 0b549414c63c
Revises: c907cb195bed
Create Date: 2023-07-26 16:38:57.910983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b549414c63c'
down_revision = 'c907cb195bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.CheckConstraint('(first_name != last_name)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], name=op.f('fk_reviews_hotel_id_hotels')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('hotels')
    op.drop_table('customers')
    # ### end Alembic commands ###