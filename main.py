from flask import Flask, redirect, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def contactForm():
    return render_template('contact_form.html')

@app.route('/result', methods=['POST'])
def summary():
    if request.method == "POST":
        form = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phoneNumber": request.form['phoneNumber'],
            "message": request.form['message'],
            "subject": request.form['subject'],
            "contactMethod": request.form['contactMethod'],
            "agreement": request.form['agreement']
        }

        if form['agreement'] == 'on':
            form['agreement'] = "Yes"

            if form['subject'] == "Other":
                form['subject'] = request.form['other']

                return render_template("confirmation.html", form=form)
            else:
                return render_template("confirmation.html", form=form)
        else:
            return "<h1>You must agree to our terms and conditions in order to continue!</h1>", 406

if __name__ == "__main__":
    app.run(debug=True)