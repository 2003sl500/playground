from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<string:color>/<string:shadowcolor>/<int:times>')
def play(color, shadowcolor, times):
    return render_template('index.html', color = color, shadowcolor = shadowcolor, times = times)
if __name__ == "__main__":
    app.run(debug=True)