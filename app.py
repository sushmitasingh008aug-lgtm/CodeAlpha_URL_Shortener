from flask import Flask, render_template
from flasgger import Swagger

from routes import url_routes


# Create Flask application
app = Flask(__name__)

# Enable Swagger
swagger = Swagger(app)

# Register URL routes
app.register_blueprint(url_routes)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Run application
if __name__ == "__main__":
    app.run(debug=True)