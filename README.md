# CRUD Application in Flask

This repository contains a basic CRUD app built in Flask for managing contacts.

## Usage

Create a python virutal environment and activate it.

```bash
python -m venv env
env\Scripts\activate
```

Install the required dependencies present in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

Run the Flask application using the following command.

```bash
python app.py
```

The application runs on `localhost:8000`. The port number can be changed by modifying [`app.py`](app.py).

```python
app.run(
    debug=True, 
    port="Enter your port here"
)
```
