from odoo import api, fields, models
from datetime import datetime

class Field_create(models.Model):
    _name ="create.field"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    date = fields.Date(string="Date", default=datetime.today())
    address = fields.Text(string='Address')
    average_mark = fields.Float(string='Average mark')

    gender = fields.Selection([('Male','Male'),('Female','Female')],string='Gender',default='Male')
    description = fields.Html(string='Description')
    create_date = fields.Datetime(string='Date of Create')
    file_for_import = fields.Binary(string='File for upload')
    active = fields.Boolean(string="Active", default=True)


