
for word in kkma_list: 6
if word in kw:
    kw[word] += 1
else:
    kw[word] = 1

for key, value in kw.items():
    if value >= 2:
        kw_list.append([
            index,
            key,
            value
        ])
        index += 1
print(kw_list)

kw_list.sort(key=lambda x: -x[2])
kw_frame = pd.DataFrame(data=kw_list, columns=kw_columns)
pd.to_pickle(kw_frame, "../data/pandas/kw.pkl")
print(kw_frame)

xlxs_dir = os.path.join("../data/pandas", "kw.xlsx")
kw_frame.to_excel(xlxs_dir,  # directory and file name to write
                  sheet_name='Sheet1',
                  na_rep='NaN',
                  float_format="%.2f",
                  header=True,
                  index=True,
                  index_label="id",
                  startrow=1,
                  startcol=1,
                  # engine = 'xlsxwriter',
                  freeze_panes=(2, 0)
                  )
