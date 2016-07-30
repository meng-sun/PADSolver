from __future__ import print_function
import random


class Board:

	def __init__(self):
		self.numsOfOrbs = [0,0,0,0,0]
		self.grid = []

	# set up random board
	def getNewBoard(self):
		for count in range(0,5):
			self.grid.append([])
			for count2 in range(0,6):
				randInt = 1+int(random.random()*5)
				self.numsOfOrbs[randInt-1] +=1
				self.grid[count].append(randInt)

	#input board
	def uploadBoard(self, g):
		self.grid = g[:]

	# print board
	def printBoard(self):
		for row in self.grid:
			print(row)

	#print number of total possible 3 matches
	# 1=R, 2=Y, 3=G, 4=B, 5=P
	def printMatches(self):
		print("\nRed orbs: "+str(numsOfOrbs[0]))
		print("Yellow orbs: "+str(numsOfOrbs[1]))
		print("Green orbs: "+str(numsOfOrbs[2]))
		print("Blue orbs: "+str(numsOfOrbs[3]))
		print("Dark orbs: "+str(numsOfOrbs[4]))

	#access database
	def getFinalBoard(self):
		for origOrb in cropGrid:
			if origOrb[0] is not finGrid[origOrb[1][0]][origOrb[1][1]]:
				a=0
				#nothing here

	#Heuristic
	def getPath(self):
		a = 0

	#GridSolver
	def match(self):
		combos = []
		for _r in range(0,5):
			for _c in range(0,6):
				if self.grid[_r][_c] != 0:
					color = self.grid[_r][_c]
					orbGroup = []
					placehold = 0
					madeCombos = False
					doWhile = True
					ok = True
					while doWhile:
						
						if placehold == 0:
							r = _r
							c = _c
						else:
							(r, c) = orbGroup[placehold]

						loc = []
						first = True
						for i in [(0,1), (1,0)]:	
							n = -6
							while n < 7:
								newR = r+(n*i[1])
								newC = c+(n*i[0])
								if newR >= 0 and newR < 5 and newC >= 0 and newC < 6 and color == self.grid[newR][newC]:
									if not first:
										loc.append((newR, newC))
									else:
										if n == 1 or n == -1 or ( n == -2 and color == self.grid[r-i[1]][c-i[0]]):
											first = False
											loc.append((newR, newC))
										# else:

										# 	print("old: ",end=' ')
										# 	print(r, end=", ")
										# 	print(c, end="\t")
										# 	print("added: ",end=' ')
										# 	print(newR, end=", ")
										# 	print(newC)
								else:
									if len(loc) > 2:
										for it in loc:
											add = True
											for o in orbGroup:
												if it == o:
													add = False
											if add:
												orbGroup.append(it)
										madeCombos = True
										if first == False:
											n = 7

									loc = []
								n += 1
						
						placehold += 1

						if placehold >= len(orbGroup):
							doWhile = False

					if madeCombos:
						for o in orbGroup:
							self.grid[o[0]][o[1]] = 0
						tup = (orbGroup, color)
						combos.append(tup)

					else:
						self.grid[_r][_c] = color

		return combos

	def shuffleDown(self):
		for r in range(4, -1, -1):
			for c in range(0, 6):
				if self.grid[r][c] is 0:
					tempR = r
					for remR in range(r, -1, -1):
						if self.grid[remR][c] != 0:
							self.grid[tempR][c] = self.grid[remR][c]
							self.grid[remR][c] = 0
							tempR -= 1


def boardSim(b):
	cont = True
	numOfCombos = 0
	while cont:
		comb = b.match()
		groupsToMerge = []
		for c_n in range(len(comb)):
			c = comb[c_n][0]
			clr = comb[c_n][1]
			for c_n2 in range(len(comb)):
				c2 = comb[c_n2][0]
				clr2 = comb[c_n2][1]
				if ((c is not c2) and (clr == clr2)):
					for (x,y) in c:
						for (x2, y2) in c2:
							count = 0
							movem = [(0,1), (1,0), (0, -1), (-1, 0)]
							while count < 4:
								(mx, my) = movem[count]
								if (x+mx) == x2 and (y+my) == y2:
									for i in [(0,1), (1,0), (0, -1), (-1, 0)]:
										xf = x+i[0]
										yf = y+i[1]
										xf2 = x2+i[0]
										yf2 = y2+i[1]
										for (tx, ty) in c:
											if xf == tx and yf == ty:

												if (xf+mx) == xf2 and (yf+my) == yf2:
													count = 3
													add = True
													for (g1,g2) in groupsToMerge:
														if (g1 == c_n and g2==c_n2) or (g1==c_n2 and g2==c_n):
															add = False
													if add:
														if c_n > c_n2:
															max_i = c_n
															min_i = c_n2
														else:
															min_i = c_n
															max_i = c_n2
														groupsToMerge.append((max_i, min_i))
								count += 1


		groupsToMerge = sorted(groupsToMerge, key = lambda tup: tup[0], reverse = True)
		#print("cmb: ",end= '')
		#print(comb)
		#print("gtm: ",end = '')
		#print(groupsToMerge)
		dictGTM = {}
		try:
			for o,t in groupsToMerge:
				while t in dictGTM:
					t = dictGTM[t]
				while o in dictGTM:
					o = dictGTM[o]

				if o > t:
					comb[t][0].extend(comb[o][0])
					dictGTM[o] = t
				else:
					comb[o][0].extend(comb[t][0])
					dictGTM[t] = o

					
				del comb[t]
		except:
			print(comb)
			print(o)
			print(t)
			print(dictGTM)
			print(groupsToMerge)
			b.printBoard()
			raise

		#print("combos= ", end='')
		#print(comb)
		numOfCombos += len(comb)
		b.shuffleDown()
		#print("fromboardsim: ", end='')
		#b.printBoard()
		#print("\n")
		if len(comb) == 0:
			cont = False
	#print("combos: ",end= ' ')
	#print(numOfCombos)
	#print("\n")
	return numOfCombos


# b = Board()
# b.getNewBoard()
# b.printBoard()
# print("\n")
# a = boardSim(b)
# b.printBoard()
# print(a)
# print("\n")








