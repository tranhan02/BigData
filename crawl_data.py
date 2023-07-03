from cryptocmd import CmcScraper
import pandas as pd

df = pd.read_csv('coin.csv', header=None)

# Hiển thị giá trị từng hàng
for i, row in df.iterrows():
    # if i >= 4478 and i <= 5000:
    if i >= 2 :
        try:
            df_list = []
            # scraper = CmcScraper(row[1], "29-05-2023", "3-6-2023")
            scraper = CmcScraper(row[1])
            df_temp = scraper.get_dataframe()
            df_temp = df_temp[::-1]
            df_temp.loc[:, 'Name'] = row[0]
            df_temp.loc[:, 'Symbol'] = row[1]
            df_list.append(df_temp)

            # Kết hợp tất cả các DataFrame thành một DataFrame lớn
            df_merged = pd.concat(df_list)

            columns = ['Name', 'Symbol'] + df_merged.columns[:-2].tolist()
            df_merged = df_merged[columns]
            # df_merged.to_csv('data_coin.csv', header=None, index=False, mode='a')
            json_data = df_merged.to_json(orient='records', indent=4, date_format='iso')
            json_data = json_data.strip("[\n]").strip("\n]")
            with open('data_coin.json', 'a') as f:
                f.write(json_data)
                f.write(",")
                f.write("\n")
        except Exception as e:
            print(e)
            df_error = pd.DataFrame([[row[0], row[1]]], columns=['col1', 'col2'])
            df_error.to_csv("loi.csv", header=None, mode='a', index=False)
            continue
    if i == 7662:
        try:
            df_list = []
            # scraper = CmcScraper(row[1], "29-05-2023", "3-6-2023")
            scraper = CmcScraper(row[1])
            df_temp = scraper.get_dataframe()
            df_temp = df_temp[::-1]
            df_temp.loc[:, 'Name'] = row[0]
            df_temp.loc[:, 'Symbol'] = row[1]
            df_list.append(df_temp)

            # Kết hợp tất cả các DataFrame thành một DataFrame lớn
            df_merged = pd.concat(df_list)

            columns = ['Name', 'Symbol'] + df_merged.columns[:-2].tolist()
            df_merged = df_merged[columns]
            # df_merged.to_csv('data_coin.csv', header=None, index=False, mode ='a')
            json_data = df_merged.to_json(orient='records', indent=4, date_format='iso')
            json_data = json_data.strip("[\n]").strip("\n]")
            with open('data_coin.json', 'a') as f:
                f.write(json_data)
                f.write("\n")
                f.write("]")
        except Exception as e:
            print(e)
            df_error = pd.DataFrame([[row[0], row[1]]], columns=['col1', 'col2'])
            df_error.to_csv("loi.csv", header=None, mode='a', index=False)
            continue
# with open('data_coin1.json', 'a') as f:
