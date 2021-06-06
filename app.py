from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import datetime

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:iotmax@localhost:5432/kafkaui"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5000


db = SQLAlchemy(app)

from models import testtopic,maintopic,empm
cors = CORS(app, resources= {
    r"/*":{
        "origins":"*",
        "Access-Control-Allow-Origin":"*"
    }
})
app.config['SECRET_KEY']='iotmaxapplication'
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'massage':'Token is invalid'}),403
        try:
            datas = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'massage':'Token is invalid'}),403
        return f(*args,**kwargs)
    return decorated

@app.route("/")
def hello():
    return "Hello welcome to ToDo API!"


@app.route('/testtopic', methods=['POST', 'GET'])
def todopg():
    if request.method == 'POST':
        data = request.get_json()
        new_car = testtopic(topicsref = data['topicsref'], owner = data['owner'], project = data['project'])

        db.session.add(new_car)
        db.session.commit()


        data = {"message": f"name created successfully"}
        return jsonify(data), 200


    elif request.method == 'GET':
        things = testtopic.query.all()
        results = [
            {
              "id" : thing.id,
                "topicsref" : thing.topicsref,
                "owner" : thing.owner,
                "project" : thing.project
                #  "compdatetime" : thing.compdatetime

            } for thing in things]

        return  jsonify(results)

@app.route('/testtopic/<id>', methods=['GET', 'PUT', 'DELETE'])
def depts(id):
    thing = testtopic.query.get_or_404(id)

    if request.method == 'GET':
        response =   {
                "id" : thing.id,
                "topicsref" : thing.topicsref,
                "owner" : thing.owner,
                "project" : thing.project

        }
        return jsonify(response)

    elif request.method == 'PUT':
        data = request.get_json()
        thing.topicsref = data['topicsref']
        thing.owner = data['owner']
        thing.project = data['project']

        # car.createdon = data['createdon']
        db.session.add(thing)
        db.session.commit()

        data = {"message": f"name updated successfully"}
        return jsonify(data), 200

    elif request.method == 'DELETE':
        data = request.get_json()
        thing.topicsref = data['topicsref']
        print('car ======================',thing.topicsref)
        db.session.delete(thing)

        db.session.commit()


        data = {"message": f"name deleted successfully"}
        return jsonify(data), 200

##################################################################################################################################################

##################################################################################################################################################
@app.route('/maintopic', methods=['POST', 'GET'])
def maintopicsa():
    if request.method == 'POST':
        data = request.get_json()
        new_car = maintopic(topicname = data['topicname'], clustername = data['clustername'], owner = data['owner'], project = data['project'])

        db.session.add(new_car)
        db.session.commit()


        data = {"message": f"name created successfully"}
        return jsonify(data), 200


    elif request.method == 'GET':
        things = maintopic.query.all()
        results = [
            {
              "id" : thing.id,
                "topicname" : thing.topicname,
                "owner" : thing.owner,
                "clustername":thing.clustername,
                "project" : thing.project
                #  "compdatetime" : thing.compdatetime

            } for thing in things]

        return  jsonify(results)



@app.route('/maintopicproject/<id>', methods=['POST', 'GET'])
def maintopicssa(id):


    
    things = maintopic.query.filter(maintopic.project == id).all()
    results = [
        {
            "id" : thing.id,
            "topicname" : thing.topicname,
            "owner" : thing.owner,
            "project" : thing.project
            #  "compdatetime" : thing.compdatetime

        } for thing in things]

    return  jsonify(results)



@app.route('/mainprojects', methods=['GET', 'PUT', 'DELETE'])
def maintopicsstopc():
    things = maintopic.query.with_entities(maintopic.project).distinct()

    if request.method == 'GET':
        response =   [{
              
                "project" : thing.project

            }for thing in things]
        return jsonify(response)

@app.route('/clusternames', methods=['GET'])
def maintopicsstopcs():
    things = maintopic.query.with_entities(maintopic.clustername).distinct()

    if request.method == 'GET':
        response =   [{
              
                "clustername" : thing.clustername

        }for thing in things]
        return jsonify(response)

@app.route('/clustercount', methods=['GET'])
def penddingclustercount():
    # datatag = "Pending"
    things = maintopic.query.with_entities(maintopic.clustername).distinct()

    if request.method == 'GET':
        response =   [{
              
                "clustername" : thing.clustername

        }for thing in things]
    print('things', type(things))
    results = len(response)
      
    
    return  jsonify({"count" : results})


@app.route('/projectscount', methods=['GET'])
def penddingprojectscount():
    # datatag = "Pending"
    things = maintopic.query.with_entities(maintopic.project).distinct()
    if request.method == 'GET':
        response =   [{
              
                "project" : thing.project

        }for thing in things]
    print('things', type(things))
    results = len(response)
    
      
    
    return  jsonify({"count" : results})

