# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:13:39 2024

@author: ZSLUCCAM

pip install flask-login
pip install mysql-connector-python
"""

from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import mysql.connector
from datetime import datetime


 
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['LOGIN_VIEW'] = 'login'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def get_db_connection():
    return  mysql.connector.connect(
      host="localhost",
      user="adlogin",           #change this in order login mysql
      password="Son@123",       #change this in order login mysql
      database="COFFEE"         #Please do not change the name of database in mysql
    )

# Mock database
'''
users = {
    "user1": {"password": generate_password_hash("password1"), "role": "staff"},
    "manager1": {"password": generate_password_hash("manager123"), "role": "manager"},
}
'''
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    # This function is not using the database, assuming the user stays logged in by ID
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userID = request.form.get('userid')
        password = request.form.get('password')
        role = request.form.get('role')  # Get the selected role from the dropdown

        # Debugging: Print the input values
        print(f"Received userID: {userID}, password: {password}, role: {role}")

        # Validate inputs
        if not userID or not password or not role:
            flash('All fields are required.', 'danger')
            print("Error: One or more fields are missing (userID, password, role).")
            return redirect(url_for('login'))

        # Validate the role
        if role not in ['staff', 'manager']:
            flash('Invalid role selected.', 'danger')
            print(f"Error: Invalid role selected: {role}")
            return redirect(url_for('login'))

        try:
            # Connect to the database
            print("Connecting to the database...")
            conn = get_db_connection()
            cursor = conn.cursor()

            # Prepare the OUT parameter
            p_Result = None  # We will fetch the OUT parameter result
            
            # Debugging: Output before calling the stored procedure
            print(f"Calling stored procedure 'FindMatchingNhanVien' with userID: {userID}, password: {password}, role: {role}")

            # Call the stored procedure with 3 IN parameters and 1 OUT parameter
            result = cursor.callproc('FindMatchingNhanVien', (userID, password, role, p_Result))
            '''
            # Debugging: Output after calling the procedure
            print("Stored procedure called, fetching result...")

            # Fetch the result from the stored procedure (OUT parameter value)
            for result in cursor.stored_results():
                # The OUT parameter should be available now in the first row
                p_Result = result.fetchone()[0]
            '''
            p_Result = result[len(result)-1]
            # Debugging: Print the result value
            print(f"Procedure result: {p_Result}")

            # Check if the result is "Yes"
            if p_Result == 'Yes':
                login_user(User(userID))  # Login user
                flash(f'Logged in as {role}.', 'success')
                print(f"User {userID} logged in as {role}.")
                # Redirect to different pages based on the role
                if role == 'manager':
                    print("Redirecting to home page...")
                    return redirect(url_for('dashboard'))  # Example manager page
                print("Redirecting to order employee page...")
                return redirect(url_for('orderemployee'))  # Example staff page
            else:
                flash('Invalid user ID, password, or role.', 'danger')
                print(f"Login failed for userID: {userID} with role: {role}.")

        except mysql.connector.Error as err:
            # Debugging: Print the database error
            print(f"Database error: {err}")
            flash(f'Database error: {err}', 'danger')
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed.")

    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        manv = request.form.get('manv')
        manager = request.form.get('manager')
        ten = request.form.get('ten')
        sodt = request.form.get('sodt')
        cccd = request.form.get('cccd')
        diachi = request.form.get('diachi')
        phuong = request.form.get('phuong')
        quan = request.form.get('quan')
        ngaysinh = request.form.get('ngaysinh')
        chinhanh = request.form.get('chinhanh')
        ngaythamgia = request.form.get('ngaythamgia')
        hoatdong = 1 if request.form.get('hoatdong') == 'on' else 0  # Convert to 1/0
        chucvu = request.form.get('chucvu')
        password = request.form.get('password')

        try:
            # Debug inputs
            print("Form Inputs:", manv, manager, ten, sodt, cccd, diachi, phuong, quan, ngaysinh, chinhanh, ngaythamgia, hoatdong, chucvu, password)

            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert data into NHANVIEN table
            sql = '''
            INSERT INTO NHANVIEN (MANV, MANAGER, TEN, SODT, CCCD, DIACHI, PHUONG, QUAN, NGAYSINH, CHINHANH, NGAYTHAMGIA, HOATDONG, CHUCVU, PASS)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            #hashed_password = generate_password_hash(password)
            cursor.execute(sql, (manv, manager, ten, sodt, cccd, diachi, phuong, quan, ngaysinh, chinhanh, ngaythamgia, hoatdong, chucvu, password))

            conn.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('register'))
        except mysql.connector.IntegrityError as e:
            flash(f'Integrity error: {e}', 'danger')
            print("Integrity Error:", e)
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
            print("Database Error:", err)
        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')



@app.route('/change_pass', methods=['GET', 'POST'])
def change_pass():
    if request.method == 'POST':
        userID = request.form.get('userid')
        old_password = request.form.get('password')  # The old password entered by the user
        new_password = request.form.get('new_password')  # The new password to be set
        confirm_password = request.form.get('confirm_password')  # Password confirmation field

        # Check if passwords match
        if new_password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('change_pass'))

        try:
            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Step 1: Check if the provided old password matches the one in the database
            check_sql = "SELECT `PASS` FROM `NHANVIEN` WHERE `MANV` = %s"
            cursor.execute(check_sql, (userID,))

            # Fetch the result
            current_password = cursor.fetchone()

            # Step 2: If the old password is correct, update the password
            if current_password:
                if current_password[0] == old_password:
                    # Step 3: Update the password in the database
                    update_sql = "UPDATE `NHANVIEN` SET `PASS` = %s WHERE `MANV` = %s"
                    cursor.execute(update_sql, (new_password, userID))

                    # Commit the changes to the database
                    conn.commit()

                    # Output the number of rows affected
                    if cursor.rowcount > 0:
                        flash('Password updated successfully!', 'success')
                        return redirect(url_for('login'))  # Redirect to login page after password change
                    else:
                        flash('No changes were made.', 'danger')
                else:
                    flash('Old password is incorrect!', 'danger')
            else:
                flash('User ID not found.', 'danger')

        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('changepass.html')


'''
orders = [] 

@app.route('/orderemployee', methods=['GET', 'POST'])
@login_required
def orderemployee():
    # Initialize the temporary order list if it doesn't exist in the session
    if 'order_items' not in session:
        session['order_items'] = []

    if request.method == 'POST':
        # Add product details to the temporary list when the "Add Item" button is clicked
        if 'add_item' in request.form:
            product_ID = request.form.get('product_ID')
            quantity = int(request.form.get('quantity'))
            price = request.form.get('price')

            # Validate price and quantity
            if not price:
                flash('Price is required.', 'danger')
                return redirect(url_for('orderemployee'))

            if quantity < 1:
                flash('Quantity must be at least 1.', 'danger')
                return redirect(url_for('orderemployee'))

            # Add the item to the session's temporary order list
            session['order_items'].append({
                'product_ID': product_ID,
                'quantity': quantity,
                'price': price,
                'total_price': float(price) * quantity  # Calculate total price
            })
            session.modified = True  # Mark the session as modified to ensure the changes are saved
            flash('Item added to temporary list!', 'success')

        # Handle submitting the order when the "Submit Order" button is clicked
        if 'submit_order' in request.form:
            if not session['order_items']:
                flash('No items to submit.', 'danger')
                return redirect(url_for('orderemployee'))

            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # Get the current row count of DATMON to generate MAORDER
                cursor.execute("SELECT COUNT(*) FROM DATMON")
                row_count = cursor.fetchone()[0]

                # Generate MAORDER as ORD-{row_count + 1}
                order_ID = f"ORD-{row_count + 1}"
                ngay_order = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Insert the new order into DATMON
                cursor.execute("""
                    INSERT INTO DATMON (MAODER, NGAYODER, MANV)
                    VALUES (%s, %s, %s)
                """, (order_ID, ngay_order, current_user.id))

                # Insert each item from the temporary list into CHITETODER
                for item in session['order_items']:
                    cursor.execute("""
                        INSERT INTO CHITETODER (MAODER, MANV, MASP, SOLUONG, GIATIEN)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_ID, current_user.id, item['product_ID'], item['quantity'], item['price']))

                conn.commit()
                flash('Order placed successfully!', 'success')

                # Clear the temporary order list after submission
                session['order_items'] = []
                session.modified = True

            except mysql.connector.Error as err:
                flash(f'Database error: {err}', 'danger')
            finally:
                cursor.close()
                conn.close()

        # Handle clearing the order (cancel the order)
        if 'cancel_order' in request.form:
            session['order_items'] = []
            session.modified = True
            flash('Order items cleared!', 'success')

    # Fetch all products from the SANPHAM table for the product dropdown
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MASP, TENSP, GIATIEN FROM SANPHAM")
        products = cursor.fetchall()
    except mysql.connector.Error as err:
        flash(f'Error fetching products: {err}', 'danger')
    finally:
        cursor.close()
        conn.close()

    # Calculate the total price of all items in the temporary list
    total_price = sum(item['total_price'] for item in session['order_items'])

    return render_template('orderemployee.html', 
                           products=products, 
                           order_items=session['order_items'], 
                           total_price=total_price)

