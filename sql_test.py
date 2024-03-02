import mysql.connector


create_tables = """
                CREATE TABLE `Posts` (
                `post_id` int PRIMARY KEY,
                `post_url` varchar(255),
                `platform_id` int
                );

                CREATE TABLE `Platforms` (
                `platform_id` int PRIMARY KEY,
                `platform_name` varchar(255)
                );

                CREATE TABLE `Comments` (
                `comment_id` int PRIMARY KEY,
                `comment_content` varchar(255),
                `post_id` int,
                `sentiment` varchar(255)
                );

                ALTER TABLE `Posts` ADD FOREIGN KEY (`platform_id`) REFERENCES `Platforms` (`platform_id`);

                ALTER TABLE `Comments` ADD FOREIGN KEY (`post_id`) REFERENCES `Posts` (`post_id`);
                """
                
insert_platforms = """
                    INSERT INTO Platforms (platform_id, platform_name)
                    VALUES (DEFAULT, 'Instagram');
                    
                    """
# Replace with your actual database credentials
insert_comment = """
                INSERT INTO comments (comment_id, comment_content, post_id, sentiment) VALUES (2, 'wow amazing', 1, 'positive');
                """

host = "localhost"
user = 'root'
password = '1234'
database = 'telaverge'
# Create a connection
db_connection = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)

# Now you can use the connection to execute queries
# For example:
cursor = db_connection.cursor()
print('connection sucessful')
cursor.execute(insert_comment)
result = cursor.fetchall()
print(result)
# Close the connection
db_connection.close()
