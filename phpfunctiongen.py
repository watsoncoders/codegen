def generate_php_code(scenario):
    php_code = ""
    
    if scenario == "echo a table from the movies database":
        php_code = """<?php
$connection = mysqli_connect('localhost', 'root', 'password');
mysqli_select_db($connection, 'movies');

$query = "SELECT * FROM movies";
$result = mysqli_query($connection, $query);

echo "<table>";

while($row = mysqli_fetch_array($result)){
    echo "<tr><td>" . $row['Name'] . "</td></tr>";
}

echo "</table>";

mysqli_close($connection);
?>
"""
    elif scenario == "connect to a MySQL database":
        php_code = """<?php
$connection = mysqli_connect('localhost', 'root', 'password');
if (!$connection) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($connection);
?>
"""
    elif scenario == "fetch and display user data":
        php_code = """<?php
$connection = mysqli_connect('localhost', 'root', 'password');
mysqli_select_db($connection, 'users_db');

$query = "SELECT * FROM users";
$result = mysqli_query($connection, $query);

while($row = mysqli_fetch_array($result)){
    echo "User: " . $row['username'] . "<br>";
}

mysqli_close($connection);
?>
"""
    elif scenario == "insert a new record into a table":
        php_code = """<?php
$connection = mysqli_connect('localhost', 'root', 'password');
mysqli_select_db($connection, 'my_database');

$name = 'John Doe';
$age = 30;

$query = "INSERT INTO my_table (name, age) VALUES ('$name', $age)";
if (mysqli_query($connection, $query)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $query . "<br>" . mysqli_error($connection);
}

mysqli_close($connection);
?>
"""
    else:
        php_code = "Scenario not recognized. Please provide a valid scenario."
    
    return php_code

def main():
    print("Enter a scenario to generate PHP code:")
    print("1. echo a table from the movies database")
    print("2. connect to a MySQL database")
    print("3. fetch and display user data")
    print("4. insert a new record into a table")
    
    choice = input("Enter your choice: ").strip().lower()
    
    php_code = generate_php_code(choice)
    print("\nGenerated PHP Code:")
    print(php_code)

if __name__ == "__main__":
    main()
