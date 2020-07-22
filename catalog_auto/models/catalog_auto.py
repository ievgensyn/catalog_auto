from odoo import fields, models


class Model(models.Model):
    _name = 'catalog.auto.model'
    _description = 'Catalog Auto Model'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Model name already exists !')
    ]

    name = fields.Char(size=50)
    brand_id = fields.Many2one(
        comodel_name='product.brand')
    vin_ids = fields.One2many(
        comodel_name='catalog.auto.vin',
        inverse_name='model_id')


class Vin(models.Model):
    _name = 'catalog.auto.vin'
    _description = 'Catalog Auto VIN'
    _rec_name = 'vin'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'VIN name already exists !')
    ]

    vin = fields.Char(size=14)
    model_id = fields.Many2one(
        comodel_name='catalog.auto.model')


class EngineCode(models.Model):
    _name = 'catalog.auto.engine.code'
    _description = 'Catalog Auto Engine Code'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Engine Code name already exists !')
    ]

    name = fields.Char(size=10)
    model_id = fields.Many2one(
        comodel_name='catalog.auto.model')


class Parts(models.Model):
    _name = 'catalog.auto.parts'
    _description = 'Catalog Auto Parts'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Parts name already exists !')
    ]

    name = fields.Char(size=14)
    model_id = fields.Many2one(
        comodel_name='catalog.auto.model')


class Color(models.Model):
    _name = 'catalog.auto.color'
    _description = 'Catalog Auto Color'

    name = fields.Char(size=10)


class Transmission(models.Model):
    _name = 'catalog.auto.transmission'
    _description = 'Catalog Auto Transmission'

    name = fields.Char(size=10)


class EngineVolume(models.Model):
    _name = 'catalog.auto.engine.volume'
    _description = 'Catalog Auto Engine Volume'

    name = fields.Char(size=4)


class FuelType(models.Model):
    _name = 'catalog.auto.fuel.type'
    _description = 'Catalog Auto Fuel Type'

    name = fields.Char(size=10)


class Power(models.Model):
    _name = 'catalog.auto.power'
    _description = 'Catalog Auto Power'

    name = fields.Char(size=4)
