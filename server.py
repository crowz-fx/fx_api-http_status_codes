from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")

app.add_api('swagger.yml')

@app.route('/')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)