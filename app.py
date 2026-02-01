"""
Telkomsel FleetSight Racing - Asphalt 8 Style
Premium 3D Racing Game untuk C-Level Presentation
"""

import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# Explicitly serve static files
@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static', 'css'), filename)

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static', 'js'), filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║  🏎️  TELKOMSEL FLEETSIGHT RACING - ASPHALT STYLE  🏎️          ║
    ║  Server: http://localhost:5000                                 ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    app.run(debug=True, host='0.0.0.0', port=5000)
