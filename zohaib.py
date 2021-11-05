import os
from flask import Flask, render_template, request, redirect, session, url_for, jsonify,flash
from os.path import join, dirname, realpath

from werkzeug.utils import secure_filename
from datetime import datetime
import csv
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/formm'
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "zb"
app.config["MYSQL_DATABASE_HOST"] = "localhost"

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
mysql.init_app(app)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.secret_key = "123456"


##############  SUPER USER AUTHENTICATION START FROM HERE  ##############

@app.route('/home', methods =["POST", "GET"])
def home():
    if session.get("sessionusername"):
        if request.method == "POST":
            return redirect(url_for("home"))
        else:
            return render_template("basic.html")
    else:
        return redirect(url_for("home"))

@app.route('/hotel-view', methods =["POST", "GET"])
def hotel_view():
    userid = request.args.get("id")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(''' SELECT rooms.sno,rooms.date, country.name as "Country",city.city as "City",snohotel.hotelname as "hotelname",rooms.price,rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country INNER JOIN snohotel ON snohotel.sno=rooms.hotelid where rooms.bed = "Single Bed" and snohotel.sno=%s;''',[int(userid)])
    var = cur.fetchall()
    #cur.execute('''select * from snohotel where sno=%s;''', [int(userid)])
    return render_template("viewhotel.html",varr=var)


@app.route('/hotel-view2', methods =["POST", "GET"])
def hotel_view2():
    if request.method == "GET":
        userid = request.args.get("id")   
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT rooms.sno,rooms.date, country.name as "Country",city.city as "City",snohotel.hotelname as "hotelname",rooms.price,rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country INNER JOIN snohotel ON snohotel.sno=rooms.hotelid where rooms.bed = "Double Beds" and snohotel.sno=%s;''',[int(userid)])
        var = cur.fetchall()
        #cur.execute('''select * from snohotel where sno=%s;''', [int(userid)])
       
        return render_template("viewhotel2.html",varr=var)


@app.route('/hotel-view3', methods =["POST", "GET"])
def hotel_view3():
    if request.method == "GET":
        userid = request.args.get("id")   
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT rooms.sno,rooms.date, country.name as "Country",city.city as "City",snohotel.hotelname as "hotelname",rooms.price,rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country INNER JOIN snohotel ON snohotel.sno=rooms.hotelid where rooms.bed = "Triple BedS" and snohotel.sno=%s;''',[int(userid)])
        var = cur.fetchall()
        #cur.execute('''select * from snohotel where sno=%s;''', [int(userid)])
       
        return render_template("viewhotel3.html",varr=var)

# @app.route('/changepasss', methods=['POST'])
# def changepasss():
#     if 'user_id' in session:
#         password = request.form.get('curpassword')
#         newpass = request.form.get('newpassword')
#         print(password)
#
#         user_id = session.get("user_id")
#         print(user_id)
#         cursor.execute(""" SELECT * FROM `users` WHERE id=%s; """, [int(user_id)])
#         password1 = cursor.fetchone()
#         print(password1)
#
#         if password1[4] == password:
#             cursor.execute("""update `users` set `password` =%s where id=%s """, [newpass, int(user_id)])
#             conn.commit()
#             return redirect(url_for("setting"))
#         else:
#             session["error"] = "Your old password was entered incorrectly. Please enter it again."
#             return redirect(url_for("changepassword"))
#     else:
#         return redirect(url_for("login"))
#


@app.route('/login', methods=["GET","POST"])
def loginn():
    if session.get("sessionusername"):
        return redirect(url_for("home"))
    else:
        if request.method == "POST":
            password = request.form.get("password")
            username = request.form.get("username")
            print(username,password)
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute("select * from auth where username=%s;",[username])
            data = cur.fetchone()
            cur.close()
            conn.close()
            if data != None:
                if data[2] == password:
                    session["sessionusername"] = data[1]
                    return redirect(url_for("home"))
                else:
                    session["error"] = "password doesn't match."
                    return redirect(url_for("loginn"))
            else:
                session["error"] = "user not exist."
                return redirect(url_for("loginn"))
        else:
            error = ""
            if session.get("error"):
                error = session.get("error")
                session.pop("error", None)
            return render_template("login.html", error=error)
           
@app.route("/logout",methods=["GET","POST"])
def logout():
    session.pop("sessionusername", None)
    return redirect(url_for("loginn"))





##############  END AUTHENTICATION  ##############
  





##############  FLIGHTS  ##############


@app.route('/add-airport',methods=["POST","GET"])
def add_airport():
    if session.get("sessionusername"):
        if request.method == "POST":
           # country = request.form.get("country")
            departure_city = request.form.get("city")
            departure_country = request.form.get("country")
            airport_name = request.form.get("airportname")
            
            
            
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into airportcity (airportname,city,country) values(%s,%s,%s);''',[airport_name,departure_city,departure_country])
            conn.commit()
            cur.close()
            flash("Country has been submitted ")
            return render_template("add-airportname.html")
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-airportname.html",data=data,subcat=subcat)



############  Flight name  ############
    
@app.route('/add-flight-name',methods=["POST","GET"])
def add_flight_name():
    if session.get("sessionusername"):
        if request.method == "POST":
            airport_country = request.form.get("airportcountry")
            airport_city = request.form.get("airportcity")
            airport = request.form.get("airport")
            flight_name = request.form.get("flightname")

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into flightname (country,city,airport,flightname) values(%s,%s,%s,%s);''',[airport_country,airport_city,airport,flight_name])
            conn.commit()
            cur.close()
            return redirect(url_for("add_flight_name"))
        
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()
            print(airport_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-flightname.html",data=data,subcat=subcat,airportname=airport_name)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)
        

############ Flight Number #############333


@app.route('/add-flight-number',methods=["POST","GET"])
def add_flight_number():
    if session.get("sessionusername"):
        if request.method == "POST":
            airport_country = request.form.get("airportcountry")
            airport_city = request.form.get("airportcity")
            airport = request.form.get("airport")
            flight_name = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into flightnum (country,city,airportname,flightname,flightnumber) values(%s,%s,%s,%s,%s);''',[airport_country,airport_city,airport,flight_name,flightnumber])
            conn.commit()
            cur.close()
            return redirect(url_for("add_flight_name"))
        
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()



            print(flight_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-flightnumber.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route('/add-flight',methods=["POST","GET"])
def add_flight():
    if session.get("sessionusername"):
        if request.method == "POST":
            flight_date = request.form.get("flightdate")
            airport_country = request.form.get("airportcountry")
            airport_city = request.form.get("airportcity")
            airport = request.form.get("airport")
            flight_name = request.form.get("flightname")
            flight_number = request.form.get("flightnumber")
            departure_city = request.form.get("departurecity")
            arrival_city = request.form.get("arrivalcity")
            departure_time = request.form.get("departuretime")
            arrival_time = request.form.get("arrivaltime")
            duration = request.form.get("duration")
            price = request.form.get("price")

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into flight (flightdate,country,city,departurecity,departure,arrival,duration,arrivalcity,airportname,flightname,flightnumber,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',[flight_date,airport_country,airport_city,departure_city,departure_time,arrival_time,duration,arrival_city,airport,flight_name,flight_number,price])
            conn.commit()
            cur.close()
            return redirect(url_for("add_flight"))
        
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()
            



            print(flight_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-flight.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)




#@app.route('/add-flight',methods=["POST","GET"])
#def add_flight():
   # if session.get("sessionusername"):
      #  if request.method == "POST":
           # country = request.form.get("country")
          #  airport_country = request.form.get("airportcountry")
          #  airport_name = request.form.get("airportname")
          #  flight_name = request.form.get("flightname")
          #  departure_city = request.form.get("departurecity")
            #departure_time = request.form.get("departuretime")
            #arrival_time = request.form.get("arrivaltime")
            #duration = request.form.get("duration")
            #duration = request.form.get("duration")
            #arrivalcity = request.form.get("arrivalcity")
            #conn = mysql.connect()
            #cur = conn.cursor()
            #cur.execute(''' insert into flight (departurecity,departure,arrival,duration,arrivalcity,country,airportname,flightname) values(%s,%s,%s,%s,%s,%s,%s,%s);''',[departure_city,departure_time,arrival_time,duration,arrivalcity,airport_country,airport_name,flight_name])
           # conn.commit()
            #cur.close()
            #flash("Country has been submitted ")
            #return render_template("add-flight.html")
        #else:
            #conn = mysql.connect()
            ##cur = conn.cursor()
            #cur.execute(''' select * from country;''')
            #
            #cur.execute(''' select * from city;''')
            #subcat = cur.fetchall()

            #cur.execute(''' select * from airportcity;''')
            #airport_name = cur.fetchall()
            #conn.commit()
            #cur.close()
            #conn.close()
            #return render_template("add-airport.html",data=data,subcat=subcat,airportname=airport_name)
    #else:
        #error = ""
        #if session.get("error"):
            #error = session.get("error")
            #session.pop("error", None)
        #return redirect(url_for("loginn"))


@app.route('/flight-list',methods=["POST","GET"])
def flight_list():
    if session.get("sessionusername"):        
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(""" SELECT flight.sno, flight.flightdate,flight.departure,flight.arrival,(select city.city from city where city.idd = flight.departurecity) as "departureCity",
(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city",(select city.city from city where city.idd = flight.city) as "Flight City",(SELECT country.name from country where country.sno = flight.country) as "flightcountry",(SELECT airportcity.airportname from airportcity where airportcity.sno = flight.airportname) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = flight.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = flight.flightnumber) as "flight number" FROM flight; """)
       # cur.execute(''' SELECT flight.sno,flight.departure,flight.arrival,flight.duration,(select city.city from city where city.idd = flight.departurecity) as "departureCity",
#(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city" FROM flight;''')



        data = cur.fetchall()
        return render_template("flight-list.html",data=data)

    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))



