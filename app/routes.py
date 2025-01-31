from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from .models import db, Users, Customers, Products, CustomerProduct
from datetime import datetime

bp = Blueprint('app', __name__) # Name the blueprint 'app'

@bp.route("/", methods=["GET", "POST"])  # Use bp.route
def index():
    if 'user_id' in session:  # Check if user is logged in
        return render_template('index.html', username=session.get('username'), role=session.get('role'))
    else:
        return redirect(url_for('app.login'))  # Redirect to login, using blueprint name

@bp.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = Users.query.filter_by(username=username).first()
            if user and user.password == password:  # In production, use proper password hashing
                session['user_id'] = user.id
                session['username'] = user.username
                session['role'] = user.role.lower()
                flash('Logged in successfully!', 'success')
                return redirect(url_for('app.index'))
            else:
                flash('Invalid username or password', 'error')
        except Exception as e:
            flash(f'Error during login: {str(e)}', 'error')
            return redirect(url_for('app.login'))
    return render_template("login.html")

@bp.route("/logout")  # Use bp.route
def logout():
    session.clear()
    return redirect(url_for('app.login')) 

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        job_position = request.form['job_position']
        name = request.form['name']

        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('app.register'))

        # Force role to be 'regular' for self-registration
        new_user = Users(
            username=username,
            password=password,  # In production, hash this password
            role='regular',  # Always set to regular for self-registration
            job_position=job_position,
            name=name
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('app.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error during registration: {str(e)}', 'error')
            return redirect(url_for('app.register'))

    return render_template('register.html')

@bp.route("/users") 
def users():
    users = Users.query.all()
    return render_template("users.html", users=users)

@bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        job_position = request.form['job_position']
        name = request.form['name']

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('app.add_user'))

        # Set role based on current user's permissions
        if session.get('role') == 'admin':
            # Admin can specify the role
            role = request.form.get('role', 'regular')
        else:
            # Non-admin can only create regular users
            role = 'regular'

        new_user = Users(
            username=username,
            password=password,  # In production, hash this password
            role=role,
            job_position=job_position,
            name=name
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully', 'success')
            return redirect(url_for('app.users'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding user: {str(e)}', 'error')
            return redirect(url_for('app.add_user'))

    return render_template('add_user.html')

@bp.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = Users.query.get_or_404(id)
    
    if request.method == 'POST':
        # Get the new role from the form
        new_role = request.form.get('role', user.role)  # Default to current role if not provided
        current_user_id = session.get('user_id')
        
        # Check if user is trying to modify their own role
        if id == current_user_id:
            if user.role == 'admin' and new_role != 'admin':
                flash('You cannot downgrade your own admin role', 'error')
                return redirect(url_for('app.users'))
        
        # Check if non-admin user is trying to set admin role
        if session.get('role') != 'admin' and new_role == 'admin':
            flash('Only administrators can grant admin privileges', 'error')
            return redirect(url_for('app.users'))
            
        # If all checks pass, update the user
        try:
            user.role = new_role
            user.job_position = request.form.get('job_position')
            user.name = request.form.get('name')
            db.session.commit()
            flash('User updated successfully', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating user: {str(e)}', 'error')
        
        return redirect(url_for('app.users'))
        
    return render_template('update_user.html', user=user)

@bp.route("/delete_user/<int:id>", methods=["POST"])
def delete_user(id):
    if session.get('role') != 'admin':
        flash('Only admins can delete users', 'error')
        return redirect(url_for('app.users'))
    
    try:
        # Check if user is trying to delete their own account
        if id == session.get('user_id'):
            flash('You cannot delete your own account', 'error')
            return redirect(url_for('app.users'))
            
        user = Users.query.get_or_404(id)
        
        # Additional check to prevent deleting the last admin
        admin_count = Users.query.filter_by(role='admin').count()
        if user.role == 'admin' and admin_count <= 1:
            flash('Cannot delete the last admin account', 'error')
            return redirect(url_for('app.users'))
            
        db.session.delete(user)
        db.session.commit()
        
        # If the deleted user is logged in somewhere, their session should be invalidated
        # This is a basic implementation - in a production environment, you'd want a more robust session management system
        if user.username == session.get('username'):
            session.clear()
            flash('Your account has been deleted. You have been logged out.', 'info')
            return redirect(url_for('app.login'))
            
        flash('User deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting user: {str(e)}', 'error')
    return redirect(url_for('app.users'))

@bp.route("/customers")
def customers():
    customers = Customers.query.all()
    return render_template("customers.html", customers=customers)

@bp.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        created_by = session.get('username')

        # Check if a customer with this name already exists
        existing_customer = Customers.query.filter_by(name=name).first()
        if existing_customer:
            flash(f'A customer with the name "{name}" already exists.', 'error')
            return redirect(url_for('app.add_customer'))

        new_customer = Customers(
            name=name,
            created_by=created_by
        )
        try:
            db.session.add(new_customer)
            db.session.commit()
            flash('Customer added successfully', 'success')
            return redirect(url_for('app.customers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding customer: {str(e)}', 'error')
            return redirect(url_for('app.add_customer'))

    return render_template('add_customer.html')

@bp.route("/update_customer/<int:id>", methods=["GET", "POST"])
def update_customer(id):
    customer = Customers.query.get_or_404(id)
    if request.method == "POST":
        new_name = request.form.get('name')
        
        # Check if another customer already has this name
        existing_customer = Customers.query.filter(
            Customers.name == new_name,
            Customers.id != id
        ).first()
        
        if existing_customer:
            flash(f'A customer with the name "{new_name}" already exists.', 'error')
            return redirect(url_for('app.update_customer', id=id))
            
        try:
            customer.name = new_name
            # Don't allow changing created_by through the form
            # customer.created_by = request.form.get('created_by')
            db.session.commit()
            flash('Customer updated successfully!', 'success')
            return redirect(url_for('app.customers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating customer: {str(e)}', 'error')
            return redirect(url_for('app.update_customer', id=id))
    return render_template("update_customer.html", customer=customer)

@bp.route("/delete_customer/<int:id>", methods=["POST"])
def delete_customer(id):
    try:
        customer = Customers.query.get_or_404(id)
        
        # Check if there are any associated customer-product relationships
        existing_associations = CustomerProduct.query.filter_by(customer_id=id).all()
        if existing_associations:
            for association in existing_associations:
                db.session.delete(association)
        
        db.session.delete(customer)
        db.session.commit()
        flash('Customer deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting customer: {str(e)}', 'error')
    return redirect(url_for('app.customers'))

@bp.route("/products") 
def products():
    products = Products.query.all()
    return render_template("products.html", products=products)

@bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']

        # Check if a product with this name already exists
        existing_product = Products.query.filter_by(name=name).first()
        if existing_product:
            flash(f'A product with the name "{name}" already exists.', 'error')
            return redirect(url_for('app.add_product'))

        new_product = Products(
            name=name
        )
        try:
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully', 'success')
            return redirect(url_for('app.products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding product: {str(e)}', 'error')
            return redirect(url_for('app.add_product'))

    return render_template('add_product.html')

@bp.route("/update_product/<int:id>", methods=["GET", "POST"])
def update_product(id):
    product = Products.query.get_or_404(id)
    if request.method == "POST":
        new_name = request.form.get('name')
        
        # Check if another product already has this name
        existing_product = Products.query.filter(
            Products.name == new_name,
            Products.id != id
        ).first()
        
        if existing_product:
            flash(f'A product with the name "{new_name}" already exists.', 'error')
            return redirect(url_for('app.update_product', id=id))
            
        try:
            product.name = new_name
            db.session.commit()
            flash('Product updated successfully!', 'success')
            return redirect(url_for('app.products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating product: {str(e)}', 'error')
            return redirect(url_for('app.update_product', id=id))
    return render_template("update_product.html", product=product)

@bp.route("/delete_product/<int:id>", methods=["POST"])
def delete_product(id):
    try:
        product = Products.query.get_or_404(id)
        
        # Check if there are any associated customer-product relationships
        existing_associations = CustomerProduct.query.filter_by(product_id=id).all()
        if existing_associations:
            for association in existing_associations:
                db.session.delete(association)
        
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting product: {str(e)}', 'error')
    return redirect(url_for('app.products'))

@bp.route("/customer_product")
def customer_product():
    customer_products = CustomerProduct.query.all()
    return render_template("customer_products.html", customer_products=customer_products)

@bp.route('/add_customer_product', methods=['GET', 'POST'])
def add_customer_product():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        product_id = request.form['product_id']

        # Check if this association already exists
        existing_association = CustomerProduct.query.filter_by(
            customer_id=customer_id, 
            product_id=product_id
        ).first()
        
        if existing_association:
            flash('This customer-product association already exists.', 'error')
            return redirect(url_for('app.add_customer_product'))

        new_customer_product = CustomerProduct(
            customer_id=customer_id,
            product_id=product_id
        )
        try:
            db.session.add(new_customer_product)
            db.session.commit()
            flash('Customer Product association added successfully', 'success')
            return redirect(url_for('app.customer_product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding customer product association: {str(e)}', 'error')
            return redirect(url_for('app.add_customer_product'))

    # Get all customers and products for the dropdowns
    customers = Customers.query.all()
    products = Products.query.all()
    return render_template('add_customer_product.html', customers=customers, products=products)

@bp.route("/update_customer_product/<int:customer_id>/<int:product_id>", methods=["GET", "POST"])
def update_customer_product(customer_id, product_id):
    customer_product = CustomerProduct.query.get_or_404((customer_id, product_id))
    if request.method == "POST":
        try:
            customer_product.customer_id = request.form.get('customer_id')
            customer_product.product_id = request.form.get('product_id')
            db.session.commit()
            flash('Customer-Product association updated successfully!', 'success')
            return redirect(url_for('app.customer_product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating customer-product association: {str(e)}', 'error')
            return redirect(url_for('app.update_customer_product', 
                                  customer_id=customer_id, 
                                  product_id=product_id))
    return render_template("update_customer_product.html", customer_product=customer_product)

@bp.route("/delete_customer_product/<int:customer_id>/<int:product_id>", methods=["POST"])
def delete_customer_product(customer_id, product_id):
    try:
        customer_product = CustomerProduct.query.get_or_404((customer_id, product_id))
        db.session.delete(customer_product)
        db.session.commit()
        flash('Customer-Product association deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting customer-product association: {str(e)}', 'error')
    return redirect(url_for('app.customer_product'))

@bp.route("/test_db")
def test_db(): # This tests the DB
    try:
        users = Users.query.all()
        result = "Users in database:\n"
        for user in users:
            result += f"Username: {user.username}, Role: {user.role}\n"
        return result
    except Exception as e:
        return f"Error accessing database: {str(e)}"