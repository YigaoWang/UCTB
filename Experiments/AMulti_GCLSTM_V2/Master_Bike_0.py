import os

import warnings
warnings.filterwarnings("ignore")

shared_params = ('python AMulti_GCLSTM_V2_Obj.py '
                 '--Dataset Bike '
                 '--CT 6 '
                 '--PT 7 '
                 '--TT 4 '
                 '--GLL 1 '
                 '--LSTMUnits 64 '
                 '--GALUnits 64 '
                 '--GALHeads 2 '
                 '--DenseUnits 32 '
                 '--DataRange All '
                 '--TrainDays All '
                 '--TC 0 '
                 '--TD 1000 '
                 '--TI 500 '
                 '--Epoch 5000 '
                 '--Train True '
                 '--lr 5e-5 '
                 '--Normalize True '
                 '--patience 0.1 '
                 '--ESlength 200 '
                 '--BatchSize 128 '
                 '--Device 0 '
                 '--CodeVersion V2 ')

if __name__ == "__main__":

    os.system(shared_params + ' --City NYC --Group NYC --K 0 --L 1 --Graph Distance')
    os.system(shared_params + ' --City NYC --Group NYC --K 1 --L 1 --Graph Distance')
    os.system(shared_params + ' --City NYC --Group NYC --K 1 --L 1 --Graph Correlation')
    os.system(shared_params + ' --City NYC --Group NYC --K 1 --L 1 --Graph Interaction')
    
    os.system(shared_params + ' --City Chicago --Group Chicago --K 0 --L 1 --Graph Distance')
    os.system(shared_params + ' --City Chicago --Group Chicago --K 1 --L 1 --Graph Distance')
    os.system(shared_params + ' --City Chicago --Group Chicago --K 1 --L 1 --Graph Correlation')
    os.system(shared_params + ' --City Chicago --Group Chicago --K 1 --L 1 --Graph Interaction')

    os.system(shared_params + ' --City DC --Group DC --K 0 --L 1 --Graph Distance')
    os.system(shared_params + ' --City DC --Group DC --K 1 --L 1 --Graph Distance')
    os.system(shared_params + ' --City DC --Group DC --K 1 --L 1 --Graph Correlation')
    os.system(shared_params + ' --City DC --Group DC --K 1 --L 1 --Graph Interaction')