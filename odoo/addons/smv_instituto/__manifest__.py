# -*- coding: utf-8 -*-
{
'name': "smv_instituto",
'summary': "Management of an institute",
'description': "This module of management of an institute allows centralized management "
"of academic and administrative information. It facilitates the registration and control of students, "
"teachers, courses and subjects",
'author': "Sergio Muros Vera",
'website': "https://www.educa2.madrid.org/web/iescanaveral",
'category': 'Uncategorized',
'version': '0.1',
# any module necessary for this one to work correctly
'depends': ['base'],
# always loaded
'data': [
# 'security/ir.model.access.csv',
'views/classroom.xml',
'views/course.xml',
'views/student.xml',
'views/subject.xml',
'views/teacher.xml',
],
# only loaded in demonstration mode
'demo': [
'demo/demo.xml',
],
}