import webbrowser, os, sys
from urllib.request import urlretrieve


def downloadPDF(problem):
	url = "https://uva.onlinejudge.org/external/%s/%s.pdf" % (problem[:-2], problem)
	file = f"./PDF/{problem}.pdf"
	urlretrieve(url, file)
	return file

def problemToId(problem):
	category = int(problem[:-2])
	number = int(problem[-2:])
	if category == 112:
		if number <= 43:                    return 2141 + number
		elif number >= 44 and number <= 52: return 2157 + number
		elif number >= 53 and number <= 69: return 2167 + number
		elif number >= 70:                  return 2175 + number
	elif category == 113:
		if number <= 52:                    return 2275 + number
		elif number >= 53 and number <= 70: return 2285 + number
		elif number >= 71:                  return 2295 + number
	elif category == 115:
		if number <= 54:                    return 2495 + number
		elif number >= 55 and number <= 64: return 2536 + number
		elif number >= 65:                  return 2547 + number
	elif category == 117:
		if number <= 22:                    return 2747 + number
		elif number >= 23:                  return 2800 + number
	elif category == 118:
		if number <= 76:                    return 2900 + number
		elif number >= 77 and number <= 87: return 2922 + number
		elif number >= 88 and number <= 98: return 2900 + number
		elif number == 99:                  return 3050
	elif category == 120:
		if number <= 48:                    return 3151 + number
		elif number >= 49:                  return 3152 + number
	elif category == 122:
		if number <= 88:                    return 3352 + number
		elif number >= 89:                  return 3621 + number
	elif category == 123:
		if number <= 96:                    return 3722 + number
		elif number >= 97:                  return 3731 + number
	elif category == 124:
		if number <= 60:                    return 3831 + number
		elif number >= 61 and number <= 64: return 3843 + number
		elif number >= 65:                  return 3844 + number
	elif category == 125:
		if number <= 12:                    return 3944 + number
		elif number >= 13 and number <= 91: return 3945 + number
		elif number >= 92:                  return 4178 + number
	elif category == 126:
		if number <= 19:                    return 4278 + number
		elif number >= 20 and number <= 26: return 4323 + number
		elif number >= 27 and number <= 36: return 4325 + number
		elif number >= 37 and number <= 45: return 4348 + number
		elif number >= 46 and number <= 55: return 4329 + number
		elif number >= 56:                  return 4338 + number
	elif category == 127:
		if number <= 19:                    return 4438 + number
		elif number >= 20 and number <= 30: return 4552 + number
		elif number >= 31 and number <= 80: return 4553 + number
		elif number >= 81:                  return 4565 + number
	elif category == 129:
		if number <= 15:                    return 4765 + number
		elif number >= 16 and number <= 80: return 4779 + number
		elif number >= 81:                  return 4783 + number
	elif category == 130:
		if number <= 33:                    return 4888 + number
		elif number >= 34:                  return 4898 + number
	elif category == 131:
		if number <=  4:                    return 4998 + number
		elif number >=  5 and number <= 94: return 5011 + number
		elif number >= 95:                  return 5023 + number
	elif category == 132:
		if number <= 63:                    return 5123 + number
		elif number >= 64:                  return 5124 + number
	else:
		return submitProblemIdBegin[category] + number


def view(problem):
	file = downloadPDF(problem)
	webbrowser.open("file://" + os.path.realpath(file))

submitProblemIdBegin = {
	  1:   36,
	  2:  136,
	  3:  236,
	  4:  341,
	  5:  441,
	  6:  541,
	  7:  641,
	  8:  741,
	  9:  841,
	100:  941,
	101: 1041,
	102: 1141,
	103: 1241,
	104: 1341,
	105: 1441,
	106: 1541,
	107: 1641,
	108: 1741,
	109: 1841,
	110: 1941,
	111: 2041,
	114: 2395,
	116: 2647,
	119: 3151,
	121: 3252,
	128: 4665,
	133: 5224
}
def submit(problem):
	id = problemToId(problem)
	webbrowser.open("https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid=" + str(id))


def eval(mode, problem):
	try:
		if mode in ["v", "view"]:
			view(problem)
		elif mode in ["s", "submit"]:
			submit(problem)
		else:
			print(f"Invalid mode: {mode}")
	except:
		print("Error")

def main(argv):
	if len(argv) == 3:
		eval(argv[1], argv[2])
	else:
		while 1:
			mode = input("Mode [v/view; s/submit]: ")
			problem = input("Problem: ")
			eval(mode, problem)
			print("\n\n")

if __name__ == "__main__":
	main(sys.argv)