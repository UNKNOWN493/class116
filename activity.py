from flask import Flask, render_template
app = Flask(__name__)

#in the function return render_template(‘index.html’)

@app.route("/Student_Activity2")
def student_webpage():
    #Create a variable
    name = 'John'
    # Pass the variable in the template
    return render_template('tempelates/index.html', student_name = name)