import pandas as pd
from pandas import DataFrame, read_csv, merge

## ALL FUNCTION ARGS ARE IN FORM STATE, PARTY, OFFICE
## STATE IS THE 2 LETTER ABBREVIATION: INDIANA-IN CALIFORNIA-CA
## PARTY IS DEM OR REP
## OFFICE IS 'H' OR 'S'
## NAME (FOR candidate_total(name) IS LAST, FIRST (MIDDLE IF APPLICABLE)

#Hardcoded Variables
person = "O'CONNOR, DANIEL JAY"
state = "CA"
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
    #print (party + " party raised: ")
    #print (partyTotal)
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

def office_in_state_total(state, office):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    dfSeat = dfState.loc[dfState['Cand_Office'] == office]
    seatTotal = dfSeat['Total_Receipt'].sum()
    return seatTotal

def state_by_office(state, office):
    dfState = df1.loc[df1['Cand_Office_St'] == state]
    dfSeat = dfState.loc[dfState['Cand_Office'] == office]
    dfNameAndReceipt = dfSeat[['Cand_Name', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNameAndReceipt = dfNameAndReceipt.sort_values(by='Total_Receipt', ascending=False)
    #print ("Office: " + office)
    #print ("State: " + state)
    #print (dfNameAndReceipt.to_string(index=False))
    sbo = dfNameAndReceipt['Total_Receipt'].sum()
    return sbo

def nationwide_total():
    df2 = df1[['Cand_Name', 'Cand_Office_St', 'Cand_Office', 'Total_Receipt', 'Cand_Party_Affiliation']]
    df2 = df2.sort_values(by='Total_Receipt', ascending=False)
   # print(df2.to_string(index=False))
    ret = df1['Total_Receipt'].sum()
    return ret

def nationwide_by_office(office):
    dfSeat = df1.loc[df1['Cand_Office'] == office]
    dfNandR = dfSeat[['Cand_Name', 'Cand_Office_St', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNandR = dfNandR.sort_values(by='Total_Receipt', ascending=False)
    #print (dfNandR.to_string(index=False))
    nbo = dfNandR['Total_Receipt'].sum()
    return nbo

def nationwide_by_party(party):
    dfParty = df1.loc[df1['Cand_Party_Affiliation'] == party]
    dfNandR = dfParty[['Cand_Name', 'Cand_Office', 'Total_Receipt', 'Cand_Party_Affiliation']]
    dfNandR = dfNandR.sort_values(by='Total_Receipt', ascending=False)
    #print(dfNandR.to_string(index=False))
    nbp = dfNandR['Total_Receipt'].sum()
    return nbp

## PERCENTAGES RETURNED

def state_over_national(state):
    st = state_total(state)
    nt = nationwide_total()
    return (100*(st/nt))

def party_over_state(state, party):
    pt = state_total_by_party(state, party)
    st = state_total(state)
    return (100*(pt/st))

def party_in_state_over_national_party(state, party):
    pt = state_total_by_party(state,party)
    npt = nationwide_by_party(party)
    return (100*(pt/npt))

def getStateData(state):
    #s = stateData()
    #s.totalContributions = state_total(state);
    #s.demPercent = party_over_state(state, "DEM")
    #s.repPercent = party_over_state(state, "REP")
    #s.otherPercent = 100 - (s.demPercent + s.repPercent)
    statePercent = state_over_national(state)
    tC = state_total(state)
    demP = party_over_state(state, "DEM")
    repP = party_over_state(state, "REP")
    otherP = 100 - demP - repP
    return (statePercent, tC, demP, repP, otherP)

#(s, con, dem, rep, other) = getStateData("CA")
#print (con)
#print (dem)
#print (rep)
#print (other)
