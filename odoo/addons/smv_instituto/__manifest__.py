# -*- coding: utf-8 -*-
{
'name': "smv_instituto",
'summary': "Gestión de un instituto",
'description': "El módulo de Gestión de Instituto permite administrar de forma centralizada "
"la información académica y administrativa. Facilita el registro y control de alumnos, "
"docentes, cursos y materias",
'author': "Sergio Muros Vera",
'website': "https://www.educa2.madrid.org/web/iescanaveral",
'category': 'Uncategorized',
'version': '0.1',
# any module necessary for this one to work correctly
'depends': ['base'],
# always loaded
'data': [
# 'security/ir.model.access.csv',
'views/views.xml',
'views/templates.xml',
],
# only loaded in demonstration mode
'demo': [
'demo/demo.xml',
],
}