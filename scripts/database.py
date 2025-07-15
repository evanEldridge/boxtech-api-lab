import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

# Sample data for testing
data = {
    "container_number": "MSCU1234567",
    "container_type": "40HC",
    "container_size": "40",
    "tare_weight": 3750.0,
    "max_gross_weight": 30480.0
}

def insert_or_update_container(data):
	conn = pyodbc.connect(os.getenv("DB_CONN_STR"))
    cursor = conn.cursor()

     # Ensure table exists
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='container_info' AND xtype='U')
    CREATE TABLE container_info (
        id INT IDENTITY PRIMARY KEY,
        container_number NVARCHAR(20) UNIQUE NOT NULL,
        container_type NVARCHAR(50),
        container_size NVARCHAR(10),
        tare_weight FLOAT,
        max_gross_weight FLOAT,
        retrieved_at DATETIME DEFAULT GETDATE()
    )
    """)

	# Check if container already exists
	cursor.execute("""SELECT id FROM container_info WHERE container_number = ?""", data["container_number"])
    existing = cursor.fetchone()

	# If exists, update fields
	if existing:
		cursor.execute("""UPDATE container_info SET container_type=?, container_size=?, tare_weight=?, max_gross_weight=?""", data["container_type"], data["container_size"], data["tare_weight"], data["max_gross_weight"])
	
	# Else, insert new row
	else:
		cursor.execute("""INSERT INTO container_info (container_number, container_type, container_size, tare_weight, max_gross_weight) VALUES (?, ?, ?, ?, ?)""", data["container_number"], data["container_type"], data["container_size"], data["tare_weight"], data["max_gross_weight"])

	conn.commit()
    cursor.close()
    conn.close()

def query_all_containers():
	pass
	# SELECT * FROM container_info
	# Pretty print or tabulate results

def query_container_by_number(container_number):
	pass
	# SELECT * FROM container_info WHERE container_number = ?
	# Pretty print result