@app.route('/edit-flight',methods=["POST","GET"])
def edit_flight():
    if session.get("sessionusername"):
        if request.method == "POST":
            sno = request.form.get("sno")
            flight_date = request.form.get("flightdate")
            airport_country = request.form.get("airportcountry")
            airport_city = request.form.get("airportcity")
            airport = request.form.get("airport")
            flight_name = request.form.get("flightname")
            flight_number = request.form.get("flightnumber")
            departure_city = request.form.get("departurecity")
            arrival_city = request.form.get("arrivalcity")
            departure_time = request.form.get("departuretime")
            arrival_time = request.form.get("arrivaltime")
            duration = request.form.get("duration")
            price = request.form.get("price")

            
            
            
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' UPDATE flight SET flightdate=%s,country=%s,city=%s,departurecity=%s,departure=%s,arrival=%s,duration=%s,arrivalcity=%s,airportname=%s,flightname=%s,flightnumber=%s,price=%s WHERE sno=%s;''',[flight_date,airport_country,airport_city,departure_city,departure_time,arrival_time,duration,arrival_city,airport,flight_name,flight_number,price,sno])
            conn.commit()
            cur.close()
            flash("Country has been submitted ")
            return redirect("/flight-list")
        
        else:
            

            
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()

            userid = request.args.get("id")
            cur.execute('''select * from flight where sno=%s;''', [int(userid)])
            value = cur.fetchone()
            print(value)
        

            print(flight_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("edit-flight.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number,value=value)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)




@app.route('/delete-flight',methods = ["GET","POST"])
def delete_flight():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''SELECT flight.sno, flight.flightdate,flight.departure,flight.arrival,(select city.city from city where city.idd = flight.departurecity) as "departureCity",
(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city",(select city.city from city where city.idd = flight.city) as "Flight City",(SELECT country.name from country where country.sno = flight.country) as "flightcountry",(SELECT airportcity.airportname from airportcity where airportcity.sno = flight.airportname) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = flight.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = flight.flightnumber) as "flight number" FROM flight where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("flight_list"))







############## pakages ##########

@app.route('/add-package',methods=["POST","GET"])
def add_package():
    if session.get("sessionusername"):
        if request.method == "POST":
            flightdate = request.form.get("flightdate")
            country = request.form.get("country")
            city = request.form.get("city")
            airport = request.form.get("airport")
            flightname = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")
            #departuredate = request.form.get("departuredate")
            flightprice = request.form.get("flightprice")
            arrivalcity = request.form.get("arrivalcity")
            hotelname = request.form.get("hotel")
            roomsprice = request.form.get("hotelprice")
            extracharges = request.form.get("extracharges")
            bed = request.form.get("beds")
            bed = bed.split(",")
            roomtype = bed[1]
            price = int(bed[0])
            days = request.form.get("days")
            acountry = request.form.get("acountry")
            image = request.files.get("images")
            if image.filename != "":
                filename = image.filename
                filename = filename
            
                
                image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                conn = mysql.connect()
                cur = conn.cursor()
                print(filename,hotelname)
                
                cur.execute(''' insert into pakage (date,country,city,airport,flightname,flightnumber,flightprice,arrivalcity,hotelname,roomsprice,extracharges,bed,days,image,acountry) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',[flightdate,country,city,airport,flightname,flightnumber,flightprice,arrivalcity,hotelname,price,extracharges,roomtype,days,filename,acountry])
                conn.commit()
                cur.close()
                flash("Package has been Added ")
            return render_template("pakage.html")
                
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from snohotel;''')
            hotel = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()


            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()

           # cur.execute(""" SELECT rooms.sno,rooms.date, country.name as "Country",city.city as "City",rooms.hotelid as "hotelid",sum(rooms.price) as "price",rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country; """)
            #rooms = cur.fetchall()

            cur.execute(""" SELECT rooms.sno,rooms.date, country.name as "Country",city.city as "City",rooms.hotelid as "hotelid",sum(rooms.price) as "price",rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country GROUP BY rooms.hotelid
 """)
            rooms = cur.fetchall()

            cur.execute(''' select * from flight;''')
            flight = cur.fetchall()

            cur.execute(""" SELECT extracharges.sno, snohotel.sno, snohotel.hotelname, country.name as "country",city.city as "city",SUM(extracharges.visa+extracharges.transfer+profit+extracharges.insurance) as "extra" FROM extracharges INNER JOIN country ON country.sno = extracharges.country INNER JOIN city ON city.idd = extracharges.city INNER JOIN snohotel ON snohotel.sno = extracharges.hotel GROUP BY snohotel.sno ; """)
            extra2 = cur.fetchall()

            cur.execute('''SELECT pakage.date,pakage.hotelname,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country",(SELECT airportcity.airportname from airportcity where airportcity.sno = pakage.airport) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = pakage.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = pakage.flightnumber) as "flight number",pakage.flightprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed FROM pakage; ''')

            
            extra = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("pakage.html",data=data,subcat=subcat,hotel=hotel,airportname=airport_name,flightname=flight_name,flightnumber=flight_number,rooms=rooms,flight=flight,extra=extra,extra2=extra2)
            
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))

@app.route('/package-edit',methods=["POST","GET"])
def edit_package():
    if session.get("sessionusername"):
        if request.method == "POST":
            flightdate = request.form.get("flightdate")
            country = request.form.get("country")
            city = request.form.get("city")
            airport = request.form.get("airport")
            flightname = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")
            departuredate = request.form.get("departuredate")
            flightprice = request.form.get("flightprice")
            arrivalcity = request.form.get("arrivalcity")
            hotelname = request.form.get("hotel")
            roomsprice = request.form.get("hotelprice")
            extracharges = request.form.get("extracharges")
            bed = request.form.get("beds")
            days = request.form.get("days")
            image = request.files.get("images")

            if image.filename != "":
                filename = secure_filename(image.filename)
                filename = filename
                print(filename)
                conn = mysql.connect()
                cur = conn.cursor()
                image.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename)))
                cur.execute(''' UPDATE pakage SET flightdate=%s, country=%s, city=%s,airport=%s,flightname=%s,hotelname=%s,flightnumber=%s,departuredate=%s,flightprice=%s,arrivalcity=%s,hotelname=%s,roomsprice=%s,extracharges=%s,bed=%s,days=%s,image=%s WHERE sno=%s;''',[flightdate,country,city,airport,flightname,flightnumber,departuredate,flightprice,arrivalcity,hotelname,roomsprice,extracharges,bed,days,filename])
                
                conn.commit()
                cur.close()
            return redirect("/package-list")

        else:
            id = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            #cur.execute(''' SELECT pakage.sno, country.name as "country Name", city.city as "City name",snohotel.hotelname as "hotelname",pakage.locationname,pakage.price,pakage.image,pakage.days
                   # FROM pakage inner join city on city.idd= pakage.city 
                    #inner join country on country.sno = pakage.country INNER JOIN snohotel ON snohotel.sno=pakage.hotelname where pakage.sno=%s;''', [int(id)])
            
            #cur.execute(""" SELECT pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country",(SELECT airportcity.airportname from airportcity where airportcity.sno = pakage.airport) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = pakage.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = pakage.flightnumber) as "flight number",pakage.flightprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed,(SELECT rooms.price FROM rooms WHERE rooms.sno = pakage.roomsprice) as "rooms price" FROM pakage """)
            

        
            var = cur.fetchone()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()
            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from snohotel;''')
            hotel = cur.fetchall()
            conn.commit()
            cur.close()
            return render_template("editpackage.html",varr=var,subcat=subcat,data=data,hotel=hotel)

            
@app.route('/package-list',methods=["POST","GET"])
def package_list():
    if session.get("sessionusername"):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute('''SELECT pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country",(SELECT airportcity.airportname from airportcity where airportcity.sno = pakage.airport) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = pakage.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = pakage.flightnumber) as "flight number",(SELECT flight.price from flight WHERE flight.sno = pakage.flightprice) as "flight price",(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed,(SELECT SUM(rooms.price) FROM rooms WHERE rooms.hotelid = pakage.roomsprice) as "rooms price", ((SELECT flight.price from flight WHERE flight.sno = pakage.flightprice)+(SELECT SUM(rooms.price) FROM rooms WHERE rooms.hotelid = pakage.roomsprice)) as "total", image,sno FROM pakage; ''')
        #cur.execute(''' SELECT * FROM snohotel INNER JOIN country ON snohotel.country = country.sno INNER JOIN city ON snohotel.country = city.id;''')
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render_template("pakagelist.html",data=data)





