import pandas as pd
from pandas import DataFrame, read_csv, merge

#Hardcoded Variables
person = "O'CONNOR, DANIEL JAY"
state = "WA"
seat = "H"
party = "DEM"

df1 = pd.read_csv('candidate_summary_2018.csv')
df1.head()

df1 = df1[df1['Total_Receipt'] > 0]

def candidate_total(name):
    cand = df1.loc[df1["Cand_Name"] == name]
    return cand['Total_Receipt'].sum()

def state_total(state):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    stateTotal = dfState['Total_Receipt'].sum()
    return stateTotal

def party_total(party):
    dfParty = df1.loc[df1['Cand_Party_Affiliation'] == party]
    partyTotal = dfParty['Total_Receipt'].sum()
    print (party + " party raised: ")
    print (partyTotal)
    return partyTotal

def seat_total(seat):
    dfSeat = df1.loc[df1['Cand_Office'] == seat]
    seatTotal = dfSeat['Total_Receipt'].sum()
    return seatTotal

def state_total_by_party(state, party):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    dfState = dfState.loc[dfState['Cand_Party_Affiliation'] == party]
    statePartyTotal = dfState['Total_Receipt'].sum()
    return statePartyTotal

def office_in_state_total(office, state):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    dfSeat = dfState.loc[dfState['Cand_Office'] == office]
    seatTotal = dfSeat['Total_Receipt'].sum()
    return seatTotal

def state_by_office(state, office):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    dfSeat = dfState.loc[dfState['Cand_Office'] == office]
    dfNameAndReceipt = dfSeat[['Cand_Name', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNameAndReceipt = dfNameAndReceipt.sort_values(by='Total_Receipt', ascending=False)
    print ("Office: " + office)
    print ("State: " + state)
    print (dfNameAndReceipt.to_string(index=False))
    return dfNameAndReceipt

def nationwide_total():
    df2 = df1[['Cand_Name', 'Cand_Office_St', 'Cand_Office', 'Total_Receipt', 'Cand_Party_Affiliation']]
    df2 = df2.sort_values(by='Total_Receipt', ascending=False)
    print(df2.to_string(index=False))

def nationwide_by_office(office):
    dfSeat = df1.loc[df1['Cand_Office'] == office]
    dfNandR = dfSeat[['Cand_Name', 'Cand_Office_St', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNandR = dfNandR.sort_values(by='Total_Receipt', ascending=False)
    print (dfNandR.to_string(index=False))

def nationwide_by_party(party):
    dfParty = df1.loc[df1['Cand_Party_Affiliation'] == party]
    dfNandR = dfParty[['Cand_Name', 'Cand_Office', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNandR = dfNandR.sort_values(by='Total_Receipt', ascending=False)
    print(dfNandR.to_string(index=False))

#pRaised = candidate_total(person)
#print (person + " raised: ")
#print (pRaised)
#sTotal = state_total(state)
#officeInState = office_in_state_total(seat, state)
#party_total(party)
state_by_office(state, seat)
#nationwide_total()
#nationwide_by_office(seat)
#nationwide_by_party(party)
#stbp = state_total_by_party(state, party)
#print (party + " Total in " + state + ": ")
#print (stbp)
