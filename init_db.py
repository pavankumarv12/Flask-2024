from app import app, db

# Create all tables in the database
with app.app_context():
    db.create_all()  # This will create the 'todo.db' file and all tables in the database
    print("Database tables created successfully.")
