
class Voter:
  def __init__(self,name,lastname,age):
    self.name = name
    self.lastname = lastname
    self.age = age

    self.hasVoted = False
    self.votedFor = None

  def vote(self,plist,name,party):
    
    foundP = False

    if self.age >= 18 and self.hasVoted == False:

      for politician in plist:

        if politician.name == name and politician.party == party:

          self.votedFor = politician

          self.hasVoted = True

          politician.addVoter(self.votedFor)

          foundP = True

      if foundP == False:
        print('Politicion not found')
    else: 
      print('You are not eligible to vote')
    
  def introduce(self):

    if self.hasVoted == True:
      print(self.name,self.lastname+' - voted')
    else:
      print(self.name,self.lastname+' - I have not voted yet')
