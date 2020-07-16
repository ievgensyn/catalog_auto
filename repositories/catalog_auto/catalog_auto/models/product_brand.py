from odoo import fields, models


class ProductBrand(models.Model):
    _inherit = 'product.brand'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Brand name already exists !')
    ]

    catalog_auto_model_ids = fields.One2many(
        comodel_name='catalog.auto.model',
        inverse_name='brand_id',
        string='Model', )
