-- Create the database (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS denton_amusement;

-- Use the newly created database
USE denton_amusement;

-- Drop tables if they already exist (for clean re-runs)
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

-- Table for storing user data (both visitors and admin staff)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('visitor', 'admin') DEFAULT 'visitor',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing park services
CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing feedback from visitors
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table for managing tickets (e.g., park entry, rides, events)
CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    service_id INT NOT NULL,
    ticket_type ENUM('entry', 'ride', 'event') NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Insert sample data into the 'users' table (for testing purposes)
INSERT INTO users (username, password, role) VALUES
('admin', 'admin', 'admin'),
('visitor1', 'visitor1', 'visitor'),
('visitor2', 'visitor2', 'visitor');

-- Insert sample data into the 'services' table
INSERT INTO services (name, description) VALUES
('Wheelchair-Friendly Pathways', 'Wide, flat, and accessible paths for wheelchair users.'),
('Sensory-Friendly Zones', 'Quiet zones for visitors with sensory sensitivities.'),
('Assistive Technologies', 'Technologies for visitors with disabilities to enhance their park experience.');

-- Insert sample data into the 'tickets' table
INSERT INTO tickets (user_id, service_id, ticket_type, price) VALUES
(2, 1, 'entry', 25.00),
(3, 2, 'ride', 10.00),
(2, 3, 'event', 15.00);

-- Sample feedback entries
INSERT INTO feedback (user_id, message) VALUES
(2, 'Great accessibility for wheelchair users!'),
(3, 'Loved the sensory-friendly areas, very calming.');
