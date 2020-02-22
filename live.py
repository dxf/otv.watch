from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def header():
    import getstatus
    return render_template('live.html',monstercat=getstatus.monstercat,poki=getstatus.poki,scarra=getstatus.scarra,lily=getstatus.lily,fed=getstatus.fed,yvonne=getstatus.yvonne)
app.run()