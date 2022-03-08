#from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import request, Flask,jsonify,render_template
from pymongo import MongoClient


app = Flask(__name__)

"""
app.config["MONGO_URI"] = "mongodb://localhost:27017/mini_project"
mongodb_client = PyMongo(app)
db = mongodb_client.db"""

client = MongoClient('mongodb://localhost:27017/')
db = client['mini_project']
feedbacks = db['feedbacks']


"""
Structure Of feedbacks Collection

{
    type:Int
    feedback : string
    Likes:0
    Comments:
    [
        {
            Comment:String
            Date:Date
            Time:Time
        }
    ]
}

"""


@app.route("/add_new_feedback",methods=["POST"])
def add_new_feedback():
    if request.method == 'POST':
        #print(request.form['type'])
        feedbacks.insert_one({"type":request.form['type'],"feedback":request.form['feedback'],"likes":0,"comments":[""]})
    else:
        print("GEt")
    return "Successful"

@app.route("/",methods=["GET"])
def display_all():
    feedbacks_cursor = feedbacks.find()
    feedbacks_list=[]
    for feedback in feedbacks_cursor:
        feedbacks_list.append({"id":str(feedback["_id"]),"type":feedback['type'],"feedback":feedback["feedback"],"likes":feedback['likes'],"comments":feedback['comments']})

    return render_template('index.html',feedbacks=feedbacks_list)


@app.route("/view",methods=["GET"])
def display_all_temp():
    feedbacks_cursor = feedbacks.find()
    feedbacks_list=[]
    for feedback in feedbacks_cursor:
        feedbacks_list.append({"id":str(feedback["_id"]),"type":feedback['type'],"feedback":feedback["feedback"],"likes":feedback['likes'],"comments":feedback['comments']})

    return render_template('demo.html',feedbacks=feedbacks_list)


@app.route("/update",methods=["PUT"])
def update():
    filter = {"_id":ObjectId("61d88dca0ae4801a46c88e1b")}
    newvalues = {"$set":{"type":1,"likes":2}}
    #adding comment
    feedbacks.update_one({"_id":ObjectId("61d88dca0ae4801a46c88e1b")}, {'$push': {'comments': {"comment":"Good Job"}}})
    feedbacks.update_one(filter,newvalues)
    return jsonify(message="success")


@app.route("/delete",methods=["DELETE"])
def delete():
    pass



if __name__ == "__main__":
    app.run(debug=True)