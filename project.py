from openerp.osv import orm, fields


class project_category(orm.Model):
    _name = 'project.category'
    _columns = {
        'name': fields.char('Name', size=30 , required=True),
        'description': fields.text('Description'),
        'code': fields.integer('Code' , required=True),
        'subcategory_ids': fields.one2many('project.subcategory','category_id', 'Sub Category'),
    }

class project_subcategory(orm.Model):
    _name = 'project.subcategory'
    _columns = {
        'name': fields.char('Name', size=30 , required=True),
        'description': fields.text('Description'),
        'code': fields.integer('Code',required=True),
        'category_id': fields.many2one('project.category', ' Category'),
        'subsubcategory_ids': fields.one2many('project.subsubcategory', 'subcategory_id', 'Sub Category')

    }

class project_subsubcategory(orm.Model):
    _name = 'project.subsubcategory'
    _columns = {
        'name': fields.char('Name', size=30),
        'description': fields.text('Description'),
        'code': fields.integer('Code', required=True),
        'subcategory_id': fields.many2one('project.subcategory', 'Sub Category')

    }

class project_product(orm.Model):
    _name = 'project.product'

    def _get_concatenate_values(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        products=self.browse(cr,uid,ids)
        for product in products:
            result[product.id] = product.catid+product.subcat+product.subsubcatid+product.prod_id


        # result = dict((x,'') for x in ids)
        # for r in records:
        #     if(r.catid and r.subcat):
        #         result[r.id] = "%s %f" % \
        #                  (r.catid.name or '', r.subcat.name or 0.0)
        #                   # (r.field1.field1 or '', r.field2.field2 or 0.0)
        return result

    _columns = {
        'name':fields.char('Name'),
        'prod_id':fields.integer('Product_ID'),
        'price':fields.char('Price'),
        'Type':fields.char('Type'),
        'company_name':fields.char('Company Name'),
        'image':fields.binary('Image'),
        'production_date':fields.date('Production Date'),
        'expiry_date':fields.date('Expiry Date'),
        'catid': fields.many2one('project.category', 'category', required=True),
        'subcat': fields.many2one('project.subcategory', 'subcategory', required=True),
        'subsubcatid': fields.many2one('project.subsubcategory', 'subsubcategory', required=True),
        'code': fields.function(_get_concatenate_values, method=True, string='Reference', type='many2one'),
        'min':fields.integer("Min Quantity"),
        'max':fields.integer("Max Quantity"),
    }


class project_warehouse(orm.Model):
    _name = 'project.warehouse'
    _columns = {
        'name':fields.char('Name', size=30, required=True),
        'address':fields.char('Address', size=100),
        #'keeper_id':fields.many2one('hr','Keeper',select=True),
        #'manager_id':fields.many2one('hr','Manager',select=True),
        #'supermanager_id':fields.many2one('hr','Supermanager',select=True),
        'product_ids':fields.one2many('iti.product', string="Products"),

    }
