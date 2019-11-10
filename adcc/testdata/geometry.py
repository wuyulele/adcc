#!/usr/bin/env python3
## vi: tabstop=4 shiftwidth=4 softtabstop=4 expandtab
## ---------------------------------------------------------------------
##
## Copyright (C) 2019 by the adcc authors
##
## This file is part of adcc.
##
## adcc is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## adcc is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with adcc. If not, see <http://www.gnu.org/licenses/>.
##
## ---------------------------------------------------------------------


# all coordinates in Bohr
xyz = {
    "h2o": """
    O 0 0 0
    H 0 0 1.795239827225189
    H 1.693194615993441 0 -0.599043184453037
    """,
    #
    "h2s": """
    S  -0.38539679062   0 -0.27282082253
    H  -0.0074283962687 0  2.2149138578
    H   2.0860198029    0 -0.74589639249
    """,
    #
    "cn": """
    C 0 0 0
    N 0 0 2.2143810738114829
    """,
    #
    "hf": """
    H 0 0 0
    F 0 0 2.5
    """,
    #
    "ch2nh2": """
    C -1.043771327642266  0.9031379094521343 -0.0433881118200138
    N  1.356218645077853 -0.0415928720016770  0.9214682528604154
    H -1.624635343811075  2.6013402912925274  1.0436579440747924
    H -2.522633198204392 -0.5697335292951204  0.1723619198215792
    H  2.681464678974086  1.3903093043650074  0.6074335654801934
    H  1.838098806841944 -1.5878801706882844 -0.2108367437177239
    """
}
