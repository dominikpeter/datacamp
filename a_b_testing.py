def get_power(n, p1, p2, cl):
  alpha = 1 - cl
  qu = stats.norm.ppf(1 - alpha/2)
  diff = abs(p2 - p1)
  bp = (p1 + p2) / 2
  v1 = p1 * (1 - p1)
  v2 = p2 * (1 - p2)
  bv = bp * (1 - bp)
  power_part_one = stats.norm.cdf((n**0.5 * diff - qu * (2 * bv)**0.5)/
  (v1 + v2)**0.5)
  power_part_two = 1 - stats.norm.cdf((n**0.5 * diff + qu * (2 * bv)**0.5)/
  (v1 + v2)**0.5)
  power = power_part_one + power_part_two
  return(power)




def get_sample_size(power, p1, p2, cl, max_n = 1000000):
  n = 1
  while n <= max_n:
    tmp_power = get_power(n, p1, p2, cl)
    if tmp_power >= power:
      return n
    else:
      n = n + 1

