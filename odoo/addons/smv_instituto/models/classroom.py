# -*- coding: utf-8 -*-

from odoo import models, fields

class Classroom(models.Model):
    _name = 'smv_instituto.classroom'
    _description = 'Classroom'

    name = fields.Char(string='Name', required=True, help='Introduce the name of the classroom.')
    code = fields.Char(string='Code', required=True, help='Introduce the unique code for the classroom.')
    capacity = fields.Integer(string='Capacity', help='Introduce the capacity of the classroom.')
    location = fields.Char(string='Location', help='Introduce the location of the classroom within the institute.')

    student_ids=fields.One2many('smv_instituto.student', 'classroom_id', string='Students')
    course_id=fields.Many2one('smv_instituto.course', string='Course')
    teacher_id=fields.Many2one('smv_instituto.teacher', string='Teacher')