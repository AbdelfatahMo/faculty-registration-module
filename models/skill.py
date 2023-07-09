from odoo import models ,fields


class StudentSkill(models.Model):
    _name = 'student.skill'
    _description = 'Student Skill'

    _rec_name = 'name'
    _order = 'name ASC'
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]
    name = fields.Char(
        string='Name',
        required=True,
        copy=False,
    )

    
