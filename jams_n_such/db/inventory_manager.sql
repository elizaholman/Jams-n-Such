DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS vendors;

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    buying_price INT,
    selling_price INT,
    stock_quantity INT,
    low_stock BOOLEAN,
    out_of_stock BOOLEAN,
    vendor_id INT NOT NULL REFERENCES vendors(id)
);
