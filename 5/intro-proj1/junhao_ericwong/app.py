from flask import Flask,render_template

app = Flask(__name__)

if __name__=="__main__":
    app.debug=True
    app.run()

@app.route("/")
def main():
    return render_template("main.html")

one = open('2012draft.csv', 'r')
info1 = open.readlines()
one.close()

two = open('2012draftexpress.csv', 'r')
info2 = open.readlines()
two.close()

three = open('2012NBAdraft.csv', 'r')
info3 = open.readlines()
three.close()

def formatdata(info):
    newdata = []
    for index in range(len(info)):
        line = info[index]
        line = line.replace('\n' , '')
        line = line.split(',')
        newdata.append(line)
    return newdata

def getanalysisinfo():
    analysis = {}
    draft = formatdata(info1)
    draftexpress = formatdata(info2)
    NBAdraft = formatdata(info3)
    for pick in range(1, 32):
        index = pick - 1
        analysis[pick] = [draft[index][0], draft[index][2], draftexpress[index][2], NBAdraft[index][2]]
    return analysis

info = getanalysisinfo()

@app.route("/draft")
def draft():
    return render_template("draft.html",info)

@app.route("/stat")
def stat():
    return render_template("stat.html")


