from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:///./app.db",
    connect_args={"check_same_thread": False}
)

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS load (
            load_id INTEGER PRIMARY KEY,
            origin TEXT,
            destination TEXT,
            picku
        )
    """))

    conn.execute(text("DELETE FROM load"))

    conn.execute(text("""
        INSERT INTO load (origin, destination, pickup) VALUES
        ('New York', 'Los Angeles', '2024-06-01'),
        ('Chicago', 'Houston', '2024-06-02'),
        ('San Francisco', 'Seattle', '2024-06-03')
    """))
