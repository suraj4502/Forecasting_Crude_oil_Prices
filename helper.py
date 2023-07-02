import pandas as pd

def data_preprocessor(file_path):
    df = pd.read_excel(file_path, sheet_name='Data 1')
    df = df.loc[2:]
    df=df.rename(columns={'Back to Contents':'Date','Data 1: Europe Brent Spot Price FOB (Dollars per Barrel)':'Price'})
    df['Date']= pd.to_datetime(df['Date'])
    df['Price']= pd.to_numeric(df['Price'])
    df['Years']= df.Date.dt.strftime("%Y") # Year Extraction
    df['Months']= df.Date.dt.strftime("%B") # month extraction
    return df


def prophet_data_processor(file_path):
    df = pd.read_excel(file_path, sheet_name='Data 1')
    df = df.loc[2:]
    df=df.rename(columns={'Back to Contents':'ds','Data 1: Europe Brent Spot Price FOB (Dollars per Barrel)':'y'})
    df['ds']= pd.to_datetime(df['ds'])
    df['y']= pd.to_numeric(df['y'])
    return df