import twitch
helix = twitch.Helix('lr8ok7604ketqe6qq5kq1bdieibcpu')
poki = bool(helix.user('pokimane').is_live)
scarra = bool(helix.user('scarra').is_live)
lily = bool(helix.user('lilypichu').is_live)
fed = bool(helix.user('fedmyster').is_live)
yvonne = bool(helix.user('yvonnie').is_live)
monstercat = bool(helix.user('monstercat').is_live)
