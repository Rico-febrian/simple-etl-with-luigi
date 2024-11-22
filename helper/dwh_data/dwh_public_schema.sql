-- CREATE TABLE FOR LOAD THE DATA


-- Product data table
CREATE TABLE product_data (
   	product_id SERIAL PRIMARY KEY, 
	product_code VARCHAR,
	product_name TEXT not null,
    stock_availability BOOLEAN,
    condition VARCHAR,
    avg_price FLOAT8,
    price_currency VARCHAR,
    is_sale BOOLEAN,
    brand VARCHAR,
    merchant VARCHAR,
    main_category VARCHAR,
    sub_category VARCHAR,
    asins VARCHAR,
    source_url text,
    latest_date DATE,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Sales data table
create table sales_data (
	sales_id SERIAL PRIMARY KEY,
	product_name text not null,
	actual_price float8,
	discount_price float8,
	price_currency varchar,
	rating_value float8,
	ratings_received int,
	main_category varchar,
	sub_category varchar,
	source_url text,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Scraped data table
create table scraped_data (
	scraped_id SERIAL PRIMARY KEY,
	listing_title text not null,
	price float8,
	price_currency varchar,
	rating float8,
	source_url text,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

