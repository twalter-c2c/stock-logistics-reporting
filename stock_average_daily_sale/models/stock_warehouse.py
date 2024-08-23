# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    average_daily_sale_root_location_id = fields.Many2one(
        comodel_name="stock.location",
        string="Average Daily Sale Root Location",
        check_company=True,
        help="This is the root location for daily sale average stock computations",
    )

    @api.model_create_multi
    def create(self, vals_list):
        # set the lot_stock_id of a newly created WH
        # as an Average Daily Sale Root Location
        warehouses = super().create(vals_list)
        for warehouse, vals in zip(warehouses, vals_list):
            if vals.get('lot_stock_id'):
                warehouse.average_daily_sale_root_location_id = vals['lot_stock_id']
        return warehouses
