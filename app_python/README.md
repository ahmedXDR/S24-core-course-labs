# Python Web Application

This Python web application displays the current time in Moscow. Built with FastAPI, it demonstrates efficient handling of asynchronous requests and serves as an example of modern web application development in Python.

## Features

- Displays the current time in Moscow, updating dynamically with each page refresh.
- Built with FastAPI for high performance and ease of development.
- Utilizes HTML and CSS for a simple and responsive user interface.

## Getting Started

### Prerequisites

What things you need to install the software and how to install them:

```

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```

### Installing

A step by step series of examples that tell you how to get a development env running:

1. Navigate to the `app_python` folder:

```bash
cd app_python
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:5000/` by default change `PORT` environment variable to change the port.

## Running the Tests

To run the automated tests for this system use the following command:

```bash
pytest
```

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Python](https://www.python.org/) - Programming Language

```

```