'''

@app.route('/orderemployee', methods=['GET', 'POST'])
@login_required
def orderemployee():
    if 'order_items' not in session:
        session['order_items'] = []  # Initialize empty order list if it doesn't exist

    if request.method == 'POST':
        # Add product details to the temporary list when the "Add Item" button is clicked
        if 'add_item' in request.form:
            product_ID = request.form.get('product_ID')
            quantity = int(request.form.get('quantity'))

            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT GIATIEN FROM SANPHAM WHERE MASP = %s", (product_ID,))
                product = cursor.fetchone()

                if not product:
                    flash('Product not found.', 'danger')
                    return redirect(url_for('orderemployee'))

                price = product[0]  # Price of the selected product
            except mysql.connector.Error as err:
                flash(f'Database error: {err.msg}', 'danger')
                return redirect(url_for('orderemployee'))
            finally:
                cursor.close()
                conn.close()

            if quantity < 1:
                flash('Quantity must be at least 1.', 'danger')
                return redirect(url_for('orderemployee'))

            session['order_items'].append({
                'product_ID': product_ID,
                'quantity': quantity,
                'price': price,
                'total_price': float(price) * quantity
            })
            session.modified = True
            flash('Item added to the temporary list!', 'success')

        # Handle submitting the order
        if 'submit_order' in request.form:
            if not session['order_items']:
                flash('No items to submit.', 'danger')
                return redirect(url_for('orderemployee'))

            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # Generate MAORDER
                cursor.execute("SELECT COUNT(*) FROM DATMON")
                row_count = cursor.fetchone()[0]
                order_ID = f"ORD-{row_count + 1}"
                ngay_order = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Insert into DATMON
                cursor.execute("""
                    INSERT INTO DATMON (MAODER, NGAYODER, MANV, HOANTHANH)
                    VALUES (%s, %s, %s, %s)
                """, (order_ID, ngay_order, current_user.id, 1))

                # Insert into CHITETODER
                for item in session['order_items']:
                    cursor.execute("""
                        INSERT INTO CHITETODER (MAODER, MANV, MASP, SOLUONG, GIATIEN)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_ID, current_user.id, item['product_ID'], item['quantity'], item['price']))

                conn.commit()
                flash('Order placed successfully!', 'success')

                session['order_items'] = []  # Clear temporary list
                session.modified = True

            except mysql.connector.Error as err:
                flash(f'Database error: {err.msg}', 'danger')
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

        # Clear order
        if 'cancel_order' in request.form:
            session['order_items'] = []
            session.modified = True
            flash('Order items cleared!', 'success')

    # Fetch products
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MASP, TENSP, GIATIEN FROM SANPHAM")
        products = cursor.fetchall()
    except mysql.connector.Error as err:
        flash(f'Error fetching products: {err.msg}', 'danger')
        products = []
    finally:
        cursor.close()
        conn.close()

    # Calculate total price
    total_price = sum(item['total_price'] for item in session['order_items'])

    return render_template('orderemployee.html', 
                           products=products, 
                           order_items=session['order_items'], 
                           total_price=total_price)






# Route to handle the order cancellation and display the orders
@app.route('/cancel_order', methods=['GET', 'POST'])
def cancel_order():
    logged_in_manv = current_user.id
    if request.method == 'POST':
        maoder = request.form.get('maoder')

        if maoder:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # Update the HOANTHANH column to 0 where MAODER matches
                cursor.execute("""
                    UPDATE DATMON SET HOANTHANH = 0 WHERE MAODER = %s AND MANV = %s
                """, (maoder,logged_in_manv))
                conn.commit()
                flash('Order cancelled successfully!', 'success')

            except mysql.connector.Error as err:
                flash(f'Database error: {err}', 'danger')
            finally:
                cursor.close()
                conn.close()

        else:
            flash('Please provide a valid MAODER.', 'danger')

    # Retrieve all orders (DATMON) to display in the frontend
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT MAODER, NGAYODER, MANV, HOANTHANH FROM DATMON WHERE MANV = %s""", (logged_in_manv,))
        orders = cursor.fetchall()
    except mysql.connector.Error as err:
        flash(f'Error retrieving orders: {err}', 'danger')
        orders = []
    finally:
        cursor.close()
        conn.close()

    return render_template('cancel.html', orders=orders)


@app.route('/warehouse_flow', methods=['GET', 'POST'])
@login_required
def warehouse_flow():
    if request.method == 'POST':
        # Retrieve form data
        manl = request.form.get('manl')
        manv = current_user.id
        soluong = request.form.get('soluong')
        ngay = request.form.get('ngay')  # Ensure format is YYYY-MM-DD
        xuatnhap = 1 if request.form.get('xuatnhap') == 'on' else 0  # Convert checkbox to BIT (1/0)
        
        # Fetch MANCC based on MANL (assuming there's a lookup table for this)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # SQL query to fetch MANCC based on MANL
            cursor.execute("SELECT MANCC FROM KHO WHERE MANL = %s", (manl,))
            result = cursor.fetchone()
            
            if result:
                mancc = result[0]  # Get the MANCC from the query result
            else:
                flash('No MANCC found for the provided MANL!', 'danger')
                return redirect(url_for('warehouse_flow'))

            # Debug input values
            print("Form Inputs:", manl, manv, soluong, ngay, xuatnhap, mancc)

            # Insert data into CHITIETXUATNHAPKHO table
            sql = '''
            INSERT INTO CHITIETXUATNHAPKHO (MANL, MANV, SOLUONG, NGAY, XUATNHAP, MANCC)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (manl, manv, soluong, ngay, xuatnhap, mancc))

            # Commit changes
            conn.commit()
            flash('Warehouse entry recorded successfully!', 'success')
            return redirect(url_for('warehouse_flow'))  # Redirect to the same page
            
        except mysql.connector.IntegrityError as e:
            flash(f'Integrity error: {e}', 'danger')
            print("Integrity Error:", e)
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
            print("Database Error:", err)
        finally:
            cursor.close()
            conn.close()

    # Render the HTML form
    return render_template('warehouse_flow.html')

