import pandas as pd


def data_frame_process(files):
    list_dataf = []
    print("procesando datos...")
    for filename in files:
        df = pd.read_csv(filename, encoding='latin-1', low_memory=False)
        list_dataf.append(df)

    frame = pd.concat(list_dataf, axis=0, ignore_index=True)

    return frame
