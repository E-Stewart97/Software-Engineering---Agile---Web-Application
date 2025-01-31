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
flask seed-db

6. **Run the application:**
python run.py
Access the application: Open your web browser and go to http://127.0.0.1:5000/.


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
**Security Enhancements:**
* Implement password hashing
* Add password complexity requirements
* Implement rate limiting
* Add OAuth2 authentication

**Feature Additions:**
* Password reset functionality
* Email verification
* User profile management
* Advanced search and filtering
* Audit logging

**Technical Improvements:**
* Add tests
* Implement API documentation

**UI/UX Improvements:**
* Add responsive design
* Implement dark and light modes
* Improve form validation feedback
* Add loading indicators