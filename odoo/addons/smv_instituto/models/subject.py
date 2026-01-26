# -*- coding: utf-8 -*-

from odoo import models, fields

class Subject(models.Model):
    _name = 'smv_instituto.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True, help='Introduce the name of the subject.')
    code = fields.Char(string='Code', required=True, help='Introduce the unique code for the subject.')
    description = fields.Text(string='Description', help='Introduce a brief description of the subject.')
    weekly_hours = fields.Integer(string='Weekly Hours', help='Introduce the number of weekly hours for the subject.')
    subject_type = fields.Selection([
        ('C', 'Core'), 
        ('E', 'Elective'), 
        ('X', 'Extracurricular'),
    ], string='Subject Type', help='Select the type of the subject.')

    teacher_ids = fields.Many2many('smv_instituto.teacher', string='Teachers')
    student_ids = fields.Many2many('smv_instituto.student', string='Students')