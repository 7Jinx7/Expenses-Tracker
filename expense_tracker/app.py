import json
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Load data from data.json (expenses and allowance)
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Initialize data if file is not found or empty
        data = {"allowance": 0, "expenses": []}
    return data

# Save data to data.json
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

# Route for the home page
@app.route('/')
def index():
    data = load_data()  # Load the current allowance and expenses
    allowance = data["allowance"]
    expenses = data["expenses"]
    total_expenses = sum(expense["amount"] for expense in expenses)
    remaining_allowance = allowance - total_expenses

    # Warning if expenses exceed allowance
    warning = ""
    if total_expenses > allowance:
        warning = "Warning! You have spent more than your allocated budget. Consider cutting back on the next purchase."

    return render_template('index.html', allowance=allowance, total_expenses=total_expenses,
                           remaining_allowance=remaining_allowance, expenses=expenses, warning=warning)

# Route to set the monthly allowance
@app.route('/set_allowance', methods=['GET', 'POST'])
def set_allowance():
    if request.method == 'POST':
        allowance = float(request.form['allowance'])
        data = load_data()
        data['allowance'] = allowance
        save_data(data)
        return redirect(url_for('index'))  # Redirect to home page after saving allowance

    return render_template('set_allowance.html')

# Route to add a new expense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = datetime.now().strftime('%Y-%m-%d')  # Current date in YYYY-MM-DD format
        data = load_data()
        data['expenses'].append({'description': description, 'amount': amount, 'date': date})
        save_data(data)
        return redirect(url_for('index'))  # Redirect to home page after adding expense

    return render_template('add_expense.html')

# Route to delete an expense
@app.route('/delete/<int:index>', methods=['GET'])
def delete_expense(index):
    data = load_data()
    del data['expenses'][index]  # Remove expense from list by index
    save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
