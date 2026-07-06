CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    fullname VARCHAR(100) NOT NULL,

    email VARCHAR(120) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    phone VARCHAR(20),

    age INT,

    gender ENUM('Male','Female','Other'),

    blood_group VARCHAR(10),

    height DECIMAL(5,2),

    weight DECIMAL(5,2),

    allergies TEXT,

    chronic_diseases TEXT,

    emergency_contact VARCHAR(20),

    profile_image VARCHAR(255) DEFAULT 'default.png',

    is_admin BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP

);
CREATE TABLE medicines (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    medicine_name VARCHAR(100) NOT NULL,

    dosage VARCHAR(50) NOT NULL,

    medicine_type VARCHAR(50),

    frequency VARCHAR(50),

    food_instruction VARCHAR(30),

    reminder_time TIME,

    start_date DATE,

    end_date DATE,

    notes TEXT,

    status ENUM('Pending','Taken','Missed')
    DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE reminders (

    id INT AUTO_INCREMENT PRIMARY KEY,

    medicine_id INT NOT NULL,

    reminder_time TIME,

    reminder_date DATE,

    status ENUM('Pending','Sent','Completed')
    DEFAULT 'Pending',

    FOREIGN KEY(medicine_id)
    REFERENCES medicines(id)
    ON DELETE CASCADE

);
CREATE TABLE water_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    glasses INT DEFAULT 0,

    goal INT DEFAULT 8,

    log_date DATE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE sleep_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    sleep_time TIME,

    wake_time TIME,

    total_hours DECIMAL(4,2),

    sleep_quality VARCHAR(20),

    log_date DATE,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE bmi_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    height DECIMAL(5,2),

    weight DECIMAL(5,2),

    bmi DECIMAL(5,2),

    category VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE chat_history (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    user_message TEXT,

    ai_response TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE insights (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    title VARCHAR(200),

    description TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE notifications (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    title VARCHAR(150),

    message TEXT,

    status ENUM('Unread','Read')
    DEFAULT 'Unread',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
CREATE TABLE activity_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    activity VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);
