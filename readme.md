# Speech Enhancement Metrics

This implementation of Matlab was originally taken from [https://ecs.utdallas.edu/loizou/speech/software.htm](https://ecs.utdallas.edu/loizou/speech/software.htm)

## REQUIREMENTS

MATLAB or Octave must be installed

```bash
# MATLAB
cd "matlabroot/extern/engines/python"
python setup.py install
# OCTAVE
pip install oct2py
apt install octave
```

PIP Package

```bash
pip install -r requirements.txt
```

## COMPOSITE MEASURE

Usage:

```matlab
[Csig,Cbak,Covl,segSNR]=composite(cleanfile.wav,enhanced.wav)
```

where ```Csig``` is the predicted rating of speech distortion, ```Cbak``` is the predicted rating of background distortion, ```Covl``` is the predicted rating of overall quality.

You may run example files included in the zip file. In MATLAB, type:

```matlab
>> [c,b,o,s]=composite('sp09.wav','enhanced_logmmse.wav')

c = 3.3050

b = 2.6160

o = 2.7133

s - 3.9917
```

where ```sp09.wav``` is the clean file and ```enhanced_logmmse.wav``` is the enhanced file.

## References

MATLAB Source: [https://ecs.utdallas.edu/loizou/speech/software.htm](https://ecs.utdallas.edu/loizou/speech/software.htm)

```bib
@ARTICLE{4389058,
  author={Y. {Hu} and P. C. {Loizou}},
  journal={IEEE Transactions on Audio, Speech, and Language Processing}, 
  title={Evaluation of Objective Quality Measures for Speech Enhancement}, 
  year={2008},
  volume={16},
  number={1},
  pages={229-238},
}
```
