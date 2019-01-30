import sys
from random import randint
class Piece(object):

   def __init__(self):
      self.ud='Z'
      self.lr='Z'
      self.fb='Z'
   
   def UDfrom(self, p):
      self.ud=p.ud
      self.lr=p.fb
      self.fb=p.lr
      
   def LRfrom(self, p):
      self.ud=p.fb
      self.lr=p.lr
      self.fb=p.ud
      
   def FBfrom(self, p):
      self.ud=p.lr
      self.lr=p.ud
      self.fb=p.fb
      
   def becomes(self, p):
      self.ud=p.ud
      self.lr=p.lr
      self.fb=p.fb
      
   def contains(self, c):
      return self.ud==c or self.lr==c or self.fb==c
      
   def isLike(self, p):
      return self.contains(p.ud) and self.contains(p.lr) and self.contains(p.fb)
      
   def __str__( self ):
      return self.ud+self.lr+self.fb
      
      
def resetCube():
   for i in range(0, last):
      for j in range(0, last):
         cube[i][0][j].ud='W'
         cube[i][last-1][j].ud='Y'
         cube[i][j][0].lr='O'
         cube[i][j][last-1].lr='R'
         cube[0][i][j].fb='G'
         cube[last-1][i][j].fb='B'
        
def showCube():
   print("Top:")
   for d in range(0, last+1):
      for c in range(0, last+1):
         sys.stdout.write(cube[last-d][0][c].ud)
      print()
   print()
   print("Left:")
   for r in range(0, last+1):
      for d in range(0, last+1):
         sys.stdout.write(cube[last-d][r][0].lr)
      print()
   print()
   print("Front:")
   for r in range(0, last+1):
      for c in range(0, last+1):
         sys.stdout.write(cube[0][r][c].fb)
      print()
   print()
   print("Right:")
   for r in range(0, last+1):
      for d in range(0, last+1):
         sys.stdout.write(cube[d][r][last].lr)
      print()
   print()
   print("Back:")
   for r in range(0, last+1):
      for c in range(0, last+1):
         sys.stdout.write(cube[last][r][last-c].fb)
      print()
   print()
   print("Bottom:")
   for d in range(0, last+1):
      for c in range(0, last+1):
         sys.stdout.write(cube[d][last][c].ud)
      print()
   print()
      
def scrambleCube():
   n=10*last
   for i in range(0, n):
      num=randint(0, last)
      if randint(0, 1)<1:
         U(num)
      else:
         L(num)
      
def turnUD(r):
   #print("r", r)
   for i in range(0, last+1):
      for j in range(0, last+1):
         temp[i][j].UDfrom(cube[j][r][last-i])
   for i in range(0, last+1):
      for j in range(0, last+1):
         cube[i][r][j].becomes(temp[i][j])
    
def turnLR(c):
   #print("c", c)
   for i in range(0, last+1):
      for j in range(0, last+1):
         temp[i][j].LRfrom(cube[last-j][i][c])
   for i in range(0, last+1):
      for j in range(0, last+1):
         cube[i][j][c].becomes(temp[i][j])
         
def turnFB(d):
   #print("d", d)
   for i in range(0, last+1):
      for j in range(0, last+1):
         temp[i][j].FBfrom(cube[d][last-j][i])
   for i in range(0, last+1):
      for j in range(0, last+1):
         cube[d][i][j].becomes(temp[i][j])
        
def Rw():
   for c in range(0, middle+1):
      R(c)
      
def Rwp():
   for n in range(0, 3):
      Rw()
      
def Uw2():
   for r in range(0, middle+1):
      U2(r)
      
def Lw2():
   for c in range(0, middle+1):
      L(c)
      L(c)
      
def U(r):
   turnUD(r)
   
def U2(r):
   U(r)
   U(r)
      
def Ep():
   turnUD(1)
      
def Dp(n):
   turnUD(last-n)
   
def Y():
   for i in range(0, last+1):
      turnUD(i)
   
def Up(n):
   for i in range(0, 3):
      U(n)
      
def E():
   for i in range(0, 3):
      Ep()
      
def D(n):
   for i in range(0, 3):
      Dp(n)
      
def Yp():
   for i in range(0, 3):
      Y()
   
def L(n):
   turnLR(n)
      
def M():
   turnLR(1)
      
def Rp(n):
   turnLR(last-n)
   
def Xp():
   for i in range(0, last+1):
      turnLR(i)
      
def Lp(n):
   for i in range(0, 3):
      L(n)
      
def Mp():
   for i in range(0, 3):
      M()
      
def R(n):
   for i in range(0, 3):
      Rp(n)
      
def X():
   for i in range(0, 3):
      Xp()

def F(n):
   turnFB(n)
      
def S():
   turnFB(1)
      
def Bp(n):
   turnFB(last-n)
  
def Z():
   for i in range(0, last+1):
      turnFB(i)
      
def Fp(n):
   for i in range(0, 3):
      F(n)
      
def Sp():
   for i in range(0, 3):
      S()
      
def B(n):
   for i in range(0, 3):
      Bp(n)
   
