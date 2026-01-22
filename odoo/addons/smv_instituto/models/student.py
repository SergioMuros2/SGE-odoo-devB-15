# -*- coding: utf-8 -*-

from odoo import models, fields

class Student(models.Model):
    _name='smv_instituto.student'
    _description='Student'

    name=fields.Char(string='Name', required=True, help='Introduce the name of the student.')
    code=fields.Char(string='Code', required=True, help='Introduce the unique code for the student.')
    dni=fields.Char(string='DNI', required=True, help='Introduce the DNI of the student.')
    phone=fields.Char(string='Phone', help='Enter the parents phone number.')
    email=fields.Char(string='Email', help='Introduce the parents email address.')
    birth_date=fields.Date(string='Birth Date', help='Introduce the birth date of the student.')
    gender=fields.Selection([
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ], string='Gender', help='Introduce the gender of the student.')

    classroom_id=fields.Many2one('smv_instituto.classroom', string='Classroom',)
    course_id=fields.Many2one('smv_instituto.course', string='Course',)
    subject_ids=fields.Many2many('smv_instituto.subject', string='Subjects',)