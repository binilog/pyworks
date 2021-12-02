from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return "<h1>로그인 페이지입니다</h1>"


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        pwd = request.form['passwd']
        name = request.form['name']
        return render_template('member_info.html', id=id , pwd=pwd, name=name)
    else:
        return render_template('register.html')


@app.route('/board/')
def board():
    return "<h1>게시판입니다</h1>"

@app.route("/loop_index")
def get_loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items=items)

app.run(debug=True)
