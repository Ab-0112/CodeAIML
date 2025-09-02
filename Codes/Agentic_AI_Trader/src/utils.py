import numpy as np

def get_state(data, index):
    """
    Extracts the state representation from the dataset at a given time index.
    """
    if index >= len(data):
        return None
    return np.array([
        float(data.loc[index, 'Close']),
        float(data.loc[index, 'SMA_5']),
        float(data.loc[index, 'SMA_20']),
        float(data.loc[index, 'Returns'])
    ])