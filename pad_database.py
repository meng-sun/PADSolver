from __future__ import print_function
import pad
import copy
f = open('pad_database.txt', 'w')
error = []
#10 combo grids
combo10 = [[(0,0), (0,1), (0,2)], [(0, 3), (0, 4), (0, 5)], [(1,0), (1,1), (1,2)], [(1, 3), (1, 4), (1, 5)], [(2,0), (2,1), (2,2)], [(2, 3), (2, 4), (2, 5)],
			[(3,0), (3,1), (3,2)], [(3, 3), (3, 4), (3, 5)], [(4,0), (4,1), (4,2)], [(4, 3), (4, 4), (4, 5)]
			]

#to string
def toString(a):
	string = ''
	for o in a:
		for t in o:
			string += str(t)
	return string

#to board
def toBoard(string, bot):
	g = []
	bot_copy = bot[:]
	for r in range(0,4):
		g.append([])
		for l in string[r*6:(r*6)+6]:
			g[r].append(int(l))
	g.append(bot_copy)
	gb = pad.Board()
	g_copy = g[:]
	gb.uploadBoard(g_copy)
	return gb


# find all solutions > 7
def ifSolution(b,db):
	global error
	b_copy = copy.deepcopy(b.grid)
	
	#print("gridcopy: ",end='')
	#print(b_copy)
	#print("normal", end='')
	#b.printBoard()
	b_extend = ""
	#u = raw_input("please press enter")
	
	if pad.boardSim(b)>= 7:
		#print(">=7") 
		b_extend = toString(b_copy)

		add = True
		for i in db:
			if i is b_extend:
				add = False

		if add:
			db.append(b_extend)
			#print(b_extend)
			#u = raw_input("enter")
			f.write(b_extend)
			f.write("\n")

def get789Combo():

	dictn = {	0: 0,
					1: 1,
					2: 1,
					3: 2,
					4: 1,
					5: 2,
					6: 2,
					7: 3,
					8: 1,
					9: 2,
					10: 2,
					11: 3,
					12: 2,
					13: 3,
					14: 3,
					15: 4,
					16: 1,
					17: 2,
					18: 2,
					19: 3,
					20: 2,
					21: 3,
					22: 3,
					23: 4,
					24: 2,
					25: 3,
					26: 3,
					27: 4,
					28: 3,
					29: 4,
					30: 4,
					31: 5,
					32: 1,
					33: 2,
					34: 2,
					35: 3,
					36: 2,
					37: 3,
					38: 3,
					39: 4,
					40: 2,
					41: 3,
					42: 3,
					43: 4,
					44: 3,
					45: 4,
					46: 4,
					47: 5,
					48: 2,
					49: 3,
					50: 3,
					51: 4,
					52: 3,
					53: 4,
					54: 4,
					55: 5,
					56: 3,
					57: 4,
					58: 4,
					59: 5,
					60: 4,
					61: 5,
					62: 5,
					63: 6

	}

	dictb = {	0: '000000',
					1: '000001',
					2: '000010',
					3: '000011',
					4: '000100',
					5: '000101',
					6: '000110',
					7: '000111',
					8: '001000',
					9: '001001',
					10:'001010',
					11:'001011',
					12:'001100',
					13:'001101',
					14:'001110',
					15:'001111',
					16:'010000',
					17:'010001',
					18:'010010',
					19:'010011',
					20:'010100',
					21:'010101',
					22:'010110',
					23:'010111',
					24:'011000',
					25:'011001',
					26:'011010',
					27:'011011',
					28:'011100',
					29:'011101',
					30:'011110',
					31:'011111',
					32:'100000',
					33:'100001',
					34:'100010',
					35:'100011',
					36:'100100',
					37:'100101',
					38:'100110',
					39:'100111',
					40:'101000',
					41:'101001',
					42:'101010',
					43:'101011',
					44:'101100',
					45:'101101',
					46:'101110',
					47:'101111',
					48:'110000',
					49:'110001',
					50:'110010',
					51:'110011',
					52:'110100',
					53:'110101',
					54:'110110',
					55:'110111',
					56:'111000',
					57:'111001',
					58:'111010',
					59:'111011',
					60:'111100',
					61:'111101',
					62:'111110',
					63:'111111'
	}

	print("running...")
	for f in range(-4, 4, 1):
		#arbitrary cap on recursion size
		if f >= 0:
			bot = [2,2,2,2,2,2]
			bot[f:f+3] = [1, 1, 1] 
		else:
			bot = [1, 1, 1, 1, 1, 1]
			bot[-(f+1):(-(f+1))+3] = [2, 2, 2] 

		database = []
		for n in range(0,64):
			code = [0,0,0,0]
			code[0] = n
			for o in range(0,64):
				code[1] = o
				for p in range(0,64):
					code[2] = p
					for q in range(0,64):
						code[3] = q

		
						total = 0
						code_extend = ""
						for c in code:
							total += dictn[c]
							code_extend += dictb[c].replace('0','2')
						
						cb = toBoard(code_extend, bot)
						#print("code ", end='')
						#print(code_extend, end=', ')
						#print("total ", end='')
						#print(total)
						#u = raw_input("press enter")
						if total > 8 and total < 22:
							ifSolution(cb, database)

	#return database


try:
	a = get789Combo()
except:
	print(error)
	raise
#print(a)


f.close()

