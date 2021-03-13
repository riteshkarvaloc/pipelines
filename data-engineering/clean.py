import pandas as pd
import os

inpath = "/data/merge"
outpath = "/data/filter"

    
if __name__ == "__main__":
    
    data = pd.read_csv(os.path.join(inpath, "tmdb_merge.csv"))

    print(data.shape)
    filtered_data = data.loc[data['revenue'] != 0]
    filtered_data['revenue'].dropna(inplace=True)

    print(filtered_data.shape)

    filtered_data.to_csv(os.path.join(outpath, "tmdb_filter.csv"), index=False)