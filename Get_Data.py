import time

import requests
from datetime import datetime, timedelta


def download_klines(start_date, end_date, symbol='BTCUSDT', interval='1h'):
    base_url = 'https://data.binance.vision/data/spot/daily/klines/{symbol}/{interval}/'

    current_date = end_date
    while current_date >= start_date:
        # Format the date as required by Binance
        date_str = current_date.strftime('%Y-%m-%d')
        file_name = f'{symbol}-{interval}-{date_str}.zip'
        file_url = base_url.format(symbol=symbol, interval=interval) + file_name

        try:
            # Send the request to Binance
            response = requests.get(file_url)
            response.raise_for_status()  # Will raise an exception for 4XX/5XX responses

            # Save the content to a file in the 'data' directory
            with open(f'data/{file_name}', 'wb') as file:
                file.write(response.content)
            print(f'Successfully downloaded {file_name}')
            time.sleep(1)

        except requests.exceptions.HTTPError as e:
            # Output the error and stop the script
            print(f'Failed to download {file_name}: {e}')
            break  # Stop the loop if there's an error

        # Move to the previous day
        current_date -= timedelta(days=1)


# Set the start and end dates
start_date = datetime(2017, 8, 17)
end_date = datetime(2023, 11, 7)

# Call the function
download_klines(start_date, end_date)
