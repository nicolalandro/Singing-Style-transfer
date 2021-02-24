# Singing-Style-transfer
This is a fork of [Jeongseungwoo/Singing-Style-transfer](https://github.com/Jeongseungwoo/Singing-Style-transfer). 
The aim is to create a method to transfer speaker style to another in order to create a single speaker dataset from many skears wav.


## Requirement
```bash
pip install -r requirements
```

## Usage
Before Training, you need to Prepare two Datasets and each must be located in "./data/train/A", "./data/train/B"
```bash
# config.py contains all paths configured
python train.py 
python test.py
```

## Citation
```bibtex
@misc{landro2021s2s,
    Author = "Nicola Landro",
    Title  = "Singing-Style-transfer",
    note   = "{{https://github.com/nicolalandro/Singing-Style-transfer}}",
    year   = 2021,}
```

