from __future__ import absolute_import

import os
import matlab.engine

path = os.path.abspath(__file__)
eng = matlab.engine.start_matlab()


def pesq(sample_rate: int, clean: str, enhanced: str):
    return eng.pesq(sample_rate, clean, enhanced)


def composite(clean: str, enhanced: str):
    csig, cbak, covl = eng.composite(clean, enhanced)
    return csig, cbak, covl


def ssnr(clean: str, enhanced: str, sample_rate: int):
    _, ssnr = eng.snr(clean, enhanced, sample_rate)
    return ssnr
