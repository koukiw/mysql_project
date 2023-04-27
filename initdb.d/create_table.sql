create table project_table(
    project_id int not null auto_increment,
    project_name varchar(50),
    primary key(project_id)
    );

create table demo_table(
    seq int not null auto_increment,
    project_id int not null,
    file_name varchar(100),
    file_format varchar(10),
    text varchar(5000),
    create_date datetime,
    upload_date datetime,
    json_data json,
    primary key(seq),
    FOREIGN KEY (project_id) REFERENCES project_table(project_id)
    );