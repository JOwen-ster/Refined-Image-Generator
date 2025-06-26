from flask import Flask
from flask import render_template


app = Flask(__name__,
            template_folder='routes',
            static_folder='routes/assets'
)


@app.route("/")
def landing():
    return render_template('index.html')

# Frontend built in React
# Use pnpm run build to create static files
# Serve static files as flask templates (re-named to routes)
