"""
added about.html
"""

# ----------
# Where to keep html files?
############
# - create a directory 'templates' inside 'website' folder
# - keep all html files inside 'templates'
######################

# ----------
# Create App for our website
############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__)
######################


# # ----------
# # END POINT - 1: URL http://127.0.0.1:5000/ MAPPED to route("/")
# ############
# @my_website_app.route("/")
# def my_index_page():
#     return "WEL COME"
# ######################


# ----------
# END POINT - 1: URL http://127.0.0.1:5000/ MAPPED to route("/")
############
@my_website_app.route("/")
def my_login_page():
    return flask.render_template("login.html")
######################

# ----------
# END POINT - 2: URL http://127.0.0.1:5000/index MAPPED to route("/index")
############
@my_website_app.route("/index")
def my_index_page():
    return flask.render_template("index.html")
######################

# ----------
# END POINT - 3: URL http://127.0.0.1:5000/validatelogin MAPPED to route("/validatelogin")
############
@my_website_app.route("/validatelogin")
def my_validatelogin_page():
    """
    Our Plan:
    Task-1: Get entered username and password
    Task-2: Validate with db and return success or failure
    """
    # ----------
    # Task-1: Get entered username and password
    ############
    entered_username = flask.request.form.get("loginname")
    entered_email = flask.request.form.get("loginemail")
    entered_password = flask.request.form.get("loginpwd")
    ######################

    # ----------
    # Task-2: Validate with db and return success or failure
    ############
    import sqlite3
    my_db_connection = sqlite3.connect("my_users_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE USERNAME = '{entered_username}' AND EMAIL = '{entered_email}' AND PASSWORD = '{entered_password}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone()  # Example: (1, )
    user_count = my_db_result[0]  # Example 1
    messages = {'user_email': entered_email}
    flask.session['messages'] = messages
    if user_count > 0:
        return flask.redirect(flask.url_for(".my_index_page", messages = messages))
    else:
        return "Login Failed.<br><a href='/'>Go Back</a>"
######################

# ----------
# END POINT - 4: URL http://127.0.0.1:5000/about MAPPED to route("/about")
############
@my_website_app.route("/about")
def my_about_page():
    return flask.render_template("about.html")
######################

# ----------
# END POINT - 5: URL http://127.0.0.1:5000/userprofile MAPPED to route("/userprofile")
############
@my_website_app.route("/userprofile")
def my_userprofile_page():
    pass
######################

# ----------
# Run builtin server
############
my_website_app.run(debug=True)
# my_website_app.run(host='127.0.0.1', port=1234)
######################