@app.route('/add_warehouse', methods=['GET', 'POST'])
@login_required
def add_warehouse():
    if request.method == 'POST':
        # Get form data
        manl = request.form.get('manl')
        tennl = request.form.get('tennl')
        soluong = 0
        donvi = request.form.get('donvi')
        xuatxu = request.form.get('xuatxu')
        mancc = request.form.get('mancc')

        try:
            # Debug inputs
            print("Form Inputs:", manl, tennl, soluong, donvi, xuatxu, mancc)

            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert data into the KHO table
            sql = '''
            INSERT INTO KHO (MANL, TENNL, SOLUONG, DONVI, XUATXU, MANCC)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (manl, tennl, soluong, donvi, xuatxu, mancc))

            conn.commit()
            flash('Warehouse item added successfully!', 'success')
            return redirect(url_for('add_warehouse'))
        except mysql.connector.IntegrityError as e:
            flash(f'Integrity error: {e}', 'danger')
            print("Integrity Error:", e)
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
            print("Database Error:", err)
        finally:
            cursor.close()
            conn.close()

    return render_template('add_warehouse.html')



@app.route('/get_material_details', methods=['POST'])
@login_required
def get_material_details():
    manl = request.json.get('manl')
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT DONVI, MANCC FROM MATERIALS WHERE MANL = %s", (manl,))
        material_details = cursor.fetchone()
        return jsonify(material_details)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/supply-er', methods=['GET', 'POST'])
@login_required
def supply_er():
    if request.method == 'POST':
        # Get form data
        mancc = request.form.get('mancc')
        tenncc = request.form.get('tenncc')
        email = request.form.get('email')
        sodt = request.form.get('sodt')
        diachi = request.form.get('diachi')

        try:
            # Debug inputs
            print("Form Inputs:", mancc, tenncc, email, sodt, diachi)

            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert data into the NHACUNGCAP table
            sql = '''
            INSERT INTO NHACUNGCAP (MANCC, TENNCC, EMAIL, SODT, DIACHI)
            VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (mancc, tenncc, email, sodt, diachi))

            conn.commit()
            flash('Supplier added successfully!', 'success')
            return redirect(url_for('supply_er'))
        except mysql.connector.IntegrityError as e:
            flash(f'Integrity error: {e}', 'danger')
            print("Integrity Error:", e)
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
            print("Database Error:", err)
        finally:
            cursor.close()
            conn.close()

    return render_template('supply_er.html')

