from odoo import fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [
        ('vin_engie_code_parts_uniq',
         'unique ('
         'catalog_auto_vin, catalog_auto_engine_code, catalog_auto_parts)',
         _('There is another product with the same vin/engine code/parts!'))
    ]

    catalog_auto_year = fields.Char(string='Year')
    catalog_auto_car_color_id = fields.Many2one(
        comodel_name='catalog.auto.color', string='Color')
    catalog_auto_engine_code = fields.Char(size=10, string='Engine code')
    catalog_auto_transmission_id = fields.Many2one(
        comodel_name='catalog.auto.transmission', string='Transmission')
    catalog_auto_part_id = fields.Many2one(
        comodel_name='catalog.auto.parts', string='Parts')
    catalog_auto_engine_volume_id = fields.Many2one(
        comodel_name='catalog.auto.engine.volume', string='Engine volume')
    catalog_auto_model_id = fields.Many2one(
        comodel_name='catalog.auto.model', string='Model')
    catalog_auto_vin_id = fields.Many2one(
        comodel_name='catalog.auto.vin', string='VIN')
    catalog_auto_fuel_type_id = fields.Many2one(
        comodel_name='catalog.auto.fuel.type', string='Fuel type')
    catalog_auto_power_id = fields.Many2one(
        comodel_name='catalog.auto.power', string='Power')
    catalog_auto_last_odometer_value = fields.Integer(
        readonly=False, track_visibility='onchange',
        string='Odometer value')
