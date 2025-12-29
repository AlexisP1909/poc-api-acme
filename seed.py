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
            pickup_datetime TEXT,
            delivery_datetime TEXT,
            equipment_type TEXT,
            loadboard_rate REAL,
            notes TEXT,
            weight INTEGER,
            commodity_type TEXT,
            num_of_pieces INTEGER,
            miles INTEGER,
            dimensions TEXT
        )
    """))

    conn.execute(text("DELETE FROM load"))

    conn.execute(text("""
        INSERT INTO load (origin, destination, pickup_datetime, delivery_datetime, equipment_type,
        loadboard_rate, notes, weight, commodity_type, num_of_pieces, miles, dimensions) VALUES 
        ('New York, NY', 'Los Angeles, CA', '2024-07-01 08:00', '2024-07-05 17:00', 'Dry Van', 2500.00, 'Handle with care', 20000, 'Electronics', 10, 2800, '48x102x110'),
        ('Chicago, IL', 'Houston, TX', '2024-07-02 09:00', '2024-07-04 18:00', 'Refrigerated', 1800.00, 'Keep refrigerated', 15000, 'Perishables', 8, 1080, '48x96x110'),
        ('Miami, FL', 'Atlanta, GA', '2024-07-03 07:30', '2024-07-03 15:30', 'Flatbed', 1200.00, 'Secure load properly', 10000, 'Construction Materials', 5, 660, '48x102x110'),
        ('Seattle, WA', 'Denver, CO', '2024-07-04 10:00', '2024-07-06 20:00', 'Dry Van', 2200.00, 'Fragile items', 18000, 'Furniture', 12, 1300, '48x102x110'),
        ('Boston, MA', 'Philadelphia, PA', '2024-07-05 06:00', '2024-07-05 14:00', 'Refrigerated', 900.00, 'Keep upright', 8000, 'Dairy Products', 6, 310, '48x96x110')
    """))
