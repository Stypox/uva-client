import webbrowser, os, sys, subprocess, platform
from urllib.request import urlretrieve

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
	 10: 3441,
	 11: 3541,
	 13: 4046,
	 14: 4146,
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

def problemToId(problem):
	volume = int(problem[:-2])
	number = int(problem[-2:])
	if volume == 12:
		if number <= 68:                    return 3641 + number
		elif number == 69:                  return 3721
		elif number >= 70 and number <= 78: return 3749 + number
		elif number >= 79 and number <= 90: return 3813 + number
		elif number >= 91:                  return 3946 + number
	elif volume == 15:
		if number <= 21:                    return 4246 + number
		elif number == 22:                  return 2812
		elif number >= 23 and number <= 67: return 4275 + number
		elif number >= 68 and number <= 69: return 4282 + number
		elif number >= 70 and number <= 82: return 4292 + number
		elif number >= 83:                  return 4375 + number
	elif volume == 16:
		if number <= 96:                    return 4475 + number
		elif number >= 97:                  return 4537 + number
	elif volume == 17:
		if number <=  8:                    return 4637 + number
		elif number >=  9 and number <= 21: return 4773 + number
		elif number >= 22 and number <= 25: return 4838 + number
		elif number >= 26 and number <= 35: return 4896 + number
		elif number >= 36 and number <= 48: return 4967 + number
		elif number >= 49:                  return 5057 + number
	elif volume == 112:
		if number <= 43:                    return 2141 + number
		elif number >= 44 and number <= 52: return 2157 + number
		elif number >= 53 and number <= 69: return 2167 + number
		elif number >= 70:                  return 2175 + number
	elif volume == 113:
		if number <= 52:                    return 2275 + number
		elif number >= 53 and number <= 70: return 2285 + number
		elif number >= 71:                  return 2295 + number
	elif volume == 115:
		if number <= 54:                    return 2495 + number
		elif number >= 55 and number <= 64: return 2536 + number
		elif number >= 65:                  return 2547 + number
	elif volume == 117:
		if number <= 22:                    return 2747 + number
		elif number >= 23:                  return 2800 + number
	elif volume == 118:
		if number <= 76:                    return 2900 + number
		elif number >= 77 and number <= 87: return 2922 + number
		elif number >= 88 and number <= 98: return 2900 + number
		elif number == 99:                  return 3050
	elif volume == 120:
		if number <= 48:                    return 3151 + number
		elif number >= 49:                  return 3152 + number
	elif volume == 122:
		if number <= 88:                    return 3352 + number
		elif number >= 89:                  return 3621 + number
	elif volume == 123:
		if number <= 96:                    return 3722 + number
		elif number >= 97:                  return 3731 + number
	elif volume == 124:
		if number <= 60:                    return 3831 + number
		elif number >= 61 and number <= 64: return 3843 + number
		elif number >= 65:                  return 3844 + number
	elif volume == 125:
		if number <= 12:                    return 3944 + number
		elif number >= 13 and number <= 91: return 3945 + number
		elif number >= 92:                  return 4178 + number
	elif volume == 126:
		if number <= 19:                    return 4278 + number
		elif number >= 20 and number <= 26: return 4323 + number
		elif number >= 27 and number <= 36: return 4325 + number
		elif number >= 37 and number <= 45: return 4348 + number
		elif number >= 46 and number <= 55: return 4329 + number
		elif number >= 56:                  return 4338 + number
	elif volume == 127:
		if number <= 19:                    return 4438 + number
		elif number >= 20 and number <= 30: return 4552 + number
		elif number >= 31 and number <= 80: return 4553 + number
		elif number >= 81:                  return 4565 + number
	elif volume == 129:
		if number <= 15:                    return 4765 + number
		elif number >= 16 and number <= 80: return 4779 + number
		elif number >= 81:                  return 4783 + number
	elif volume == 130:
		if number <= 33:                    return 4888 + number
		elif number >= 34:                  return 4898 + number
	elif volume == 131:
		if number <=  4:                    return 4998 + number
		elif number >=  5 and number <= 94: return 5011 + number
		elif number >= 95:                  return 5023 + number
	elif volume == 132:
		if number <= 63:                    return 5123 + number
		elif number >= 64:                  return 5124 + number
	else:
		return submitProblemIdBegin[volume] + number


def downloadPDF(problem):
	url = f"https://uva.onlinejudge.org/external/{problem[:-2]}/{problem}.pdf"
	dir = "./PDF/"
	file = f"{dir}{problem}.pdf"
	print("Downloading pdf", file, "from", url)

	os.makedirs(dir, exist_ok=True)
	urlretrieve(url, file)
	return file

def view(problem, flag):
	filepath = downloadPDF(problem)
	filepath = os.path.realpath(filepath)
	filepathProtocol = "file://" + filepath
	
	vscodeAliases = ["code", "codium", "vscodium", "vscode"]
	if flag in vscodeAliases:
		for program in vscodeAliases:
			try:
				subprocess.check_output(("which", program))
				subprocess.call((program, filepath))
				break
			except:
				pass
	else:
		if platform.system() == 'Darwin':
			subprocess.call(('open', filepathProtocol))
		elif platform.system() == 'Windows':
			os.startfile(filepathProtocol)
		else: # Linux
			subprocess.call(('xdg-open', filepathProtocol))

def submit(problem):
	id = problemToId(problem)
	url = f"https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid={id}"
	print("Submit url:", url)
	webbrowser.open(url)


def eval(mode, problem, flag):
	try:
		if mode in ["v", "view"]:
			view(problem, flag)
		elif mode in ["s", "submit"]:
			submit(problem)
		elif mode in ["d", "download"]:
			downloadPDF(problem)
		else:
			print(f"Invalid mode: {mode}")
	except Exception as e:
		print("Error:", e)

def main(argv):
	if len(argv) in [3, 4]:
		eval(argv[1], argv[2], argv[3] if len(argv) == 4 else "")
	else:
		while 1:
			mode = input("Mode [v/view; s/submit; d/download]: ")
			problem = input("Problem: ")
			if mode in ["v", "view"]:
				flag = input("Program to use for view (code/codium/vscodium/vscode for vscode; leave empty for default): ")
			else:
				flag = ""
			eval(mode, problem, flag)
			print("\n\n")

if __name__ == "__main__":
	main(sys.argv)
