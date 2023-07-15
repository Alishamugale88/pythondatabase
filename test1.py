import pymysql.cursors
# Connect to the database
name=input("Please Enter your Name : ")
age=input("Please Enter your Age : ")
contact=input("Please Enter your Mobile Number : ")

# imp ===  install package at terminal- 'python -m pip install PyMySQL'.

#get the code from pymysql link
try:
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             port=3307,
                             database='python_db',
                             cursorclass=pymysql.cursors.DictCursor)


    with connection:
      with connection.cursor() as cursor:
        # Create a new record
         sql = "INSERT INTO `student` (`Name`, `Age`, `Contact`) VALUES (%s, %s,%s)"
         cursor.execute(sql, (name,age,contact))
 
    # connection is not autocommit by default. So you must commit to save
    # your changes.
         connection.commit()

         print("User Register Sucessfully")
except:
      print("Error")