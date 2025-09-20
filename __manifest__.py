{
    'name': "Student Management",
    'summary': "Manage Students and Courses",
    'description': """""",
    'author': "Rakibul Alam",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/course_view.xml',
        'views/menu.xml',
        'report/student_report_template.xml'
    ],
    'installable': True,
    'application': True
}

