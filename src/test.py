from flask import Flask, render_template
import os

app = Flask(__name__)

# Serve static files from the 'public' directory
app.static_folder = 'public'

# Define a route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