@app.route('/pro-duct', methods=['GET', 'POST'])
@login_required
def pro_duct():
    if request.method == 'POST':
        # Get form data
        masp = request.form.get('masp')
        tensp = request.form.get('tensp')
        giatien = request.form.get('giatien')

        try:
            # Debug inputs
            print("Form Inputs:", masp, tensp, giatien)

            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert data into the SANPHAM table
            sql = '''
            INSERT INTO SANPHAM (MASP, TENSP, GIATIEN)
            VALUES (%s, %s, %s)
            '''
            cursor.execute(sql, (masp, tensp, giatien))

            conn.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('pro_duct'))
        except mysql.connector.IntegrityError as e:
            flash(f'Integrity error: {e}', 'danger')
            print("Integrity Error:", e)
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'danger')
            print("Database Error:", err)
        finally:
            cursor.close()
            conn.close()

    return render_template('pro_duct.html')


@app.route('/dashboard')
@login_required
def dashboard():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all records from the KHO table
        cursor.execute("SELECT MANL, TENNL, SOLUONG, DONVI, XUATXU, MANCC FROM KHO")
        kho_data = cursor.fetchall()

    except mysql.connector.Error as err:
        flash(f"Database error: {err}", 'danger')
        kho_data = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

    # Render the dashboard template and pass the KHO data
    return render_template('dashboard.html', kho_data=kho_data)