#################  Extra--Charges   #################



@app.route('/extra-charges',methods=["POST","GET"])
def extra_charges():
    if session.get("sessionusername"):
        if request.method == "POST":
            country = request.form.get("country")
            city = request.form.get("city")
            hotelname = request.form.get("hotelname")
            transfer = request.form.get("transfer")
            visa = request.form.get("visa")
            insurance = request.form.get("insurance")
            profit = request.form.get("profit")
            
            
            conn = mysql.connect()
            cur = conn.cursor()
            
            cur.execute(''' insert into extracharges (country,city,hotel,transfer,visa,insurance,profit) values(%s,%s,%s,%s,%s,%s,%s);''',[country,city,hotelname,transfer,visa,insurance,profit])
            conn.commit()
            cur.close()
            flash("Hotel has been Added ")
                    
            return render_template("extra-charges.html")
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from snohotel;''')
            hotel = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("extra-charges.html",data=data,subcat=subcat,hotel=hotel)

@app.route('/extracharges-list',methods=["POST","GET"])
def extra_charges_list():
    if session.get("sessionusername"):
        
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT extracharges.sno,country.name as "country",city.city as "city",snohotel.hotelname as "hotel",extracharges.transfer,extracharges.visa,extracharges.insurance,extracharges.profit from extracharges INNER JOIN country  on country.sno = extracharges.country INNER JOIN city ON city.idd = extracharges.city INNER JOIN snohotel ON snohotel.sno = extracharges.hotel; ''')
        data = cur.fetchall()
        return render_template("extra-charges-list.html",extra=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))



@app.route('/delete-extracharges',methods = ["GET","POST"])
def delete_extracharges():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from extracharges where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("extra_charges_list"))

    

            

@app.route('/add-country',methods=["POST","GET"])
def add_country():
    if session.get("sessionusername"):
        if request.method == "POST":
            name = request.form.get("name")
            des = request.form.get("des")
            visareq = request.form.get("visareq")
            language = request.form.get("language")
            currency = request.form.get("currency")
            area = request.form.get("area")
            cimage = request.files.getlist("cimage")
            hotel_images = ""

            
            
            for img in cimage:
                if img.filename != "":
                    filename = img.filename
                    print(filename)
                    img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                    hotel_images = hotel_images + ","+str(filename)

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select name from country where name=%s;''',[name])
            data = cur.fetchone()
            if data is None:
                cur.execute(''' insert into country (name,description,visareq,language,currency,area,cimage) values(%s,%s,%s,%s,%s,%s,%s);''',[name,des,visareq,language,currency,area,hotel_images])
                conn.commit()
                cur.close()
                flash("Country has been Added ")
            else:
                flash("This Country Is Already Exist")
            return render_template("addcountry.html")
        else:
            return render_template("addcountry.html")
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))
        #return render_template("basic.html", error=error)
@app.route('/country-list',methods=["POST","GET"])
def country_list():
    if session.get("sessionusername"):
        
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from country;''')
        data = cur.fetchall()
        return render_template("countrylist.html",country=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))

@app.route('/admin-country-detail',methods=["POST","GET"])
def admin_country_detail():
    if session.get("sessionusername"):
        userid = request.args.get("id")
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from country where sno=%s;''',[int(userid)])
        data = cur.fetchall()
        return render_template("admin-country-detail.html",country=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))

@app.route("/edit-country", methods=["GET", "POST"])
def edit_country():
    if session.get("sessionusername"):
        if request.method == "POST":
            sno = request.form.get("sno")
            name = request.form.get("name")
            des = request.form.get("des")
            visareq = request.form.get("visareq")
            language = request.form.get("language")
            currency = request.form.get("currency")
            area = request.form.get("area")
            cimage = request.files.getlist("cimage")
            hotel_images = ""
            
            for img in cimage:
                if img.filename != "":
                    filename = img.filename
                    print(filename)
                    img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                    hotel_images = hotel_images + ","+str(filename)

            conn = mysql.connect()
            cur = conn.cursor()
           
            
            cur.execute(''' Update country Set name=%s,description=%s,visareq=%s,language=%s,currency=%s,area=%s,cimage=%s where sno=%s;''',[name,des,visareq,language,currency,area,hotel_images,sno])
            conn.commit()
            cur.close()
            flash(" Data Has Been Updated ")
              
          
            return render_template("addcountry.html")
        
        else:
            userid = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select * from country where sno=%s;''', [int(userid)])
            var = cur.fetchone()
            return render_template("countryedit.html",varr=var)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return redirect(url_for("loginn"))

        #print(var)
        #return render_template("countryedit.html", varr=var1)
        
    #else:
        #return jsonify({"success": True, "sno": var1[0], "name": var1[1]})

@app.route('/delete-country',methods = ["GET","POST"])
def delete():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from country where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("country_list"))






