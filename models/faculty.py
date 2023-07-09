from odoo import models, fields


class RegistrationFaculty(models.Model):
    _name = 'registration.faculty'
    _description = 'RegistrationFaculty'

    _rec_name = 'name'
    _order = 'name ASC'

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]

    name = fields.Char(
        string='Name',
        required=True,
        copy=False
    )
    
    application_id = fields.Many2one('application.info')
