from app import db
from app.models import Users, Customers, Products, CustomerProduct
from datetime import datetime

#Initial Data
# Insert data into the Users table
users_data = [
    Users(id=1, username='jsmith', password='Kj#9mNpQ2$xL', role='admin', job_position='Software_Developer', name='John Smith', created_when=datetime(2024, 3, 15, 8, 0), updated_when=datetime(2024, 12, 20, 10, 15)), # datetime: Year, month, day, hour, minute, second
    Users(id=2, username='ajones', password='Dragon5#Flight2023', role='regular', job_position='Product_Manager', name='Alice Jones', created_when=datetime(2024, 6, 22, 14, 30), updated_when=datetime(2024, 12, 28, 16, 45)),
    Users(id=3, username='bbrown', password='P@ssw0rd_Keeper!', role='regular', job_position='Product_Owner', name='Bob Brown', created_when=datetime(2024, 9, 5, 9, 15), updated_when=datetime(2024, 12, 18, 11, 30)),
    Users(id=4, username='clee', password='Bl@ckC@t9Lives', role='regular', job_position='QA_Tester', name='Carol Lee', created_when=datetime(2024, 11, 12, 17, 45), updated_when=datetime(2025, 1, 2, 13, 0)),
    Users(id=5, username='ddavis', password='Secure_P@ss123', role='regular', job_position='Customer_Support_Specialist', name='David Davis', created_when=datetime(2024, 2, 18, 11, 0), updated_when=datetime(2024, 11, 25, 9, 30)),
    Users(id=6, username='emiller', password='Nebul@2024Star!', role='regular', job_position='Software_Developer', name='Emily Miller', created_when=datetime(2024, 5, 3, 16, 30), updated_when=datetime(2024, 12, 5, 14, 45)),
    Users(id=7, username='fwilson', password='Th3_Qu1ck#Fox', role='regular', job_position='Product_Manager', name='Frank Wilson', created_when=datetime(2024, 8, 10, 8, 45), updated_when=datetime(2024, 12, 22, 17, 0)),
    Users(id=8, username='ggarcia', password='C0de_M@ster365', role='regular', job_position='Product_Owner', name='Gina Garcia', created_when=datetime(2024, 10, 27, 15, 0), updated_when=datetime(2025, 1, 4, 10, 15)),
    Users(id=9, username='hmartinez', password='Jump$4Success!', role='regular', job_position='QA_Tester', name='Henry Martinez', created_when=datetime(2024, 1, 15, 12, 15), updated_when=datetime(2024, 11, 10, 15, 30)),
    Users(id=10, username='irobinson', password='Br1ght_Futur3#', role='regular', job_position='Customer_Support_Specialist', name='Isabella Robinson', created_when=datetime(2024, 4, 8, 10, 30), updated_when=datetime(2024, 12, 12, 11, 45))
]

# Insert data into the Customers table
customers_data = [
    Customers(id=1, name='Acme Corp', created_by='ajones', created_when=datetime(2024, 7, 1, 10, 0), updated_when=datetime(2024, 12, 20, 14, 30)),
    Customers(id=2, name='Beta Industries', created_by='ajones', created_when=datetime(2024, 9, 15, 15, 30), updated_when=datetime(2024, 12, 28, 11, 15)),
    Customers(id=3, name='Gamma Solutions', created_by='bbrown', created_when=datetime(2024, 11, 1, 8, 45), updated_when=datetime(2025, 1, 2, 9, 0)),
    Customers(id=4, name='Delta Systems', created_by='bbrown', created_when=datetime(2024, 1, 15, 13, 0), updated_when=datetime(2024, 11, 25, 16, 30)),
    Customers(id=5, name='Epsilon Technologies', created_by='clee', created_when=datetime(2024, 3, 30, 16, 15), updated_when=datetime(2024, 12, 5, 10, 45)),
    Customers(id=6, name='Zeta Innovations', created_by='clee', created_when=datetime(2024, 5, 15, 9, 30), updated_when=datetime(2024, 12, 22, 12, 0)),
    Customers(id=7, name='Eta Enterprises', created_by='ddavis', created_when=datetime(2024, 8, 1, 14, 45), updated_when=datetime(2025, 1, 4, 9, 15)),
    Customers(id=8, name='Theta Solutions', created_by='ddavis', created_when=datetime(2024, 10, 15, 11, 0), updated_when=datetime(2024, 11, 10, 14, 30)),
    Customers(id=9, name='Iota Systems', created_by='emiller', created_when=datetime(2024, 2, 28, 17, 15), updated_when=datetime(2024, 12, 12, 8, 45)),
    Customers(id=10, name='Kappa Innovations', created_by='emiller', created_when=datetime(2024, 4, 15, 10, 30), updated_when=datetime(2024, 12, 18, 11, 0))
]

