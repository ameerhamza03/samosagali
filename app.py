from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Menu Data
MENU = {
    "frozen_samosa": [
        {"id": 1, "name": "Pizza Samosa", "price": 700, "per": "12 pcs", "emoji": "🍕", "desc": "Cheesy pizza filling wrapped in crispy samosa shell", "tag": "bestseller"},
        {"id": 2, "name": "Cheese Samosa", "price": 700, "per": "12 pcs", "emoji": "🧀", "desc": "Gooey melted cheese with herbs — pure bliss", "tag": "popular"},
        {"id": 3, "name": "Malai Boti Samosa", "price": 500, "per": "12 pcs", "emoji": "🍗", "desc": "Tender malai boti chicken with aromatic spices", "tag": ""},
        {"id": 4, "name": "Bar.B.Q Samosa", "price": 600, "per": "12 pcs", "emoji": "🔥", "desc": "Smoky BBQ chicken with tangy sauce filling", "tag": "spicy"},
        {"id": 5, "name": "Chicken Samosa", "price": 400, "per": "12 pcs", "emoji": "🐔", "desc": "Classic spiced chicken mince — the original", "tag": ""},
        {"id": 6, "name": "Keema Samosa", "price": 500, "per": "12 pcs", "emoji": "🥩", "desc": "Juicy minced beef with green chillies & onion", "tag": ""},
        {"id": 7, "name": "Macaroni Samosa", "price": 350, "per": "12 pcs", "emoji": "🍝", "desc": "Spiced macaroni pasta fusion — unique & delicious", "tag": "unique"},
        {"id": 8, "name": "Potato Samosa", "price": 300, "per": "12 pcs", "emoji": "🥔", "desc": "Classic aloo filling with cumin & coriander", "tag": ""},
        {"id": 9, "name": "Chicken Vegetable Roll", "price": 500, "per": "12 pcs", "emoji": "🌯", "desc": "Crispy roll stuffed with chicken & fresh veggies", "tag": ""},
    ],
    "fry_samosa": [
        {"id": 10, "name": "Pizza Samosa", "price": 70, "per": "1 pc", "emoji": "🍕", "desc": "Freshly fried pizza samosa — hot & crispy", "tag": "bestseller"},
        {"id": 11, "name": "Cheese Samosa", "price": 70, "per": "1 pc", "emoji": "🧀", "desc": "Fried cheese samosa with melty center", "tag": "popular"},
        {"id": 12, "name": "B.B.Q Samosa", "price": 60, "per": "1 pc", "emoji": "🔥", "desc": "BBQ chicken fried samosa", "tag": ""},
        {"id": 13, "name": "Malai Boti Samosa", "price": 50, "per": "1 pc", "emoji": "🍗", "desc": "Creamy malai boti filling", "tag": ""},
        {"id": 14, "name": "Keema Samosa", "price": 50, "per": "1 pc", "emoji": "🥩", "desc": "Minced meat fried samosa", "tag": ""},
        {"id": 15, "name": "Chicken Vegetable Samosa", "price": 50, "per": "1 pc", "emoji": "🐔", "desc": "Chicken & veg combo samosa", "tag": ""},
        {"id": 16, "name": "Chicken Vegetable Roll", "price": 50, "per": "1 pc", "emoji": "🌯", "desc": "Crispy fried roll with chicken & veggies", "tag": ""},
    ],
    "fries": [
        {"id": 17, "name": "Masala Regular", "price": 100, "per": "serving", "emoji": "🍟", "desc": "Classic masala fries — small size", "tag": ""},
        {"id": 18, "name": "Masala Regular (Large)", "price": 150, "per": "serving", "emoji": "🍟", "desc": "Masala fries — large size", "tag": "popular"},
        {"id": 19, "name": "Flavour Fries", "price": 200, "per": "serving", "emoji": "✨", "desc": "Special flavoured fries — Regular 200 / Large 250", "tag": "special"},
    ],
    "nuggets": [
        {"id": 20, "name": "Chicken Nuggets", "price": 30, "per": "1 pc", "emoji": "🍗", "desc": "Crispy golden chicken nuggets", "tag": ""},
    ]
}

CONTACT = {
    "whatsapp": "923107740183",
    "phone": "+92-310-7740183",
    "jazzcash": "0310-7740183"
}

@app.route('/')
def index():
    return render_template('index.html', menu=MENU, contact=CONTACT)

@app.route('/api/menu')
def api_menu():
    return jsonify(MENU)

@app.route('/api/order', methods=['POST'])
def api_order():
    data = request.json
    return jsonify({"status": "ok", "message": "Order received", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
