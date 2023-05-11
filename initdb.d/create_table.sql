create table demo_table(
    seq int not null auto_increment,
    project_name varchar(50),
    path varchar(200),
    file_name varchar(100),
    file_format varchar(10),
    create_date datetime,
    upload_date datetime,
    json_data json,
    primary key(seq)
    );
    
create table text_table(
    seq int not null auto_increment,
    project_name varchar(50),
    path varchar(200),
    file_name varchar(100),
    text varchar(15000) CHARACTER SET utf8mb4,
    primary key(seq)
    );