from flask import Flask, render_template, request, redirect
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
import os
import time
from database import User, Friend
from PIL import Image

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import create_card

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login")
def login():

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    name = request.form["name"]
    password = request.form["password"]
    user = User.get(name=name)
    if check_password_hash(user.password, password):
        login_user(user)
        return redirect("/")
    return render_template("/login")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def register():
    create_id = request.form["create_id"]
    name = request.form["name"]
    password = request.form["password"]
    belong = request.form["belong"]
    position = request.form["position"]
    tel = request.form["tel"]
    email = request.form["email"]
    comment = request.form["comment"]
    link = request.form["link"]
    icon = request.files["icon"]
    # img=Image.open(icon)
    # img.save("data/icon/"+str(create_id)+".jpeg")
    file_path = "static/icon/" + create_id + ".png"
    icon.save(os.path.join("static/icon/", create_id + ".png"))


    User.create(
        create_id=create_id,
        name=name,
        password=generate_password_hash(password, method="sha256"),
        belong=belong,
        position=position,
        tel=tel,
        email=email,
        comment=comment,
        link=link,
        icon=file_path
    )

    return redirect("/login")



    
@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect("/login")


@app.route("/search")
def search_page():
    return render_template("search.html")

@app.route("/search", methods=["POST"])
def search():
    id = request.form["search_id"]
    searching = User.select().where(User.create_id==id).get()
    if(searching):
        return render_template("search_result.html", searching=searching, height=calcPx(searching.icon))
    else:
        print("存在しないIDです")
        time.sleep(2000)
        return render_template("search.html")


@app.route("/edit")
@login_required
def edit_page():
    return render_template("edit.html", user=current_user)

@app.route("/edit", methods=["POST"])
def edit():
    details = User.select().where(User.id==current_user.id).get()

    new_belong = request.form["belong"]
    details.belong = new_belong

    new_position = request.form["position"]
    details.position = new_position

    new_tel = request.form["tel"]
    details.tel = new_tel

    new_email = request.form["email"]
    details.email = new_email

    new_comment = request.form["comment"]
    details.comment = new_comment

    new_link = request.form["link"]
    details.link = new_link

    new_icon = request.files["icon"]
    file_path = "static/icon/" + current_user.create_id + ".png"
    new_icon.save(os.path.join("static/icon/", current_user.create_id + ".png"))
    details.icon = file_path
    
    details.save()

    # q = User.update(belong=new_belong, position=new_position, tel=new_tel, email=new_email, comment=new_comment, link=new_link)
    # q.excute()

    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    create_id_to = request.form["create_id_to"]
    # create_id_from = User.select().where(User.create_id==current_user.create_id).get()
    Friend.create(
        create_id_to=create_id_to,
        create_id_from=current_user.create_id
    )

    return render_template("search.html")


@app.route("/list")
def friend():
    friend = Friend.select().where(
        (Friend.create_id_from).contains(current_user.create_id)
        | (Friend.create_id_to).contains(current_user.create_id)
    )
    friend_ids = []
    for f in friend:
        if f.create_id_to != current_user.create_id:
            friend_ids.append(f.create_id_to)
        if f.create_id_from != current_user.create_id:
            friend_ids.append(f.create_id_from)
    friends = User.select().where(User.create_id in friend_ids)
    return render_template("list.html", friend=friends)


@app.route("/create", methods=["POST"])
@login_required
def create():
    me = User.select().where(User.id==current_user.id).get()
    create_card.create_card(me)
    create_card.resize(me)
    create_card.paste(me)

    return render_template("display_card.html", create_id=me.create_id)


def calcPx(img):
    image = Image.open(img)
    (y, x) = image.size
    multi = 200 / x
    return multi * y


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)