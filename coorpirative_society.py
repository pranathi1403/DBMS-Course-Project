import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# ==========================================================
# MYSQL CONFIGURATION
# ==========================================================

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "pranathi6853"
DATABASE = "CooperativeSocietyDB"


# ==========================================================
# DATABASE SETUP
# ==========================================================

def setup_database():

    # Connect to MySQL
    db = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )

    cursor = db.cursor()

    # Create database
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DATABASE}"
    )

    cursor.close()
    db.close()

    # Connect to created database
    db = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DATABASE
    )

    cursor = db.cursor()

    # ------------------------------------------------------
    # MEMBERS TABLE
    # ------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            gender VARCHAR(20),
            phone VARCHAR(15),
            address VARCHAR(200),
            join_date DATE
        )
    """)

    # ------------------------------------------------------
    # SAVINGS TABLE
    # ------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings (
            saving_id INT PRIMARY KEY AUTO_INCREMENT,
            member_id INT,
            amount DECIMAL(10,2),
            transaction_date DATE,
            FOREIGN KEY (member_id)
            REFERENCES members(member_id)
            ON DELETE CASCADE
        )
    """)

    # ------------------------------------------------------
    # LOANS TABLE
    # ------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INT PRIMARY KEY AUTO_INCREMENT,
            member_id INT,
            loan_amount DECIMAL(10,2),
            loan_date DATE,
            status VARCHAR(30),
            FOREIGN KEY (member_id)
            REFERENCES members(member_id)
            ON DELETE CASCADE
        )
    """)

    # ------------------------------------------------------
    # SHARES TABLE
    # ------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shares (
            share_id INT PRIMARY KEY AUTO_INCREMENT,
            member_id INT,
            shares_count INT,
            share_value DECIMAL(10,2),
            FOREIGN KEY (member_id)
            REFERENCES members(member_id)
            ON DELETE CASCADE
        )
    """)

    db.commit()

    # ======================================================
    # INSERT SAMPLE MEMBERS
    # ======================================================

    cursor.execute("SELECT COUNT(*) FROM members")
    count = cursor.fetchone()[0]

    if count == 0:

        members = [
            ("Pranathi", "Female", "9876543210", "Hyderabad", "2026-01-10"),
            ("Ananya", "Female", "9876543211", "Secunderabad", "2026-01-15"),
            ("Sufiyan", "Male", "9876543212", "Hyderabad", "2026-02-05"),
            ("Rishil", "Male", "9876543213", "Gachibowli", "2026-02-20"),
            ("Rahul", "Male", "9876543214", "Kukatpally", "2026-03-01"),
            ("Sneha", "Female", "9876543215", "Madhapur", "2026-03-12"),
            ("Arjun", "Male", "9876543216", "Miyapur", "2026-03-18"),
            ("Keerthi", "Female", "9876543217", "Kondapur", "2026-04-02"),
            ("Varun", "Male", "9876543218", "Banjara Hills", "2026-04-15"),
            ("Divya", "Female", "9876543219", "Ameerpet", "2026-05-01")
        ]

        cursor.executemany("""
            INSERT INTO members
            (name, gender, phone, address, join_date)
            VALUES (%s, %s, %s, %s, %s)
        """, members)

        db.commit()

    # ======================================================
    # INSERT SAMPLE SAVINGS
    # ======================================================

    cursor.execute("SELECT COUNT(*) FROM savings")
    count = cursor.fetchone()[0]

    if count == 0:

        savings = [
            (1, 5000, "2026-09-01"),
            (2, 3000, "2026-09-02"),
            (3, 4500, "2026-09-03"),
            (4, 6000, "2026-09-04"),
            (5, 2500, "2026-09-05"),
            (6, 7000, "2026-09-06"),
            (7, 3500, "2026-09-07"),
            (8, 5500, "2026-09-08"),
            (9, 4000, "2026-09-09"),
            (10, 6500, "2026-09-10")
        ]

        cursor.executemany("""
            INSERT INTO savings
            (member_id, amount, transaction_date)
            VALUES (%s, %s, %s)
        """, savings)

        db.commit()

    # ======================================================
    # INSERT SAMPLE LOANS
    # ======================================================

    cursor.execute("SELECT COUNT(*) FROM loans")
    count = cursor.fetchone()[0]

    if count == 0:

        loans = [
            (1, 20000, "2026-06-01", "Approved"),
            (2, 15000, "2026-06-10", "Pending"),
            (3, 30000, "2026-07-05", "Approved"),
            (4, 10000, "2026-07-15", "Completed"),
            (5, 25000, "2026-07-20", "Approved"),
            (6, 18000, "2026-08-01", "Pending"),
            (7, 12000, "2026-08-10", "Approved"),
            (8, 22000, "2026-08-20", "Completed")
        ]

        cursor.executemany("""
            INSERT INTO loans
            (member_id, loan_amount, loan_date, status)
            VALUES (%s, %s, %s, %s)
        """, loans)

        db.commit()

    # ======================================================
    # INSERT SAMPLE SHARES
    # ======================================================

    cursor.execute("SELECT COUNT(*) FROM shares")
    count = cursor.fetchone()[0]

    if count == 0:

        shares = [
            (1, 10, 1000),
            (2, 5, 500),
            (3, 15, 1500),
            (4, 8, 800),
            (5, 12, 1200),
            (6, 20, 2000),
            (7, 7, 700),
            (8, 14, 1400),
            (9, 10, 1000),
            (10, 18, 1800)
        ]

        cursor.executemany("""
            INSERT INTO shares
            (member_id, shares_count, share_value)
            VALUES (%s, %s, %s)
        """, shares)

        db.commit()

    cursor.close()
    db.close()


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def connect_db():

    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DATABASE
    )


