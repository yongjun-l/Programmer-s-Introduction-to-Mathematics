'''
Code By : Yongjun Lee (yongjun.lee5@gmail.com)

Stable Marriage Example

This code captures an angorithm for constructing a bijection that will cause no "cheating"

we will have suitors, and the suited which they will both have a preference list for the other party. 
each time, the suitors will propose to the first person on their preference list which the suited will defer to the one that is on their highest preffered list. 
when rejected, the suitors will move on to the next person on the list and repeat the process.

'''

class Suitor:
    def __init__(self, id, preference_list):
        self.id = id
        self.preference_list = preference_list
        self.index_to_propose_next = 0

    def proposal(self):
        return self.preference_list[self.index_to_propose_next]


    def rejected(self):
        self.index_to_propose_next += 1

    def __repr__(self):
        return "Suitor({})".format(self.id)

    def __eq__(self,other):  #this returns boolean
        return isinstance(other, Suitor) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Suited:
    def __init__(self, id, preference_list):
        self.id = id
        self.held = None
        self.preference_list = preference_list
        self.candidates = set() #when the poposal is made, they are put into this list until the decision is made

    def proposed(self, suitor):
            self.candidates.add(suitor)

    def rejection(self): #when proposed, suitors will be put into the candidates set, and get rid of all but one suitor that has the lowest index on the preference list 
    
        if len(self.candidates)==0:
            return set()
        
        self.held = min(self.candidates, 
                        key=lambda suitor: self.preference_list.index(suitor.id))
        
        rejected = self.candidates - set([self.held])
        return rejected

    def __repr__(self):
        return "Suited({})".format(self.id)

    def __eq__(self,other):  #this returns boolean
        return isinstance(other, Suited) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


def stable_marriage(Suitors, Suiteds):
    
    Rejected = set(Suitors)

    while len(Rejected) > 0 :
        for suitor in Rejected:
       
            Suiteds[suitor.proposal()].proposed(suitor)

        Rejected = set()
        for suited in Suiteds:
            Rejected |= suited.rejection()

        for suitor in Rejected:
            suitor.rejected()

    #return in dictionary form 

    
    
   
    
    
    
    return dict([(suited.held, suited) for suited in Suiteds])

