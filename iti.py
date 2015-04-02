from openerp.osv import orm, fields


class iti_students(orm.Model):
    gender = [('f', 'female'), ('m', 'male')]
    grade = [('g', 'good'), ('v', 'very good'), ('e', 'excellent')]
    graduation_year = [('2', '2012'), ('3', '2013'), ('4', '2014')]
    _name = 'iti.student'
    _columns = {
        'name': fields.char('Name'),
        'age': fields.integer('Age'),
        'salary': fields.integer('Salary'),
        'gender': fields.selection(gender, 'Gender'),
        'faculty': fields.char('Faculty'),
        'grade': fields.selection(grade, 'Grade'),
        'graduation_year': fields.selection(graduation_year, 'Graduation_year'),
        'info': fields.html('info'),
        'accept': fields.text('Accept'),
        'check': fields.boolean('Check'),
         'pic': fields.binary('Image',widget='Image'),
 'department_id': fields.many2one('iti.department', 'Department'),
        'skills_ids':fields.many2many('iti.skills',string='skills')

      

    }
class iti_manger(orm.Model):
    gender = [('f', 'female'), ('m', 'male')]
    grade = [('g', 'good'), ('v', 'very good'), ('e', 'excellent')]
    graduation_year = [('2', '2012'), ('3', '2013'), ('4', '2014')]
    _name = 'iti.manger'
    _columns = {
        'name': fields.char('Name'),
        'age': fields.integer('Age'),
        'salary': fields.integer('Salary'),
        'gender': fields.selection(gender, 'Gender'),
        'faculty': fields.char('Faculty'),
        'grade': fields.selection(grade, 'Grade'),
        'graduation_year': fields.selection(graduation_year, 'Graduation_year'),
        'info': fields.html('info'),
        'accept': fields.text('Accept'),
        'check': fields.boolean('Check'),
         'pic': fields.binary('Image',widget='Image'),
        'department_id': fields.many2one('iti.department', 'Department'),
        'skills_ids':fields.many2many('iti.skills',string='skills')

    }



class iti_department(orm.Model):
    _name = 'iti.department'
    _columns = {
        'dname': fields.char('Department_name'),
        'desc': fields.text('Descraption'),
        'student_ids': fields.one2many('iti.student','department_id' ,string='Students'),
          'skills_id': fields.one2many('iti.skills', 'department_skills_ids','Skills')
    }
    _rec_name = 'dname'

class iti_skills(orm.Model):
    _name = 'iti.skills'
    _columns = {
        'name': fields.char('skill_name'),
        'desc': fields.text('Descraption'),
        'department_skills_ids': fields.many2one('iti.department',string='Skills'),
        'student_skills_ids':fields.many2many('iti.student',string='student_skills')

    }