@app.route('/city-list-country',methods=["POST","GET"])
def city_list_country():
    if session.get("sessionusername"):        
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute(''' select * from city where idd=%s;''',[int(userid)])
        data = cur.fetchone()
        cur.execute(''' select * from city where city.country=%s;''',[int(userid)])
        city = cur.fetchall()

        cur.execute(''' select * from country where sno=%s;''',[int(userid)])
        country = cur.fetchone()
        

        return render_template("citylistcountry.html",city=city,country=country)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)








@app.route('/add-city',methods=["POST","GET"])
def add_city():
    if session.get("sessionusername"):        
        if request.method == "POST":
            country = request.form.get("country")
            city = request.form.get("city")
            print(city,country)
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select city from city where city=%s;''',[city])
            data = cur.fetchone()
            if data is None:
                cur.execute(''' insert into city (city,country) values(%s,%s);''',[city,    country])
                conn.commit()
                cur.close()
                flash("City has been Added ")
                
            else:
                flash("this City Is Already Exist")
            return render_template("addcity.html")


        else:
            conn = mysql.connect()
            cur = conn.cursor()
    
            
            #cur.execute(''' SELECT * FROM snohotel INNER JOIN country ON snohotel.id = country.sno INNER JOIN city ON snohotel.id = city.id;''')
            

            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()
            print(subcat)
            conn.commit()
            cur.close()
            conn.close()
            return render_template("addcity.html",data=data,subcat=subcat)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)

@app.route('/city-list',methods=["POST","GET"])
def city_list():
    if session.get("sessionusername"):        
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from city;''')
        data = cur.fetchall()
        return render_template("citylist.html",country=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route("/edit-city", methods=["GET", "POST"])
def edit_city():
    if session.get("sessionusername"):
        if request.method == "POST":
            idd = request.form.get("idd")
            name = request.form.get("name")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''UPDATE city SET city=%s WHERE idd=%s;''',
            [name,idd])
            conn.commit()
            conn.close()
            return redirect("/city-list")

        else:
            userid = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select * from city where idd=%s;''', [int(userid)])
            var = cur.fetchone()
            return render_template("cityedit.html",varr=var)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)

@app.route('/delete-city',methods = ["GET","POST"])
def delete_city():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from city where id=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("city_list"))


@app.route('/hotel-list-country',methods=["POST","GET"])
def hotel_list_country():
    if session.get("sessionusername"):        
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute(''' select * from city where city.idd=%s;''',[int(userid)])
        data = cur.fetchone()
        cur.execute(''' select sno, hotelname FROM snohotel where snohotel.city=%s;''',[int(userid)])
        hotel = cur.fetchall()
        return render_template("hotel-list-country.html",hotel=hotel)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)
        


@app.route('/add-hotel',methods=["POST","GET"])
def add_hotel():
    if session.get("sessionusername"):
        if request.method == "POST":
            print(request.form)
            print(request.files)
            hotelname = request.form.get("hotelname")
            category = request.form.get("category")
            city = request.form.get("scategory")
            des = request.form.get("des")
            image = request.files.getlist("image")
            hotel_images = ""
            for img in image:
                if img.filename != "":
                    filename = img.filename
                    print(filename)
                    img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                    hotel_images = hotel_images + ","+str(filename)
            
            
       

           # image = request.files.getlist("image")
            #if cimage.filename != "":
                #filename = cimage.filename
                #filename = filename
                #print(filename)
                #cimage.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select hotelname from snohotel where hotelname=%s;''',[hotelname])
            data = cur.fetchone()
            if data is None:
                cur.execute(''' insert into snohotel (hotelname,country,city,image,des) values(%s,%s,%s,%s,%s);''',[hotelname,category,city,hotel_images,des])
                conn.commit()
                cur.close()
                flash("Hotel has been Added ")
                    
            else:
                flash("This Hotel Is Already Exist ")
               
                
                
            return redirect("/add-hotel")
            #filenames = []
           # for img in image:
              #  if img.filename != "":
                 #   filename = secure_filename(img.filename)
                 #   filename = str(datetime.now()) + filename
                 #   print(filename)
                #    img.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename#(filename)))
               # filenames.append(filename)
            #filenames = str(filenames).strip('[]')
            #filenames = str(filenames).replace("'", "")
           # print("filenames")
            #print(filenames)
            
            #return str(True)
                
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from snohotel;''')
            hotel = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("rough.html",data=data,subcat=subcat,hotel=hotel)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)
   

@app.route('/hotel-list',methods=["POST","GET"])
#'''SELECT snohotel.hotelname as "Hotel Name", city.city as "City", country.name as "Country" FROM snohotel inner join city on city.id= snohotel.city inner join country on country.sno = snohotel.country'''
def hotel_list():
    if session.get("sessionusername"):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT snohotel.sno, snohotel.hotelname as "Hotel Name", city.city as "City",
                    country.name as "Country" FROM snohotel inner join city on city.idd= snohotel.city 
                    inner join country on country.sno = snohotel.country;''')
        #cur.execute(''' SELECT * FROM snohotel INNER JOIN country ON snohotel.country = country.sno INNER JOIN city ON snohotel.country = city.id;''')
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render_template("hotellist.html",data=data)


@app.route("/edit-hotel", methods=["GET", "POST"])
def edit_hotel():
    if session.get("sessionusername"):
        if request.method == "POST":
            sno = request.form.get("sno")        
            category = request.form.get("category")
            city = request.form.get("scategory")
            hotelname = request.form.get("hotelname")
            rooms = request.form.get("rooms")
            image = request.files.get("image")
        
            print(sno,hotelname)
            if image.filename != "":
                filename = secure_filename(image.filename)
                filename = filename
                print(filename)
                conn = mysql.connect()
                cur = conn.cursor()
                image.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename)))
                cur.execute(''' UPDATE snohotel SET country=%s, city=%s,hotelname=%s,id=%s,image=%s WHERE sno=%s;''',[category,city,hotelname,rooms,filename,sno])
                
                conn.commit()
                cur.close()
            return redirect("/hotel-list")

        else:
            userid = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select * from snohotel where sno=%s;''', [int(userid)])
            var = cur.fetchone()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()
            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()
            conn.commit()
            cur.close()
            return render_template("edithotel.html",varr=var,subcat=subcat,data=data)

@app.route('/hotel-rooms',methods=["POST","GET"])
def add_rooms():
    if session.get("sessionusername"):
        if request.method == "POST":
            date = request.form.get("date")
            country = request.form.get("country")
            city = request.form.get("city")
            hotelid = request.form.get("hotelid")
            bed = request.form.get("bed")   
            price = request.form.get("price")                    
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into rooms (date,country,city,hotelid,bed,price) values(%s,%s,%s,%s,%s,%s);''',[date,country,city,hotelid,bed,price])
            conn.commit()
            cur.close()
            flash("rooms has been Added ")
            return render_template("addroom.html")
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from snohotel;''')
            hotel = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("addroom.html",data=data,subcat=subcat,hotel=hotel)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route('/rooms-detail',methods=["POST","GET"])
def rooms_detail():
    if session.get("sessionusername"):
        pass
        #conn = mysql.connect()
        #cur = conn.cursor()
        #cur.execute(""" SELECT  snohotel.sno,rooms.date, country.name as "Country",city.city as "City",snohotel.hotelname as "hotelname",rooms.price,rooms.bed FROM rooms inner join city on city.idd=rooms.city inner join country on country.sno = rooms.country INNER JOIN snohotel ON snohotel.sno=rooms.hotelid; """)
       # cur.execute(''' SELECT  snohotel.hotelname as "Hotel Name", rooms.price as "price",rooms.bed as "beds",rooms.bathroom as "bathroom",rooms.status as "status" from snohotel INNER JOIN rooms on rooms.hotelid=snohotel.sno ORDER BY snohotel.hotelname;''')
        #data = cur.fetchall()
        #conn.commit()
        #cur.close()
        #conn.close()
        return render_template("roomslist.html")
    else:
        return render_template("roomslist.html")


@app.route('/delete-rooms',methods = ["GET","POST"])
def delete_rooms():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from rooms where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("hotel_list"))
    
        
     
        
@app.route('/delete-hotel',methods = ["GET","POST"])
def delete_hotel():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from snohotel where sno=%s;''', [int(userid)])
       
        conn.commit()
        conn.close()
    return redirect(url_for("hotel_list"))

