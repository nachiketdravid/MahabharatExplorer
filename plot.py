from jaal import Jaal
import pandas as pd
import time

while True:
    edge_df = pd.read_csv("mb_edge_df.csv")
    node_df = pd.read_csv("mb_node_df.csv")

    Jaal(edge_df, node_df).plot(directed=True)

    time.sleep(1)