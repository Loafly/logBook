from pymongo import MongoClient
import jwt
import datetime
import hashlib
import secrets
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, escape
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

# client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
client = MongoClient('localhost', 27017)
db = client.LogBook

# doc = {'eamil': 'aaa@aaa','password': 'bbb'}

# arr_coord = [
#     [358, 256, 18],
#     [428, 236, 16],
#     [503, 253, 17],
#     [577, 235, 17],
#     [656, 222, 18],
#     [726, 242, 16],
#     [744, 300, 18],
#     [682, 334, 16],
#     [601, 329, 17],
#     [531, 341, 15],

#     [453, 335, 13],
#     [376, 348, 18],
#     [312, 402, 16],
#     [363, 427, 15],
#     [442, 422, 16],
#     [510, 418, 18],
#     [590, 424, 16],
#     [656, 420, 18],
#     [725, 423, 17],
#     [733, 485, 17],

#     [682, 510, 18],
#     [615, 513, 19],
#     [546, 498, 18],
#     [463, 505, 17],
#     [396, 494, 18],
#     [325, 503, 19],
#     [243, 483, 17],
#     [171, 511, 17],
#     [218, 558, 18],
#     [288, 566, 18],

#     [357, 565, 17],
#     [423, 557, 17],
#     [479, 591, 17],
#     [553, 587, 17],
#     [610, 610, 16],
#     [670, 596, 16],
#     [752, 596, 16],
#     [821, 623, 19],
#     [853, 677, 19],
#     [793, 705, 19],

#     [724, 690, 16],
#     [659, 695, 17],
#     [606, 746, 16],
#     [529, 755, 17],
#     [476, 714, 18],
#     [422, 662, 18],
#     [368, 644, 18],
#     [298, 660, 18],
#     [236, 640, 18],
#     [167, 631, 19],

#     [110, 648, 16],
#     [128, 686, 20],
#     [179, 679, 17],
#     [233, 729, 17],
#     [312, 748, 18],
#     [381, 737, 19],
#     [440, 762, 18],
#     [480, 818, 18],
#     [554, 822, 16],
#     [623, 817, 19],

#     [688, 782, 16],
#     [757, 781, 19],
#     [820, 810, 16],
#     [867, 849, 19],
#     [839, 893, 17],
#     [764, 908, 16],
#     [701, 885, 17],
#     [632, 886, 16],
#     [551, 905, 17],
#     [480, 884, 16],

#     [409, 871, 17],
#     [368, 830, 14],
#     [302, 830, 16],
#     [244, 840, 18],
#     [173, 821, 17],
#     [113, 865, 19],
#     [156, 922, 18],
#     [212, 908, 18],
#     [280, 936, 16],
#     [354, 936, 16],

#     [423, 959, 17],
#     [507, 955, 17],
#     [589, 967, 17],
#     [659, 951, 17],
#     [734, 964, 16],
#     [802, 986, 18],
#     [743, 1035, 17],
#     [656, 1042, 18],
#     [580, 1030, 16],
#     [489, 1023, 17],

#     [418, 1038, 16],
#     [333, 1021, 19],
#     [258, 1036, 18],
#     [291, 1085, 15],
#     [361, 1117, 17],
#     [441, 1119, 15],
#     [507, 1165, 17],
#     [566, 1126, 16],
#     [624, 1130, 16],
# ]


# print(arr_coord[0])
# for i in range(0, 99):
#     doc = {'coords':arr_coord[i], 'num' : i + 1}
#     db.imgcircle.insert_one(doc)


SECRET_KEY = 'SPARTA'

# client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
client = MongoClient('localhost', 27017)
db = client.LogBook

# HTML 화면 보여주기


@app.route('/')
def home():
    return render_template('login.html')

##login
@app.route('/api/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login_post():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']


    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'email': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'email': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


##join
@app.route('/api/page', methods=['GET'])
def signup_get():
    return render_template('join.html')

@app.route('/api/signup', methods=['POST'])
def signup_post():
    email = request.form['email']
    exists = bool(db.users.find_one({'email':email}))
    if exists:
        # return jsonify({'result' : "id is already exist"})
        return jsonify({'result': 'fail', 'msg': '아이디가 이미 존재합니다.'})
    name = request.form['name']
    birth = request.form['birth']
    password = request.form['password']
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    doc = {
        "email" : email,
        "name" : name,
        "birth" : birth,
        "password" : password_hash
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

## comment
@app.route('/api/comment', methods=['GET'])
def comment_get():
    return render_template('login.html')

@app.route('/api/comment', methods=['POST'])
def comment_post():
    return render_template('login.html')

## ToDolist
@app.route('/api/todolist', methods=['GET'])
def todolist_get():
    return render_template('login.html')

@app.route('/api/todolist', methods=['POST'])
def todolist_post():
    return render_template('login.html')


if __name__ == '__main__':    app.run('0.0.0.0', port=5000, debug=True)
