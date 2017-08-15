from browser import document


def exists(obj, attName):
    try:
        getattr(obj, attName)
        return True
    except AttributeError:
        return False


def goFull():
    docelem = document.documentElement
    try:
        document.fullscreenElement
    except AttributeError:
        if exists(docelem, 'requestFullscreen'):
            docelem.requestFullscreen()
        elif exists(docelem, 'mozRequestFullScreen'):
            docelem.mozRequestFullScreen()
        elif exists(docelem, 'webkitRequestFullscreen'):
            docelem.webkitRequestFullscreen()
        elif exists(docelem, 'msRequestFullscreen'):
            docelem.msRequestFullscreen()


document.bind('click', goFull)
