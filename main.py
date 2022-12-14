
import helperFunctions as helpFunc

i = 0

def main():
  plist = []
  vlist = []
  
  while i == 0:

    choice = input('A. Create a politician\nB. Create a voter\nC. Vote for a politician\nD. Get current election winner\nE. Get list of voters ordered by last name\nF. Get list of politicians ordered by party name\nG. Introduce Politicians\nH. Introduce Voters\nX. Exit\n\n')
    print()

    if choice == 'X':
      exit(main)

    elif choice == 'A':
      c = helpFunc.createAPolitician(plist)
      if c != None:
        plist.append(c)
      print()

    elif choice == 'B':
      c = helpFunc.createAVoter(vlist)
      if c != None:
        vlist.append(c)
      print()

    elif choice == 'C':
      helpFunc.vote(vlist,plist)
      print()

    elif choice == 'D':
      c = helpFunc.findWinner(plist)
      if c != None:
        print('The current election winner is',c.name,'-',c.party)
    
      print()
    elif choice == 'E':
      helpFunc.sortingAlgorithm2(vlist)
      for k in range(len(vlist)):
        print(vlist[k].name,vlist[k].lastname)

      print()
    elif choice == 'F':
      helpFunc.sortingAlgorithm1(plist)
      print()

    elif choice == 'G':
      helpFunc.introducePoliticions(plist)
      print()

    elif choice == 'H':
      helpFunc.introduceVoters(vlist)
      print()
      
    else:
      print('Invalid menu option, please try again')
      print()

    
if __name__ == "__main__":
    main()

