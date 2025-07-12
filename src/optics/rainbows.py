from __future__ import annotations
import numpy as np
from scipy.optimize import minimize_scalar

__all__ = ["deviation", "stationary_theta", "primary_secondary", "demo"]

def deviation(theta, n, order=1):
    """Return total deviation δ(θ) for given order."""
    φ = np.arcsin(np.sin(theta) / n)
    if order == 1:
        return np.pi + 2*theta - 4*φ
    elif order == 2:
        return 2*np.pi + 2*theta - 6*φ
    else:
        raise ValueError("order must be 1 or 2")

def stationary_theta(n, order=1):
    """θ where dδ/dθ = 0 (minimum ⇒ bright bow)."""
    res = minimize_scalar(
        lambda t: deviation(t, n, order),
        bounds=(0, np.pi/2),
        method="bounded"
    )
    return res.x

def primary_secondary(n=1.333):
    th1 = stationary_theta(n, 1)
    th2 = stationary_theta(n, 2)
    ε1 = np.pi - deviation(th1, n, 1)
    ε2 = deviation(th2, n, 2) - np.pi
    return th1, ε1, th2, ε2  # rad

def demo(ax=None):
    import matplotlib.pyplot as plt
    if ax is None:
        ax = plt.gca()
    θ = np.linspace(0, np.pi/2, 800)
    δ = deviation(θ, n=1.333, order=1)
    ax.plot(np.degrees(θ), np.degrees(δ))
    th1, ε1, *_ = primary_secondary()
    ax.axvline(np.degrees(th1), ls="--", color="crimson",
               label=f"min ⇒ ε≈{np.degrees(ε1):.1f}°")
    ax.set(
        xlabel=r"θ (deg)",
        ylabel=r"δ (deg)",
        title="Deviation in a water drop (primary)"
    )
    ax.legend()
