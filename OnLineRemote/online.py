import numpy as np
import pandas as pd

def print_grid_from_webpage(url):
    try:
        data = pd.read_html(url, header=0, flavor='bs4')
        df = data[0].sort_values(by=["x-coordinate", "y-coordinate"], ignore_index=True)

        len_x = len(df['x-coordinate'])  # 350
        # max_x = df['x-coordinate'].max() # 0...93
        max_y = df['y-coordinate'].max() # 0...6

        np_grid = np.array([ [' '] * (len_x) ] * (max_y + 1))   # 7x350

        df.reset_index(inplace=True)
        for idx, row in df.iterrows():
            np_grid[ row['y-coordinate'] ][ row['x-coordinate'] ]= row['Character']     # 7x350

        for row in reversed(np_grid):   # reversed grid desc
            print(''.join(row))

    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
#url='https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
print_grid_from_webpage(url)