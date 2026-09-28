from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/" ,methods=["GET", "POST"])
def home():

    if request.method=="POST":

        name = request.form["name"]

        if name.strip() == "":
            return "student name enter karo."

        hindi = int(request.form["hindi"])
        english = int(request.form["english"])
        math = int(request.form["math"])
        science = int(request.form["science"])
        computer = int(request.form["computer"])

        marks = [hindi,english,math,science,computer]

        if any(mark < 0 or mark > 100 for mark in marks):
            return "marks 0 se 100 ke beech hone chahiye."

        total = hindi + english + math + science + computer
        percentage = total/5

        if percentage >=90:
            grade = "A"
        elif percentage >=75:
            grade = "B"
        elif percentage >=60:
            grade = "B"
        elif percentage >=40:
            grade = "D"
        else:
            grade = "F"
        if percentage >=40:
            result = "pass"
        else:
            result = "fail"

        return render_template("result.html",name=name,hindi=hindi,english=english,math=math,science=science,computer=computer,total=total,percentage=percentage,grade=grade,result=result)

    return render_template("index.html")


app.run(debug=True)