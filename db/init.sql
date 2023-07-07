CREATE TABLE account(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    username CHAR(20),
    password CHAR(30)
);

CREATE TABLE organization(
    id          SERIAL PRIMARY KEY,
    join_code   CHAR(10) UNIQUE,
    name        VARCHAR(50)
);

CREATE TABLE account_organization(
    a_id        INT,
    o_id        INT,
    PRIMARY KEY (a_id, o_id),
    FOREIGN KEY (a_id) REFERENCES account(id),
    FOREIGN KEY (o_id) REFERENCES organization(id),
    role        INT, -- 0 = owner, 1 = member
    join_date   DATE
);

CREATE TABLE project(
    id      SERIAL PRIMARY KEY,
    o_id    INT, -- organization --
    join_code CHAR(10) UNIQUE,
    title VARCHAR(50),
    description VARCHAR(255),
    start_date  DATE,
    end_date    DATE,
    FOREIGN KEY (o_id) REFERENCES organization(id)
);

CREATE TABLE account_project(
    a_id        INT,
    p_id        INT,
    PRIMARY KEY (a_id, p_id),
    FOREIGN KEY (a_id) REFERENCES account(id),
    FOREIGN KEY (p_id) REFERENCES project(id),
    role        INT, -- 0 : owner, 1 : reporter, 2 : member
    join_date   DATE
);

CREATE TABLE task(
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(50),
    description VARCHAR(255),
    priority INT,
    type     INT,
    status   INT,
    score    INT,
    p_id     INT,
    due_to   DATE,
    FOREIGN KEY (p_id) REFERENCES project(id)
);

CREATE TABLE account_task(
    a_id       INT,
    t_id       INT,
    role       INT,
    PRIMARY KEY (a_id, t_id),
    FOREIGN KEY (a_id) REFERENCES account(id),
    FOREIGN KEY (t_id) REFERENCES task(id)
);

INSERT INTO account(username, password, name)
VALUES
('20200563', '20200563', 'Nguyễn Quang Tuấn'),
('20205096', '20205096', 'Đinh Thành Long');


INSERT INTO organization(join_code, name)
VALUES
('HUST', 'HUST');


INSERT INTO account_organization(a_id, o_id, role)
VALUES
(1, 1, 0),
(2, 1, 1);

INSERT INTO project(o_id, join_code, title, description, start_date, end_date)
VALUES
(1, 'ITSSPROJ', 'Gym Management System', 'Bài tập lớn ITSS nhóm', '2023-04-06', '2023-05-10'),
(1, 'UIUXPROJ', 'Task Management Application', 'Bài tập nhóm 40', '2023-03-12', '2023-06-01');


INSERT INTO account_project(a_id, p_id, role)
VALUES
(1, 1, 0),
(2, 1, 1),
(2, 2, 0);


INSERT INTO task(title, priority, status, due_to, p_id)
VALUES
('Thiết kế usecase', 1, 0, '2023-04-20', 1),
('Điền form báo cáo', 2, 1, '2023-05-22', 2),
('Nộp form đánh giá kêt quả', 2, 2, '2023-05-29', 2);
