from odoo import models, fields

class Course(models.Model):
    _name = "course.management"
    _description = "Course"

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code", required=True)
    credit = fields.Integer(string="Credit")
    student_ids = fields.Many2many(
        "student.management",
        string="Enrolled Students"
    )