"""
The dataset is taken from https://commonvoice.mozilla.org
"""
import os
import pandas as pd

PATH = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it'

OUT = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/VoiceStyleTransfer/v2'

if __name__ == '__main__':
    train_tsv_path = os.path.join(PATH, 'train.tsv')
    train_df = pd.read_csv(train_tsv_path, sep='\t')

    print(train_df.info())

    count = train_df['client_id'].value_counts(ascending=False)
    print(count[:5])

    selected1 = count.index.to_list()[1]
    selected2 = count.index.to_list()[2]

    for client_id, name in zip([selected1, selected2], ['A', 'B']):
        client_data_all = train_df[train_df['client_id'] == client_id]
        for _, client_data in client_data_all.iterrows():
            original_path = os.path.join(PATH, 'clips', client_data['path'])
            new_path = os.path.join(OUT, name, client_data['path'])
            os.system(f'cp "{original_path}" "{new_path}"')
            break
        break
