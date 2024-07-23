# Flask Notes App

This is a simple Notes application built using Flask, a lightweight WSGI web application framework in Python. The application allows users to create, view, edit, and delete notes.

## Features

- Create new notes
- View all notes
- Edit existing notes
- Delete notes
- User authentication (register/login/logout)
- Responsive UI with Bootstrap

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-notes-app.git
    cd flask-notes-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```bash
    cp .env.example .env
    ```

5. Initialize the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Run the application:
    ```bash
    flask run
    ```

7. Open your browser and navigate to `http://127.0.0.1:5000/`.
