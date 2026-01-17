# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'smv_instituto.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True, help='Introduce the name of the course.')
    code = fields.Char(string='Code', required=True, help='Introduce the unique code for the course.')
    description = fields.Text(string='Description', help='Introduce a brief description of the course.')
    level = fields.Selection([
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ], string='Level', help='Select the level of the course.')
    group = fields.Selection([
        ('A', 'Group A'),
        ('B', 'Group B'),
        ('C', 'Group C'),
    ], string='Group', help='Select the group of the course.')
