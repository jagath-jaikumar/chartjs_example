from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    data = [1,3,2]
    labels = ['M','T','W']

    gauge = {
     "value" :  56,
     "gage_title" : "my gauge"
    }

    return render_template('index.html', labels = labels, data = data, gauge = gauge)


if __name__ == "__main__":
    app.run()
