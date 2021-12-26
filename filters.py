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

def filter_multiplycolor(processing_image_data, params):
    """Another stupid dummy filter
    Usage: run.py <image> multiplycolor,<x>,<muliplier>
    where x is the channel id (1 = red, 2 = green, 3 = blue)
    multiplier is a float number
    """
    params[1] = float(params[1])
    params[0] = int(params[0]) - 1
    if params[0] < 0:
        params[0] = 0
    if params[0] > 2:
        params[0] = 2
    for row in processing_image_data:
        for pixel in row:
            pixel[params[0]] *= params[1]
    return processing_image_data


def filter_mix1color(processing_image_data, params):
    """Channel mixer presets with 1 channel affected
    Usage: run.py <image> mix1color,<x>,<preset>
    where x is the channel id (1-3), and preset can be:
    - min2
    - avg2
    - max2
    - min3
    - avg3
    - max3
    - avg2iflt
    - avg3iflt
    - avg2ifgt
    - avg3ifgt
    - min2ifmin
    - max2iflt
    - min2ifgt
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
            if params[1] == 'min2':
                c1 = min(c2, c3)
            elif params[1] == 'avg2':
                c1 = (c2 + c3) / 2
            elif params[1] == 'max2':
                c1 = max(c2, c3)
            elif params[1] == 'min3':
                c1 = min(c1, c2, c3)
            elif params[1] == 'avg3':
                c1 = (c2 + c3 + c1) / 3
            elif params[1] == 'max3':
                c1 = max(c1, c2, c3)
            elif params[1] == 'avg2iflt':
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
            elif params[1] == 'max2iflt':
                if c1 < c2 or c1 < c3:
                    c1 = max(c2, c3)
            elif params[1] == 'min2ifgt':
                if c1 > c2 or c1 > c3:
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


def filter_mix2colors_sym(processing_image_data, params):
    """Channel mixer presets with 3 channels affected, but 2 of them in a same way (symmetrical)
    Usage: run.py <image> mix2colors,<x>,<preset>
    where x is the channel id (1-3), and preset can be:
    - all2avg
    - miniflt
    - avg2iflt
    - avg2ifgt
    - maxifgt
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
            if params[1] == 'all2avg':
                c = (c2 + c3) / 2
                c2 = c
                c3 = c
            elif params[1] == 'grey2ifmax':
                if c1 > c2 and c1 > c3:
                    c = (c2 + c3) / 2
                else:
                    c = (c1 + c2 + c3) / 3
                    c1 = c
                c2 = c
                c3 = c
            elif params[1] == 'miniflt':
                if c1 < c2:
                    c2 = c1
                if c1 < c3:
                    c3 = c1
            elif params[1] == 'avg2iflt':
                if c1 < c2:
                    c2 = (c2 + 2 * c1) / 3
                if c1 < c3:
                    c3 = (c3 + 2 * c1) / 3
            elif params[1] == 'avg2ifgt':
                if c1 > c2:
                    c2 = (c2 + 2 * c1) / 3
                if c1 > c3:
                    c3 = (c3 + 2 * c1) / 3
            elif params[1] == 'maxifgt':
                if c1 > c2:
                    c2 = c1
                if c1 > c3:
                    c3 = c1
            else:
                raise Exception('Unknown mix2colors_sym preset "' + params[1] + '"')
            pixel[c_ind] = c1
            pixel[c_ind + 1 if c_ind < 2 else 0] = c2
            pixel[c_ind + 2 if c_ind == 0 else c_ind - 1] = c3
    return processing_image_data


def filter_mix2colors_asym(processing_image_data, params):
    """Channel mixer presets with 3 channels affected asymmetrically
    Usage: run.py <image> mix2colors,<x1>,<x2><preset>
    where x1 and x2 are the channels ids (1-3), and preset can be:
    - swap
    - swampifmin
    - swampiflt
    - swapifgt
    - swampifmax
    - replace
    - replaceifmin
    - replaceiflt
    - replaceifgt
    - replaceifmax
    """
    c1_ind = int(params[0]) - 1
    c2_ind = int(params[1]) - 1
    if c1_ind < 0:
        c1_ind = 0
    if c1_ind > 2:
        c1_ind = 2
    if c2_ind < 0:
        c2_ind = 0
    if c2_ind > 2:
        c2_ind = 2
    c3_ind = c1_ind + 1 if c1_ind < 2 else 0
    if c3_ind == c2_ind:
        c3_ind += 1
    if c3_ind > 2:
        c3_ind -= 3
    for row in processing_image_data:
        for pixel in row:
            c1 = pixel[c1_ind]
            c2 = pixel[c2_ind]
            c3 = pixel[c3_ind]
            if params[2] == 'swap':
                c1, c2 = c2, c1
            elif params[2] == 'swapifmin':
                if c1 < c2 and c1 < c3:
                    c1, c2 = c2, c1
            elif params[2] == 'swapiflt':
                if c1 < c2:
                    c1, c2 = c2, c1
            elif params[2] == 'swapifgt':
                if c1 > c2:
                    c1, c2 = c2, c1
            elif params[2] == 'swapifmax':
                if c1 > c2 and c1 > c3:
                    c1, c2 = c2, c1
            elif params[2] == 'replace':
                c1 = c2
            elif params[2] == 'replaceifmin':
                if c1 < c2 and c1 < c3:
                    c1 = c2
            elif params[2] == 'replaceiflt':
                if c1 < c2:
                    c1 = c2
            elif params[2] == 'replaceifgt':
                if c1 > c2:
                    c1 = c2
            elif params[2] == 'replaceifmax':
                if c1 > c2 and c1 > c3:
                    c1 = c2
            else:
                raise Exception('Unknown mix2colors_asym preset "' + params[2] + '"')
            pixel[c1_ind] = c1
            pixel[c2_ind] = c2
            pixel[c3_ind] = c3
    return processing_image_data


def filter_scurve(processing_image_data, params):
    """
    Make the color more contrast by applying to it the s-form curve
    (make it lower in shadows, brighter in lights)
    Usage: run.py <image> scurve,<x>[,<middle>[,<efficiency>]]
    where x is the color index (1-3),
    middle is the middle of the curve (0-255, 127 by default)
    efficiency is the contrast miltiplier (1 by default)
    max is the right end of the curve (0-255, 255 by default)
    """
    c_ind = int(params[0]) - 1
    if c_ind < 0:
        c_ind = 0
    if c_ind > 2:
        c_ind = 2
    fmiddle = float(params[1]) if len(params) > 1 else 127
    fefficiency = float(params[2]) if len(params) > 2 else 1
    for row in processing_image_data:
        for pixel in row:
            c = pixel[c_ind]
            if c > fmiddle:
                fdistance = 255 - fmiddle
                x = (c - fmiddle) / fdistance
                x = -1 * x * x + x
            else:
                fdistance = fmiddle
                x = c / fdistance
                x = x * x - x
            c = fefficiency * fdistance * x + c
            pixel[c_ind] = c
    return processing_image_data
