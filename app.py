from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('dashboard.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)