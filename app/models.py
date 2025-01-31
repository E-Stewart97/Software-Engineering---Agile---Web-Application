from app import db

# Users Table
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)  # Store hashed passwords
    role = db.Column(db.String(50), nullable=False)
    job_position = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    created_when = db.Column(db.DateTime, default=db.func.now())
    updated_when = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # Validate enums
    VALID_ROLES = ['Admin', 'Regular']
    VALID_POSITIONS = ['Software_Developer', 'Product_Manager', 'Product_Owner', 
                      'QA_Tester', 'Customer_Support_Specialist']

# Customers Table
class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    created_by = db.Column(db.String(150), db.ForeignKey('users.username'), nullable=False)
    created_when = db.Column(db.DateTime, default=db.func.now())
    updated_when = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

# Products Table
class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    created_when = db.Column(db.DateTime, default=db.func.now())
    updated_when = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

# Customer_Product Association Table
class CustomerProduct(db.Model):
    __tablename__ = 'customer_product'
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    created_when = db.Column(db.DateTime, default=db.func.now())
    updated_when = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
