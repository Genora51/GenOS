from browser import window
jq = window.jQuery

def toggleStart():
    if(jq('.home').hasClass('open')):
        jq('.startWin').removeClass('active')
        jq('.home').removeClass('open')
    else:
        jq('.startWin').addClass('active')
        jq('.home').addClass('open')

def startTS():
    jq('[toggleStart]').click(toggleStart)

jq(startTS)