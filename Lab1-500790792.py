def getName():
	return "Fiorante, Nicole"
	
class Pathfinder():

    def __init__(self, vector):
        self.vector = vector
        self.paths = []
        self.findAllPaths(0,[])
        

    def findAllPaths(self, position, solution):
        if ((position > len(self.vector)) or (position < 0) or (position in solution)):
            return None
        elif self.vector[position] == 0:
            solution.append(position)
            self.paths.append(solution)
            return None
        else:
            solution.append(position)
            x = self.vector[position]
            self.findAllPaths(position + x, solution.copy())
            self.findAllPaths(position - x, solution.copy())
            
    def getLongest(self):
        longest = self.paths[0]
        length2 = len(self.paths[0])
        for m in range(1, len(self.paths)):
            if (len(self.paths[m]) > len(longest)):
                longest = self.paths[m]
        return longest
            
        
    def getShortest(self):
        shortest = self.paths[0]
        length3 = len(self.paths[0])
        for n in range(1, len(self.paths)):
            if (len(self.paths[n]) < len(shortest)):
                shortest = self.paths[n]
        return shortest


# TEST

v = [2, 8, 3, 2, 7, 2, 2, 3, 2, 1, 3, 0]
test1 = Pathfinder(v)
for p in test1.paths:
    print(p)

print ('longest: ')
print (test1.getLongest())

print ('shortest: ')
print (test1.getShortest())
