import pymysql

#Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")

#prepare a cursor object using cursor() method
cursor = db.cursor()

#POKEMON TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS POKEMON")
#Create table as per requirement
sql = """CREATE TABLE POKEMON (
   ID INT PRIMARY KEY,
   PNAME  VARCHAR(20) NOT NULL,
   ABOUT VARCHAR(20),  
   DESCRIPTION VARCHAR(255) )"""
cursor.execute(sql)

#TYPES TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS TYPES")
#Create table as per requirement
sql = """CREATE TABLE TYPES (
   ID INT,
   TYPE VARCHAR(15) NOT NULL)"""
cursor.execute(sql)

#PROFILE TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS PROFILE")
#Create table as per requirement
sql = """CREATE TABLE PROFILE (
   ID INT PRIMARY KEY,
   HEIGHT  VARCHAR(6) NOT NULL,
   CATCHRATE FLOAT(1) NOT NULL,  
   WEIGHT FLOAT(3) NOT NULL)"""
cursor.execute(sql)

#ABILITIES TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS ABILITY")
#Create table as per requirement
sql = """CREATE TABLE ABILITY (
   ID INT PRIMARY KEY,
   ABILITY VARCHAR(20) NOT NULL)"""
cursor.execute(sql)

#STATS TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS STATS")
#Create table as per requirement
sql = """CREATE TABLE STATS (
   ID INT PRIMARY KEY,
   HP INT(250) NOT NULL,
   ATTACK INT(200) NOT NULL,  
   DEFENSE INT(200) NOT NULL,
   SPEED INT(200) NOT NULL,
   SPATK INT(200) NOT NULL,
   SPDEF INT(200) NOT NULL )"""
cursor.execute(sql)

#EVOLUTIONS TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EVOLUTIONS")
#Create table as per requirement
sql = """CREATE TABLE EVOLUTIONS (
   ID INT,
   EVOLVESTO INT)"""
cursor.execute(sql)

#DAMAGEWHENATTACKED TABLE
#Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS DAMAGEWHENATTACKED")
#Create table as per requirement
sql = """CREATE TABLE DAMAGEWHENATTACKED (
   ID INT,
   NOR FLOAT(10),
   FIR FLOAT(10),
   WAT FLOAT(10),
   ELE FLOAT(10),
   GRA FLOAT(10),
   ICE FLOAT(10),
   FIG FLOAT(10),
   POI FLOAT(10),
   GRO FLOAT(10),
   FLY FLOAT(10),
   PSY FLOAT(10),
   BUG FLOAT(10),
   ROC FLOAT(10),
   GHO FLOAT(10),
   DRA FLOAT(10),
   DAR FLOAT(10),
   STE FLOAT(10),
   FAI FLOAT(10))"""
cursor.execute(sql)

# disconnect from server
db.close()