@app.route('/add-slider',methods=["POST","GET"])
def add_slider():
    if session.get("sessionusername"):
        if request.method == "POST":
            title = request.form.get("title")
            des = request.form.get("des")
            image = request.files.get("img")
            conn = mysql.connect()
            cur = conn.cursor()
            if image.filename != "":
                filename = secure_filename(image.filename)
                filename = filename
                print(filename)
                image.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename)))
                cur.execute(''' insert into slider (title,des,img) values(%s,%s,%s);''',[title,des,filename])
                conn.commit()
                cur.close()
            flash("slider has been Added ")
            return render_template("slider.html")
        else:
            return render_template("slider.html")
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)

@app.route('/slider-list',methods=["POST","GET"])
def slider_list():
    if session.get("sessionusername"):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from slider;''')
        data = cur.fetchall()
        return render_template("sliderlist.html",slider=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route('/edit-slider',methods=["POST","GET"])
def edit_slider():
    if session.get("sessionusername"):
        if request.method == "POST":
            sno = request.form.get("sno")
            title = request.form.get("title")
            des = request.form.get("des")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''UPDATE slider SET title=%s,des=%s WHERE id=%s;''',
            [title,des,sno])
            conn.commit()
            cur.close()           
            return redirect("/slider-list")
        else:
            userid = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''select * from slider where id=%s;''', [int(userid)])
            var = cur.fetchone()
            return render_template("slideredit.html",varr=var)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)

@app.route('/delete-slider',methods = ["GET","POST"])
def delete_slider():
    if request.method == "POST":
    
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from slider where id=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("slider_list"))


###################### dashboard end #########################

@app.route('/alldestinations')
def alldestinations():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(''' select *  from country;''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('alldestinations.html', data=data)



@app.route('/viewalltour')
def viewalltour():
    userid = request.cookies.get("id")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT tour.country as "country sno",(SELECT country.name FROM country WHERE country.sno = tour.dcountry)as "departure Country",(SELECT country.name FROM country WHERE country.sno = tour.acountry)as "Arrival Country",tour.days,tour.flightprice+tour.packageprice+tour.transfer+tour.visa+tour.insurance+tour.profit AS "total price",tour.images,tour.sno FROM tour where tour.country = %s  ;""",[userid])
    tour =  cur.fetchall()
    cur.execute(''' select * from country where sno=%s;''', [userid])
    data = cur.fetchone()

    cur.close()
    conn.close()
    return render_template('viewalltour.html', tour=tour,data=data)


@app.route('/viewalltour2')
def viewalltour2():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT tour.country as "country sno",(SELECT country.name FROM country WHERE country.sno = tour.dcountry)as "departure Country",(SELECT country.name FROM country WHERE country.sno = tour.acountry)as "Arrival Country",tour.days,tour.flightprice+tour.packageprice+tour.transfer+tour.visa+tour.insurance+tour.profit AS "total price",tour.images,tour.sno FROM tour ;""")
    tour = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('viewalltour2.html', tour=tour)







@app.route('/view-country-detail')
def view_country_detail():
    userid = request.cookies.get("id")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(
        """ SELECT pakage.sno,pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country", pakage.airport,pakage.flightname,pakage.flightnumber,pakage.flightprice,pakage.roomsprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed, pakage.flightprice+pakage.roomsprice+pakage.extracharges as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.arrivalcity) as "departure city" FROM pakage where pakage.country=%s ; """,
        [userid])
    package7_days = cur.fetchall()
    cur.close()
    conn.close()
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(''' select * from country where sno=%s;''', [userid])
    data = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('view-country-detail.html', package=package7_days, data=data)


@app.route('/7-day-Package')
def all_packages():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(
        """ SELECT pakage.sno,pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country", pakage.airport,pakage.flightname,pakage.flightnumber,pakage.flightprice,pakage.roomsprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed, pakage.flightprice+pakage.roomsprice+pakage.extracharges as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.arrivalcity) as "departure city" FROM pakage  ; """
        )
    package7_days = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view-country-detail2.html', package=package7_days)




@app.route('/')
def testing_2():
    if request.method == "POST":
        pass
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from slider;''')
        slider = cur.fetchall()
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select *  from country;''')
        data = cur.fetchall()
        print(data)
        # image = data[7].split(",")

        

        cur.execute(''' select * from city;''')
        subcat = cur.fetchall()
        

        cur.execute(''' select * from airportcity;''')
        airport = cur.fetchall()
        #cur.execute(''' select * from flight;''')
        #flight = cur.fetchall()
        cur.execute(''' SELECT flight.departurecity, flight.sno,flight.country,flight.departure,flight.arrival,flight.duration,(select airportcity.airportname from airportcity where airportcity.sno = flight.airportname) as "departureCity",
(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city" FROM flight;''')
        

      #  cur.execute(''' SELECT flight.departurecity, flight.sno,flight.country,flight.departure,flight.arrival,flight.duration,(select city.city from city where city.idd = flight.departurecity) as "departureCity",
#(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city" FROM flight; ''')
        flight = cur.fetchall()



        
        
       # cur.execute('''SELECT pakage.sno,country.name as "country Name", city.city as "City name",snohotel.hotelname as "hotelname",pakage.price,pakage.image,pakage.days
                   # FROM pakage inner join city on city.idd= pakage.city 
                  #  inner join country on country.sno = pakage.country INNER JOIN snohotel ON snohotel.sno=pakage.hotelname''')
        #pakages = cur.fetchall()
        #print(pakages)
        cur.execute(""" select * from snohotel; """)
        hotel = cur.fetchall()

        cur.execute(""" SELECT pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country",(SELECT airportcity.airportname from airportcity where airportcity.sno = pakage.airport) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = pakage.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = pakage.flightnumber) as "flight number",(SELECT flight.price from flight WHERE flight.sno = pakage.flightprice) as "flight price",(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed,(SELECT SUM(rooms.price) FROM rooms WHERE rooms.hotelid = pakage.roomsprice) as "rooms price", ((SELECT flight.price from flight WHERE flight.sno = pakage.flightprice)+(SELECT SUM(rooms.price) FROM rooms WHERE rooms.hotelid = pakage.roomsprice)) as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.city) as "departure city" FROM pakage ;""")


        package7_days = cur.fetchall()
        print(package7_days)
        
        

        conn.commit()
        cur.close()
        conn.close()
        return render_template("testing2.html",slider=slider,data=data,subcat=subcat,flight=flight,hotel=hotel,airport=airport,package=package7_days)

    






#@app.route('/')
#def user_home():
    #if request.method == "POST":
    ##  else:
      #  conn = mysql.connect()
       # cur = conn.cursor()
       # cur.execute(''' select * from slider;''')
        #slider = cur.fetchall()
       # conn = mysql.connect()
      #  cur = conn.cursor()
        #cur.execute(''' select * from country;''')
        #data = cur.fetchall()

       # cur.execute(''' select * from city;''')
        #subcat = cur.fetchall()

       # cur.execute(''' select * from flight;''')
       # flight = cur.fetchall()
        
       # conn.commit()
       ##conn.close()
       # return render_template("search.html",slider=slider,data=data,subcat=subcat,#flight=flight)

