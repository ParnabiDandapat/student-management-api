from flask import Flask, request,jsonify
import re
app=Flask(__name__)
students={}

email_regex=r'^[a-zA-Z0-9._+*-]+@gmail\.com$'
phone_regex=r'^[6-9]\d{9}$'

#home
@app.route('/',methods=['GET'])
def home():
    return jsonify ({'success':'Welcome To Student Management System'}),200

#add
@app.route('/add',methods=['POST'])
def add_student():
    data=request.json
    for stu in data:
        id=int(stu.get('id'))
        name=stu.get('name')
        email=stu.get('email')
        phone=stu.get('phone')
    if not re.match(email_regex,email):
        return jsonify({'error':'Invalid email'}),400
    if not  re.match(phone_regex,phone):
        return jsonify({'error':'Invalid Phone number'}),400
    for s in students.values():
        if s['email']==email:
            return jsonify ({
                'message':'email has already added, please enter another email'
            })
        if s['phone']==phone:
            return jsonify({
                'error':'phone number has already added, please enter another phone number'
            })
    students[id]={
        'name':name,
        'email':email,
        'phone':phone
    }    
    return jsonify({
        'success':f'student {name} with id {id} successfully added'
    })
        
    
#view
@app.route('/view',methods=['GET'])
def view_students():
    return jsonify (students)


#delete
@app.route('/delete',methods=['POST'])
def del_students():
    data=request.json
    for stu in data:
        id=int(stu.get('id'))
    if id in students:
        del students[id]
        return jsonify({
            'message':'Student is successfully deleted'
        })
    else :
        return jsonify({
           'error':'Student not found' 
        })
    

if __name__=="__main__":
    app.run(debug=True,port=8000)



