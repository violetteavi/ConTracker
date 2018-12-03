import pandas as pd
from sqlalchemy import create_engine
#engine = create_engine('postgresql://jverhoff:john@localhost:5432/fecInfo')
engine = create_engine('postgresql://databasemaster:Purdue2020!@mydbinstance.cfaohzw41elj.us-east-2.rds.amazonaws.com:5432/databasemaster')
df = pd.read_csv('indiv_header_file.csv', low_memory=False)
df.columns = [c.lower() for c in df.columns]
df.to_sql("contribution_table", engine)
for df1 in pd.read_csv('indivCont.csv', chunksize=50000, error_bad_lines=False, warn_bad_lines=False):
    df1.columns = [c.lower() for c in df.columns]
    df1.to_sql("contribution_table", engine, if_exists='append')
