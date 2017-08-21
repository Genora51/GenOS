from browser import document, window

class Application:

    def goHome():
        iframe = document['ifr']
        iframe.src = iframe.src

    def checkChange(self, event):
        if event.keyCode == 13:
            iframe = document['ifr']
            iframe.src = self.j('.searchbar').val()

    def start(self):
        self.j('.home').click(self.goHome)
        self.j('.searchbar').on('keydown', lambda e: self.checkChange(e))