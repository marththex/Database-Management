import pymysql
import prettytable
import csv
from flask import Flask, render_template, url_for, Blueprint, request, g, redirect, url_for, send_file

bp = Blueprint('pokedex', __name__)


@bp.route("/index")
#1. Print/display records from your database/tables.
def printPokemon():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute(
        'SELECT *'
        'FROM POKEMON'
    )
    results = cursor.fetchall()

    with open('Pokemon.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         for row in results:
             writer.writerow(row)
         print("Pokemon CSV Created")
    # disconnect from server
    db.close()
    return render_template('index.html', posts=results)

@bp.route('/getPokemon')
def getPokemon():
    return send_file('Pokemon.csv',
                     mimetype='text/csv',
                     attachment_filename='Pokemon.csv',
                     as_attachment=True)

@bp.route("/profile")
def printProfile():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """SELECT P.ID, N.PNAME, P.HEIGHT,P.CATCHRATE, P.WEIGHT
                FROM PROFILE P, POKEMON N
                WHERE P.ID = N.ID"""

    cursor.execute(sql)

    results = cursor.fetchall()


    with open("Profile.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
            print("Profile CSV Created")

    # disconnect from server
    db.close()
    return render_template('profile.html', posts=results)

@bp.route('/getProfile')
def getProfile():
    return send_file('Profile.csv',
                     mimetype='text/csv',
                     attachment_filename='Profile.csv',
                     as_attachment=True)

@bp.route("/stats")
def printStats():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """SELECT S.ID, N.PNAME, S.HP, S.ATTACK, S.DEFENSE, S.SPEED, S.SPATK, S.SPDEF
                 FROM STATS S, POKEMON N
                 WHERE S.ID = N.ID"""

    cursor.execute(sql)

    results = cursor.fetchall()

    with open("Stats.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
            print("Stats CSV Created")

    # disconnect from server
    db.close()
    return render_template('stats.html', posts=results)

@bp.route('/getStats')
def getStats():
    return send_file('Stats.csv',
                     mimetype='text/csv',
                     attachment_filename='Stats.csv',
                     as_attachment=True)

@bp.route("/damage")
def printDamage():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """SELECT D.ID, N.PNAME, D.NOR, D.FIR, D.WAT, D.ELE, D.GRA, D.ICE, D.FIG, D.POI, D.GRO, D.FLY, D.PSY, D.BUG, D.ROC, D.GHO, D.DRA, D.DAR, D.STE, D.FAI
                 FROM DAMAGEWHENATTACKED D, POKEMON N
                 WHERE D.ID = N.ID"""

    cursor.execute(sql)

    results = cursor.fetchall()

    with open("Damage.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
        print("Damage CSV Created")

    # disconnect from server
    db.close()

    return render_template('damage.html', posts=results)

@bp.route('/getDamage')
def getDamage():
    return send_file('Damage.csv',
                     mimetype='text/csv',
                     attachment_filename='Damage.csv',
                     as_attachment=True)

@bp.route("/filter")
#2. Filter
def filter():
    return render_template('filter.html')
    print("How would you like to filter the Pokemon data?")
    print("1. By Name")
    print("2. By Type")
    print("3. By Height")
    print("4. By Catch Rate")
    print("5. By Weight")
    print("6. By HP")
    print("7. By Attack")
    print("8. By Defense")
    print("9. By Speed")
    print("10. By Special Attack")
    print("11. By Special Defense")
    print("12. By Ability")
    print("13. By Evolution")
    selection = input()

    if selection == "1":
        printName()
    elif selection == "2":
        printType()
    elif selection == "3":
        printHeight()
    elif selection == "4":
        printCatchRate()
    elif selection == "5":
        printWeight()
    elif selection == "6":
        printHP()
    elif selection == "7":
        printAttack()
    elif selection == "8":
        printDefense()
    elif selection == "9":
        printSpeed()
    elif selection == "10":
        printSPAttack()
    elif selection == "11":
        printSPDefense()
    elif selection == "12":
        printAbility()
    elif selection == "13":
        printEvolution()
    else:
        print("INVALID INPUT")
        return

@bp.route("/name", methods=('GET', 'POST'))
#2. Print by Name
def printName():
    results = ""
    if request.method == 'POST':
        letter = request.form['name']
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT *
                FROM POKEMON
                WHERE PNAME LIKE %s"""
        try:
            cursor.execute(sql, (letter + "%"))
        except:
            print("INVALID INPUT")
            db.close()
            return

        results = cursor.fetchall()
        with open("SortByName.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByName.csv CSV Created")
        # disconnect from server
        db.close()

    return render_template('name.html', posts = results)

@bp.route("/type", methods=('GET', 'POST'))
#2. Print by Type
def printType():
    results = ""
    if request.method == 'POST':
        type = request.form['type']

        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        #Sub-query
        sql = """SELECT *
            FROM POKEMON
            WHERE ID  IN (SELECT ID FROM TYPES WHERE TYPE = %s )"""

        cursor.execute(sql, type)

        results = cursor.fetchall()

        with open("SortByType.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByType" + " CSV Created")

        # disconnect from server
        db.close()
    return render_template('type.html', posts=results)

@bp.route("/height", methods=('GET', 'POST'))
#2. Print by Heights
def printHeight():
    results = ""
    if request.method == 'POST':
        min_height = int(request.form['min'])
        max_height = int(request.form['max'])
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT N.ID, N.PNAME, P.HEIGHT
                    FROM PROFILE P, POKEMON N
                    WHERE N.ID = P.ID AND CAST(LEFT(P.HEIGHT, (LOCATE(%s, P.HEIGHT)-1)) AS SIGNED) >= %s AND CAST(LEFT(P.HEIGHT, (LOCATE(%s, P.HEIGHT)-1)) AS SIGNED) < %s
                    ORDER BY CAST(LEFT(P.HEIGHT, (LOCATE(%s, P.HEIGHT)-1)) AS SIGNED) DESC"""
        try:
            cursor.execute(sql, ("'", min_height, "'", max_height, "'"))
        except:
            print("INVALID INPUT")
            db.close()
            return
        results = cursor.fetchall()
        with open("SortByHeight.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByHeight CSV Created")

        # disconnect from server
        db.close()
    return render_template('height.html', posts=results)

@bp.route("/catchrate", methods=('GET', 'POST'))
#2. Print by Catch Rate
def printCatchRate():
    results = ""
    if request.method == 'POST':
        catchrate = request.form['min']

        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Sub-query
        sql = """SELECT N.ID, N.PNAME, P.CATCHRATE
                    FROM PROFILE P, POKEMON N
                    WHERE N.ID = P.ID AND CATCHRATE >= %s"""
        try:
            cursor.execute(sql, catchrate)
        except:
            print("INVALID INPUT")
            db.close()
            return
        results = cursor.fetchall()
        with open("SortByCatchRate.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByCatchRate CSV Created")

        # disconnect from server
        db.close()
    return render_template('catchrate.html', posts=results)

@bp.route("/weight", methods=('GET', 'POST'))
#2 Print by Weight
def printWeight():
    results = ""
    if request.method == 'POST':
        min_weight = float(request.form['minW'])
        max_weight = float(request.form['maxW'])
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Sub-query
        sql = """SELECT N.ID, N.PNAME, P.WEIGHT
                        FROM PROFILE P, POKEMON N
                        WHERE N.ID = P.ID AND WEIGHT >= %s AND WEIGHT <= %s
                        ORDER BY P.WEIGHT DESC"""
        try:
            cursor.execute(sql, (min_weight, max_weight))
        except:
            print("INVALID INPUT")
            db.close()
            return
        results = cursor.fetchall()

        with open("SortByWeight.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByWeight CSV Created")

        # disconnect from server
        db.close()
    return render_template('weight.html', posts=results)

@bp.route("/hp")
#2.Print by HP
def printHP():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.HP
                FROM STATS S, POKEMON N
                WHERE N.ID = S.ID
                ORDER BY S.HP DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()

    with open("SortByHP.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortByHP CSV Created")

    # disconnect from server
    db.close()
    return render_template('hp.html', posts=results)

@bp.route("/attack", methods=('GET', 'POST'))
#2.Print by Attack
def printAttack():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.ATTACK
                    FROM STATS S, POKEMON N
                    WHERE N.ID = S.ID
                    ORDER BY S.ATTACK DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()

    with open("SortByAttack.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortByAttack CSV Created")

    # disconnect from server
    db.close()
    return render_template('attack.html', posts=results)

@bp.route("/defense", methods=('GET', 'POST'))
#2.Print by Defense
def printDefense():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.DEFENSE
                    FROM STATS S, POKEMON N
                    WHERE N.ID = S.ID
                    ORDER BY S.DEFENSE DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()

    with open("SortByDefense.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortByDefense CSV Created")

    # disconnect from server
    db.close()
    return render_template('defense.html', posts=results)

@bp.route("/speed", methods=('GET', 'POST'))
#2.Print by Speed
def printSpeed():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.SPEED
                    FROM STATS S, POKEMON N
                    WHERE N.ID = S.ID
                    ORDER BY S.SPEED DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()

    with open("SortBySpeed.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortBySpeed CSV Created")

    # disconnect from server
    db.close()
    return render_template('speed.html', posts=results)

@bp.route("/spatk", methods=('GET', 'POST'))
#2.Print by Special Attack
def printSPAttack():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.SPATK
                    FROM STATS S, POKEMON N
                    WHERE N.ID = S.ID
                    ORDER BY S.SPATK DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()

    with open("SortBySpatk.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortBySpatk CSV Created")

    # disconnect from server
    db.close()
    return render_template('spatk.html', posts=results)

@bp.route("/spdef", methods=('GET', 'POST'))
#2.Print by Special Defense
def printSPDefense():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Sub-query
    sql = """SELECT N.ID, N.PNAME, S.SPDEF
                    FROM STATS S, POKEMON N
                    WHERE N.ID = S.ID
                    ORDER BY S.SPDEF DESC"""
    try:
        cursor.execute(sql)
    except:
        print("INVALID INPUT")
        db.close()
        return

    results = cursor.fetchall()
    with open("SortBySpdef.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortBySpdef CSV Created")

    # disconnect from server
    db.close()
    return render_template('spdef.html', posts=results)

@bp.route("/ability", methods=('GET', 'POST'))
#2. Print by Ability
def printAbility():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    #Sub-query
    sql = """SELECT N.ID, N.PNAME, A.ABILITY
        FROM POKEMON N, ABILITY A
        WHERE N.ID = A.ID
        ORDER BY A.ABILITY"""

    cursor.execute(sql)

    results = cursor.fetchall()
    with open("SortByAbility.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
    print("SortByAbility CSV Created")

    # disconnect from server
    db.close()
    return render_template('ability.html', posts=results)

@bp.route("/evolution", methods=('GET', 'POST'))
#2. Print by Evolution
def printEvolution():
    results = ""
    if request.method == 'POST':
        pname = request.form['evolution']

        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        #FIND ID
        sql = """SELECT ID 
                 FROM POKEMON 
                 WHERE PNAME = %s"""
        try:
            cursor.execute(sql, pname)
        except:
            print("ERROR: COULDN'T FIND POKEMON")
            db.close()
            return
        id = cursor.fetchone()
        db.close()

        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        #FIND EVOLVE-FORM ID
        sql = """SELECT EVOLVESTO
                 FROM EVOLUTIONS
                 WHERE ID = %s"""
        try:
            cursor.execute(sql, id)
        except:
            print("ERROR: COULDN'T FIND POKEMON")
            db.close()
            return
        evolvedID = cursor.fetchone()
        db.close()

        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT *
                 FROM POKEMON
                 WHERE ID = %s"""
        # Sub-query
        try:
            cursor.execute(sql, evolvedID)
        except:
            print("ERROR: COULDN'T FIND POKEMON")
            db.close()
            return

        results = cursor.fetchall()
        with open("SortByEvolution.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in results:
                writer.writerow(row)
        print("SortByEvolution CSV Created")
        #disconnect from server
        db.close()
    return render_template('evolution.html', posts=results)

@bp.route("/create", methods=('GET', 'POST'))
#3. Create a new Pokemon
def create():
    if request.method == 'POST':
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        id = int(request.form['id'])
        pname = request.form['name']
        about = request.form['about']
        description = request.form['description']

        sql = """INSERT INTO POKEMON(ID,
        PNAME, ABOUT, DESCRIPTION)
        VALUES (%s,%s,%s,%s)"""

        try:
         # Execute the SQL command
            cursor.execute(sql,(id, pname, about, description))
        except:
        # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        type = (request.form['type']).upper()

        sql = """INSERT INTO TYPES (ID,
                       TYPE)
                       VALUES (%s, %s)"""
        try:
            # Execute the SQL command
            cursor.execute(sql, (id, type))
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        height = request.form['height']
        catchrate = request.form['catchrate']
        weight = float(request.form['weight'])

        sql = """INSERT INTO PROFILE (ID,
                  HEIGHT, CATCHRATE, WEIGHT)
                  VALUES (%s, %s, %s, %s)"""

        try:
            #Execute the SQL command
            cursor.execute(sql, (id, height, catchrate, weight))
        except:
            #Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        ability = request.form['ability']

        sql = """INSERT INTO ABILITY (ID,
               ABILITY)
               VALUES (%s, %s)"""

        try:
             # Execute the SQL command
             cursor.execute(sql, (id, ability))
        except:
             # Rollback in case there is any error
             db.rollback()
             print("ERROR: ROLLBACK")

        hp = int(request.form['hp'])
        attack = int(request.form['attack'])
        defense = int(request.form['defense'])
        speed = int(request.form['speed'])
        spatk = int(request.form['spatk'])
        spdef = int(request.form['spdef'])

        sql = """INSERT INTO STATS (ID,
               HP, ATTACK, DEFENSE, SPEED, SPATK, SPDEF)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        try:
             # Execute the SQL command
             cursor.execute(sql,(id, hp, attack, defense, speed, spatk, spdef))
        except:
             # Rollback in case there is any error
             db.rollback()
             print("ERROR: ROLLBACK")

        evolution = int(request.form['evolution'])
        sql = """INSERT INTO EVOLUTIONS (ID,
                       EVOLVESTO)
                       VALUES (%s, %s)"""

        try:
            # Execute the SQL command
            cursor.execute(sql,(id, evolution))
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        nor = float(request.form['nor'])
        fir = float(request.form['fir'])
        wat = float(request.form['wat'])
        ele = float(request.form['ele'])
        gra = float(request.form['gra'])
        ice = float(request.form['ice'])
        fig = float(request.form['fig'])
        poi = float(request.form['poi'])
        gro = float(request.form['gro'])
        fly = float(request.form['fly'])
        psy = float(request.form['psy'])
        bug = float(request.form['bug'])
        roc = float(request.form['roc'])
        gho = float(request.form['gho'])
        dra = float(request.form['dra'])
        dar = float(request.form['dar'])
        ste = float(request.form['ste'])
        fai = float(request.form['fai'])

        sql = """INSERT INTO DAMAGEWHENATTACKED (ID,
              NOR, FIR, WAT, ELE, GRA, ICE, FIG, POI, GRO,
              FLY, PSY, BUG, ROC, GHO, DRA, DAR, STE, FAI)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            # Execute the SQL command
            cursor.execute(sql, (id, nor, fir, wat, ele, gra,
                                 ice, fig, poi, gro, fly, psy,
                                 bug, roc, gho, dra, dar, ste, fai))
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        db.commit()

        print("POKEMON CREATED")
        # disconnect from server
        db.close()
        return redirect(url_for('home'))

    return render_template('create.html')

@bp.route("/delete", methods=('GET', 'POST'))
#4. Delete an existing Pokemon
def delete():
    if request.method == 'POST':
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        id = int(request.form['id'])

        #Delete from Pokemon
        sql = """DELETE FROM POKEMON WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql,id)
            # Commit your changes in the database
            #db.commit()
            #print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        #Delete from Type
        sql = """DELETE FROM TYPES WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            #print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # Delete from Profile
        sql = """DELETE FROM PROFILE WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            # print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # Delete from Stats
        sql = """DELETE FROM STATS WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            # print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # Delete from Ability
        sql = """DELETE FROM ABILITY WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            # print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # Delete from EVOLUTIONS
        sql = """DELETE FROM EVOLUTIONS WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            # print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # Delete from DamageWhenAttacked
        sql = """DELETE FROM DAMAGEWHENATTACKED WHERE ID = %s"""
        try:
            # Execute the SQL command
            cursor.execute(sql, id)
            # Commit your changes in the database
            # db.commit()
            # print("POKEMON " + str(id) + " DELETED")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        db.commit()
        # disconnect from server
        db.close()
        return redirect(url_for('home'))

    return render_template('delete.html')

@bp.route("/update", methods=('GET', 'POST'))
#5. Update	records
def updateDescription():
    if request.method == 'POST':
        # Open database connection
        db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        id = request.form['id']
        str = request.form['description']

        sql = """UPDATE POKEMON SET DESCRIPTION = %s WHERE ID = %s"""

        try:
            # Execute the SQL command
            cursor.execute(sql, (str, id))
            # Commit your changes in the database
            db.commit()
            print("POKEMON DECRIPTION UPDATED")

        except:
            # Rollback in case there is any error
            db.rollback()
            print("ERROR: ROLLBACK")

        # disconnect from server
        db.close()
        return redirect(url_for('home'))
    return render_template('update.html')


#7. Generate	reports	that	can	be	exported	(excel	or	csv	format)
def writePokemon():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute(
        'SELECT *'
        'FROM POKEMON'
    )

    with open('pokemon.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in cursor.fetchall():
            writer.writerow(row)
            #print(row)

    print("Pokemon CSV Created")
    # disconnect from server
    db.close()

def writeProfile():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute(
        'SELECT *'
        'FROM PROFILE'
    )

    with open('profile.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in cursor.fetchall():
            writer.writerow(row)
            #print(row)

    print("Profile CSV Created")
    # disconnect from server
    db.close()

def writeStats():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "pokemondb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute(
        'SELECT *'
        'FROM STATS'
    )

    with open('stats.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in cursor.fetchall():
            writer.writerow(row)
            #print(row)

    print("Stats CSV Created")
    # disconnect from server
    db.close()