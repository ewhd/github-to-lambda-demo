# import pandas as pd


# def lambda_handler(event, context):
#     d = {'col1': [1, 2], 'col2': [3, 4]}
#     df = pd.DataFrame(data=d)
#     print(df)
#     print('Done x1.4')

import requests


def lambda_handler(event, context):
    # Make a GET request to a public API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")
    print('Done x1.1')
