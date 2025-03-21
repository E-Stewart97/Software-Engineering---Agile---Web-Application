# Contact Management Web Application

A Flask-based web application for managing users, customers, products, and their relationships. The application features role-based access control and secure authentication.

## Features

### User Management
* View users with detailed information (ID, username, role, job position, name, timestamps)
* Add new users with role-based permissions
* Update existing user information
* Delete users (admin only)
* Self-registration for regular users
* Password confirmation on registration
* Prevent deletion of last admin account
* Prevent users from modifying their own admin status

### Customer Management
* View customers (ID, name, created by, creation/update timestamps)
* Add new customers with automatic creator tracking
* Update customer information
* Delete customers (admin only)
* Prevent duplicate customer names
* Track creation and modification timestamps

### Product Management
* View products (ID, name, creation/update timestamps)
* Add new products
* Update product information
* Delete products (admin only)
* Prevent duplicate product names
* Track creation and modification timestamps

### Customer-Product Associations
* View existing customer-product relationships
* Add new associations
* Update existing associations
* Remove associations (admin only)
* Prevent duplicate associations
* Track creation and modification timestamps

### Security Features
* Role-based access control (Admin/Regular users)
* Session management
* Password confirmation on registration
* Protected routes requiring authentication
* Admin-only delete operations
* Form validation and error handling

## Technologies Used

* **Backend:**
  * Flask (Python web framework)
  * SQLAlchemy (ORM)
  * Flask-Migrate (Database migrations)
  * SQLite (Database)

* **Frontend:**
  * HTML5
  * CSS3
  * JavaScript
  * Jinja2 (Templating)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd contact-management-system

2. **Create and activate a virtual environment:**
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt

4. **Initialize the database:**
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. **Seed the database:**
flask seed-db **This command can be used to repopulate the inital data**

6. **Run the application:**
python run.py

7. **Access the application:**
Open your web browser and go to http://127.0.0.1:5000/.

## Usage
1. **Register a new user:**
   * Go to the registration page.
   * Enter a username, password, and confirm password.
   * Select a role (Admin or Regular).
   * Click "Register".
2. **Login:**
   * Go to the login page.
   * Enter your username and password.
   * Click "Login".
3. **Manage Users:**
   * Go to the "Users" page.
   * View, add, update, or delete users.
   * Ensure you have the appropriate role to perform these actions.
4. **Manage Customers:**
   * Go to the "Customers" page.
   * View, add, update, or delete customers.
   * Ensure you have the appropriate role to perform these actions.
5. **Manage Products:**
   * Go to the "Products" page.
   * View, add, update, or delete products.
   * Ensure you have the appropriate role to perform these actions.
6. **Manage Customer-Product Associations:**
   * Go to the "Customer-Product" page.
   * View, add, update, or remove customer-product associations.
   * Ensure you have the appropriate role to perform these actions.

## Predefined user login accounts
* Admin: admin/admin
 username='jsmith', password='Kj#9mNpQ2$xL'
* Regular: regular/regular
 username='ajones', password='Dragon5#Flight2023'
 username='bbrown', password='P@ssw0rd_Keeper!'
 username='clee', password='Bl@ckC@t9Lives'
 username='ddavis', password='Secure_P@ss123'
 username='emiller', password='Nebul@2024Star!'
 username='fwilson', password='Th3_Qu1ck#Fox'
 username='ggarcia', password='C0de_M@ster365'
 username='hmartinez', password='Jump$4Success!'
 username='irobinson', password='Br1ght_Futur3#'
More data of these intial user logins can be found in seed_data.py file.

### Database Schema
**Users:**
* id (Primary Key)
* username (Unique)
* password
* role
* job_position
* name
* created_when
* updated_when

**Customers:**
* id (Primary Key)
* name
* created_by (Foreign Key to Users)
* created_when
* updated_when

**Products:**
* id (Primary Key)
* name
* created_when
* updated_when

**Customer_Product:**
* customer_id (Primary Key, Foreign Key)
* product_id (Primary Key, Foreign Key)
* created_when
* updated_when

### Future Improvements
**Known Issues:**
* Implementation CRUD operation: Deletion

**Security Enhancements:**
* Implement password hashing
* Add password complexity requirements
* Implement rate limiting
* Add OAuth2 authentication

**Feature Additions:**
* Deletion implementation of CRUD operations to delete records, however only Admin users can delete records
* Implement role-based access control for different user roles
* Implement user authentication and authorization
* Implement user session management
* Implement password confirmation on registration
* Implement password reset functionality
* Implement email verification
* Implement user profile management
* Implement advanced search and filtering
* Implement audit logging
* Implement data validation
* Implement error handling
* Password reset functionality
* Email verification
* User profile management
* Advanced search and filtering
* Audit logging via logging file or logging on Azure  for 'Application logging' and 'Web Server Diagnostics'
* Data validation as when adding records it's possible to add a record with just a number or letter which reduces data integrity
* Error handling

**Technical Improvements:**
* Add tests
* Implement API documentation

**UI/UX Improvements:**
* Add responsive design
* Implement dark and light modes
* Improve form validation feedback
* Add loading indicators