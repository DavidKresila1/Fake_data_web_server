from flask import Flask, render_template


from .workWithFile import getDataAboutUser, getIndividualDataAboutUser, getPostsData, getIndividualPostData

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/download")
def download():
    return render_template("download.html")

@app.route("/users")
def users():
    data = getDataAboutUser()
    return render_template("users.html", data=data)

@app.route('/users/<int:id>')
def displayDataByID(id):
    data = getIndividualDataAboutUser()
    item = next((item for item in data if item['userid'] == id), None)
    return render_template('detailAboutUser.html', item=item)



@app.route("/api/users")
def apiUsers():
    data = getDataAboutUser()
    return data

@app.route('/api/users/<int:id>')
def apiDisplayDataByID(id):
    data = getIndividualDataAboutUser()
    item = next((item for item in data if item['userid'] == id), None)
    return item

@app.route("/posts")
def posts():
    data = getPostsData()
    return render_template("posts.html", data=data)

@app.route('/posts/<int:id>')
def displayPostByPostID(id):
    data = getIndividualPostData()
    item = next((item for item in data if item['postid'] == id), None)
    return render_template('detailAboutPost.html', item=item)


@app.route("/api/posts")
def apiPosts():
    data = getPostsData()
    return data
    
    
@app.route('/api/posts/<int:id>')
def apiDisplayPostByPostID(id):
    data = getIndividualPostData()
    item = next((item for item in data if item['postid'] == id), None)
    return item