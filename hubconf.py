# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

dependencies = ["torch"]
from pytorchvideo.models.hub import (  # noqa: F401, E402
    efficient_x3d_s,
    efficient_x3d_xs,
    slow_r50,
    slowfast_r50,
    slowfast_r101,
    slowfast_16x8_r101_50_50,
    x3d_m,
    x3d_s,
    x3d_xs,
)
