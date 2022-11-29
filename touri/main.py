from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot

app = Flask("Touri")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