# ==========================================================
# MAIN WINDOW
# ==========================================================

root = tk.Tk()

root.title(
    "Cooperative Society Membership and Savings Management System"
)

root.geometry("1250x750")

root.configure(bg="#F4F6F8")


# ==========================================================
# HEADER
# ==========================================================

header = tk.Frame(
    root,
    bg="#17365D",
    height=80
)

header.pack(
    side="top",
    fill="x"
)

header_title = tk.Label(
    header,
    text="COOPERATIVE SOCIETY MEMBERSHIP AND SAVINGS MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#17365D",
    fg="white"
)

header_title.pack(pady=22)


# ==========================================================
# SIDEBAR
# ==========================================================

sidebar = tk.Frame(
    root,
    bg="#1F4E78",
    width=230
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# ==========================================================
# CONTENT AREA
# ==========================================================

content = tk.Frame(
    root,
    bg="#F4F6F8"
)

content.pack(
    side="right",
    fill="both",
    expand=True
)


# ==========================================================
# CLEAR CONTENT
# ==========================================================

def clear_content():

    for widget in content.winfo_children():
        widget.destroy()


# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard():

    clear_content()

    title = tk.Label(
        content,
        text="Dashboard",
        font=("Arial", 28, "bold"),
        bg="#F4F6F8",
        fg="#17365D"
    )

    title.pack(pady=30)

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM members"
    )

    total_members = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COALESCE(SUM(amount),0) FROM savings"
    )

    total_savings = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COALESCE(SUM(loan_amount),0) FROM loans"
    )

    total_loans = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COALESCE(SUM(share_value),0) FROM shares"
    )

    total_shares = cursor.fetchone()[0]

    cursor.close()
    db.close()

    cards_frame = tk.Frame(
        content,
        bg="#F4F6F8"
    )

    cards_frame.pack(pady=20)

    create_card(
        cards_frame,
        "TOTAL MEMBERS",
        total_members,
        0
    )

    create_card(
        cards_frame,
        "TOTAL SAVINGS",
        f"₹{total_savings:,.2f}",
        1
    )

    create_card(
        cards_frame,
        "TOTAL LOANS",
        f"₹{total_loans:,.2f}",
        2
    )

    create_card(
        cards_frame,
        "TOTAL SHARES",
        f"₹{total_shares:,.2f}",
        3
    )

    info = tk.Label(
        content,
        text="Welcome to Cooperative Society Management System",
        font=("Arial", 16),
        bg="#F4F6F8",
        fg="#555555"
    )

    info.pack(pady=40)


# ==========================================================
# DASHBOARD CARD
# ==========================================================

