#!/bin/python

def filter_dummy(processing_image_data, params):
    """Just a stupid dummy filter without parameters"""
    return processing_image_data


def filter_zerocolor(processing_image_data, params):
    """Another stupid dummy filter
    Usage: run.py <image> zerocolor,<x>
    where x is the channel id (1 = red, 2 = green, 3 = blue)
    """
    params = int(params[0]) - 1
    if params < 0:
        params = 0
    if params > 2:
        params = 2
    for row in processing_image_data:
        for pixel in row:
            pixel[params] = 0
    return processing_image_data


def filter_mix1color(processing_image_data, params):
    """Channel mixer presets with 1 channel affected
    Usage: run.py <image> mixcolor,<x>,<preset>
    where x is the channel id (1-3), and preset can be:
    - avg2iflt
    - avg3iflt
    - avg2ifgt
    - avg3ifgt
    - min2ifmin
    - max2ifmax
    """
    c_ind = int(params[0]) - 1
    if c_ind < 0:
        c_ind = 0
    if c_ind > 2:
        c_ind = 2
    for row in processing_image_data:
        for pixel in row:
            c1 = pixel[c_ind]
            c2 = pixel[c_ind + 1 if c_ind < 2 else 0]
            c3 = pixel[c_ind + 2 if c_ind == 0 else c_ind - 1]
            if params[1] == 'avg2iflt':
                if c1 < c2 or c1 < c3:
                    c1 = max((c2 + c3) / 2, c1)
            elif params[1] == 'avg3iflt':
                if c1 < c2 or c1 < c3:
                    c1 = max((c2 + c3) / 2, c2, c3)
            elif params[1] == 'avg2ifgt':
                if c1 > c2 or c1 > c3:
                    c1 = min((c2 + c3) / 2, c1)
            elif params[1] == 'avg3ifgt':
                if c1 > c2 or c1 > c3:
                    c1 = min((c2 + c3) / 2, c2, c3)
            elif params[1] == 'min2ifmin':
                if c1 < c2 and c1 < c3:
                    c1 = min(c2, c3)
            elif params[1] == 'max2ifmax':
                if c1 > c2 and c1 > c3:
                    c1 = max(c2, c3)
            else:
                raise Exception('Unknown mix1color preset "' + params[1] + '"')
            pixel[c_ind] = c1
            pixel[c_ind + 1 if c_ind < 2 else 0] = c2
            pixel[c_ind + 2 if c_ind == 0 else c_ind - 1] = c3
    return processing_image_data


def filter_mix2colors(processing_image_data, params):
    """Channel mixer presets with 2 channels affected
        Usage: run.py <image> mixcolor,<x>,<preset>
        where x is the channel id (1-3), and preset can be:
        - avg2iflt
        - avg3iflt
        - avg2ifgt
        - avg3ifgt
        - min2ifmin
        - max2ifmax
        """
    c_ind = int(params[0]) - 1
    if c_ind < 0:
        c_ind = 0
    if c_ind > 2:
        c_ind = 2
    for row in processing_image_data:
        for pixel in row:
            c1 = pixel[c_ind]
            c2 = pixel[c_ind + 1 if c_ind < 2 else 0]
            c3 = pixel[c_ind + 2 if c_ind == 0 else c_ind - 1]
            if params[1] == 'avg2iflt':
                if c1 < c2 or c1 < c3:
                    c1 = max((c2 + c3) / 2, c1)
            elif params[1] == 'avg3iflt':
                if c1 < c2 or c1 < c3:
                    c1 = max((c2 + c3) / 2, c2, c3)
            elif params[1] == 'avg2ifgt':
                if c1 > c2 or c1 > c3:
                    c1 = min((c2 + c3) / 2, c1)
            elif params[1] == 'avg3ifgt':
                if c1 > c2 or c1 > c3:
                    c1 = min((c2 + c3) / 2, c2, c3)
            elif params[1] == 'min2ifmin':
                if c1 < c2 and c1 < c3:
                    c1 = min(c2, c3)
            elif params[1] == 'max2ifmax':
                if c1 > c2 and c1 > c3:
                    c1 = max(c2, c3)
            else:
                raise Exception('Unknown mix1color preset "' + params[1] + '"')
            pixel[c_ind] = c1
            pixel[c_ind + 1 if c_ind < 2 else 0] = c2
            pixel[c_ind + 2 if c_ind == 0 else c_ind - 1] = c3
    return processing_image_data