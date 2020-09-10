from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def header():
    import getstatus
    return render_template('live.html',monstercat=getstatus.monstercat,poki=getstatus.poki,scarra=getstatus.scarra,lily=getstatus.lily,yvonne=getstatus.yvonne)
if __name__ == '__main__':
    app.run()
