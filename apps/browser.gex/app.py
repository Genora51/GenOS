from browser import document

hist = []

def urlChanged():
	hist.append(document['ifr']