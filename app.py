from flask import Flask, jsonify, render_template
import yfinance as yf
import sqlite3

app = Flask(__name__)

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('banknifty.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS banknifty_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, value REAL, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Function to insert Bank Nifty data into the database
def insert_data(value):
    conn = sqlite3.connect('banknifty.db')
    c = conn.cursor()
    c.execute("INSERT INTO banknifty_data (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()

# Function to fetch the most recent Bank Nifty data from the database
def get_latest_data():
    conn = sqlite3.connect('banknifty.db')
    c = conn.cursor()
    c.execute("SELECT value, timestamp FROM banknifty_data ORDER BY timestamp DESC LIMIT 1")
    row = c.fetchone()
    conn.close()
    return row

# Function to fetch historical Bank Nifty data from the database
def get_history_data():
    conn = sqlite3.connect('banknifty.db')
    c = conn.cursor()
    c.execute("SELECT value, timestamp FROM banknifty_data ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return rows

# Route to fetch Bank Nifty data and update the database
@app.route('/update')
def update_banknifty():
    bn = yf.Ticker("^NSEBANK").history(period="1d")
    current_value = bn['Close'].iloc[-1]
    insert_data(current_value)
    return jsonify({'message': 'Bank Nifty data updated successfully!'})

# Route to serve main page with live Bank Nifty value
@app.route('/')
def index():
    value, timestamp = get_latest_data()
    return render_template('index.html', bank_nifty=value)

# Route to serve Bank Nifty live value
@app.route('/api/banknifty')
def get_banknifty():
    bn = yf.Ticker("^NSEBANK")
    current_value = bn.history(period="1d")['Close'].iloc[-1]
    return jsonify({'bank_nifty': current_value})

# Route to serve Bank Nifty history page
@app.route('/history')
def history():
    history_data = get_history_data()
    return render_template('history.html', history=history_data)

if __name__ == '__main__':
    create_table()  # Create the database table
    app.run(debug=True)
