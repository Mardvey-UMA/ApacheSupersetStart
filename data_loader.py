from clickhouse_driver import Client
from faker import Faker
import random
from datetime import datetime, timedelta

client = Client(
    host='clickhouse',
    port=9000,
    user='test',
    password='test',
    database='test'
)

def create_tables():
    client.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id UUID DEFAULT generateUUIDv4(),
        product_name String,
        quantity UInt32,
        price Float64,
        sale_date Date,
        total_amount Float64 MATERIALIZED quantity * price
    ) ENGINE = MergeTree()
    ORDER BY (sale_date, product_name);
    ''')

    client.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id UUID DEFAULT generateUUIDv4(),
        first_name String,
        last_name String,
        position String,
        salary Float64,
        hire_date Date
    ) ENGINE = MergeTree()
    ORDER BY (hire_date, position);
    ''')

    client.execute('''
    CREATE TABLE IF NOT EXISTS cryptocurrency_prices (
        crypto_id UUID DEFAULT generateUUIDv4(),
        crypto_name String,
        price Float64,
        date DateTime
    ) ENGINE = MergeTree()
    ORDER BY (date, crypto_name);
    ''')

    client.execute('''
    CREATE TABLE IF NOT EXISTS geography_data (
        location_id UUID DEFAULT generateUUIDv4(),
        country String,
        city String,
        latitude Float64,
        longitude Float64,
        revenue Float64,
        event_date Date
    ) ENGINE = MergeTree()
    ORDER BY (event_date, country);
    ''')

    client.execute('''
    CREATE TABLE IF NOT EXISTS ml_results (
        experiment_id UUID DEFAULT generateUUIDv4(),
        epoch UInt32,
        roc_auc Float64,
        pr_auc Float64,
        loss Float64,
        accuracy Float64,
        timestamp DateTime
    ) ENGINE = MergeTree()
    ORDER BY (timestamp, epoch);
    ''')

def generate_data(num_records=1000):
    fake = Faker()
    Faker.seed(42)
    random.seed(42)

    sales_data = []
    employees_data = []
    crypto_data = []
    geography_data = []
    ml_data = []

    for _ in range(num_records):
        sales_data.append((
            random.choice(['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']),
            random.randint(1, 10),
            round(random.uniform(50.0, 1000.0), 2),
            (datetime.now() - timedelta(days=random.randint(0, 365))).date()
        ))

    for _ in range(num_records):
        employees_data.append((
            fake.first_name(),
            fake.last_name(),
            random.choice(['Manager', 'Developer', 'Designer', 'Analyst', 'Sales']),
            round(random.uniform(3000, 10000), 2),
            fake.date_this_decade()
        ))

    for _ in range(num_records):
        crypto_data.append((
            random.choice(['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple', 'Dogecoin']),
            round(random.uniform(1000.0, 50000.0), 2),
            datetime.now() - timedelta(days=random.randint(0, 365))
        ))

    for _ in range(num_records):
        geography_data.append((
            fake.country(),
            fake.city(),
            float(fake.latitude()),
            float(fake.longitude()),
            round(random.uniform(1000, 50000), 2),
            fake.date_this_year()
        ))

    for epoch in range(1, 101):
        ml_data.append((
            epoch,
            min(0.8 + epoch/100 + random.uniform(-0.05, 0.05), 1.0),  # ROC-AUC
            min(0.7 + epoch/80 + random.uniform(-0.05, 0.05), 1.0),   # PR-AUC
            max(0.4 - epoch/150 + random.uniform(-0.05, 0.05), 0.01), # Loss
            min(0.75 + epoch/120 + random.uniform(-0.05, 0.05), 1.0), # Accuracy
            datetime.now() - timedelta(hours=100-epoch)
        ))

    return sales_data, employees_data, crypto_data, geography_data, ml_data

if __name__ == "__main__":
    create_tables()
    sales, employees, crypto, geo, ml = generate_data(5000)

    client.execute(
        'INSERT INTO sales (product_name, quantity, price, sale_date) VALUES',
        sales
    )

    client.execute(
        'INSERT INTO employees (first_name, last_name, position, salary, hire_date) VALUES',
        employees
    )

    client.execute(
        'INSERT INTO cryptocurrency_prices (crypto_name, price, date) VALUES',
        crypto
    )

    client.execute(
        'INSERT INTO geography_data (country, city, latitude, longitude, revenue, event_date) VALUES',
        geo
    )

    client.execute(
        'INSERT INTO ml_results (epoch, roc_auc, pr_auc, loss, accuracy, timestamp) VALUES',
        ml
    )

    print("Все данные успешно загружены!")