//
// Copyright (C) 2018 by the adcc authors
//
// This file is part of adcc.
//
// adcc is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published
// by the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// adcc is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with adcc. If not, see <http://www.gnu.org/licenses/>.
//

#include <adcc/ReferenceStateOld.hh>
#include <adcc/tmp_build_reference_state.hh>
#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace adcc {
namespace py_iface {

/** Exports adcc/ReferenceStateOld.hh to python */
void export_ReferenceStateOld(py::module& m) {
  // Temporary explicit import function
  m.def("tmp_build_reference_state", &tmp_build_reference_state,
        "Import a HFData into a ReferenceStateOld object.");

  py::class_<ReferenceStateOld, std::shared_ptr<ReferenceStateOld>>(
        m, "ReferenceStateOld",
        "Class representing information about the reference state for ADCman.",
        py::dynamic_attr())
        .def("eri", &ReferenceStateOld::eri)
        .def("fock", &ReferenceStateOld::fock)
        .def("n_orbs", &ReferenceStateOld::n_orbs)
        .def("n_orbs_alpha", &ReferenceStateOld::n_orbs_alpha)
        .def("n_orbs_beta", &ReferenceStateOld::n_orbs_beta)
        .def("orbital_coefficients", &ReferenceStateOld::orbital_coefficients)
        .def("orbital_coefficients_alpha", &ReferenceStateOld::orbital_coefficients_alpha)
        .def("orbital_coefficients_beta", &ReferenceStateOld::orbital_coefficients_beta)
        .def_property_readonly("has_core_valence_separation",
                               &ReferenceStateOld::has_core_valence_separation)
        .def_property_readonly("conv_tol", &ReferenceStateOld::conv_tol)
        .def_property_readonly("restricted", &ReferenceStateOld::restricted,
                               "Return whether the reference state is from a restricted"
                               " calculation or not.")
        .def_property_readonly(
              "spin_multiplicity", &ReferenceStateOld::spin_multiplicity,
              "Return the spin multiplicity of the reference state. 0 indicates "
              "that the spin cannot be determined or is not integer (e.g. UHF)")
        //
        ;

  // TODO Expose hf_ctx_ptr
}

}  // namespace py_iface
}  // namespace adcc
