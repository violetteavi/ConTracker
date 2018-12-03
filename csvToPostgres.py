import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://jverhoff:john@localhost:5432/fecInfo')
#df = pd.read_csv('indiv_header_file.csv', low_memory=False)
#df.columns = [c.lower() for c in df.columns]
#df.to_sql("contribution_table", engine)
for df in pd.read_csv('indivCont.csv', chunksize=500):
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("contribution_table", engine, if_exists='append')