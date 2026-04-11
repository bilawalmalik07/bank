from flask import Flask, render_template, request, redirect, session
import os
import psycopg2
from dotenv import load_dotenv

if os.path.exists("database.env"):
    load_dotenv("database.env")
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "key")


def get_db_connection():
    connection_url = os.environ.get("DATABASE_URL")
    return psycopg2.connect(connection_url)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/open_account', methods=['GET', 'POST'])
def open_account():
    if request.method == 'POST':
        name = request.form['name'].capitalize()
        username = request.form['username']
        pin = request.form['pin']
        initial_deposit = float(request.form['deposit'])

        if initial_deposit < 20:
            return render_template('error.html', message="Minimum deposit is $20. Please try again with a higher amount.")
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT username from accounts WHERE username=%s", (username,))
        if cur.fetchone():
            cur.close()
            return render_template('error.html', message="That username is already taken. Please pick another one.")

        cur.execute("INSERT INTO accounts (name, username, pin, balance) VALUES (%s, %s, %s, %s)",
                    (name, username, pin, initial_deposit))
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/signin')

    return render_template('open_account.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        login_username = request.form['username']
        login_pin = request.form['pin']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT name, balance FROM accounts WHERE username = %s AND pin = %s",
                    (login_username, login_pin))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['username'] = login_username
            session['name'] = user[0]
            return redirect('/dashboard')
        else:
            return "Invalid login. <a href='/signin'>Try again</a>"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/signin')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE username = %s",
                (session['username'],))
    current_balance = cur.fetchone()[0]
    cur.close()
    conn.close()

    return render_template('dashboard.html', name=session['name'], balance=current_balance)


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'username' not in session:
        return redirect('/signin')

    if request.method == 'POST':
        amount = float(request.form['amount'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE username = %s",
                    (amount, session['username']))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/dashboard')

    return render_template('deposit.html')


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'username' not in session:
        return redirect('/signin')

    if request.method == 'POST':
        amount = float(request.form['amount'])
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT balance FROM accounts WHERE username = %s",
                    (session['username'],))
        current_balance = cur.fetchone()[0]

        if amount > current_balance:
            cur.close()
            conn.close()
            return render_template('error.html', message="Insufficient funds! You don't have enough money for this withdrawal.")

        cur.execute("UPDATE accounts SET balance = balance - %s WHERE username = %s",
                    (amount, session['username']))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/dashboard')

    return render_template('withdraw.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
