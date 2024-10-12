from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.books"
    _description = "Library Books"

    name = fields.Char('Title', required=True)
    author_id = fields.Many2one('hr.employee', string="Author", required=True)
    isbn = fields.Char('ISBN')
    category = fields.Many2one('library.category', string="Category", required=True)
    available = fields.Boolean('Available', default=True)
    publication_date = fields.Date('Publish Date')


class LibraryCategory(models.Model):
    _name = "library.category"
    _description = "Library Category"

    name = fields.Char('Name', required=True)
    description = fields.Char('Description')