def Zp():
   for i in range(0, 3):
      Z()
      
def flipEdge():
   Up(0)
   Rp(0)
   U(0)
   Fp(0)
   
def fixCorner():
   Rp(0)
   Dp(0)
   R(0)
   D(0)
   
def placeEdgeLeft():
   Up(0)
   Lp(0)
   U(0)
   L(0)
   U(0)
   F(0)
   Up(0)
   Fp(0)
   
def placeEdgeRight():
   U(0)
   R(0)
   Up(0)
   Rp(0)
   Up(0)
   Fp(0)
   U(0)
   F(0)
      
def makeCross():
   F(0)
   R(0)
   U(0)
   Rp(0)
   Up(0)
   Fp(0)
   
def goodEdges():
   good=0
   for i in range(0, 4):
      if cube[0][0][1].fb==cube[0][1][1].fb:
         good+=1
      Y()
   return good
   
def matchEdges():
   R(0)
   U(0)
   Rp(0)
   U(0)
   R(0)
   U2(0)
   Rp(0)
   U(0)
   
def allBad():
   for i in range(0, 4):
      if cube[0][0][last].contains(cube[0][1][1].fb) and cube[0][0][last].contains(cube[1][1][last].lr):
         return False
      Y()
   return True
   
def switchCorners():
   U(0)
   R(0)
   Up(0)
   Lp(0)
   U(0)
   Rp(0)
   Up(0)
   L(0)
   
def okayEdges(t):
   okay=0
   for i in range(0, 4):
      if cube[last][0][1].ud==t:
         okay+=1
      U(0)
   return okay
    
def okayCorners(t):
   okay=0
   for i in range(0, 4):
      if cube[0][0][0].contains(cube[1][1][0].lr) and cube[0][0][0].contains(cube[0][1][1].fb):
         okay+=1
      Y()
   return okay
   
def getEdgy(t):
   while goodEdges()<2:
      U(0)
   while cube[last][0][1].fb!=cube[last][1][1].fb:
      Y()
   if cube[0][0][1].fb==cube[0][1][1].fb and cube[1][0][last].lr!=cube[1][1][last].lr:
      matchEdges()
      Up(0)
   while cube[1][0][last].lr!=cube[1][1][last].lr or cube[last][0][1].fb!=cube[last][1][1].fb:
      Y()
   if cube[0][0][1].fb!=cube[0][1][1].fb:
      matchEdges()
   if okayCorners(t)<1:
      switchCorners()
   if okayCorners(t)==1:
      while not (cube[0][0][last].contains(cube[0][1][1].fb) and cube[0][0][last].contains(cube[1][1][last].lr)):
         Y()
   
def solveStandardCube():
   top=cube[1][0][1].ud
   for i in range(0, 4):
      while cube[0][0][1].contains(top) or cube[0][1][last].contains(top):
         while cube[0][last][1].contains(top):
            Dp(0)
         F(0)
      Y()
   for i in range(0, 4):
      while not (cube[0][last][1].contains(cube[0][1][1].fb) and cube[0][last][1].contains(top)):
         Dp(0)
      F(0)
      F(0)
      Y()
   for i in range(0, 4):
      if cube[0][0][1].ud!=top:
         flipEdge()
      Y()
   for i in range(0, 4):
      if cube[0][0][last].contains(top):
         while cube[0][last][last].contains(top):
            Dp(0)
         fixCorner()
      Y()
   for i in range(0, 4):
      while not (cube[0][last][last].contains(cube[0][1][1].fb) and cube[0][last][last].contains(cube[1][1][last].lr) and cube[0][last][last].contains(top)):
         Dp(0)
      while cube[0][0][last].fb!=cube[0][1][1].fb or cube[0][0][last].ud!=top:
         fixCorner()
      Y()
   Z()
   Z()
   top=cube[1][0][1].ud
   for i in range(0, 8):
      if cube[0][0][1].contains(top):
         while cube[0][1][last].contains(top):
            for r in range(1, last+1):
               turnUD(r)
         placeEdgeRight()
      U(0)
   for i in range(0, 4):
      while cube[0][0][1].contains(top):
         U(0)
      while cube[0][0][1].fb!=cube[0][1][1].fb:
         for r in range(1, last+1):
            turnUD(r)
      if cube[0][0][1].ud==cube[1][1][0].lr:
         placeEdgeLeft()
      else:
         placeEdgeRight()
      Y()
   if even:
      for i in range(0, 8):
         if cube[0][0][1].ud!=top:
            crossParity()
         U(0)
   else:
      if okayEdges(top)<1:
         makeCross()
      while cube[1][0][0].ud!=top:
         U(0)
      if cube[last][0][1].ud==top and cube[1][0][last].ud!=top:
         makeCross()
      if cube[0][0][1].ud==top and cube[1][0][last].ud!=top:
         U(0)
         makeCross()
      if cube[0][0][1].ud!=top:
         makeCross()
   getEdgy(top)
   if even:
      okay=okayCorners(top)
      if okay<1 or okay==2:
         cornerParity()
         getEdgy(top)
   while not (cube[0][0][0].contains(cube[0][1][1].fb) and cube[0][0][0].contains(cube[1][1][0].lr)):
      switchCorners()
   if even and okayCorners(top)<4:
      cornerParity()
      getEdgy(top)
      while not (cube[0][0][0].contains(cube[0][1][1].fb) and cube[0][0][0].contains(cube[1][1][0].lr)):
         switchCorners()
   for i in range(0, 4):
      while cube[0][0][last].ud!=top:
         fixCorner()
      U(0)
      
