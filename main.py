from __future__ import absolute_import

import os
import logging
import oct2py
from pesq import pesq
from scipy.io import wavfile

logging.basicConfig(level=logging.ERROR)
oc = oct2py.Oct2Py(logger=logging.getLogger())


def pesq_mos(clean: str, enhanced: str):
    sr1, clean_wav = wavfile.read(clean)
    sr2, enhanced_wav = wavfile.read(enhanced)
    assert sr1 == sr2
    mode = "nb" if sr1 < 16000 else "wb"
    return pesq(sr1, clean_wav, enhanced_wav, mode)


def composite(clean: str, enhanced: str):
    csig, cbak, covl, ssnr = oc.feval(os.path.join(os.path.dirname(__file__), "composite.m"), clean, enhanced, nout=4)
    pesq_score = pesq_mos(clean, enhanced)
    csig += 0.603 * pesq_score
    cbak += 0.478 * pesq_score
    covl += 0.805 * pesq_score
    return csig, cbak, covl, ssnr


if __name__ == "__main__":
    clean = "./audio/sp09.wav"
    enhanced = "./audio/enhanced_logmmse.wav"
    print(composite(clean, enhanced))
