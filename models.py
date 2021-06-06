from flask_sqlalchemy import SQLAlchemy 
from app import db
from sqlalchemy import create_engine, Column, Integer, String, Sequence




class testtopic(db.Model):
    __tablename__ = 'test_topic_table'

    id = db.Column(db.Integer, primary_key=True)
    topicsref = db.Column(db.String())
    owner = db.Column(db.String())
    project = db.Column(db.String())
    # compdatetime = db.Column(db.DateTime)

    def __init__(self, topicsref, owner,project):
        self.topicsref = topicsref
        self.owner = owner
        self.project = project
        # self.compdatetime = compdatetime

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'topicsref': self.topicsref,
            'owner': self.owner,
            'project':self.project,
            #  'compdatetime':self.compdatetime,
        }


class maintopic(db.Model):
    __tablename__ = 'maintopicstable'

    id = db.Column(db.Integer, primary_key=True)
    topicname = db.Column(db.String())
    owner = db.Column(db.String())
    project = db.Column(db.String())
    clustername = db.Column(db.String())
    # compdatetime = db.Column(db.DateTime)

    def __init__(self, topicname, owner,project,clustername):
        self.topicname = topicname
        self.owner = owner
        self.project = project
        self.clustername = clustername
        # self.compdatetime = compdatetime

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'topicname': self.topicname,
            'owner': self.owner,
            'project':self.project,
            'clustername' :self.clustername
            #  'compdatetime':self.compdatetime,
        }

class empm(db.Model):
    __tabledept__ = 'emp'

    id = db.Column(Integer, primary_key=True)
    dept =  db.Column(db.String())
    empname = db.Column(db.String())
    empnid = db.Column(db.String())
    empnuid = db.Column(db.String())
    groups = db.Column(db.String())
    category = db.Column(db.String())
    location = db.Column(db.String())
    role = db.Column(db.String())
    password = db.Column(db.String())
  
    def __init__(self, dept,location,empname,empnid,empnuid,groups,role,password,category):
        self.dept = dept
        self.location = location
        self.empname = empname
        self.empnuid = empnuid
        self.empnid = empnid
        self.role = role
        self.groups = groups
        self.password = password
        self.category = category
        

    def __repr__(self):
        return f"<Car {self.id}>"
    def serialize(self):
        return {
            'id': self.id,
              'dept' :self.dept , 
         'location':self.location,
        'empname' :self.empname  ,
         'empnuid' : self.empnuid ,
         'empnid' :self.empnid ,
         'role'  : self.role ,
        'groups' :self.groups , 
        'password' : self.password , 
        'category' : self.category 
            #  'compdatetime':self.compdatetime,
        }
# class todolog(db.Model):
#     __tablename__ = 'todolog'

#     id = db.Column(db.Integer, primary_key=True)
#     log = db.Column(db.String())
#     textid =  db.Column(db.Integer, db.ForeignKey('todo.id'), nullable=False)
#     createdon = db.Column(db.DateTime)

#     def __init__(self, textid, log,createdon, compdatetime):
#         self.textid = textid
#         self.log = log
#         self.createdon = createdon


#     def __repr__(self):
#         return '<id {}>'.format(self.id)

#     def serialize(self):
#         return {
#             'id': self.id,
#             'textid': self.textid,
#             'log': self.log,
#             'createdon':self.createdon,

#         }

class todolog(db.Model):
    __tablename__ = 'todolog'

    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String())
    text =  db.Column(db.String())
    createdon = db.Column(db.DateTime)

    def __init__(self, text, log,createdon):
        self.text = text
        self.log = log
        self.createdon = createdon


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'log': self.log,
            'createdon':self.createdon,

        }

