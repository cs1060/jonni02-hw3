# Grocery Store List Optimizer

A web application that helps users create and manage shopping lists, find the best stores based on their needs, and complete their grocery shopping efficiently.

## Live Demo

The application is deployed and accessible at: [https://jonni02-hw3.onrender.com](https://jonni02-hw3.onrender.com)

## Features

- **Shopping List Management**
  - Create and manage multiple shopping lists
  - Add items with quantities
  - Track unique items per list
  - Enter key support for quick additions

- **Store Recommendations**
  - Sort stores by price, distance, ETA, or rating
  - Prioritize stores with all desired items
  - View missing items at each store
  - Compare total prices

- **Checkout Process**
  - Clear payment summary
  - Tax and delivery fee calculation
  - Order confirmation
  - Order tracking

## Setup

1. Install dependencies:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

3. Open in browser:
```
http://127.0.0.1:5001
```

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Visit `http://localhost:10000` in your browser

## Technologies Used

- Flask
- Bootstrap
- Font Awesome
- JavaScript
- Python/Flask for backend
- Bootstrap for frontend styling
- Jinja2 for templating
- Gunicorn for production deployment
