import pandas as pd


# case "mc" market cap
def mc():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'market_cap', 'market_cap_rank'])
    df = df.sort_values(['market_cap'], ascending=False)

    # change format market_cap
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')
    df["market_cap"] = df["market_cap"].apply(lambda x: '${:,.2f}'.format(x))

    df.rename(columns={'id': 'Coin',
                       'market_cap_rank': 'Market Cap Rank',
                       'market_cap': '  Market Cap'}, inplace=True)

    display(df.to_string(index=False))