@app.route("/hotelsearch",methods=["GET","POST"])
def search():
    if request.method == "GET":
        country = request.args.get("country")
        city = request.args.get("city")
        persons = request.args.get("person")
        #persons = request.args.get("persons")
        departure = request.args.get("deaparture")
        arrival = request.args.get("arrival")
        duration = request.args.get("duration")
        flight = request.args.get("flight")
        connection = mysql.connect()
        cur = connection.cursor()
       


        cur.execute(""" SELECT pakage.sno,pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country", pakage.airport,pakage.flightname,pakage.flightnumber,pakage.flightprice,pakage.roomsprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed, pakage.flightprice+pakage.roomsprice+pakage.extracharges as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.arrivalcity) as "departure city" FROM pakage where acountry=%s and arrivalcity = %s ; """,[int(country), int(city)])
        package7_days = cur.fetchall()
        
        persons = persons
        print(persons)
       


        return render_template("searchresult.html",package=package7_days,persons=persons)


        #cur.execute(""" SELECT pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country",(SELECT airportcity.airportname from airportcity where airportcity.sno = pakage.airport) as "airportname",(SELECT flightname.flightname from flightname where flightname.sno = pakage.flightname) as "flightname",(SELECT flightnum.flightnumber FROM flightnum where flightnum.sno = pakage.flightnumber) as "flight number",(SELECT flight.price from flight WHERE flight.sno = pakage.flightprice) as "flight price",(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed,(select SUM(extracharges.visa+extracharges.transfer+profit+extracharges.insurance) as "extra" from extracharges INNER JOIN snohotel ON snohotel.sno = extracharges.hotel GROUP BY extracharges.hotel) as "extra",(SELECT SUM(rooms.price) FROM rooms WHERE rooms.hotelid = pakage.roomsprice) as "rooms price" FROM pakage ;""")
   
   #    country = request.args.get("country")
      #  city = request.args.get("city")
        #flight = request.args.get("flight")
        #persons = request.args.get("persons")
      #  departure = request.args.get("deaparture")
      #  arrival = request.args.get("arrival")
      #  duration = request.args.get("duration")
      #  connection = mysql.connect()
      #  cur = connection.cursor()
      #  cur.execute('''SELECT flight.sno,flight.departure,flight.arrival,flight.duration,(select city.city from city where city.idd = flight.departurecity) as "departureCity",
#(select city.city from city where city.idd = flight.arrivalcity)  as "arrival city" FROM flight;''',[city,persons])
       # flightt = cur.fetchall()
        #conn.commit()
        #conn.close()
        #return render_template("searchresult.html",data=data,flightt=flightt)



########## alll hotels for user #####


@app.route('/user-hotel-list')
def user_hotel_list():
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT snohotel.sno, snohotel.hotelname as "Hotel Name",snohotel.image as "image", city.city as "City",country.name as "Country",rooms.price as "price",snohotel.stars as "stars",rooms.roomnum as "avail" FROM snohotel inner join city on city.idd= snohotel.city inner join country on country.sno = snohotel.country inner join rooms on rooms.hotelid=snohotel.sno;''')
        #cur.execute(''' SELECT * FROM snohotel INNER JOIN country ON snohotel.country = country.sno INNER JOIN city ON snohotel.country = city.id;''')
        hotel = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render_template("package.html",hotel=hotel)


@app.route('/user-hotel-detail')
def user_hotel_detail():
    id = request.cookies.get("id")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(""" SELECT pakage.sno,pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country", pakage.airport,pakage.flightname,pakage.flightnumber,pakage.flightprice,pakage.roomsprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed, pakage.flightprice+pakage.roomsprice+pakage.extracharges as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.arrivalcity) as "departure city" FROM pakage where pakage.sno=%s ; """,[id])
    # package7_days = cur.fetchall()

    hotel = cur.fetchone()
    print("hotel")

    cur.execute(""" select pakage.sno as "pakagesno",country.name as "counrty", city.city as "city",snohotel.image as "image",des from snohotel INNER JOIN country ON country.sno = snohotel.country INNER JOIN city ON city.idd = snohotel.city INNER JOIN pakage ON pakage.hotelname = snohotel.sno where pakage.sno=%s """,[id])
    hotelimg = cur.fetchone()
    print(hotelimg)
    hotelImages = hotelimg[3].split(",")
    print(hotelImages)

    conn.commit()
    cur.close()
    conn.close()
    
    
    return render_template("hotel-details.html",hotel=hotel,hotelimg=hotelimg,hotelImages=hotelImages)
    #else:
       # conn = mysql.connect()
       # cur = conn.cursor()
      #  cur.execute(''' SELECT snohotel.sno, snohotel.hotelname as "Hotel Name",snohotel.image as "image", city.city as "City",country.name as "Country",rooms.price as "price",snohotel.stars as "stars",snohotel.des as "describtion"  FROM snohotel inner join city on city.idd= snohotel.city inner join country on country.sno = snohotel.country inner join rooms on rooms.hotelid=snohotel.sno ;''')
       # hotel = cur.fetchone()
       # print("hotel")
       # conn.commit()
       # cur.close()
       # conn.close()
        #return render_template("hotel-details.html",hotel=hotel)


@app.route('/testing')
def testing():
    return render_template("index.html")


@app.route('/index',methods=["GET","POST"])
def index():
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        startdate = request.form.get("startdate")
        enddate = request.form.get("enddate")
        persons = request.form.get("persons")
        conn = mysql.connect()
        cur = conn.cursor() 
        cur.execute(''' select * from city;''')
        city = cur.fetchall()
        conn.commit()
        cur.close()
        
    else:
        userid = request.args.get("id")
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from country;''')
        data = cur.fetchall()
        cur.execute(''' select * from city;''')
        subcat = cur.fetchall()
        conn.commit()
        cur.close()
        return render_template("index.html",subcat=subcat,data=data)

        
        


    ########## add user registration form ##########

@app.route('/user-reg',methods = ["GET","POST"])
def user_reg():
    if request.method == "POST":
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        mobile = request.form.get("mobile")
        country = request.form.get("country")
        hotelname = request.form.get("hotelname")
        persons = request.form.get("persons")
        city = request.form.get("city")
        adress = request.form.get("adress")
        
        startdate = request.form.get("startdate")
        enddate = request.form.get("enddate")
        conn = mysql.connect()
        cur = conn.cursor()   
        ##idproduct=%s and status="available";''',
                                 #  [int(product_id)])   
        cur.execute('''update rooms set status="notavailable" where 
                    sno=%s and status="yes";''',
                                   [int(persons)])  

        cur.execute(''' insert into registration (name,lastname,mobile,country,hotelname,persons,city,adress,startdate,enddate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',[name,lastname,mobile,country,hotelname,persons,city,adress,startdate,enddate])
        conn.commit()
        cur.close()
        flash(" Your Registration Form Has Been submitted ")
        return render_template("registration.html")
    else:
        return render_template("package-book.html")


############# registred forms list ############


@app.route('/user-registred-list',methods=["POST","GET"])
def user_registred_list():
    if session.get("sessionusername"):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' select * from registration;''')
        data = cur.fetchall()
        return render_template("userregistredlist.html",slider=data)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route('/delete-regi-form',methods = ["GET","POST"])
def delete_reg_form():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from registration where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("user_registred_list"))

########### All Countries ###########

@app.route('/all-countries',methods=["POST","GET"])
def all_countries():
    if request.method == "GET":
        conn = mysql.connect()
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(''' select * from country;''')
        all_countries = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template("index.html",allcountries=all_countries)
    

