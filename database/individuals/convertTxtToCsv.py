import csv
txt_file = r"itcont.txt"
csv_file = r"indivCont.csv"
hdr_file = r"indiv_header_file.csv"

hdr_txt = csv.reader(open(hdr_file, "rb"), delimiter = ',')
in_txt = csv.reader(open(txt_file, "rb"), delimiter = '|')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(hdr_txt)
out_csv.writerows(in_txt)
