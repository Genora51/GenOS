from browser import document, window

class BaseApplication:    
    def __init__(self):
        self.j(document).ready(lambda: self.start())
        self.j(window).on('message', lambda e: self.message(e))

    def j(self, *args):
        return window.jQuery(*args)

    def message(self, e):
        event = e.originalEvent
        data = event.data
        if data.name == 'closeEvent':
            self.onClosed()
        else:
            self.onMessage(event)

    def onMessage(self, event):
        pass

    def start(self):
        pass

    def tellOS(self, message):
        window.parent.postMessage(message, '*')

    def close(self):
        self.tellOS({'name' : 'closeWindow'})

    def onClosed(self):
        self.close()

    def makeWindow(self, path):
        self.tellOS({
            'name' : 'makeWindow',
            'path' : path
        })

    def makeDialog(self, path):
        self.tellOS({
            'name' : 'makeDialog',
            'path' : path
        })