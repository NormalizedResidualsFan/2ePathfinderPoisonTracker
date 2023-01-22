"""
This script was made to facilitate tracking various poisons applied to multiple individuals mid-combat in Pathinder 2nd Edition

It is intended to be run from a terminal with python 3.0 (or newer)

It will print out to terminal a set of poison victims as entered by the user, with remaining round durations and present poison stage. Remaining round durations may be decremented individually or all active victims may have their rounds remaining decremented simultaneously

Only common and uncommon injury poisons, as found on 2e.aonprd.com as of 2023-01-22, are included here
"""

class poison:
    def __init__(self,name,dc,duration,stages):
        self.name=name
        self.dc=dc
        self.duration=duration
        self.stages=stages

class victim:
    def __init__(self,idNum,name,poison,stageIdx,roundsLeft):
        self.idNum=idNum
        self.name=name
        self.poison=poison
        self.stageIdx=stageIdx
        self.roundsLeft=roundsLeft

    def strOut(self):
        return f"{self.idNum}) {self.name}, {self.poison.name}\nDC: {self.poison.dc}, Rounds Remaining: {self.roundsLeft}\n{self.poison.stages[self.stageIdx]}\n\n"

def main():
    menuText="To see command list, enter help\n"
    helpText=("+ -> Add new poison victim\n"
    "- -> Remove poison victim\n"
    "N+ -> Increase victim number N's poison stage by one\n"
    "N- -> Decrease victim number N's poison stage by one\n"
    "N; -> Reduce victim number N's poison rounds remaining by one\n"
    "; -> Reduce the poison rounds remaining of all victims by one\n"
    "clear -> Clear all victims\n"
    "quit -> Exit program\n"
    )
    victimList=[]
    running=True
    while running:
        victimStr=""
        # making string for list of active victims
        for i in victimList:
            victimStr+=i.strOut()
        
        uIn=input(victimStr+"\n"+menuText)

        if uIn=="":
            # assuming this was a mistake
            pass
        
        elif uIn.lower()=="help":
            # printing help text
            print(helpText)

        elif uIn=="+":
            # adding new victim
            vname=input("Enter a name for this victim\n")
            for idx,i in enumerate(poisonList):
                print(f"{idx}) {i.name}")

            pidx=input("Select poison from list above by number\n")
            try:
                pidx=int(pidx)
                if pidx>=0 and pidx<len(poisonList):
                    # valid selection, adding victim
                    victimList.append(victim(len(victimList),vname,poisonList[pidx],0,poisonList[pidx].duration))
                else:
                    print("Invalid entry")
            except:
                print("Invalid entry")

        elif uIn=="-":
            # removing poison victim
            delVicNum=input("Enter number of victim to remove\n")
            try:
                delVicNum=int(delVicNum)
                if delVicNum>=0 and delVicNum<len(victimList):
                    victimList.pop(delVicNum)
                else:
                    print("Invalid entry")
            except:
                print("Invalid entry")

        elif len(uIn)>1 and uIn[-1]=="+":
            # increasing victim's stage
            try:
                vicId=int(uIn[:-1])
                if vicId>=0 and vicId<len(victimList):
                    # checking if at final stage
                    if victimList[vicId].stageIdx==(len(victimList[vicId].poison.stages)-1):
                        # do nothing
                        pass
                    else:
                        # increment stage
                        victimList[vicId].stageIdx+=1
            except:
                print("Invalid entry")

        elif len(uIn)>1 and uIn[-1]=="-":
            # decreasing victim's stage
            try:
                vicId=int(uIn[:-1])
                if vicId>=0 and vicId<len(victimList):
                    # checking if at first stage
                    if victimList[vicId].stageIdx==0:
                        # remove from list
                        print(f"{victimList[vicId].name} is no longer poisoned")
                        victimList.pop(vicId)
                    else:
                        # decrease stage
                        victimList[vicId].stageIdx-=1
            except:
                print("Invalid entry")

        elif len(uIn)>1 and uIn[-1]==";":
            # decreasing victim's poison duration
            try:
                vicId=int(uIn[:-1])
                if vicId>=0 and vicId<len(victimList):
                    # checking if they were on last round of poison
                    if victimList[vicId].roundsLeft==1:
                        # remove from list
                        print(f"{victimList[vicId].name} is no longer poisoned")
                        victimList.pop(vicId)
                    else:
                        # decrease rounds left
                        victimList[vicId].roundsLeft-=1
            except:
                print("Invalid entry")

        elif uIn==";":
            # decreasing all victim's poison duration
            for idx,i in enumerate(victimList):
                # checking if they were on last round of poison
                if i.roundsLeft==1:
                    # remove from list
                    print(f"{i.name} is no longer poisoned")
                    victimList.pop(idx)
                else:
                    # decrease rounds left
                    i.roundsLeft-=1

        elif uIn.lower()=="clear":
            victimList=[]

        elif uIn.lower()=="quit":
            running=False

        else:
            print("Invalid entry")

