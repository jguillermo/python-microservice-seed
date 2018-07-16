# -*- coding: utf-8 -*-
"""create stage table

Revision ID: 0c991f431dfa
Revises: 956cea0a528d
Create Date: 2018-04-09 21:06:52.558940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c991f431dfa'
down_revision = '956cea0a528d'
branch_labels = None
depends_on = None

stageTable = 'stage'


def upgrade():
    table = op.create_table(
        stageTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('alias', sa.String(255), nullable=False),
        sa.Column('type', sa.SmallInteger, nullable=False, server_default='1', comment='1:Proyecto,2:Unidad'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )

    op.bulk_insert(
        table,
        [
            {'id': 1, 'name': 'En Pre-venta', 'alias': 'pre-venta', 'type': 1},
            {'id': 2, 'name': 'En Construcción', 'alias': 'construccion', 'type': 1},
            {'id': 3, 'name': 'En Estreno', 'alias': 'estreno', 'type': 1},
            {'id': 4, 'name': 'Disponible', 'alias': 'disponible', 'type': 2},
            {'id': 5, 'name': 'Separado', 'alias': 'separado', 'type': 2},
            {'id': 6, 'name': 'Alquilado', 'alias': 'alquilado', 'type': 2},
            {'id': 7, 'name': 'Vendido', 'alias': 'vendido', 'type': 2},
        ]
    )


def downgrade():
    op.drop_table(stageTable)
