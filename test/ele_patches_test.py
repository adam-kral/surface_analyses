#!/usr/bin/env python
# -*- coding: utf-8 -*-

from surface_analyses.ele_patches import main
from contextlib import redirect_stdout
import io

import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np
import pytest


def run_commandline(pdb, dx, *args, surface_type="sas"):
    output = io.StringIO()
    with redirect_stdout(output):
        main([pdb, dx, "--surface_type", surface_type, '--check_cdrs'] + list(args))
    return output.getvalue()


def test_trastuzumab_sas_integrals():
    expected = np.array(
        [
            22575.20631872,
            12389.29284473,
            27131.66874305,
            -4556.46242433,
            -1867.35195722,
        ]
    )
    out_lines = run_commandline(
        "test/trastuzumab/apbs-input.pdb",
        "test/trastuzumab/apbs-potential.dx",
        '--out',
        'test/trastuzumab/apbs-patches.csv',
        surface_type="sas",
    )
    last = out_lines.splitlines()[-1]
    integrals = np.array([float(x) for x in last.split()])
    assert np.allclose(expected, integrals)
    patches = pd.read_csv('test/trastuzumab/apbs-patches.csv')
    expected_patches = pd.read_csv('test/trastuzumab/apbs-patches.save')
    assert_frame_equal(patches, expected_patches)
