<?php
$mysqli = new mysqli("db", "evgen", "ggghosttt123321", "db_parse");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

echo "Connected successfully to the database!";
?>
