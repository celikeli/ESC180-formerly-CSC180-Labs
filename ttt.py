from tttlib import *

T=genBoard()
player=int(input("Who do you want to play as (Enter 1 for X, 2 for O only)? "))
if player==1:
   while True:
      state=analyzeBoard(T)
      if state==2:
         break
      elif state==3:
         break
      printBoard(T)
      print ("\n")
      moveX=input("X move? ")
      if 0<=int(moveX)<=8 and T[int(moveX)]==0:
         T[int(moveX)]=1

         state=analyzeBoard(T)
         if int(state)==1:
            print("X won")
            printBoard(T)
            print ("\n")
            break
         elif int(state)==3:
            print("Draw")
            printBoard(T)
            print ("\n")
            break

         while True:
            printBoard(T)
            print ("\n")
            moveO=genWinningMove(T,player)

            if moveO == -1:
               moveO = genNonLoser(T,player)
               if moveO==-1:
                  moveO=genRandomMove(T,player)
                  if moveO==-1:
                     moveO = genOpenMove(T,player)


            T[int(moveO)] = 2

            state=analyzeBoard(T)
            if int(state)==2:
               print("O won")
               printBoard(T)
               print ("\n")
               break
            elif int(state)==3:
               print("Draw")
               printBoard(T)
               print ("\n")
               break
elif player==2:
   while True:
      state=analyzeBoard(T)
      if state==2:
         break
      elif state==3:
         break
      printBoard(T)
      print ("\n")
      moveO=input("O move? ")
      if 0<=int(moveO)<=8 and T[int(moveO)]==0:
         T[int(moveO)]=2

         state=analyzeBoard(T)
         if int(state)==2:
            print("O won")
            printBoard(T)
            print ("\n")
            break
         elif int(state)==3:
            print("Draw")
            printBoard(T)
            print ("\n")
            break

         while True:
            printBoard(T)
            print ("\n")
            moveX=genWinningMove(T,player)

            if moveX == -1:
               moveX = genNonLoser(T,player)
               if moveX==-1:
                  moveX=genRandomMove(T,player)
                  if moveX==-1:
                     moveX = genOpenMove(T,player)


            T[int(moveX)] = 1

            state=analyzeBoard(T)
            if int(state)==1:
               print("X won")
               printBoard(T)
               print ("\n")
               break
            elif int(state)==3:
               print("Draw")
               printBoard(T)
               print ("\n")
               break
            else:
               break
else:
   print("Invalid number")
                                                
