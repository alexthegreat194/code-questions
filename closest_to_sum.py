# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

def closest_to_sum(a, b, t):
    a.sort()
    b.sort()
    i = 0
    j = len(b) - 1
    closest = None
    while i < len(a) and j >= 0:
        sum = a[i] + b[j]
        if closest is None or abs(t - sum) < abs(t - closest):
            closest = sum
        if sum == t:
            return [a[i], b[j]]
        elif sum < t:
            i += 1
        else:
            j -= 1
    return closest