from flask import Flask, render_template, request, jsonify, redirect
import json
from datetime import datetime

app = Flask(__name__)

# Synthetic data - Common grocery items
GROCERY_ITEMS = [
    {"id": 1, "name": "Milk", "category": "Dairy", "unit": "gallon"},
    {"id": 2, "name": "Bread", "category": "Bakery", "unit": "loaf"},
    {"id": 3, "name": "Eggs", "category": "Dairy", "unit": "dozen"},
    {"id": 4, "name": "Bananas", "category": "Produce", "unit": "bunch"},
    {"id": 5, "name": "Chicken Breast", "category": "Meat", "unit": "lb"},
    {"id": 6, "name": "Rice", "category": "Grains", "unit": "lb"},
    {"id": 7, "name": "Tomatoes", "category": "Produce", "unit": "lb"},
    {"id": 8, "name": "Cheese", "category": "Dairy", "unit": "lb"},
]

# Synthetic data - Stores
STORES = [
    {
        "id": 1,
        "name": "SuperMart",
        "distance": 1.2,
        "eta": "10 mins",
        "total_price": 45.67,
        "rating": 4.5,
        "items_list": [
            {"name": "Milk", "price": 3.99},
            {"name": "Bread", "price": 2.49},
            {"name": "Eggs", "price": 3.99}
        ],
        "missing_items": ["Rice", "Tomatoes"]
    },
    {
        "id": 2,
        "name": "FreshGrocer",
        "distance": 2.5,
        "eta": "15 mins",
        "total_price": 42.89,
        "rating": 4.7,
        "items_list": [
            {"name": "Milk", "price": 4.29},
            {"name": "Bread", "price": 2.29},
            {"name": "Eggs", "price": 3.79},
            {"name": "Rice", "price": 2.99},
            {"name": "Tomatoes", "price": 1.99}
        ],
        "missing_items": []
    },
    {
        "id": 3,
        "name": "ValueMart",
        "distance": 3.1,
        "eta": "20 mins",
        "total_price": 39.99,
        "rating": 4.2,
        "items_list": [
            {"name": "Milk", "price": 3.89},
            {"name": "Bread", "price": 2.19},
            {"name": "Eggs", "price": 3.69},
            {"name": "Rice", "price": 2.79}
        ],
        "missing_items": ["Tomatoes"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', items=GROCERY_ITEMS)

@app.route('/stores')
def stores():
    sort_by = request.args.get('sort', 'has_all_items')  # Default sort by availability
    
    # First sort by whether store has all items
    sorted_stores = sorted(STORES, key=lambda x: len(x['missing_items']))
    
    # Then apply secondary sort if specified
    if sort_by == 'price':
        sorted_stores = sorted(sorted_stores, key=lambda x: (len(x['missing_items']), x['total_price']))
    elif sort_by == 'eta':
        # Convert eta string to minutes for sorting
        def get_minutes(eta):
            return int(eta.split()[0])
        sorted_stores = sorted(sorted_stores, key=lambda x: (len(x['missing_items']), get_minutes(x['eta'])))
    elif sort_by == 'distance':
        sorted_stores = sorted(sorted_stores, key=lambda x: (len(x['missing_items']), x['distance']))
    elif sort_by == 'rating':
        sorted_stores = sorted(sorted_stores, key=lambda x: (len(x['missing_items']), -x['rating']))  # Negative for descending
        
    return render_template('stores.html', stores=sorted_stores, current_sort=sort_by)

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(GROCERY_ITEMS)

@app.route('/api/stores', methods=['POST'])
def get_store_recommendations():
    selected_items = request.json.get('items', [])
    # In a real app, we would calculate recommendations based on selected items
    # For now, return synthetic data
    return jsonify(STORES)

@app.route('/payment/<int:store_id>')
def payment(store_id):
    store = next((store for store in STORES if store['id'] == store_id), None)
    if not store:
        return redirect('/')
    return render_template('payment.html', store=store)

@app.route('/confirm/<int:store_id>')
def confirm(store_id):
    store = next((store for store in STORES if store['id'] == store_id), None)
    if not store:
        return redirect('/')
    # In a real app, we would generate this
    order_id = f"ORD-{store_id}-{int(datetime.now().timestamp())}"
    estimated_delivery = "4:30 PM - 5:00 PM"  # Mock delivery time
    return render_template('confirmation.html', store=store, order_id=order_id, estimated_delivery=estimated_delivery)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