poisonList=[
    poison("Spear Frog Poison",15,6,["S1: 1d4 poison (1 rnd)","S2: 1d6 poison & enfeebled 1 (1 rnd)"]),
    poison("Giant Centipede Venom",17,6,["S1: 1d6 poison (1 rnd)","S2: 1d12 poison & clumsy 1 & flat-footed (1 rnd)"]),
    poison("Black Smear Poison",16,6,["S1: 1d6 poison & enfeebled 1 (1 rnd)","S2: 1d6 poison & enfeebled 1 (1 rnd)","S3: 1d6 poison and enfeebled 2 (1 rnd)"]),
    poison("Lethargy Poison",18,2400,["S1: slowed 1 (1 rnd)","S2: slowed (1 minute)","S3: unconscious with no Perception check to wake up (1 rnd)","S4: unconscious with no Perception check to wake up (1d4 hrs)"]),
    poison("Cytillesh Oil",19,4,["S1: 1d10 poison (1 rnd)","S2: 1d12 poison (1 rnd)","S3: 2d10 poison (1 rnd)"]),
    poison("Graveroot",19,4,["S1: 1d10 poison (1 rnd)","S2: 1d12 poison and stupefied 1 (1 rnd)", "S3: 2d6 poison and stupefied 2 (1 rnd)"]),
    poison("Leadenleg",20,6,["S1: 1d10 poison and -5f status penalty to all Speeds (1 rnd)","S2: 2d6 poison and -10ft status penalty to all Speeds (1 rnd)","S3: 2d6 poison and -20ft status penalty to all Speeds (1 rnd)"]),
    poison("Stupor Poison",20,3600,["S1: slowed 1 and flat-fotted (1 rnd)","S2: slowed 2 and flat-footed (1 rnd)","S3: unconscious with no Perception check to wake up (1 rnd)","S4: unconscious with no Perception check to wake up (1d6 hr)"]),
    poison("Hunting Spider Venom",21,6,["S1: 1d10 poison and flat-footed (1 rnd)","S2: 1d12 poison, clumsy 1 and flat-footed (1 round)","S3: 2d6 poison, clumsy 2, and flat-footed (1 rnd)"]),
    poison("Giant Scorpion Venom",22,6,["S1: 1d10 poison and enfeebled 1 (1 rnd)","S2: 2d10 poison and enfeebled 1 (1 rnd)","S3: 2d10 poison and enfeebled 2 (1 rnd)"]),
    poison("Giant Wasp Venom",25,6,["S1: 2d6 poison and clumsy 1 (1 rnd)", "S2: 3d6 poison and clumsy 2 (1 rnd)","S3: 4d6 poison and clumsy 2 (1 rnd)"]),
    poison("Wyvern Poison", 26,6,["S1: 5d6 poison (1 rnd)","S2: 6d6 poison (1 rnd)","S3: 8d6 poison (1 rnd)"]),
    poison("Shadow Essence",29,6,["S1: 3d6 negative and 2d6 poison (1 rnd)","S2: 3d6 negative, 2d6 poison and enfeebled 1 (1 rnd)","S3: 3d6 negative, 2d6 poison, and enfeebled 2 (1 rnd)"]),
    poison("Mage Bane",32,6,["S1: 2d6 mental and stupefied 2 (1 rnd)","S2: 3d6 mental and stupefied 3 (1 rnd)","S3: 4d6 mental and stupefied 4 (1 rnd)"]),
    poison("Spell-Eating Pitch",31,6,["S1: 5d6 poison and stupefied 1 (1 rnd)","S2: 6d6 poison and stupefied 3 (1 rnd)","7d6 poison and stupefied 4 (1 rnd)"]),
    poison("Purple Worm Venom",32,6,["S1: 5d6 poison and enfeebled 2 (1 rnd)","S2: 6d6 poison and enfeebled 2 (1 rnd)","S3: 8d6 poison and enfeebled 2 (1 rnd)"]),
    poison("Death Knell Powder",34,6,["S1: 7d6 poison (1 rnd)","S2: 9d6 poison (1 rnd)","S3: 12d6 poison (1 rnd)"]),
    poison("Lifeblight Residue",35,6,["S1: 5d6 negative and 3d6 poison (1 rnd)","S2: 6d6 negative and 4d6 poison (1 rnd)","S3: 7d6 negative and 5d6 poison (1 rnd)"]),
    poison("Weeping Midnight",36,6,["S1: 6d6 poison and dazzled (1 rnd)","S2: 7d6 poison, dazzled, and sickened 1 (1 rnd)","S3: 8d6 poison and blinded (1 rnd)"]),
    poison("Cerulean Scourge",36,6,["S1: 9d6 poison (1 rnd)","S2: 12d6 poison (1 rnd)","S3: 15d6 poison (1 rnd)"]),
    poison("Oblivion Essence",42,6,["S1: 8d6 poison and slowed 1 (1 rnd)","S2: 10d6 poison, enfeebled 2, and slowed 1 (1 rnd)","S3: 12d6 poison, enfeebled 3 and slowed 1 (1 rnd)"])
    ]


if __name__=="__main__":
    main()
