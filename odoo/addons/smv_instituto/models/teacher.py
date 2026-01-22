# -*- coding: utf-8 -*-

from odoo import models, fields

class Teacher(models.Model):
    _name = 'smv_instituto.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True, help='Introduce the name of the teacher.')
    code = fields.Char(string='Code', required=True, help='Introduce the unique code for the teacher.')
    dni = fields.Char(string='DNI', required=True, help='Introduce the DNI of the teacher.')
    phone = fields.Char(string='Phone', help='Introduce the phone number of the teacher.')
    email = fields.Char(string='Email', help='Introduce the email address of the teacher.')
    birth_date = fields.Date(string='Birth Date', help='Introduce the birth date of the teacher.')
    gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ], string='Gender', help='Introduce the gender of the teacher.')

    subject_ids = fields.Many2many('smv_instituto.subject', string='Subjects')
    classroom_ids = fields.One2many('smv_instituto.classroom', 'teacher_id', string='Classrooms')
    course_ids = fields.One2many('smv_instituto.course', 'teacher_id', string='Courses')