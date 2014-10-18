import urllib

### GATHER ALL SCANS ###
def getScans():
	# urlretrieve takes the image to save and the place to save it to. Does this automatically.
	for i in range(1, 150):
		urllib.urlretrieve("http://www.serebii.net/card/boundariescrossed/" + str(i) + ".jpg", "/pythonProjects/Pokemon/bcrScans/" + str(i) + '-149' + ".jpg")
		print "Card added to collection."
	for i in range(1, 136):
		urllib.urlretrieve("http://www.serebii.net/card/plasmastorm/" + str(i) + ".jpg", '/pythonProjects/Pokemon/plsScans/' + str(i) + '-135' + '.jpg')
		print "Card added to collection."
	for i in range(1, 117):
		urllib.urlretrieve("http://www.serebii.net/card/plasmafreeze/" + str(i) + ".jpg", '/pythonProjects/Pokemon/plfScans/' + str(i) + '-116' + '.jpg')
		print "Card added to collection."
	for i in range(1, 114):
		urllib.urlretrieve("http://www.serebii.net/card/legendarytreasures/" + str(i) + ".jpg", '/pythonProjects/Pokemon/ltrScans/' + str(i) + '-113' + '.jpg')
		print "Card added to collection."
	for i in range(1, 40):
		urllib.urlretrieve("http://www.serebii.net/card/kalosstarterset/" + str(i) + ".jpg", '/pythonProjects/Pokemon/kssScans/' + str(i) + '-39' + '.jpg')
		print "Card added to collection."
	for i in range(1, 147):
		urllib.urlretrieve("http://www.serebii.net/card/xy/" + str(i) + ".jpg", '/pythonProjects/Pokemon/xyScans/' + str(i) + '-146' + '.jpg')
		print "Card added to collection."
	for i in range(1, 107):
		urllib.urlretrieve('http://www.serebii.net/card/flashfire/' + str(i) + ".jpg", '/pythonProjects/Pokemon/flfScans/' + str(i) + '-106' + '.jpg')
		print "Card added to collection."
	for i in range(1, 112):
		urllib.urlretrieve('http://www.serebii.net/card/furiousfists/' + str(i) + ".jpg", '/pythonProjects/Pokemon/ffScans/' + str(i) + '-111' + '.jpg')
		print "Card added to collection."

	return "All scans downloaded."

print getScans()