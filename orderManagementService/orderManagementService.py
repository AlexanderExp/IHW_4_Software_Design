from flask import Flask, jsonify, render_template, request, redirect, session, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from dbModels import db, Dish, Order, OrderDish, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'URI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret_key"

app.config['SESSION_COOKIE_DOMAIN'] = 'localhost'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/order_management', methods=['GET', 'POST'])
def order_management():
    if request.method == 'POST':
        user_id = request.get_json()['user_id']
        print("fine")
        return redirect('http://localhost:5800')
    else:
        return render_template('mainPage.html')


@app.route('/get_menu', methods=['GET', 'POST'])
def get_menu():
    dishes = Dish.query.all()
    dishes_serialized = [dish.serialize() for dish in dishes]

    return jsonify(dishes_serialized)


@app.route('/add_to_order', methods=['POST', 'GET'])
def add_to_order():
    dish = request.get_json()
    user_opened_order = Order.query.filter_by(user_id=current_user.id, status="creation").all()
    if len(user_opened_order) == 0:
        new_order = Order(user_id=current_user.id, status="creation")
        db.session.add(new_order)
        db.session.commit()
        new_order_dish = OrderDish(order_id=new_order.id, dish_id=dish['id'], quantity=1, price=dish['price'],
                                   dish_name=dish['name'])
        db.session.add(new_order_dish)
        db.session.commit()
    else:
        user_order = user_opened_order[0]
        similar_dish = OrderDish.query.filter_by(order_id=user_order.id, dish_id=dish['id']).all()
        if len(similar_dish) == 0:
            new_order_dish = OrderDish(order_id=user_order.id, dish_id=dish['id'], quantity=1, price=dish['price'],
                                       dish_name=dish['name'])
            db.session.add(new_order_dish)
            db.session.commit()
        else:
            similar_dish[0].quantity += 1
            db.session.commit()
    return "Item added to order successfully."


@app.route('/get_current_user_order', methods=['POST', 'GET'])
def get_current_user_order():
    user_opened_order = Order.query.filter_by(user_id=current_user.id, status="creation").first()
    user_order_dishes = OrderDish.query.filter_by(order_id=user_opened_order.id)
    dishes_serialized = [dish.serialize() for dish in user_order_dishes]
    return jsonify(dishes_serialized)


@app.route('/remove_from_order', methods=['POST', 'GET'])
def remove_from_order():
    order_dish_id = request.get_json()['order_dish_id']
    print(order_dish_id)

    user_opened_order = Order.query.filter_by(user_id=current_user.id, status="creation").all()[0]
    user_order_dish_to_be_removed = OrderDish.query.filter_by(order_id=user_opened_order.id,
                                                              id=order_dish_id).all()
    print(user_order_dish_to_be_removed[0].id)

    if user_order_dish_to_be_removed[0].quantity != 0:
        print(user_order_dish_to_be_removed[0].quantity)
        user_order_dish_to_be_removed[0].quantity -= 1
        db.session.commit()
        return jsonify("Successfully deleted dish from order")
    else:
        return jsonify("Something went wrong in remove_from_order")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/', methods=['POST', 'GET'])
def home():
    # add_dish_to_menu()
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    # print(user.id)
    login_user(user)
    if user.role == "Customer":
        return render_template('menu.html')
    elif user.role == "Manager":
        return render_template("mainPage.html")
    else:
        return jsonify("SOmething went wrong in home root")


@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_new_dish', methods=['POST', 'GET'])
def add_new_dish():
    if request.method == 'POST':
        new_dish_json = request.get_json()
        new_dish = Dish(name=new_dish_json['name'], description=new_dish_json['description'],
                        price=new_dish_json['price'], quantity=new_dish_json['quantity'])
        db.session.add(new_dish)
        db.session.commit()
        return jsonify("Successfully added new dish")
    return jsonify("Something went wrong while adding a new dish")


@app.route('/change_dish_quantity', methods=['POST', 'GET'])
def change_dish_quantity():
    if request.method == 'POST':
        data = request.get_json()
        dish_id = data['dish_id']
        new_quantity = data['quantity']
        dish_to_update = Dish.query.get(id=dish_id)
        dish_to_update.quantity = new_quantity
        return jsonify("Successfully updated dish quantity")
    return jsonify("Something went wrong while updating dish quantity")


@app.route('/change_dish_price', methods=['POST', 'GET'])
def change_dish_price():
    if request.method == 'POST':
        data = request.get_json()
        dish_id = data['dish_id']
        new_price = data['price']
        dish_to_update = Dish.query.get(id=dish_id)
        dish_to_update.price = new_price
        return jsonify("Successfully updated dish price")
    return jsonify("Something went wrong while updating dish price")


@app.route('/change_dish_name', methods=['POST', 'GET'])
def change_dish_name():
    if request.method == 'POST':
        data = request.get_json()
        dish_id = data['dish_id']
        new_name = data['name']
        dish_to_update = Dish.query.get(id=dish_id)
        dish_to_update.name = new_name
        return jsonify("Successfully updated dish name")
    return jsonify("Something went wrong while updating dish name")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def add_dish_to_menu():
    new_dish = Dish(id=1, name="Пицца", price=10, quantity=5)
    new_dish2 = Dish(id=2, name="Паста", price=15, quantity=10)
    new_dish3 = Dish(id=3, name="Салат", price=8, quantity=15)
    db.session.add(new_dish)
    db.session.add(new_dish2)
    db.session.add(new_dish3)
    db.session.commit()


# Запуск приложения
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5800)
