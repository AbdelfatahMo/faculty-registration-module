from odoo import fields, models


class ApplicationInfo(models.Model):
    _name = 'application.info'
    _description = 'Application Information'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        required=True,
        copy=False
    )

    address = fields.Char(string="City", required=True)

    national_number = fields.Integer(
        required=True
    )

    pesonal_image = fields.Binary(
        required=True
    )

    age = fields.Integer(
        required=True
    )

    date_of_birth = fields.Date(
        required=True
    )

    height = fields.Float(
        required=True
    )

    weight = fields.Float(
        required=True)

    secondary_certification_image = fields.Binary(
        required=True
    )

    degree_with_precent = fields.Float(
        required=True,
        default=0
    )

    degree_with_numbers = fields.Float(
        required=True,
        default=0
    )

    number_of_family = fields.Integer(
        required=True
    )

    memeber_of_family_ids = fields.Many2many(
        "family.memeber",
        string="Name"
        )

    family_memeber_age = fields.Integer(string="Age")

    faculty_ids = fields.Many2many(
        'registration.faculty',
        string='Desired Faculties',
        required=True
    )

    expected_faculty = fields.Reference(
        [('registration.faculty', 'Faculty')],
    )

    desired_faculty = fields.Reference(
        [("registration.faculty", 'Faculty')],
        required=True
    )

    reason_of_desired = fields.Text(
        required=True
    )

    skill_ids = fields.Many2many(
        "student.skill",
        string='Skills',
        required=True
    )


    

# @api.depends('depends')
# def _compute_age(self):
#     for record in self:   
#         record.age = something


