from scipy.stats import norm
import numpy as np

def calculate_sample_size(p1, lift, power, alpha):
    p2 = p1 + lift
    pooled_prob = (p1 + p2) / 2
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)
    numerator = (z_alpha * np.sqrt(2 * pooled_prob * (1 - pooled_prob)) + z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))**2
    denominator = (p2 - p1)**2
    return numerator / denominator

def calculate_power(p1, p2, n, alpha):
    pooled_prob = (p1 + p2) / 2
    z = (p2 - p1) / np.sqrt((pooled_prob * (1 - pooled_prob)) * 2 / n)
    z_alpha = norm.ppf(1 - alpha / 2)
    return norm.cdf(z - z_alpha)