@app.route('/projectsname', methods=['GET'])
def penddingprojectsname():
    # datatag = "Pending"
    things = maintopic.query.with_entities(maintopic.project).distinct()
    if request.method == 'GET':
        response =   [{
              
                "project" : thing.project

        }for thing in things]
    print('things', type(things))
    
    
      
    
    return  jsonify(response)


@app.route('/topicscount', methods=['GET'])
def penddingcount():
    # datatag = "Pending"
    things = maintopic.query.with_entities(maintopic.topicname).distinct()
    if request.method == 'GET':
        response =   [{
              
                "topicname" : thing.topicname

        }for thing in things]
    print('things', type(things))
    results = len(response)
      
    
    return  jsonify({"count" : results})

@app.route('/ownercount', methods=['GET'])
def penddingownercount():
    # datatag = "Pending"
    things = maintopic.query.with_entities(maintopic.owner).distinct()
    if request.method == 'GET':
        response =   [{
              
                "owner" : thing.owner

        }for thing in things]
    print('things', type(things))
    results = len(response)
      
    
    return  jsonify({"count" : results})

@app.route('/maintopic/<id>', methods=['GET', 'PUT', 'DELETE'])
def maintopicss(id):
    thing = maintopic.query.get_or_404(id)

    if request.method == 'GET':
        response =   {
                "id" : thing.id,
                "topicname" : thing.topicname,
                "owner" : thing.owner,
                "project" : thing.project,
                "maintopic" :thing.maintopic

        }
        return jsonify(response)

    elif request.method == 'PUT':
        data = request.get_json()
        thing.topicname = data['topicname']
        thing.owner = data['owner']
        thing.project = data['project']
        thing.maintopic = data['maintopic']

        # car.createdon = data['createdon']
        db.session.add(thing)
        db.session.commit()

        data = {"message": f"name updated successfully"}
        return jsonify(data), 200

    elif request.method == 'DELETE':
        data = request.get_json()
        thing.topicname = data['topicname']
        print('car ======================',thing.topicsref)
        db.session.delete(thing)

        db.session.commit()


        data = {"message": f"name deleted successfully"}
        return jsonify(data), 200



@app.route('/emp', methods=['POST', 'GET'])
def emp():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
           
            new_car = empm(dept=data['dept'],role= data['role'],password=data['password'], location=data['location'], category = data['category'], groups=data['groups'], empnuid=data['empnuid'], empnid=data['empnid'], empname=data['empname'])
            db.session.add(new_car)
            db.session.commit()
            return jsonify('done')
        else:
            return jsonify('done')

    elif request.method == 'GET':
        things = empm.query.all()
        results = [
            {"id" : str(thing.id),
                "empname" : thing.empname,
                "empnid" : str(thing.empnid),
                "empnuid" : str(thing.empnuid),
                "dept" :str(thing.dept),
                "groups" : thing.groups,
                "category" : thing.category,
                "location" : thing.location,
                "role" : str(thing.role),
                "password" : thing.password
            } for thing in things]
        return  jsonify(results)
@app.route('/emp/<id>', methods=['GET', 'PUT', 'DELETE'])
def emps(id):
    car = empm.query.get_or_404(id)
    
    if request.method == 'GET':
        response = {
                "empname" : car.empname,
                "empnid" : car.empnid,
                "empnuid" : car.empnuid,
                "dept" : car.dept,
                "groups" : car.groups,
                "category" : car.category,
                "location" : car.location,
                "role": car.role,
                "password" : car.password
        }
        return jsonify(response)

    elif request.method == 'PUT':
        data = request.get_json()
        car.empname = data['empname']
        car.empnid = data['empnid']
        car.empnuid = data['empnuid']
        car.groups = data['groups']
        car.category = data['category']
        car.location = data['location']
        car.password = data['password']
        car.dept  = data['dept']
        car.role  = data['role']
        db.session.add(car)
        db.session.commit()
        return jsonify('done')

    elif request.method == 'DELETE':
        if car.empname != 'Admin':
            db.session.delete(car)
            db.session.commit()
            return jsonify('done')


@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    #login_user = Employee.find_one({'user_name' : username})
   # login_user = empm.query.filter_by(empname='username').first()

    login_user = empm.query.filter(empm.empname == username).value('password')
    roless =  empm.query.filter(empm.empname == username).value('role')
  
  
    if username:
        if login_user == password:
           # token= jwt.encode({'username':username,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=11000)},app.config['SECRET_KEY'])
            # Role = login_user['Roles']
            # return jsonify({'username' :username,'id': id  , "role" :roless })
            return jsonify({'username' :username , "role" :roless })
        else :
            return make_response('could not verify password is wrong! ',401,{'www-Authenticate':'Basic realm="Login required"'})
    else:
        return make_response('could not verify username is wrong! ',401,{'www-Authenticate':'Basic realm="Login required"'})
    return ' imei is not registered'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port = '5300')