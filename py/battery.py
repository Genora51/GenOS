from browser import window, document
navigator = window.navigator

def doBat(battery):
    window.battery = battery
    document['battery'].innerHTML = str(int(battery.level * 100)) + '%'


navigator.getBattery().then(doBat)