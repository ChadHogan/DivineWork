import pandas as pd


'''this creates dataframes from the pandas library... they work in a simialr way to excel columns adn rows appraoch'''

Eshop_data = pd.read_json('/Users/Emma/Desktop/DataStuff/EposWork/EShop_data.json')

Rota_data = pd.read_json('/Users/Emma/Desktop/DataStuff/EposWork/rota_data.json')

shopify_data = pd.read_json('/Users/Emma/Desktop/DataStuff/EposWork/shopify_data.json')

Eshop_data.loc[1] #loc is used to find the row
Eshop_data.loc[1]['items'] #goes into a specific column

items_list = Eshop_data.loc[1]['items'] #asign that list to a variable that you can use

'''in the section below I am merging to tables with just the order's items listed along with an order_number'''

short_shop = shopify_data[['id', 'items']] # just show two columns 
short_online = Eshop_data[['order_number', 'items']]

new_df = pd.DataFrame()


short_shop = short_shop.rename(columns={'id': 'order_number'})

new_df = pd.concat([short_shop, short_online], ignore_index=True)


new_df.to_excel('/Users/Emma/Desktop/DataStuff/EposWork/output/ExampleSheet.xlsx', engine='openpyxl')  # options to exports as different formats
new_df.to_csv('/Users/Emma/Desktop/DataStuff/EposWork/output/ExampleCSV.csv')
new_df.to_json('/Users/Emma/Desktop/DataStuff/EposWork/output/Examplejson.json')

print(new_df)