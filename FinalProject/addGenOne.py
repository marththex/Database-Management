import pymysql

# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
# prepare a cursor object using cursor() method
cursor = db.cursor()

#Bulubasaur
sql = """INSERT INTO POKEMON(ID,
      PNAME, ABOUT, DESCRIPTION)
      VALUES (001, 'Bulbasaur', 'Seed Pokemon', '')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (001, 'GRASS')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (001, 'POISON')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (001, %s, .059, 15.2)"""
height = "2\'04\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("001 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (001, 'Overgrow')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (001, 45, 59, 49, 45, 65, 65)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (001, 002)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (001, 1, 2, .5, .5, .25, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, .5)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("001 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ivysaur
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (002, 'Ivysaur', 'Seed Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (002, 'GRASS')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (002, 'POISON')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (002, %s, .059, 28.7)"""
height = "3\'03\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("002 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (002, 'Overgrow')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (002, 60, 62, 63, 60, 80, 80)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (002, 003)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (002, 1, 2, .5, .5, .25, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, .5)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("002 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Venusaur
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (003, 'Venusaur', 'Seed Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (003, 'GRASS')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (003, 'POISON')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (003, %s, .059, 220.5)"""
height = "6\'07\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("003 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (003, 'Overgrow')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (003, 80, 82, 83, 80, 100, 100)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (003, 1, 2, .5, .5, .25, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, .5)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("003 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Charmander
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (004, 'Charmander', 'Lizard Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (004, 'FIRE')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (004, %s, .059, 18.7)"""
height = "2\'00\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("004 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (004, 'Blaze')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (004, 39, 52, 43, 65, 60, 50)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (004, 005)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (004, 1, .5, 2, 1, .5, .5, 1, 1, 2, 1, 1, .5, 2, 1, 1 ,1, .5, .5)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("004 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Charmeleon
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (005, 'Charmeleon', 'Flame Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (005, 'FIRE')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (005, %s, .059, 41.9)"""
height = "3\'07\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("005 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (005, 'Blaze')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (005, 58, 64, 58, 80, 80, 65)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (005, 006)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (005, 1, .5, 2, 1, .5, .5, 1, 1, 2, 1, 1, .5, 2, 1, 1 ,1, .5, .5)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("005 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Charizard
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (006, 'Charizard', 'Flame Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (006, 'FIRE')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

sql = """INSERT INTO TYPES (ID,
      TYPE)
      VALUES (006, 'FLYING')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (006, %s, .059, 199.5)"""
height = "5\'07\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("006 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (006, 'Blaze')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (006, 78, 84, 78, 100, 109, 85)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (006, 1, .5, 2, 2, .25, 1, .5, 1, 0, 1, 1, .25, 4, 1, 1, 1, .25, .25)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("006 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Squirtle
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (007, 'Squirtle', 'Tiny Turtle Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
          VALUES (007, 'WATER')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (007, %s, .059, 19.8)"""
height = "1\'08\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("007 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (007, 'Torrent')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (007, 44, 48, 65, 43, 50, 64)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (007, 008)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (007, 1, .5, .5, 2, 2, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("007 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Wartortle
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (008, 'Wartortle', 'Turtle Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
      TYPE)
          VALUES (008, 'WATER')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Profile
sql = """INSERT INTO PROFILE (ID,
      HEIGHT, CATCHRATE, WEIGHT)
      VALUES (008, %s, .059, 49.6)"""
height = "3\'03\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("008 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (008, 'Torrent')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (008, 59, 63, 80, 58, 65, 80)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Evolutions
sql = """INSERT INTO EVOLUTIONS (ID,
      EVOLVESTO)
      VALUES (008, 009)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 EVOLUTION ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (008, 1, .5, .5, 2, 2, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("008 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

#Blastoise
sql = """INSERT INTO POKEMON(ID,
       PNAME, ABOUT, DESCRIPTION)
       VALUES (009, 'Blastoise', 'Shellfish Pokemon', '')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("009 POKEMON CREATED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Type
sql = """INSERT INTO TYPES (ID,
        TYPE)
              VALUES (009, 'WATER')"""
try:
     # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("009 TYPE ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Profile
sql = """INSERT INTO PROFILE (ID,
        HEIGHT, CATCHRATE, WEIGHT)
        VALUES (009, %s, .059, 188.5)"""
height = "5\'03\""

try:
    # Execute the SQL command
    cursor.execute(sql, height)
    # Commit your changes in the database
    db.commit()
    print("009 Profile ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# Ability
sql = """INSERT INTO ABILITY (ID,
      ABILITY)
      VALUES (009, 'Torrent')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("009 Ability ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

 # Stats
sql = """INSERT INTO STATS (ID,
      HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
      VALUES (009, 79, 83, 100, 78, 85, 105)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("009 Stats ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# DAMAGEWHENATTACKED
sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
      NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO, 
      FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
      VALUES (009, 1, .5, .5, 2, 2, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("009 DAMAGEWHENATTACKED ADDED")
except:
    # Rollback in case there is any error
    db.rollback()
    print("ERROR: ROLLBACK")

# disconnect from server
    db.close()