#!/usr/bin/env python3

import sys

class State:
    def __init__(self, id : str, onTrueOutput : str, onFalseOutput : str):
        self.id=id
        self.next={'0':[onFalseOutput], '1':[onTrueOutput]}
    
    def setOnFalseState(self, falseState) -> None:
        self.next['0'].append(falseState)
    def setOnTrueState(self, trueState) -> None:
        self.next['1'].append(trueState)


    
def trellis(in_seq : str) -> str:
    state00 = State('00', '11', '00')
    state01 = State('01', '01', '10')
    state10 = State('10', '00', '11')
    state11 = State('11', '10', '01')
    state00.setOnFalseState(state00)
    state00.setOnTrueState(state01)
    state01.setOnFalseState(state10)
    state01.setOnTrueState(state11)
    state10.setOnFalseState(state00)
    state10.setOnTrueState(state01)
    state11.setOnFalseState(state10)
    state11.setOnTrueState(state11)
    
    if sys.argv[2]=='00':
        currentState = state00
    if sys.argv[2]=='01':
        currentState = state01
    if sys.argv[2]=='10':
        currentState = state10
    if sys.argv[2]=='11':
        currentState = state11
    output=""
    for character in in_seq:
        output+=currentState.next[character][0]
        currentState=currentState.next[character][1]

    return output

if __name__=="__main__":
    to_do = sys.argv[1]
    print(trellis(to_do))
