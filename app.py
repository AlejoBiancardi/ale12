from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tu_archivo_html.html')

@app.route('/redireccionar', methods=['GET'])
def redireccionar():
    # Redirigir a "nose.html"
    return redirect('/nose.html')

if __name__ == '__main__':
    app.run(debug=True)