@app.route('/view-supply-er')
@login_required
def view_supply_er():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all records from the NHACUNGCAP table
        cursor.execute("SELECT MANCC, TENNCC, EMAIL, SODT, DIACHI FROM NHACUNGCAP")
        supply_data = cursor.fetchall()

    except mysql.connector.Error as err:
        flash(f"Database error: {err}", 'danger')
        supply_data = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

    # Render the view-supply-er template and pass the supplier data
    return render_template('view_supply_er.html', supply_data=supply_data)


@app.route('/view-pro-duct')
@login_required
def view_pro_duct():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all records from the SANPHAM table
        cursor.execute("SELECT MASP, TENSP, GIATIEN FROM SANPHAM")
        product_data = cursor.fetchall()

    except mysql.connector.Error as err:
        flash(f"Database error: {err}", 'danger')
        product_data = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

    # Render the view-pro-duct template and pass the product data
    return render_template('view_pro_duct.html', product_data=product_data)

@app.route('/h-r')
@login_required
def h_r():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all records from the NHANVIEN table
        cursor.execute("""
            SELECT MANV, MANAGER, TEN, SODT, CCCD, DIACHI, PHUONG, QUAN, 
                   DATE_FORMAT(NGAYSINH, '%Y-%m-%d') as NGAYSINH, 
                   CHINHANH, DATE_FORMAT(NGAYTHAMGIA, '%Y-%m-%d') as NGAYTHAMGIA, 
                   HOATDONG, CHUCVU 
            FROM NHANVIEN
        """)
        hr_data = cursor.fetchall()

    except mysql.connector.Error as err:
        flash(f"Database error: {err}", 'danger')
        hr_data = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

    # Render the h-r template and pass the HR data
    return render_template('h_r.html', hr_data=hr_data)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))
 
