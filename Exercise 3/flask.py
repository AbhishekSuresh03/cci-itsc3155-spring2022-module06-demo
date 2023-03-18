from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded list of organizations
ORGANIZATIONS = ['Club A', 'Club B', 'Club C', 'Club D', 'Club E']

# Dictionary to store registered users
REGISTERED_USERS = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from form
        name = request.form['name']
        organization = request.form['organization']

        # Validate user input
        if name.strip() == '':
            error = 'Name is required'
        elif organization not in ORGANIZATIONS:
            error = 'Invalid organization'
        else:
            # Add user to registered users
            REGISTERED_USERS[name] = organization
            return redirect(url_for('registered_users'))

        # Render home page with error message
        return render_template('home.html', organizations=ORGANIZATIONS, error=error)
    else:
        # Render home page
        return render_template('home.html', organizations=ORGANIZATIONS)


@app.route('/registered_users')
def registered_users():
    # Render registered users page with list of registered users
    return render_template('registered_users.html', users=REGISTERED_USERS)


if __name__ == '__main__':
    app.run(debug=True)