def create_card(parent, heading, value, column):

    card = tk.Frame(
        parent,
        bg="white",
        width=210,
        height=150,
        relief="solid",
        bd=1
    )

    card.grid(
        row=0,
        column=column,
        padx=12
    )

    card.grid_propagate(False)

    tk.Label(
        card,
        text=heading,
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(30, 10))

    tk.Label(
        card,
        text=value,
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#17365D"
    ).pack()


# ==========================================================
# GENERIC TABLE FUNCTION
# ==========================================================

def display_table(
    page_title,
    columns,
    query
):

    clear_content()

    title = tk.Label(
        content,
        text=page_title,
        font=("Arial", 26, "bold"),
        bg="#F4F6F8",
        fg="#17365D"
    )

    title.pack(pady=20)

    table_frame = tk.Frame(
        content,
        bg="white"
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    # Headings
    for column in columns:

        tree.heading(
            column,
            text=column
        )

        tree.column(
            column,
            width=150,
            anchor="center"
        )

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # Get database records
    try:

        db = connect_db()
        cursor = db.cursor()

        cursor.execute(query)

        records = cursor.fetchall()

        for record in records:

            tree.insert(
                "",
                "end",
                values=record
            )

        cursor.close()
        db.close()

    except mysql.connector.Error as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ==========================================================
# MEMBERS PAGE
# ==========================================================

def members_page():

    display_table(
        "Member Management",

        (
            "Member ID",
            "Name",
            "Gender",
            "Phone",
            "Address",
            "Join Date"
        ),

        """
        SELECT
            member_id,
            name,
            gender,
            phone,
            address,
            join_date
        FROM members
        ORDER BY member_id
        """
    )


# ==========================================================
# SAVINGS PAGE
# ==========================================================

def savings_page():

    display_table(
        "Savings Management",

        (
            "Saving ID",
            "Member ID",
            "Amount",
            "Transaction Date"
        ),

        """
        SELECT
            saving_id,
            member_id,
            amount,
            transaction_date
        FROM savings
        ORDER BY saving_id
        """
    )


# ==========================================================
# LOANS PAGE
# ==========================================================

def loans_page():

    display_table(
        "Loan Management",

        (
            "Loan ID",
            "Member ID",
            "Loan Amount",
            "Loan Date",
            "Status"
        ),

        """
        SELECT
            loan_id,
            member_id,
            loan_amount,
            loan_date,
            status
        FROM loans
        ORDER BY loan_id
        """
    )


# ==========================================================
# SHARES PAGE
# ==========================================================

def shares_page():

    display_table(
        "Share Management",

        (
            "Share ID",
            "Member ID",
            "Shares Count",
            "Share Value"
        ),

        """
        SELECT
            share_id,
            member_id,
            shares_count,
            share_value
        FROM shares
        ORDER BY share_id
        """
    )


# ==========================================================
# SIDEBAR BUTTON
# ==========================================================

def sidebar_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        bg="#1F4E78",
        fg="white",
        activebackground="#2E75B6",
        activeforeground="white",
        relief="flat",
        bd=0,
        width=22,
        height=2,
        cursor="hand2"
    )

    button.pack(
        pady=5
    )


# ==========================================================
# SIDEBAR MENU
# ==========================================================

sidebar_button(
    "🏠  Dashboard",
    dashboard
)

sidebar_button(
    "👤  Members",
    members_page
)

sidebar_button(
    "💰  Savings",
    savings_page
)

sidebar_button(
    "🏦  Loans",
    loans_page
)

sidebar_button(
    "📊  Shares",
    shares_page
)


# ==========================================================
# EXIT BUTTON
# ==========================================================

tk.Button(
    sidebar,
    text="Exit",
    command=root.destroy,
    font=("Arial", 12, "bold"),
    bg="#C00000",
    fg="white",
    activebackground="#900000",
    relief="flat",
    width=22,
    height=2,
    cursor="hand2"
).pack(
    side="bottom",
    pady=25
)


# ==========================================================
# START PROGRAM
# ==========================================================

try:

    setup_database()

    dashboard()

    root.mainloop()

except mysql.connector.Error as error:

    messagebox.showerror(
        "MySQL Connection Error",
        "Could not connect to MySQL.\n\n"
        + str(error)
    )