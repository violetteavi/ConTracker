from ConTrackerFetcher import candidate_total, state_total, party_total, seat_total
from ConTrackerFetcher import state_total_by_party, office_in_state_total, state_by_office
from ConTrackerFetcher import nationwide_total, nationwide_by_office, nationwide_by_party
from ConTrackerFetcher import state_over_national, party_over_state, party_in_state_over_national_party

name = "O'ROURKE, ROBERT (BETO)"
state = "TX"
office = "S"
party = "DEM"

beto = candidate_total(name)
beto = beto.astype(str)
print (name + " raised $" + beto)

st = state_total(state)
st = st.astype(str)
print (state + " raised $" + st)

pt = party_total(party)
pt = pt.astype(str)
print (party + " raised $" + pt)

seatT = seat_total(office)
seatT = seatT.astype(str)
print (office + " candidates raised $" + seatT)

stbp = state_total_by_party(state, party)
stbp = stbp.astype(str)
print (party + " in " + state + " raised $" + stbp)

ost = office_in_state_total(state, office)
ost = ost.astype(str)
print (office + " candidates in " + state + " raised $" + ost)

sbo = state_by_office(state, office)
print (sbo)

nationTotal = nationwide_total()
print (nationTotal)

nbo = nationwide_by_office(office)
print (nbo)

nwbp = nationwide_by_party(party)
print (nwbp)

son = state_over_national(state)
print (son)

pos = party_over_state(state, party)
print (pos)

psonp = party_in_state_over_national_party(state, party)
print (psonp)
