SET datestyle = "ISO, DMY";
show datestyle;
CREATE TABLE USER_DATA(name  TEXT  NOT NULL, street   TEXT NOT NULL,city TEXT, state  TEXT, date  DATE);
\copy user_data from '/tmp/test.csv' DELIMITER  ',' CSV HEADER;