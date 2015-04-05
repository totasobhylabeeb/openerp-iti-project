from openerp.osv import orm, fields




class project_subcategory(orm.Model):
    _name = 'project.subcategory'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.char('Description'),
        'code': fields.char('Code'),
        'category_id': fields.many2one('project.category','Sub Category')
	'subsubcategory_ids': fields.one2many('project.subsubcategory','subcategory_id','SubSub Category')

    }

class project_subsubCategory(orm.Model):
    _name = 'project.subsubCategory'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.char('Description'),
        'code': fields.char('Code'),
        'subcategory_id': fields.many2one('project.subcategory','SubSub Category')

    }
