from flask import Flask, render_template

app = Flask(__name__)

project_data = {
    1 : {"호선명" : "우이신설선", "이용객수" : {"승차총승객수" : 4614, "하차총승객수" : 4561}},
    2 : {"호선명" : "경원선", "이용객수" : {"승차총승객수" : 7451, "하차총승객수" : 7248}}
}

@app.route('/')

def index():
    return render_template("index.html", 
            template_project = project_data)
@app.route("/project/<int:id>")
def project(id):
    return render_template("more.html", 
            template_name=project_data[id]["호선명"], 
            template_p=project_data[id]["이용객수"])
if __name__ == '__main__':
    app.run(debug=True)