#!/usr/bin/env python3
# encoding: utf-8
# @Time    : 2017/12/16 下午8:41
# @Author  : yuchangqian
# @Contact : changqian_yu@163.com
# @File    : mclane.py

from datasets.BaseDataset import BaseDataset


class AniSeg(BaseDataset):
    @classmethod
    def get_class_colors(*args):
        return [[0, 0, 0],[255, 0, 0], [255, 0, 255], [255, 255, 0], [225, 97, 0],
                [255, 153, 18], [245, 222, 179], [218, 165, 105],
                [127, 255, 0],
                [0, 255, 0], [8, 46, 84], [64, 224, 208],
                [176, 226, 255],
                [0, 139, 139], [144, 238, 144], [139, 101, 8],
                [74, 112, 139]]

    @classmethod
    def get_class_names(*args):
        return ['00_unlabeled','01_hair', '02_hair_decoration', '03_face', '04_eyes',"05_mouth",
                '06_face_wearing/decoration',
                '07_ears', '08_torso', '09_torso_wearing', '10_arms', '11_hands',
                '12_legs',
                '13_feet', '14_legs_wearing/decoration', '15_stockings',
                '16_shoes']



