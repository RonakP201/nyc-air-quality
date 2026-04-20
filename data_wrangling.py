import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    df.drop(columns=['Unique ID', 'Indicator ID', 'Geo Type Name', 'Geo Join ID', 'Message'], inplace=True)

    df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')

    df.dropna(subset=['Data Value', 'Start_Date'], inplace=True)

    df.rename(columns={
        'Name': 'Pollutant',
        'Geo Place Name': 'Location',
        'Time Period': 'Period',
        'Data Value': 'Value'
    }, inplace=True)

    return df

if __name__ == "__main__":
    cleaned_df = load_and_clean_data("data/Air_Quality.csv")
    cleaned_df.to_csv("data/cleaned_air_quality.csv", index=False)
    print("Data cleaned and saved to 'cleaned_air_quality.csv'")
