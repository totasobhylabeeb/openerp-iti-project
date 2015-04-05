from openerp.osv import orm, fields
class category(orm.Model):
    _name = 'sales.category'
    _columns = {
        'name':fields.char('Name'),
        'catid':fields.integer('CategoryID'),
        'subcatid':fields.one2many('sales.subcategory','catid','subcategory'),

    }

class subcategory(orm.Model):
    _name = 'sales.subcategory'
    _columns = {
        'name':fields.char('Name'),
        'subcatid':fields.integer('SubCategoryID'),
        'catid': fields.many2one('sales.category', 'category'),
        'subsubcatid':fields.one2many('sales.subsubcategory','subsubcatid','subsubcategory'),

    }

class subsubcategory(orm.Model):
    _name = 'sales.subsubcategory'
    _columns = {
        'name':fields.char('Name'),
        'subsubcatid':fields.integer('SubSubCategoryID'),
        'subcatid': fields.many2one('sales.subcategory', 'subcategory'),


    }

class product(orm.Model):
    _name = 'sales.product'

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
        'catid': fields.many2one('sales.category', 'category', required=True),
        'subcat': fields.many2one('sales.subcategory', 'subcategory', required=True),
        'subsubcatid': fields.many2one('sales.subsubcategory', 'subsubcategory', required=True),
        'code': fields.function(_get_concatenate_values, method=True, string='Reference', type='many2one'),

    }
















