#!/usr/bin/env python3
## vi: tabstop=4 shiftwidth=4 softtabstop=4 expandtab
## ---------------------------------------------------------------------
##
## Copyright (C) 2018 by the adcc authors
##
## This file is part of adcc.
##
## adcc is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published
## by the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## adcc is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with adcc. If not, see <http://www.gnu.org/licenses/>.
##
## ---------------------------------------------------------------------
import adcc
import unittest
import pytest

import numpy as np

from adcc.testdata.cache import cache

from .misc import assert_allclose_signfix
from pytest import approx
from numpy.testing import assert_allclose
from .test_state_densities import Runners

# The methods to test
basemethods = ["adc0", "adc1", "adc2", "adc2x", "adc3"]
methods = [m for bm in basemethods for m in [bm, "cvs_" + bm]]
methods.remove("cvs_adc3")  # Not implemented yet


class TestTransitionDipoleMoments(unittest.TestCase, Runners):
    def base_test(self, system, method, kind, propmethod=None):
        if propmethod is None:
            propmethod = method
        method = method.replace("_", "-")
        propmethod = propmethod.replace("_", "-")

        refdata = cache.reference_data[system]
        state = cache.adc_states[system][method][kind]
        state = adcc.attach_state_densities(state, method=propmethod,
                                            state_diffdm=False,
                                            ground_to_excited_tdm=True,
                                            state_to_state_tdm=False)

        res_tdms = adcc.properties.transition_dipole_moments(state)
        ref_tdms = refdata[method][kind]["transition_dipole_moments"]
        refevals = refdata[method][kind]["eigenvalues"]
        n_ref = len(refevals)
        for i in range(n_ref):
            res_tdm = res_tdms[i]
            ref_tdm = ref_tdms[i]
            assert state.eigenvalues[i] == refevals[i]
            res_tdm_norm = np.sum(res_tdm * res_tdm)
            ref_tdm_norm = np.sum(ref_tdm * ref_tdm)
            assert res_tdm_norm == approx(ref_tdm_norm, abs=1e-5)
            assert_allclose_signfix(res_tdm, ref_tdm, atol=1e-5)


class TestOscillatorStrengths(unittest.TestCase, Runners):
    def base_test(self, system, method, kind, propmethod=None):
        if propmethod is None:
            propmethod = method
        method = method.replace("_", "-")
        propmethod = propmethod.replace("_", "-")

        refdata = cache.reference_data[system]
        state = cache.adc_states[system][method][kind]
        state = adcc.attach_state_densities(state, method=propmethod,
                                            state_diffdm=False,
                                            ground_to_excited_tdm=True,
                                            state_to_state_tdm=False)

        res_oscs = adcc.properties.oscillator_strengths(
            adcc.properties.transition_dipole_moments(state), state.eigenvalues
        )
        ref_tdms = refdata[method][kind]["transition_dipole_moments"]
        refevals = refdata[method][kind]["eigenvalues"]
        n_ref = len(refevals)
        for i in range(n_ref):
            assert state.eigenvalues[i] == refevals[i]
            ref_tdm_norm = np.sum(ref_tdms[i] * ref_tdms[i])
            assert res_oscs[i] == approx(2. / 3. * ref_tdm_norm * refevals[i])


class TestStateDipoleMoments(unittest.TestCase, Runners):
    def base_test(self, system, method, kind, propmethod=None):
        if propmethod is None:
            propmethod = method
        method = method.replace("_", "-")
        propmethod = propmethod.replace("_", "-")

        refdata = cache.reference_data[system]
        state = cache.adc_states[system][method][kind]
        state = adcc.attach_state_densities(state, method=propmethod,
                                            state_diffdm=True,
                                            ground_to_excited_tdm=False,
                                            state_to_state_tdm=False)

        res_dms = adcc.properties.state_dipole_moments(state)
        ref = refdata[method][kind]
        n_ref = len(ref["eigenvalues"])
        assert_allclose(res_dms[:n_ref],
                        ref["state_dipole_moments"], atol=1e-4)
