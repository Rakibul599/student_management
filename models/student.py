from odoo import fields,models

class Student(models.Model):
    _name="student.management"
    _description="Student "


    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email",required=True)
    roll_no = fields.Char(string="Roll Number", required=True)
    department = fields.Char(string="Department")
    course_ids = fields.Many2many(
        "course.management",
        string="Enrolled Courses"
    )


    def action_show_courses(self):
        """
        This method returns a window action to show the courses enrolled by the student.
        It explicitly defines the views to be used to avoid client errors.
        """
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Enrolled Courses",
            "res_model": "course.management",
            "views": [(self.env.ref('student_management.course_list_view').id, 'list'),
                      (self.env.ref('student_management.course_form_view').id, 'form')],
            "domain": [("id", "in", self.course_ids.ids)],
            "target": "current",
        }

