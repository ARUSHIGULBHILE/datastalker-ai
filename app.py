from flask import Flask, render_template
from database.db import init_db
from routes.api_routes import api_bp


app = Flask(__name__)

# Register API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)