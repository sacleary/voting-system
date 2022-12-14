
class Politician:
  def __init__(self,name,party):
    self.name = name
    self.party = party
    self.voters = []

  def addVoter(self,voter):
    self.voters.append(voter)

  def countVoter(self):
    return len(self.voters)


  def introduce(self):
    print(self.name+' - '+self.party+' - '+str(self.countVoter()),'vote(s)')
    
    

