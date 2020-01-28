def draw_park(length = 5, width = 5):
    print ("this is a park")
    if length < 0 or width < 0:
    	#print("value error")
        raise ValueError("length or width is undefined")
    for i in range(length):
    	if i == 0 or i == length - 1:
    		print()
    		for j in range(width):
    			print("=", end = "")
    	else:
    		print()
    		for k in range(width):
    			if k == 0 or k == width - 1:
    				print("||", end = "")
    			else:
    				print(" ", end = "")

    print()
    return
