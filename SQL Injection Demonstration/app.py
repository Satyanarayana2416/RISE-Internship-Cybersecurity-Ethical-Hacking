@app.route("/safe", methods=["GET", "POST"])
def safe_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # ✅ SAFE: Using parameterized query
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        
        if result:
            return "✅ Logged in securely!"
        else:
            return "❌ Invalid credentials."

    return render_template_string('''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login (Safe)">
        </form>
    ''')