# Define the menu items
menu_items = [
    {"name": "Espresso", "description": "A strong, full-bodied coffee.", "price": "72.000 VND", "image": "PIC/esp.png"},
    {"name": "Latte", "description": "Creamy and smooth.", "price": "112.500 VND", "image": "PIC/lat.png"},
    {"name": "Cappuccino", "description": "Perfectly foamy and rich.", "price": "100.000 VND", "image": "PIC/cap.png"},
    {"name": "Espresso", "description": "A strong, full-bodied coffee.", "price": "72.000 VND", "image": "PIC/esp.png"},
    {"name": "Latte", "description": "Creamy and smooth.", "price": "112.500 VND", "image": "PIC/lat.png"},
    {"name": "Cappuccino", "description": "Perfectly foamy and rich.", "price": "100.000 VND", "image": "PIC/cap.png"},
    {"name": "Espresso", "description": "A strong, full-bodied coffee.", "price": "72.000 VND", "image": "PIC/esp.png"},
    {"name": "Latte", "description": "Creamy and smooth.", "price": "112.500 VND", "image": "PIC/lat.png"},
    {"name": "Cappuccino", "description": "Perfectly foamy and rich.", "price": "100.000 VND", "image": "PIC/cap.png"},
    {"name": "Espresso", "description": "A strong, full-bodied coffee.", "price": "72.000 VND", "image": "PIC/esp.png"},
    {"name": "Latte", "description": "Creamy and smooth.", "price": "112.500 VND", "image": "PIC/lat.png"},
]
 
# Home route to serve the homepage
@app.route("/")
def home():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all records from the SANPHAM table
        cursor.execute("SELECT MASP, TENSP, GIATIEN FROM SANPHAM")
        product_data = cursor.fetchall()

    except mysql.connector.Error as err:
        flash(f"Database error: {err}", 'danger')
        product_data = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

    # Render the view-pro-duct template and pass the product data
    return render_template('index.html', product_data=product_data)

# Define a sample menu_items for the /menu route
menu_items = [
    {"name": "Home", "url": "/"},
    {"name": "Products", "url": "/pro_duct"},
    {"name": "Suppliers", "url": "/supply_er"},
]
 
# API route to fetch the menu
@app.route("/menu", methods=["GET"])
def menu():
    return jsonify(menu_items)
 
# Contact form submission handling
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # Process the form data (e.g., save to database or send email)
    print(f"Received contact form submission: {name}, {email}, {message}")
    return "Message received. Thank you for contacting us!"
 
if __name__ == "__main__":
    app.run(debug=True)