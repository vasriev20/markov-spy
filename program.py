"""
"""

def createpclist():
    """
    Returns list of all of the daily percent change values
    """

    f=open('adjdaily%changespy.txt','r')
    listpc=[]
    for x in f:
        #print(x)
        if(x!=''):
            a=float(x)
            listpc.append(a)
        else:
            break
        #print(listpc)
    f.close()
    return listpc

def creatematrix():
    lessneg2=[0,0,0,0,0]
    betweennegs=[0,0,0,0,0]
    betweenzero=[0,0,0,0,0]
    betweenpos=[0,0,0,0,0]
    morepos2=[0,0,0,0,0]

    lessneg2count=0
    betweennegscount=0
    betweenzerocount=0
    betweenposcount=0
    morepos2count=0

    listpcvalues=createpclist()
    for pos in range(len(listpcvalues)-1):
        if(listpcvalues[pos]<-0.02):
            if(listpcvalues[pos+1]<-0.02):
                lessneg2[0]+=1
            elif(listpcvalues[pos+1]<-0.005 and listpcvalues[pos+1]>=-0.02):
                lessneg2[1]+=1
            elif(listpcvalues[pos+1]>=-0.005 and listpcvalues[pos+1]<=0.005):
                lessneg2[2]+=1
            elif(listpcvalues[pos+1]>0.005 and listpcvalues[pos+1]<=0.02):
                lessneg2[3]+=1
            else:
                lessneg2[4]+=1
            lessneg2count+=1

        elif(listpcvalues[pos]<-0.005 and listpcvalues[pos]>=-0.02):
            if(listpcvalues[pos+1]<-0.02):
                betweennegs[0]+=1
            elif(listpcvalues[pos+1]<-0.005 and listpcvalues[pos+1]>=-0.02):
                betweennegs[1]+=1
            elif(listpcvalues[pos+1]>=-0.005 and listpcvalues[pos+1]<=0.005):
                betweennegs[2]+=1
            elif(listpcvalues[pos+1]>0.005 and listpcvalues[pos+1]<=0.02):
                betweennegs[3]+=1
            else:
                betweennegs[4]+=1
            betweennegscount+=1

        elif(listpcvalues[pos]>=-0.005 and (listpcvalues[pos])<=0.005):
            if(listpcvalues[pos+1]<-0.02):
                betweenzero[0]+=1
            elif(listpcvalues[pos+1]<-0.005 and listpcvalues[pos+1]>=-0.02):
                betweenzero[1]+=1
            elif(listpcvalues[pos+1]>=-0.005 and listpcvalues[pos+1]<=0.005):
                betweenzero[2]+=1
            elif(listpcvalues[pos+1]>0.005 and listpcvalues[pos+1]<=0.02):
                betweenzero[3]+=1
            else:
                betweenzero[4]+=1
            betweenzerocount+=1

        elif(listpcvalues[pos]>0.005 and listpcvalues[pos]<=0.02):
            if(listpcvalues[pos+1]<-0.02):
                betweenpos[0]+=1
            elif(listpcvalues[pos+1]<-0.005 and listpcvalues[pos+1]>=-0.02):
                betweenpos[1]+=1
            elif(listpcvalues[pos+1]>=-0.005 and listpcvalues[pos+1]<=0.005):
                betweenpos[2]+=1
            elif(listpcvalues[pos+1]>0.005 and listpcvalues[pos+1]<=0.02):
                betweenpos[3]+=1
            else:
                betweenpos[4]+=1
            betweenposcount+=1

        else:
            if(listpcvalues[pos+1]<-0.02):
                morepos2[0]+=1
            elif(listpcvalues[pos+1]<-0.005 and listpcvalues[pos+1]>=-0.02):
                morepos2[1]+=1
            elif(listpcvalues[pos+1]>=-0.005 and listpcvalues[pos+1]<=0.005):
                morepos2[2]+=1
            elif(listpcvalues[pos+1]>0.005 and listpcvalues[pos+1]<=0.02):
                morepos2[3]+=1
            else:
                morepos2[4]+=1
            morepos2count+=1

    for pos in range(len(lessneg2)):
        lessneg2[pos]=round(lessneg2[pos]/lessneg2count,4)
    for pos in range(len(betweennegs)):
        betweennegs[pos]=round(betweennegs[pos]/betweennegscount,4)
    for pos in range(len(betweenzero)):
        betweenzero[pos]=round(betweenzero[pos]/betweenzerocount,4)
    for pos in range(len(betweenpos)):
        betweenpos[pos]=round(betweenpos[pos]/betweenposcount,4)
    for pos in range(len(morepos2)):
        morepos2[pos]=round(morepos2[pos]/morepos2count,4)


    print(repr(lessneg2))
    print(repr(betweennegs))
    print(repr(betweenzero))
    print(repr(betweenpos))
    print(repr(morepos2))


#script code
creatematrix()
