## Author: Sanjana Suresh

# Personal Expenses Tracker: 
Your very own tracker for your expenses! Set an allowance, and record expenses for monitoring and bettering your spending habits!

Overview: 
This is a simple, interactive personal expense tracker application built using the Flask framework. The app allows users to track their monthly allowance, record new expenses, and see the remaining allowance after each expense. It is designed with a clean user interface using HTML and CSS, providing an intuitive experience. The project uses Jinja2 templating for dynamic content rendering and integrates file I/O for saving and loading expense data.

Installation Instructions: 
To run the Expense Tracker app, ensure that you have Python installed on your machine. You will also need to install the required Python packages, which can be easily done using the `pip` command.

1. Clone or Download the Project:
   Download the project files to your local machine.

2. Install Required Dependencies:
   Open a terminal or command prompt and navigate to the project folder. Run the following command to install the required Python packages:
   pip install -r requirements.txt

3. Run the Application:
   Once the dependencies are installed, you can run the app using the following command:
   python app.py
The application will start a local web server on `http://127.0.0.1:5000/`, which you can open in any web browser.

Functionality: 

The Expense Tracker allows users to:

- **Set a Monthly Allowance:** Users can set their monthly allowance, which is used to track how much of their budget has been spent.
- **Add Expenses:** Users can enter the description, amount, and date for each expense. The app will keep track of total expenses and subtract them from the allowance.
- **View Expense List:** All expenses are displayed in a table format, showing the description, amount, and date.
- **Delete Expenses:** Users can remove any expense from the list.

Technical Details: 

1. Flask
Flask, a lightweight Python web framework, is used to build this app. Flask provides the core functionality needed to route HTTP requests to Python functions, making it simple to set up a basic web application. In this app, Flask handles routes for displaying the home page, adding expenses, and setting the monthly allowance.

2. Jinja2 Templating
The app uses Jinja2, which is Flask's default templating engine, to dynamically render HTML pages. Jinja2 allows us to insert dynamic content, such as the current allowance, total expenses, and individual expenses, into the HTML templates. This feature helps create an interactive user interface that updates in real-time based on user input.

3. File I/O
The expense data (monthly allowance and expenses) is stored locally in a simple text file. Every time the user adds or deletes an expense, the data is updated and saved back to the file, ensuring persistence between app sessions. This allows the app to keep track of the user's expenses even after they close and reopen the application.

4. User Interface
The user interface is built with a combination of HTML and CSS. The app uses tables to display the expenses, and the layout is styled to give a clean and professional look. The buttons for adding expenses and setting the allowance are styled to look like clickable buttons, enhancing the user experience.

How It Works: 
When a user accesses the homepage, they can view their current allowance, total expenses, and remaining allowance. If the total expenses exceed the allowance, a warning message is displayed. Users can then add new expenses by entering a description, amount, and date. The app dynamically updates the total expenses and remaining allowance based on each new entry. The data is saved to a file, so it persists even after the app is closed. Additionally, users can delete individual expenses from the list.
