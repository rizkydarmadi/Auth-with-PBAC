-- Drop table if exist
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS role_permissions;

-- Users table
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Roles table
CREATE TABLE roles (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Permissions table
CREATE TABLE permissions (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- User Roles table (many-to-many relationship between users and roles)
CREATE TABLE user_roles (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);

-- Role Permissions table (many-to-many relationship between roles and permissions)
CREATE TABLE role_permissions (
    role_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (permission_id) REFERENCES permissions(id),
    PRIMARY KEY (role_id, permission_id)
);

-- Inserting a user
INSERT INTO users (id, username, password, email) VALUES (1, 'johndoe', 'password123', 'johndoe@example.com');

-- Inserting a role
INSERT INTO roles (id, name) VALUES (1, 'admin');

-- Inserting a permission
INSERT INTO permissions (id, name) VALUES (1, 'create_users');

-- Assigning a role to a user
INSERT INTO user_roles (user_id, role_id) VALUES (1, 1);

-- Assigning a permission to a role
INSERT INTO role_permissions (role_id, permission_id) VALUES (1, 1);