#@app.route('/countrieshotel/<int:name>',methods=["POST","GET"])
#def countries_hotel(name):
   # conn = mysql.connect()
   # cur = conn.cursor()
   # cur = conn.cursor()
   # cur.execute("""SELECT country.sno, snohotel.hotelname as "Hotel Name", city.city as "City",country.name as "Country",snohotel.image as "image" FROM snohotel inner join city on city.idd= snohotel.city inner join country on country.sno = snohotel.country;""")
    #all_hotel = cur.fetchall()
    #conn.commit()
    #conn.close()
    #return render_template("countryhotel.html",hotel=all_hotel,name=name)

@app.route('/countrieshotel',methods=["POST","GET"])
def countries_hotel():
    id = request.cookies.get("id")
    conn = mysql.connect()
    cur = conn.cursor()
    cur = conn.cursor()
    #cur.execute("""SELECT country.sno, snohotel.hotelname as "Hotel Name", city.city as "City",country.name as "Country",snohotel.image as "image" FROM snohotel inner join city on city.idd= snohotel.city inner join country on country.sno = snohotel.country where  snohotel.sno=%s;""",[int(id)])
    #cur.execute("""SELECT * from country where  country.sno=%s;""",[int(id)])
    #country = cur.fetchall()
    #cur.execute("""SELECT country.sno, snohotel.hotelname as "Hotel Name", city.city as "City",country.name as "Country",snohotel.image as "image" FROM snohotel inner join city on city.idd= snohotel.city inner join country on country.sno = snohotel.country where  country.sno=%s;""",[int(id)])
    #hotel = cur.fetchall()

    cur.execute("""SELECT pakage.sno, snohotel.hotelname as "Hotel Name", city.city as "City",country.name as "Country",pakage.image  FROM pakage  inner join city on city.idd= pakage.city inner join country on country.sno = pakage.country INNER JOIN snohotel ON snohotel.sno=pakage.hotelname where  country.sno=%s;""",[int(id)])
    hotel = cur.fetchall()
    conn.commit()
    conn.close()
    return render_template("countryhotel.html",hotel=hotel)


######### pakages for user ######

@app.route('/pakage-list-user',methods=["POST","GET"])

def pakage_list_user():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('''SELECT pakage.sno,country.name as "country Name", city.city as "City name",snohotel.hotelname as "hotelname",pakage.locationname,pakage.price
                    FROM pakage inner join city on city.idd= pakage.city 
                    inner join country on country.sno = pakage.country INNER JOIN snohotel ON snohotel.sno=pakage.hotelname; ''')
        #cur.execute(''' SELECT * FROM snohotel INNER JOIN country ON snohotel.country = country.sno INNER JOIN city ON snohotel.country = city.id;''')
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return render_template(".html",data=data)




########### country Details #########3


@app.route('/country-detail',methods=["POST","GET"])
def city_detail():
    conn = mysql.connect()
    cur = conn.cursor()
    userid = request.cookies.get("id")
    cur.execute(''' select * from country where sno=%s;''',[userid])
    data = cur.fetchone()
    hotelImages = data[7].split(",")
    print(hotelImages)


    cur.execute(""" SELECT pakage.sno,pakage.date,(select city.city from city where city.idd = pakage.city) as "City",(SELECT country.name from country where country.sno = pakage.country) as "country", pakage.airport,pakage.flightname,pakage.flightnumber,pakage.flightprice,pakage.roomsprice,(SELECT snohotel.hotelname FROM snohotel where snohotel.sno = pakage.hotelname) as "hotelname",(SELECT flight.departure FROM flight WHERE flight.sno = pakage.departuredate)as "departure date",bed, pakage.flightprice+pakage.roomsprice+pakage.extracharges as "total", image,arrivalcity,(SELECT city.city FROM city WHERE city.idd = pakage.arrivalcity) as "departure city" FROM pakage where pakage.acountry=%s ; """,[userid])
    package7_days = cur.fetchall()
    print(userid,"hotel")

    cur.execute("""SELECT tour.country as "country sno",(SELECT country.name FROM country WHERE country.sno = tour.dcountry)as "departure Country",(SELECT country.name FROM country WHERE country.sno = tour.acountry)as "Arrival Country",tour.days,tour.flightprice+tour.packageprice+tour.transfer+tour.visa+tour.insurance+tour.profit AS "total price",tour.images,tour.sno FROM tour where tour.country = %s  ;""",[userid])
    tour =  cur.fetchall()


    hotel = cur.fetchone()
    return render_template("user-country-detail.html",data=data,hotel=hotel,hotelImages=hotelImages,package=package7_days,tour=tour)

