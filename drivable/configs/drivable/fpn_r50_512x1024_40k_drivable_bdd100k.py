"""FPN with ResNet-50."""

_base_ = [
    "../_base_/models/fpn_r50.py",
    "../_base_/datasets/bdd100k_512x1024.py",
    "../_base_/default_runtime.py",
    "../_base_/schedules/schedule_40k.py",
]
load_from = "https://dl.cv.ethz.ch/bdd100k/drivable/models/fpn_r50_512x1024_40k_drivable_bdd100k.pth"