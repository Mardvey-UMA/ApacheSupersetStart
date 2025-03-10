from clickhouse_driver import Client
from faker import Faker
import random
from datetime import datetime, timedelta

# Используем имя сервиса из docker-compose
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
        sale_date DateTime,
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


def generate_data(num_records=1000):
    fake = Faker()
    Faker.seed(42)
    random.seed(42)

    sales_data = []
    employees_data = []
    crypto_data = []

    for _ in range(num_records):
        sales_data.append((
            random.choice(['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']),
            random.randint(1, 10),
            round(random.uniform(50.0, 1000.0), 2),
            datetime.now() - timedelta(days=random.randint(0, 365))
        ))

        employees_data.append((
            fake.first_name(),
            fake.last_name(),
            random.choice(['Manager', 'Developer', 'Designer', 'Analyst', 'Sales']),
            round(random.uniform(3000, 10000), 2),
            fake.date_this_decade()
        ))

        crypto_data.append((
            random.choice(['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple', 'Dogecoin']),
            round(random.uniform(1000.0, 50000.0), 2),
            datetime.now() - timedelta(days=random.randint(0, 365))
        ))

    return sales_data, employees_data, crypto_data


if __name__ == "__main__":
    create_tables()
    sales, employees, crypto = generate_data(5000)

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

    print("Данные успешно загружены!")