<py-script>
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        session['logged_in'] = username
        return redirect(url_for('views.home'))
        
    return render_template("login.html")
</py-script>