@app.route('/all_delete',methods = ["GET","POST"])
def all_delete():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from country where sno=%s;''', [int(userid)])
        cur.execute('''delete  from city where city.country=%s;''', [int(userid)])
        cur.execute('''delete  from snohotel where snohotel.country=%s;''', [int(userid)])
        cur.execute('''delete  from rooms where rooms.country=%s;''', [int(userid)])
        
        conn.commit()
        conn.close()
    return redirect(url_for("country_list"))

#cur.execute("delete from country where idcountry = %s", [idcountry])
        #conn.commit()
        #cur.execute("delete from city where idcountry = %s",[idcountry])



######## Tours #########


@app.route('/add-tour',methods=["POST","GET"])
def add_tour():
    if session.get("sessionusername"):
        if request.method == "POST":
            country = request.form.get("country")
            days = request.form.get("days")
            cities = request.form.get("cities")
            place = request.form.get("place")
            plimit = request.form.get("plimit")
            day1 = request.form.get("day1")
            day2 = request.form.get("day2")
            day3 = request.form.get("day3")
            day4 = request.form.get("day4")
            day5 = request.form.get("day5")
            day6 = request.form.get("day6")
            day7 = request.form.get("day7")
            dpoint = request.form.get("dpoint")
            dtime = request.form.get("dtime")
            returndetail = request.form.get("returndetail")
            dcountry = request.form.get("dcountry")
            dcity = request.form.get("dcity")
            acountry = request.form.get("acountry")
            acity = request.form.get("acity")
            airportname = request.form.get("airportname")
            flightname = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")
            flightprice = request.form.get("flightprice")
            packageprice = request.form.get("packageprice")
            transfer = request.form.get("transfer")
            visa = request.form.get("visa")
            insurance = request.form.get("insurance")
            profit = request.form.get("profit")
            image = request.files.getlist("images")

            hotel_images = ""
            for img in image:
                if img.filename != "":
                    filename = img.filename
                    print(filename)
                    img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                    hotel_images = hotel_images + ","+str(filename)
            
            
       

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into tour (country,days,cities,place,plimit,day1,day2,day3,day4,day5,day6,day7,dpoint,dtime,returndetail,images,dcountry,dcity,acountry,acity,airportname,flightname,flightnumber,flightprice,packageprice,transfer,visa,insurance,profit) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',[country,days,cities,place,plimit,day1,day2,day3,day4,day5,day6,day7,dpoint,dtime,returndetail,hotel_images,dcountry,dcity,acountry,acity,airportname,flightname,flightnumber,flightprice,packageprice,transfer,visa,insurance,profit])
            conn.commit()
            cur.close()
            flash("Data has been Added ")
                    
          
               
                
                
            return redirect("/add-hotel")
          
                
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()


            cur.execute(''' select * from flight2;''')
            flight2 = cur.fetchall()
            



            print(flight_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-tour.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number,flight2=flight2)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)

@app.route('/edit-tour',methods=["POST","GET"])
def edit_tour():
    if session.get("sessionusername"):
       
        if request.method == "POST":
            sno = request.form.get("sno")
         
            country = request.form.get("country")
            days = request.form.get("days")
            cities = request.form.get("cities")
            place = request.form.get("place")
            plimit = request.form.get("plimit")
            day1 = request.form.get("day1")
            day2 = request.form.get("day2")
            day3 = request.form.get("day3")
            day4 = request.form.get("day4")
            day5 = request.form.get("day5")
            day6 = request.form.get("day6")
            day7 = request.form.get("day7")
            dpoint = request.form.get("dpoint")
            dtime = request.form.get("dtime")
            returndetail = request.form.get("returndetail")
            dcountry = request.form.get("dcountry")
            dcity = request.form.get("dcity")
            acountry = request.form.get("acountry")
            acity = request.form.get("acity")
            airportname = request.form.get("airportname")
            flightname = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")
            flightprice = request.form.get("flightprice")
            packageprice = request.form.get("packageprice")
            transfer = request.form.get("transfer")
            visa = request.form.get("visa")
            insurance = request.form.get("insurance")
            profit = request.form.get("profit")
            image = request.files.getlist("images")

            hotel_images = ""
            for img in image:
                if img.filename != "":
                    filename = img.filename
                    print(filename)
                    img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                    hotel_images = hotel_images + ","+str(filename)
            
            
       

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' UPDATE tour SET  country=%a,days=%s,cities=%s,place=%s,plimit=%s,day1=%s,day2=%s,day3=%s,day4=%s,day5=%s,day6=%s,day7=%s,dpoint=%s,dtime=%s,returndetail=%s,images=%s,dcountry=%s,dcity=%s,acountry=%s,acity=%s,airportname=%s,flightname=%s,flightnumber=%s,flightprice=%s,packageprice=%s,transfer=%s,visa=%s,insurance=%s,profit=%s WHERE sno=%s ''',[country,days,cities,place,plimit,day1,day2,day3,day4,day5,day6,day7,dpoint,dtime,returndetail,hotel_images,dcountry,dcity,acountry,acity,airportname,flightname,flightnumber,flightprice,packageprice,transfer,visa,insurance,profit,sno])
            conn.commit()
            cur.close()
            return redirect("/tour-list")
        
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()


            cur.execute(''' select * from flight2;''')
            flight2 = cur.fetchall()
            



            print(flight_name)

            userid = request.args.get("id")
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('''SELECT tour.sno,(SELECT country.name FROM country WHERE country.sno = tour.country) as "country",tour.days,tour.cities,tour.place,tour.plimit,tour.day1,tour.day2,tour.day3,tour.day4,tour.day5,tour.day6,tour.day7,tour.dpoint,tour.dtime,tour.returndetail,tour.images,(SELECT country.name FROM country WHERE country.sno = tour.dcountry) as "departurecountry",(SELECT city.city FROM city WHERE city.idd = tour.dcity) as "departure city",(SELECT country.name FROM country WHERE country.sno = tour.acountry) as "aarival country", (SELECT city.city FROM city WHERE city.idd = tour.acity) as "arrival city",tour.airportname,tour.flightname,tour.flightnumber,tour.flightprice,tour.packageprice,tour.transfer,tour.visa,tour.insurance,tour.profit FROM tour where tour.sno=%s;''', [int(userid)])
            var = cur.fetchone()


            conn.commit()
            cur.close()
            conn.close()
            return render_template("edit-tour.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number,flight2=flight2,tour_data=var)


@app.route('/delete-tour',methods = ["GET","POST"])
def delete_tour():
    if request.method == "POST":
        conn = mysql.connect()
        cur = conn.cursor()
        userid = request.args.get("id")
        cur.execute('''delete  from tour where sno=%s;''', [int(userid)])
        variable = cur.fetchone()
        conn.commit()
        conn.close()
    return redirect(url_for("tour_list"))

        

######### flight 2 ######


@app.route('/add-flight2',methods=["POST","GET"])
def add_flight2():
    if session.get("sessionusername"):
        if request.method == "POST":
            date = request.form.get("date")
            dcountry = request.form.get("dcountry")
            dcity = request.form.get("dcity")
            acountry = request.form.get("acountry")
            acity = request.form.get("acity")
            airport = request.form.get("airport")
            flightname = request.form.get("flightname")
            flightnumber = request.form.get("flightnumber")

            price = request.form.get("price")

            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(""" select * from flight2 """)
            data = cur.fetchall()
            conn.commit()
            cur.close()
            
                
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' insert into flight2 (date,dcountry,dcity,acountry,acity,airport,flightname,flightnumber,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);''',[date,dcountry,dcity,acountry,acity,airport,flightname,flightnumber,price])
            conn.commit()
            cur.close()
            flash("data has been added")
            return redirect(url_for("add_flight"))
        
        else:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute(''' select * from country;''')
            data = cur.fetchall()

            cur.execute(''' select * from city;''')
            subcat = cur.fetchall()

            cur.execute(''' select * from airportcity;''')
            airport_name = cur.fetchall()

            cur.execute(''' select * from flightname;''')
            flight_name = cur.fetchall()

            cur.execute(''' select * from flightnum;''')
            flight_number = cur.fetchall()
            



            print(flight_name)


            conn.commit()
            cur.close()
            conn.close()
            return render_template("add-flight2.html",data=data,subcat=subcat,airportname=airport_name,flightname=flight_name,flightnumber=flight_number)
    else:
        error = ""
        if session.get("error"):
            error = session.get("error")
            session.pop("error", None)
        return render_template("login.html", error=error)


@app.route('/tour-list',methods=["POST","GET"])

def tour_list():
    if session.get("sessionusername"):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute(''' SELECT tour.sno,(SELECT country.name FROM country WHERE country.sno = tour.country) as "country",tour.days,tour.cities,tour.place,tour.plimit,tour.day1,tour.day2,tour.day3,tour.day4,tour.day5,tour.day6,tour.day7,tour.dpoint,tour.dtime,tour.returndetail,tour.images,(SELECT country.name FROM country WHERE country.sno = tour.dcountry) as "departurecountry",(SELECT city.city FROM city WHERE city.idd = tour.dcity) as "departure city",(SELECT country.name FROM country WHERE country.sno = tour.acountry) as "aarival country", (SELECT city.city FROM city WHERE city.idd = tour.acity) as "arrival city",tour.airportname,tour.flightname,tour.flightnumber,tour.flightprice,tour.packageprice,tour.transfer,tour.visa,tour.insurance,tour.profit FROM tour; ''')
       
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render_template("tour-list.html",data=data)



@app.route('/user-tour-detail',methods=["POST","GET"])
def user_tour_detail():
    conn = mysql.connect()
    cur = conn.cursor()
    userid = request.cookies.get("id")
    cur.execute(''' select * from tour where sno=%s;''',[userid])
    data = cur.fetchone()
    print(data)
    hotelImages = data[16].split(",")
    


    cur.execute(""" SELECT tour.sno,(SELECT country.name FROM country WHERE country.sno = tour.dcountry)as "departure Country",(SELECT country.name FROM country WHERE country.sno = tour.acountry)as "Arrival Country",tour.days,tour.flightprice+tour.packageprice+tour.transfer+tour.visa+tour.insurance+tour.profit AS "total price",tour.images,tour.cities FROM tour INNER JOIN country ON country.sno = tour.country where tour.sno = %s  ;""",[userid])
    tour =  cur.fetchone()

    


    hotel = cur.fetchone()
    return render_template("user-tour-detail.html", hotelImages=hotelImages, data=data, tour=tour)



@app.route("/getprices")
def getprices():
    startdate = request.args.get("startdate")
    enddate = request.args.get("enddate")
    idcity = request.args.get("idcity")
    idhotel = request.args.get("hotel")
    print(startdate, enddate, idcity, idhotel)
    connection = mysql.connect()
    cur = connection.cursor()
    cur.execute("""select sum(price), bed from rooms where city = %s and date >= %s and date <= %s and 	hotelid = %s group by bed; """, [idcity, startdate, enddate, idhotel])
    data = cur.fetchall()
    print(data)
    prices = []
    for price in data:
        prices.append([int(price[0]), price[1]])
    return jsonify({"data": prices})







if __name__=="__main__":
    app.run(debug=True, port=5009)