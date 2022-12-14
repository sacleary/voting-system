
import myPolitician as pol
import myVoter as vo


def createAPolitician(plist):

  pName = input('Politician Name: ')
  pParty = input('Politician Party: ')

  politician = pol.Politician(pName,pParty)

  for p in plist:
    if p.name == pName and p.party == pParty:
      print('This politician already exists!')
      return
    else:
      return politician
  else:
    return politician


def createAVoter(vlist):

  vName = input('First Name: ')
  vLName = input('Last Name: ')
  
  i = 0
  while i == 0:
    vAge = input('Age: ')
    if vAge.isnumeric() == True:
      vAge = int(vAge)
      i = 1
    else:
      print('Error: That is not a number, please try again.')
      

  voter = vo.Voter(vName, vLName, vAge)

  for v in vlist:
    if v.name == vName and v.lastname == vLName:
      print('This voter already exists!')
      return
    else:
      return voter
  else:
    return voter


def vote(vlist,plist):

  vName = input('First Name: ')
  vLName = input('Last Name: ')
  voterFound = None
  for voter in vlist:
    if voter.name == vName and voter.lastname == vLName:
      voterFound = voter
      break
    else:
      pass
  else:
    print('Voter not found')
    return
      
  pName = input('Politician Name: ')
  pParty = input('Politician Party: ')

  for politician in plist:
    if politician.name == pName and politician.party == pParty:
      break
    else:
      pass
  else:
    print('This politicion does not exist!')
    return
  if voterFound != None:
    voterFound.vote(plist,pName,pParty)  


def findWinner(plist):

  if plist != []:
      
    i = None

    for politician in plist:

      if (i is None or politician.countVoter() > i):
            i = politician.countVoter()
            j = politician 

    if i != 0:
      return j
    else:
      print('Error: No one has voted')
      return
  

def sortingAlgorithm1(politician):

  l = len(politician)
  for i in range (l-1):
    for j in range(0,l-i-1):
      if politician[j].party > politician[j+1].party:
        politician[j],politician[j+1] = politician[j+1],politician[j]


  for i in range(l):
    print(politician[i].name,politician[i].party)
  

def sortingAlgorithm2(voters):

  if len(voters) > 1:

    mid = len(voters)//2

    l = voters[:mid]
    r = voters[mid:]

    sortingAlgorithm2(l)
    sortingAlgorithm2(r)

    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
      if l[i].lastname < r[j].lastname:
          voters[k] = l[i]
          i += 1
      else:
          voters[k] = r[j]
          j += 1
      k += 1

    while i < len(l):
      voters[k] = l[i]
      i += 1
      k += 1

    while j < len(r):
      voters[k] = r[j]
      j += 1
      k += 1

    

    
def introducePoliticions(plist):
  
  for politician in plist:
    politician.introduce()
  
  
def introduceVoters(vlist):

  for voters in vlist:
    voters.introduce()


