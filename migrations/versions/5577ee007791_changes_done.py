"""Changes done

Revision ID: 5577ee007791
Revises: 77fa77b301e5
Create Date: 2025-01-30 12:50:50.144884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5577ee007791'
down_revision = '77fa77b301e5'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('booking', schema=None) as batch_op:
        # Avoid dropping constraints if unsure about names
        batch_op.create_foreign_key('fk_booking_fitness_class', 'fitness_class', ['fitness_class_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('fk_booking_user', 'user', ['user_id'], ['id'], ondelete='CASCADE')


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        # Drop constraints by name if necessary
        batch_op.drop_constraint('fk_booking_fitness_class', type_='foreignkey')
        batch_op.drop_constraint('fk_booking_user', type_='foreignkey')

        # Recreate the original foreign key constraints
        batch_op.create_foreign_key('fk_booking_fitness_class', 'fitness_class', ['fitness_class_id'], ['id'])
        batch_op.create_foreign_key('fk_booking_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
