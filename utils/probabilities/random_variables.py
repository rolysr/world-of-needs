"""
    Some probabilities util functions for
    generate and calculate random variables with a certain
    distribution
"""

from scipy import stats

def uniform(a=0.0, b=1.0):
    return stats.uniform(a, b)

def binom(n, p):
    return stats.binom(n, p)

def bernoulli(p):
    return stats.bernoulli(p)

def poisson(mu):
    return stats.poisson(mu)

def hypergeom(M, n, N):
    return stats.hypergeom(M, n, N)

def norm(mu, sigma):
    return stats.norm(mu, sigma)

def lognorm(sigma):
    return stats.lognorm(sigma)

def expon(a=0.0):
    return stats.expon(a)

def gamma(a):
    return stats.gamma(a)

def lognorm(sigma):
    return stats.lognorm(sigma)

def pareto(k):
    return stats.pareto(k)