# Insert data into the Products table
products_data = [
    Products(id=1, name='In-store Payment Terminals', created_when=datetime(2024, 1, 1, 9, 0), updated_when=datetime(2024, 10, 1, 10, 0)),
    Products(id=2, name='Online Payment Gateway', created_when=datetime(2024, 5, 15, 14, 0), updated_when=datetime(2024, 12, 15, 15, 0)),
    Products(id=3, name='Mobile Payment App', created_when=datetime(2024, 8, 1, 11, 0), updated_when=datetime(2024, 12, 1, 12, 0)),
    Products(id=4, name='Payment Processing API', created_when=datetime(2024, 11, 15, 10, 0), updated_when=datetime(2025, 1, 15, 11, 0)),
    Products(id=5, name='Fraud Prevention Tools', created_when=datetime(2024, 2, 1, 15, 0), updated_when=datetime(2024, 11, 1, 16, 0)),
    Products(id=6, name='Data Analytics', created_when=datetime(2024, 4, 15, 12, 0), updated_when=datetime(2024, 12, 15, 13, 0)),
    Products(id=7, name='Acquiring Processing', created_when=datetime(2024, 7, 1, 13, 0), updated_when=datetime(2024, 12, 1, 14, 0)),
    Products(id=8, name='Digital Banking Solutions', created_when=datetime(2024, 10, 15, 12, 0), updated_when=datetime(2025, 1, 15, 13, 0)),
    Products(id=9, name='eTicketing Solutions', created_when=datetime(2024, 3, 1, 16, 0), updated_when=datetime(2024, 11, 1, 17, 0)),
    Products(id=10, name='Trusted Digital Services', created_when=datetime(2024, 6, 15, 13, 0), updated_when=datetime(2024, 12, 15, 14, 0))
]

# Insert data into the Customer_Products table
customer_products_data = [
    CustomerProduct(customer_id=1, product_id=1, created_when=datetime(2024, 7, 2, 11, 0), updated_when=datetime(2024, 12, 21, 15, 30)),
    CustomerProduct(customer_id=1, product_id=3, created_when=datetime(2024, 7, 2, 11, 15), updated_when=datetime(2024, 12, 21, 15, 45)),
    CustomerProduct(customer_id=2, product_id=2, created_when=datetime(2024, 9, 16, 16, 0), updated_when=datetime(2024, 12, 29, 12, 15)),
    CustomerProduct(customer_id=2, product_id=4, created_when=datetime(2024, 9, 16, 16, 15), updated_when=datetime(2024, 12, 29, 12, 30)),
    CustomerProduct(customer_id=3, product_id=5, created_when=datetime(2024, 11, 2, 9, 0), updated_when=datetime(2025, 1, 3, 10, 0)),
    CustomerProduct(customer_id=3, product_id=7, created_when=datetime(2024, 11, 2, 9, 15), updated_when=datetime(2025, 1, 3, 10, 15)),
    CustomerProduct(customer_id=4, product_id=6, created_when=datetime(2024, 1, 16, 14, 0), updated_when=datetime(2024, 11, 26, 17, 30)),
    CustomerProduct(customer_id=4, product_id=8, created_when=datetime(2024, 1, 16, 14, 15), updated_when=datetime(2024, 11, 26, 17, 45)),
    CustomerProduct(customer_id=5, product_id=9, created_when=datetime(2024, 3, 31, 17, 0), updated_when=datetime(2024, 12, 6, 11, 45)),
    CustomerProduct(customer_id=5, product_id=10, created_when=datetime(2024, 3, 31, 17, 15), updated_when=datetime(2024, 12, 6, 12, 0)),
    CustomerProduct(customer_id=6, product_id=1, created_when=datetime(2024, 5, 16, 10, 0), updated_when=datetime(2024, 12, 23, 13, 30))
]

# Add all the data to the session and commit
try:
    db.session.bulk_save_objects(users_data)
    db.session.bulk_save_objects(customers_data)
    db.session.bulk_save_objects(products_data)
    db.session.bulk_save_objects(customer_products_data)
    db.session.commit()
    print("Data seeded successfully!")
except Exception as e:
    db.session.rollback()
    print(f"Error seeding data: {e}")
