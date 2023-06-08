from flask import request, redirect, flash, url_for, render_template
from ez2erp.auth import bp_auth
from ez2erp.auth.models import User



@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup_page.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email_address = request.form.get('email_address')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        
        if password != confirm_password:
            flash('Password do not match', 'error')
            return redirect(url_for('auth.signup'))
        
        new_user: User = User({
            'username': username,
            'email_address': email_address,
            'fname': fname,
            'lname': lname
        })
        new_user.set_password(password)
        new_user.save()
        
        flash('User created successfully!', 'success')
        return redirect(url_for('auth.login'))