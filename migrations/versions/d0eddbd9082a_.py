"""empty message

Revision ID: d0eddbd9082a
Revises: 
Create Date: 2023-01-27 19:46:11.678699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0eddbd9082a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.drop_table('shipping_template')
    op.add_column('item', sa.Column('id', sa.String(), nullable=False))
    op.alter_column('item', 'title',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('item', 'shipping_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('item_shipping_id_fkey', 'item', type_='foreignkey')
    op.drop_column('item', 'item_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('item_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.create_foreign_key('item_shipping_id_fkey', 'item', 'shipping_template', ['shipping_id'], ['shipping_id'])
    op.alter_column('item', 'shipping_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('item', 'title',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.drop_column('item', 'id')
    op.create_table('shipping_template',
    sa.Column('shipping_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('shipping_name', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('shipping_time', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('shipping_id', name='shipping_template_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
