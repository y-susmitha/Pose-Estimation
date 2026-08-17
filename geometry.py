import math


def calculate_angle(a, b, c):
    """
    Calculate the angle ABC.

    Parameters
    ----------
    a : tuple
        Coordinates of first point (x, y)

    b : tuple
        Coordinates of middle point (x, y)

    c : tuple
        Coordinates of third point (x, y)

    Returns
    -------
    float
        Angle in degrees
    """

    # Vector BA
    ba_x = a[0] - b[0]
    ba_y = a[1] - b[1]

    # Vector BC
    bc_x = c[0] - b[0]
    bc_y = c[1] - b[1]

    # Dot product
    dot_product = (
        ba_x * bc_x +
        ba_y * bc_y
    )

    # Magnitudes
    magnitude_ba = math.sqrt(
        ba_x ** 2 +
        ba_y ** 2
    )

    magnitude_bc = math.sqrt(
        bc_x ** 2 +
        bc_y ** 2
    )

    # Avoid division by zero
    if magnitude_ba == 0 or magnitude_bc == 0:
        return 0.0

    # Cosine of angle
    cosine_angle = (
        dot_product /
        (magnitude_ba * magnitude_bc)
    )

    # Numerical protection
    cosine_angle = max(
        -1.0,
        min(1.0, cosine_angle)
    )

    # Convert radians to degrees
    angle = math.degrees(
        math.acos(cosine_angle)
    )

    return angle


def calculate_distance(a, b):
    """
    Calculate Euclidean distance between
    two 2-D points.
    """

    dx = a[0] - b[0]
    dy = a[1] - b[1]

    distance = math.sqrt(
        dx ** 2 + dy ** 2
    )

    return distance


def midpoint(a, b):
    """
    Calculate midpoint between two points.
    """

    x = (a[0] + b[0]) / 2.0
    y = (a[1] + b[1]) / 2.0

    return (x, y)


def normalize_point(point, width, height):
    """
    Convert pixel coordinates to normalized
    coordinates between 0 and 1.
    """

    x = point[0] / float(width)
    y = point[1] / float(height)

    return (x, y)


def pixel_point(point, width, height):
    """
    Convert normalized coordinates to pixel
    coordinates.
    """

    x = int(point[0] * width)
    y = int(point[1] * height)

    return (x, y)


def angle_from_landmarks(
        landmarks,
        point_a,
        point_b,
        point_c):
    """
    Calculate angle using landmark IDs.

    landmarks should be a dictionary such as:

    {
        12: (0.45, 0.30),
        14: (0.50, 0.50),
        16: (0.55, 0.70)
    }
    """

    if point_a not in landmarks:
        return None

    if point_b not in landmarks:
        return None

    if point_c not in landmarks:
        return None

    a = landmarks[point_a]
    b = landmarks[point_b]
    c = landmarks[point_c]

    return calculate_angle(a, b, c)