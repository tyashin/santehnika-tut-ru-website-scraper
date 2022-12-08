import re
from datetime import datetime

import pandas as pd
from pandas import ExcelWriter


if __name__ == '__main__':
    df = pd.read_csv('santehnika_tut.csv', dtype=object)
    df = df.astype(str)
    df.drop_duplicates()

    for ind in df.index:
        characteristics = df['characteristics'][ind]
        cur_characteristics = characteristics.split('###')
        cur_characteristics = [re.sub(r'(\n+)', '\n', x).replace(':', '').split('\n') for x in
                               [y.strip() for y in cur_characteristics] if x != '']
        for i in cur_characteristics:
            if len(i) != 2:
                continue

            col_name = (i[0]).strip()
            col_value = (i[1]).strip()

            if not col_name in df.columns:
                df[col_name] = ''

            df.at[ind, col_name] = col_value

    df['url'] = df['url'].str.replace('https://', '')
    df.drop(columns=['characteristics', 'article'], inplace=True, axis=1)
    xl_file_name = 'santehnika_tut_data.xlsx'
    with ExcelWriter(xl_file_name, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=datetime.today().strftime('%d-%m-%Y'), index=False)
