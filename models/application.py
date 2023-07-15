from datetime import datetime
from odoo import fields, models, api, _


class ApplicationInfo(models.Model):
    _name = 'application.info'
    _description = 'Application Information'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    _rec_name = 'name'
    _order = 'name ASC'

    _sql_constraints = [
        (
            'national_id_unique',
            'unique(national_id)',
            _('Please make sure about your National ID')
        )
    ]

    name = fields.Char(
        required=True,
        copy=False
    )

    address = fields.Char(string="City", required=True)

    national_id = fields.Integer(
        # required=True
    )

    pesonal_image = fields.Binary(
        # required=True
    )

    age = fields.Integer(
        compute="_compute_age",
    )

    date_of_birth = fields.Date(
        
        default=datetime(2005,1,1)       
        # required=True
    )

    ref = fields.Char(
        readonly=True,
    )

    height = fields.Float(
        # required=True
    )

    weight = fields.Float(
        # required=True
    )

    secondary_certification_image = fields.Binary(
        # required=True
    )

    degree_with_precent = fields.Float(
        # required=True,
        default=0
    )

    degree_with_numbers = fields.Float(
        # required=True,
        default=0
    )

    number_of_family = fields.Integer(
        # required=True
    )

    memeber_of_family_ids = fields.Many2many(
        comodel_name="family.memeber",
        string="Name"
    )

    desired_faculty_ids = fields.Many2many(
        comodel_name='registration.faculty',
        string='Desired Faculties',
        # required=True
    )

    expected_faculty = fields.Reference(
        selection=[('registration.faculty', 'Faculty')],
    )

    reason_of_desired = fields.Text(
        # required=True
    )

    skill_ids = fields.Many2many(
        comodel_name="student.skill",
        string='Skills',
        # required=True
    )

    @api.model
    def create(self, values):
        result = super(ApplicationInfo, self)
        values['ref'] = self.env['ir.sequence'].next_by_code(
            "application.info")
        return result.create(values)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = datetime.today()
        for record in self:
            record.age = today.year - record.date_of_birth.year - \
                ((record.date_of_birth.month, record.date_of_birth.day)
                 > (today.month, today.day))
        


# @api.depends('depends')
# def _compute_age(self):
#     for record in self:
#         record.age = something
