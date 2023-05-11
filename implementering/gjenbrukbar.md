# Gjenbrukbar kode

Når man snakker om gjenbrukbar kode, snakker man hovedsakelig om to ting. Det første er dokumentasjon av kode som gjør det lettere å forstå eller bruke igjen senere. Det andre er mer generelt og tar for seg ting man skriver én gang som man kan bruke om igjen flere ganger. Dette kan være alt fra programmer og faktisk kode (for eksempel funksjoner eller databaser), til snippets og andre "shortcuts".

## Eksempler

### Eksempel 1 - dokumentasjon

```python
class Pokemon:
    """En klasse for pokemons.
    
    Attributes:
        navn: En string med pokemonens navn
        type: En string med pokemonens hoved/første type
        helsepoeng: Et tall (int) med pokemonens totale helse
        angrep: Et tall (int) med pokemonens angrepsskade
        forsvar: Et tall (int) med pokemonens forsvarsmengde

    """
    def __init__(self, navn, type, helsepoeng, angrep, forsvar):
        self._navn = navn
        self._type = type
        self._helsepoeng = helsepoeng
        self._angrep = angrep
        self._forsvar = forsvar
```

### Eksempel 2 - snippet

```json
{
	// Place your global snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and 
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope 
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is 
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are: 
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. 
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
		"Lag python-klasse": {
		"scope": "python",
		"prefix": "class",
		"body": [
			"class $1:",
			"    def __init__(self, $2, $3):",
			"        self._$2 = $2",
			"        self._$3 = $3"
		],
		"description": "Lag en Python-klasse"
	}
}
```

### Eksempel 3 - funksjoner i et program

```python
def finn_gjennomsnittet(liste):
    total = 0
    for i in liste:
        total += i
    gjennomsnittet = total/len(liste)
    return gjennomsnittet

print(finn_gjennomsnittet([1,4,72,6,3]))

print(finn_gjennomsnittet([1,2,3,4]))
```

## Eksempel av bruk i et større program

```python
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    #password = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=func.now())
    password_hash = db.Column(db.String(128))
    currency = db.Column(db.String(100), nullable=True)
    profile_pic = db.Column(db.String(), nullable=True)
    games = db.Column(MutableList.as_mutable(PickleType), default=[])
    posts = db.relationship('Posts', backref='poster')
    comments = db.relationship('Comments', backref='poster')
    likes = db.relationship('Like', backref='user')
    

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Username %r>' % self.username
```

```python
class UserForm(FlaskForm):
    username = StringField("Enter Username:", validators=[InputRequired()])
    email = EmailField("Enter Email:", validators=[InputRequired()])
    #password = PasswordField("Enter Password:", validators=[InputRequired()])
    password_hash = PasswordField("Enter Password:", validators=[InputRequired(), EqualTo('password_hash2', message="Passwords Must Match!")])
    password_hash2 = PasswordField("Confirm Password:", validators=[InputRequired()])
    currency = SelectField("Choose a Currency:", choices=[("USD"),("EUR"),("NOK")])
    profile_pic = FileField("Profile Picture")
    submit = SubmitField("Submit")
    apply = SubmitField("Apply Changes")
```

```python
@app.route("/user/add", methods=['GET', 'POST'])
def add_user():
    username = None
    form = UserForm()
    if form.validate_on_submit():
        user_email = Users.query.filter_by(email=form.email.data).first()
        user_username = Users.query.filter_by(username=form.username.data).first()
        if user_email is None and user_username is None:
            hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
            user = Users(username=form.username.data, email=form.email.data, password_hash=hashed_pw, currency=form.currency.data)  #, password=form.password.data)
            db.session.add(user)
            db.session.commit()
        elif user_email is None:
            flash("Username Taken")
            return redirect("/user/add")
        elif user_username is None:
            flash("Email already in use")
            return redirect("/user/add")
        elif user_email is not None and user_username is not None:
            flash("Email and Username Taken")
            return redirect("/user/add")
        username = form.username.data
        form.username.data = ''
        form.email.data = ''
        form.password_hash.data = ''
        #form.password.data = ''

        flash("User Added Successfully - " + username)
    our_users = Users.query.order_by(Users.date_added)
    return render_template("signup.html", form=form, username=username, our_users=our_users)
```
