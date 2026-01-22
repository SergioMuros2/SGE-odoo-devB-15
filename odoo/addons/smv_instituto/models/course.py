# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'smv_instituto.course'
    _description = 'Course'
    
    year = fields.Selection([
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ], string='Year', help='Select the year of the course.')
    group = fields.Selection([
        ('A', 'Group A'),
        ('B', 'Group B'),
        ('C', 'Group C'),
    ], string='Group', help='Select the group of the course.')
    code = fields.Char(string='Code', required=True, help='Introduce the unique code for the course.')

    teacher_id = fields.Many2one('smv_instituto.teacher', string='Teacher')
    classroom_ids = fields.One2many('smv_instituto.classroom', 'course_id', string='Classrooms')
    student_ids = fields.One2many('smv_instituto.student', 'course_id', string='Students')
    
    
