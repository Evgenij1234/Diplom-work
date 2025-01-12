<?php
$servername = "mysql-container";
$username = "evgen";
$password = "ggghosttt123321";
$dbname = "parser";

// Подключение к базе данных
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверяем подключение
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Database connected successfully";

// Создаем тестовую таблицу
$sql = "CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)";
if ($conn->query($sql) === TRUE) {
    echo "<br>Table 'test_table' created successfully!!!!!!!";
} else {
    echo "<br>Error creating table: " . $conn->error;
}

$conn->close();
?>
