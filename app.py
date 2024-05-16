import os
from core import app

if __name__ == "__main__":
    is_debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=is_debug)