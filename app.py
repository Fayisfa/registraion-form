# Required libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Flask App setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Fayisfa'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

# Home Route
@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        mobile_number = request.form['mobile_number']
        role = request.form['role']
        status_or_profession = request.form.get('status_or_profession', '')
        batch = request.form.get('batch', '')  # New batch field

        # Insert data into the database
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (name, mobile_number, role, status_or_profession, batch) VALUES (%s, %s, %s, %s, %s)",
                (name, mobile_number, role, status_or_profession, batch)
            )
            mysql.connection.commit()
            cur.close()
            flash('Registration successful!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')

        return redirect(url_for('index'))

# Main
if __name__ == '__main__':
    app.run(debug=True)
