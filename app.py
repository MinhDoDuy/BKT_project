from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Dữ liệu cố định
USER_EMAIL = "123@test.com"
USER_PASSWORD = "123456"


# Trang login
@app.route('/', methods=['GET'])
def login_page():
    if session.get("logged_in"):
        return redirect(url_for('dashboard'))  # redirect đúng route
    return render_template('login.html')


# # Xử lý form login
# @app.route('/login', methods=['POST'])
# def login():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     if email == USER_EMAIL and password == USER_PASSWORD:
#         session['logged_in'] = True
#         session['user_email'] = email
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('login.html', error="Email hoặc mật khẩu không đúng", email=email)
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email == USER_EMAIL and password == USER_PASSWORD:
        session['logged_in'] = True
        session['user_email'] = email
        return redirect(url_for('dashboard'))
    else:
        # truyền error về template
        error_msg = "Email hoặc mật khẩu không đúng"
        return render_template('login.html', error=error_msg, email=email)

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for('login_page'))
    return render_template('dashboard.html', user_email=session.get('user_email'))


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == '__main__':
    app.run(debug=True)