def turnFront(prime, clock):
   if (prime and clock) or not (prime or clock):
      Fp(0)
   else:
      F(0)     
      
def placeMiddle(r, c):
   prime=last-r==c
   n=r
   if prime:
      n=last-r
   L(c)
   turnFront(prime, True)
   Rp(n)
   turnFront(prime, False)
   Lp(c)
   turnFront(prime, True)
   R(n)
   turnFront(prime, False)
      
def placeMiddles():
   for i in range(1, last):
      for j in range(1, last):
         if cube[0][i][j].fb==top:
            while cube[last-i][0][j].ud==top:
               U(0)
            placeMiddle(i, j)
      
def bottomsUp():
   X()
   placeMiddles()
   Xp()
      
def fixEdges():
   mid=Piece()
   badEdges=True
   while badEdges:
      badEdges=False
      for i in range(0, 4):
         for j in range(0, 4):
            mid.becomes(cube[0][middle][last])
            for r in range(1, last):
               if not cube[0][r][last].isLike(mid):
                  badEdges=True
                  matchEdge(matchingEdge())
            F(0)
         Y()
      
def matchingEdge():
   mid=Piece()
   mid.becomes(cube[0][middle][last])
   for h in range(0, 2):
      for i in range(0, 2):
         for j in range(0, 4):
            for r in range(1, last):
               if cube[0][r][0].isLike(mid):
                  if i>0:
                     F(0)
                     F(0)
                     Y()
                     return last-r
                  return r
            L(0)
         Yp()
      L(0)
      L(0)
      F(0)
      F(0)
   L(0)
   L(0)
   F(0)
   F(0)
   print("nothing found", mid)
   showCube()
   return -1
      
def matchEdge(r):
   double=cube[0][r][0].isLike(cube[0][last-r][last])
   if double:
      L(0)
      L(0)
      D(r)
      D(r)
   else:
      Up(r)
   R(0)
   Fp(0)
   U(0)
   Rp(0)
   F(0)
   if double:
      Dp(r)
      Dp(r)
   else:
      U(r)
   Y()
   F(0)
   F(0)
      
def imperfectEdge():
   for i in range(0, 4):
      for j in range(0, 4):
         for c in range(1, last):
            if not cube[0][0][c].fb==cube[0][0][middle].fb:
               return c
         F(0)
      Y()
   return -1
      
def flipBigEdge(c):
   Rp(c)
   U2(0)
   L(c)
   F(0)
   F(0)
   Lp(c)
   F(0)
   F(0)
   R(c)
   R(c)
   U2(0)
   R(c)
   U2(0)
   Rp(c)
   U2(0)
   F(0)
   F(0)
   R(c)
   R(c)
      
def crossParity():
   Rw()
   U2(0)
   X()
   Rw()
   U2(0)
   Rw()
   U2(0)
   Rwp()
   U2(0)
   for c in range(0, middle+1):
      L(c)
   U2(0)
   Rwp()
   U2(0)
   Rw()
   U2(0)
   Rwp()
   U2(0)
   Rwp()
     
def cornerParity():
   Uw2()
   Lw2()
   U2(0)
   for c in range(0, middle):
      L(c+1)
      L(c+1)
   U2(0)
   Lw2()
   Uw2()
   
last=int(input("Which size cube would you like?"))
cube=[[[Piece() for c in range(0, last)] for r in range(0, last)]for d in range(0, last+1)]
temp=[[Piece() for c in range(0, last)] for r in range(0, last)]
resetCube()
even=last%2<1
last-=1
middle=int(last/2)
top='W'
scrambleCube()
showCube()
if last>2:
   if not even:
      if cube[middle][0][middle].ud!='W':
         if cube[middle][0][middle].ud=='Y':
            Xp()
         while cube[0][middle][middle].fb!='W':
            Y()
         X()
   bottomsUp()
   for n in range(0, 4):
      placeMiddles()
      Y()
   X()
   X()
   top='Y'
   for n in range(0, 4):
      placeMiddles()
      Y()
   if not even:
      while cube[0][middle][middle].fb!='G':
         Y()
   X()
   while cube[0][middle][middle].fb=='W' or cube[0][middle][middle].fb=='Y':
      Y()
   top='G'
   bottomsUp()
   placeMiddles()
   Y()
   Y()
   placeMiddles()
   X()
   top='R'
   bottomsUp()
   placeMiddles()
   X()
   top='B'
   placeMiddles()
   fixEdges()
   while imperfectEdge()>-1:
      flipBigEdge(imperfectEdge())
solveStandardCube()
showCube()