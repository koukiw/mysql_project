
create table demo_table(
    seq int not null auto_increment,
    project_name varchar(50),
    path varchar(200),
    file_name varchar(100),
    file_format varchar(10),
    text varchar(5000),
    create_date datetime,
    upload_date datetime,
    json_data json,
    primary key(seq)
    );

create table text_table(
    seq_text int not null auto_increment,
    project_name varchar(50),
    text_data varchar(5000),
    primary key(seq_text)
    );