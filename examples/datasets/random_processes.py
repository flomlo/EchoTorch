# -*- coding: utf-8 -*-
#
# File : examples/datasets/random_processes.py
# Description : Examples of time series generation based on random processes
# Date : 12th of August, 2021
#
# This file is part of EchoTorch.  EchoTorch is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti <nils.schaetti@unine.ch>


# Imports
import matplotlib.pyplot as plt
import torch
import echotorch.data
import echotorch.viz

# Random seed
torch.manual_seed(1)

# Random walk
# random_walk = echotorch.data.unirw(1, length=10000)
# print("Univariate Random walk: {}".format(random_walk))
random_walk = echotorch.data.random_walk(1, length=10000, shape=(2,))
print("Multivariate Random Walk: {}".format(random_walk[0]))

# Plot random walk
plt.figure()
echotorch.viz.timeplot(
    random_walk[0],
    tstart=0.0,
    tstep=0.01,
    title="Random walk",
    xlab="x(t)"
)
plt.show()

# Multivariate moving average (VMA)
moving_average = echotorch.data.ma(1, length=200, order=30, size=1)

# Plot MA(q)
plt.figure()
echotorch.viz.timeplot(
    moving_average[0][:, 0],
    tstart=0.0,
    tstep=0.01,
    title="Multivariate Moving Average MA(q)",
    xlab="x(t)"
)
plt.show()

# Autoregressive process
autoregressive_process = echotorch.data.ar(1, length=200, order=5, size=1)

# Plot AR(p)
plt.figure()
echotorch.viz.timeplot(
    autoregressive_process[0][:, 0],
    tstart=0.0,
    tstep=0.01,
    title="Autoregressive Process AR(p)",
    xlab="X(t)"
)
plt.show()

#  ARMA
arma_process = echotorch.data.arma(1, length=200, regressive_order=5, moving_average_order=7, size=1)

# Plot ARMA(p, q)
plt.figure()
echotorch.viz.timeplot(
    arma_process[0],
    tstart=0,
    tstep=0.01,
    title="AutoRegressive Moving Average process ARMA(p, q)",
    xlab="x(t)"
)
