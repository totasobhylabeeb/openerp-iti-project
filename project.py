from openerp.osv import orm, fields
class project_employees(orm.Model):
    gender = [('f', 'female'), ('m', 'male')]
    _name = 'project.employees'
    _columns = {
        'name': fields.char('Name'),
        'age': fields.integer('Age'),
        'salary': fields.integer('Salary'),
        'gender': fields.selection(gender, 'Gender'),
        'check': fields.boolean('Check'),
         'pic': fields.binary('Image',widget='Image'),
 'warehouse_id': fields.many2one('project.warehouse', 'Warehouse'),

    }

class project_category(orm.Model):
    _name = 'project.category'
    _columns = {
        'name': fields.char('Name', size=30),
        'description': fields.text('Description'),
        'code': fields.integer('Code'),
        'subcategory_ids': fields.one2many('project.subcategory','category_id', 'Sub Category'),
    }

class project_subcategory(orm.Model):
    _name = 'project.subcategory'
    _columns = {
        'name': fields.char('Name', size=30),
        'description': fields.text('Description'),
        'code': fields.integer('Code'),
        'category_id': fields.many2one('project.category', ' Category'),
        'subsubcategory_ids': fields.one2many('project.subsubcategory', 'subcategory_id', 'Sub Category')

    }


class project_subsubcategory(orm.Model):
    _name = 'project.subsubcategory'
    _columns = {
        'name': fields.char('Name', size=30),
        'description': fields.text('Description'),
        'code': fields.integer('Code'),
        'subcategory_id': fields.many2one('project.subcategory', 'Sub Category')

    }
class project_warehouse(orm.Model):
    _name = 'project.warehouse'
    _columns = {
        'name':fields.char('Name', size=30, required=True),
        'address':fields.char('Address', size=100),
 'category_ids': fields.many2one('project.category', 'Category'),

    }
