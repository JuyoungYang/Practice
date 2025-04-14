def check_parallel(p1, p2, p3, p4):
    dy1 = p2[1] - p1[1]
    dx1 = p2[0] - p1[0]
    dy2 = p4[1] - p3[1]
    dx2 = p4[0] - p3[0]

    return dy1 * dx2 == dy2 * dx1

def solution(dots):
  p0, p1, p2, p3 = dots[0], dots[1], dots[2], dots[3]

  if check_parallel(p0, p1, p2, p3):
      return 1

  if check_parallel(p0, p2, p1, p3):
      return 1

  if check_parallel(p0, p3, p1, p2):
      return 1

  return 0