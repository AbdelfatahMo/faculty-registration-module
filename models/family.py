from odoo import models, fields


class FamilyMemeber(models.Model):
    _name = 'family.memeber'
    _description = 'Family Memeber'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        required=True,
    )
    

    age = fields.Integer()
    
    

    