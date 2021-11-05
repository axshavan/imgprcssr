#!/bin//python
import math

def filter_convertcmy(processing_image_data, params):
    """Convert the image to another color space
    Usage: run.py <image> convertcmy,<direction>
    where <direction> can be
    - 1 (converts rgb -> cmy)
    - 2 (converts cmy -> rgb)
    """
    for row in processing_image_data:
        for pixel in row:
            if params[0] == '1':
                r = pixel[0] * pixel[0]
                g = pixel[1] * pixel[1]
                b = pixel[2] * pixel[2]
                pixel[0] = math.sqrt(g + b)
                pixel[1] = math.sqrt(b + r)
                pixel[2] = math.sqrt(r + g)
            elif params[0] == '2':
                c = pixel[0] * pixel[0]
                m = pixel[1] * pixel[1]
                y = pixel[2] * pixel[2]
                pixel[0] = math.sqrt(max(y + m - c, 0)) / 1.42
                pixel[1] = math.sqrt(max(y + c - m, 0)) / 1.42
                pixel[2] = math.sqrt(max(m + c - y, 0)) / 1.42
            else:
                raise Exception('Unknown conversion direction')
    return processing_image_data


def filter_convertmatrix(processing_image_data, params):
    """Applies the matrix transformation to each pixel
    Pixel has three color values, these are coordinates of the color vector
    in the color space. Thus, it can be multiplied by a matrix to
    achieve some transformation
    Usage: run.py <image> convertmatrix,<m00>,<m01>,<m02>,<m10>,<m11>,<m12>,<m20>,<m21>,<m22>"""
    m00 = float(params[0])
    m01 = float(params[1])
    m02 = float(params[2])
    m10 = float(params[3])
    m11 = float(params[4])
    m12 = float(params[5])
    m20 = float(params[6])
    m21 = float(params[7])
    m22 = float(params[8])
    for row in processing_image_data:
        for pixel in row:
            p0 = pixel[0]
            p1 = pixel[1]
            p2 = pixel[2]
            pixel[0] = p0 * m00 + p1 * m01 + p2 * m02
            pixel[1] = p0 * m10 + p1 * m11 + p2 * m12
            pixel[2] = p0 * m20 + p1 * m21 + p2 * m22
    return processing_image_data


def filter_convertinvmatrix(processing_image_data, params):
    """Applies inverted matrix transformation to each pixel
    Pixel has three color values, these are coordinates of the color vector
    in the color space. Thus, it can be multiplied by a matrix to
    achieve some transformation
    Usage: run.py <image> convertinvmatrix,<m00>,<m01>,<m02>,<m10>,<m11>,<m12>,<m20>,<m21>,<m22>"""
    m00 = float(params[0])
    m01 = float(params[1])
    m02 = float(params[2])
    m10 = float(params[3])
    m11 = float(params[4])
    m12 = float(params[5])
    m20 = float(params[6])
    m21 = float(params[7])
    m22 = float(params[8])
    inv_m00 = m11 * m22 - m12 * m21
    inv_m10 = m20 * m12 - m10 * m22
    inv_m20 = m10 * m21 - m11 * m20
    inv_m01 = m02 * m21 - m01 * m22
    inv_m11 = m00 * m22 - m02 * m20
    inv_m21 = m01 * m20 - m00 * m21
    inv_m02 = m01 * m12 - m02 * m11
    inv_m12 = m02 * m10 - m00 * m12
    inv_m22 = m00 * m11 - m01 * m10
    det = inv_m00 * m00 + inv_m10 * m01 + inv_m20 * m02
    if det == 0:
        det = 1
    for row in processing_image_data:
        for pixel in row:
            p0 = pixel[0]
            p1 = pixel[1]
            p2 = pixel[2]
            pixel[0] = (p0 * inv_m00 + p1 * inv_m01 + p2 * inv_m02) / det
            pixel[1] = (p0 * inv_m10 + p1 * inv_m11 + p2 * inv_m12) / det
            pixel[2] = (p0 * inv_m20 + p1 * inv_m21 + p2 * inv_m22) / det
    return processing_image_data


def filter_convertmatrix2(processing_image_data, params):
    """Applies matrix transformation to each pixel; the third matrix column is calculated.
    The 3x3 matrix describes the 3d space basis. The parameter of the function is 3x2 matrix,
    and the third its column (the third basis vector) is calculated to be perpendicular
    to the first two. Pixel has three color values, these are coordinates of the color vector
    in the color space. Thus, it can be multiplied by a matrix to
    achieve some transformation
    Usage: run.py <image> convertmatrix2,,<m00>,<m01>,<m02>,<m10>,<m11>,<m12>
    """
    m00 = float(params[0])
    m01 = float(params[1])
    m02 = float(params[2])
    m10 = float(params[3])
    m11 = float(params[4])
    m12 = float(params[5])
    m20 = m02 * m11 - m01 * m12
    m21 = m00 * m12 - m02 * m10
    m22 = m01 * m10 - m00 * m11
    return filter_convertmatrix(processing_image_data, [m00, m01, m02, m10, m11, m12, m20, m21, m22])


def filter_convertinvmatrix2(processing_image_data, params):
    """The same as filter_convertmatrix2, but inverted transformation"""
    m00 = float(params[0])
    m01 = float(params[1])
    m02 = float(params[2])
    m10 = float(params[3])
    m11 = float(params[4])
    m12 = float(params[5])
    m20 = m02 * m11 - m01 * m12
    m21 = m00 * m12 - m02 * m10
    m22 = m01 * m10 - m00 * m11
    return filter_convertinvmatrix(processing_image_data, [m00, m01, m02, m10, m11, m12, m20, m21, m22])

