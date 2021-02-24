"""
The dataset is taken from https://commonvoice.mozilla.org
"""
import os
import pandas as pd

PATH = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it'

OUT = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/VoiceStyleTransfer/train'

if __name__ == '__main__':
    train_tsv_path = os.path.join(PATH, 'train.tsv')
    train_df = pd.read_csv(train_tsv_path, sep='\t')

    print(train_df.info())

    count = train_df['client_id'].value_counts(ascending=False)
    print(count[:5])

    selected1 = '5f92abf45bb53630a853ffec6284a30311daa32d5e1dce986627c586f41963cf7db36fdc49c6f46597373cc36ee2130ffd7419381cc40267f4254ead759ba2e3'
    selected2 = 'bfc5b28dfb00554c36867d82c475794292c5a7cfeb6accf30e674eec408bb3e5e57cd3216b49f50edde6a0e9dd35c5605212c6899cb3c692ad91b7848abf3fd3'

    for client_id, name in zip([selected1, selected2], ['A', 'B']):
        client_data_all = train_df[train_df['client_id'] == client_id]
        for _, client_data in client_data_all.iterrows():
            original_path = os.path.join(PATH, 'clips', client_data['path'])
            new_path = os.path.join(OUT, name, client_data['path'])
            os.system(f'cp "{original_path}" "{new_path}"')
