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

arr_coord = [
    [358, 256, 18],
    [428, 236, 18],
    [503, 253, 18],
    [577, 235, 18],
    [656, 222, 18],
    [726, 242, 18],
    [744, 300, 18],
    [682, 334, 18],
    [601, 329, 18],
    [531, 341, 18],

    [453, 335, 18],
    [376, 348, 18],
    [312, 402, 18],
    [363, 427, 18],
    [442, 422, 18],
    [510, 418, 18],
    [590, 424, 18],
    [656, 420, 18],
    [725, 423, 18],
    [733, 485, 18],

    [682, 510, 18],
    [615, 513, 18],
    [546, 498, 18],
    [463, 505, 18],
    [396, 494, 18],
    [325, 503, 18],
    [243, 483, 18],
    [171, 511, 18],
    [218, 558, 18],
    [288, 566, 18],

    [357, 565, 18],
    [423, 557, 18],
    [479, 591, 18],
    [553, 587, 18],
    [610, 610, 18],
    [670, 596, 18],
    [752, 596, 18],
    [821, 623, 18],
    [853, 677, 18],
    [793, 705, 18],

    [724, 690, 18],
    [659, 695, 18],
    [606, 746, 18],
    [529, 755, 18],
    [476, 714, 18],
    [422, 662, 18],
    [368, 644, 18],
    [298, 660, 18],
    [236, 640, 18],
    [167, 631, 18],

    [110, 648, 18],
    [128, 686, 18],
    [179, 679, 18],
    [233, 729, 18],
    [312, 748, 18],
    [381, 737, 18],
    [440, 762, 18],
    [480, 818, 18],
    [554, 822, 18],
    [623, 817, 18],

    [688, 782, 18],
    [757, 781, 18],
    [820, 810, 18],
    [867, 849, 18],
    [839, 893, 18],
    [764, 908, 18],
    [701, 885, 18],
    [632, 886, 18],
    [551, 905, 18],
    [480, 884, 18],

    [409, 871, 18],
    [368, 830, 18],
    [302, 830, 18],
    [244, 840, 18],
    [173, 821, 18],
    [113, 865, 18],
    [156, 922, 18],
    [212, 908, 18],
    [280, 936, 18],
    [354, 936, 18],

    [423, 959, 18],
    [507, 955, 18],
    [589, 967, 18],
    [659, 951, 18],
    [734, 964, 18],
    [802, 986, 18],
    [743, 1035, 18],
    [656, 1042, 18],
    [580, 1030, 18],
    [489, 1023, 18],

    [418, 1038, 18],
    [333, 1021, 18],
    [258, 1036, 18],
    [291, 1085, 18],
    [361, 1117, 18],
    [441, 1119, 18],
    [507, 1165, 18],
    [566, 1126, 18],
    [624, 1130, 18],
]


print(arr_coord[0])
for i in range(0, 99):
    arr_coord[i][2] = 18
    doc = {'coords':arr_coord[i], 'num' : i + 1}
    db.imgcircle.insert_one(doc)