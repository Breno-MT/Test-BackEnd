import os

from src.app import create_app


app = create_app(os.getenv('FLASK_ENV'))


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)), host="0.0.0.0", debug=False)

