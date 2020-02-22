import twitch
from flask import Flask, render_template
app = Flask(__name__)
helix = twitch.Helix('lr8ok7604ketqe6qq5kq1bdieibcpu')
monstercat = bool(helix.user('monstercat').is_live)
poki = bool(helix.user('pokimane').is_live)
scarra = bool(helix.user('scarra').is_live)
lily = bool(helix.user('lilypichu').is_live)
fed = bool(helix.user('fedmyster').is_live)
yvonne = bool(helix.user('yvonnie').is_live)
tpp = bool(helix.user('twitchplayspokemon').is_live)
print(monstercat)
@app.route('/')
def header():
    return render_template('live.html',monstercat=monstercat,poki=poki,scarra=scarra,lily=lily,fed=fed,yvonne=yvonne,tpp=tpp)
app.run()