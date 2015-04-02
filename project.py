from openerp.osv import orm, fields


class iti_students(orm.Model):
    gender = [('m', 'Male'), ('f', 'Female')]
    grade = [('g', 'Good'), ('vg', 'VeryGood'), ('A', 'Accept'), ('e', 'Excellent')]
    graduationyear = [('first', 2012), ('second', 2013), ('third', 2014)]

    def change_department(self, cr, uid, ids, skills_id, context=None):

        skills = self.pool.get('iti.skills').browse(cr, uid, skills_id[0][2])
        for skill in skills:
            if skill.php == 'php':
                skill.dept_id.name = 'opensource'
            else:
                skill.dept_id.name = 'systemdevelopper'

    _name = 'iti.student'
    _columns = {
        'name': fields.char('Name', size=30, required=True),
        'tel': fields.char('Telephone'),
        'picture': fields.binary('Image'),
        'age': fields.integer('Age', size=3),
        'salary': fields.float('Salary', size=8),
        'gender': fields.selection(gender, 'Gender'),
        'grade': fields.selection(grade, 'Grade'),
        'graduationyear': fields.selection(graduationyear, 'Graduationyear'),
        'accepted': fields.boolean('Accepted'),
        'faculty': fields.char('Faculty', size=10),
        'birthday': fields.date('Birthday'),
        'signature': fields.html('Signature'),
        'skill': fields.text('Skill'),
        'department_id': fields.many2one('iti.department', 'Department'),
        'skills_id': fields.many2many('iti.skills', string='Skills')
    }


class iti_department(orm.Model):
    _name = 'iti.department'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('Description'),
        'students_ids': fields.one2many('iti.student', 'department_id', 'Students'),
        'skill_id': fields.many2one('iti.skills', 'Skills')

    }


class iti_skills(orm.Model):
    _name = 'iti.skills'
    _columns = {
        'php': fields.char('PHP'),
        'rails': fields.char('Rails'),
        'openerp': fields.char('OpenERP'),
        'dept_id': fields.one2many('iti.department', 'skill_id', 'Department')

    }