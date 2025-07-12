from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

__all__ = ["PlaneMirror", "ThinLens", "SphericalMirror", "draw_axes"]

#──────────────────────────────────────────────────────────────────────────
# Generic helpers
#──────────────────────────────────────────────────────────────────────────
def draw_axes(ax, xlim=(-0.2, 0.4), ylim=(-0.15, 0.15)):
    ax.axhline(0, color="k", lw=0.6)
    ax.set_aspect("equal")
    ax.set(xlim=xlim, ylim=ylim, xlabel="x (m)", ylabel="y (m)")

@dataclass
class Ray:
    x0: float
    y0: float
    θ: float       # angle to +x (rad)
    length: float = 0.3

    def xy(self):
        xs = np.array([self.x0, self.x0 + self.length * np.cos(self.θ)])
        ys = np.array([self.y0, self.y0 + self.length * np.sin(self.θ)])
        return xs, ys

#──────────────────────────────────────────────────────────────────────────
# 4a Plane mirror
#──────────────────────────────────────────────────────────────────────────
class PlaneMirror:
    """Mirror lies on y=0, front side y>0."""
    def reflect_point(self, x, y):
        return x, -y

    def demo(self, ax=None):
        if ax is None:
            ax = plt.gca()
        draw_axes(ax)
        ax.axhline(0, color="steelblue", lw=3, alpha=.4)
        P = (0.05, 0.07)
        Pv = self.reflect_point(*P)
        ax.scatter(*P, s=50, color="crimson", label="Object")
        ax.scatter(*Pv, s=50, facecolors='none', edgecolors='crimson',
                   label="Virtual")
        # two sample rays
        for θ in (+0.8, +0.2):
            ray = Ray(*P, θ, 0.15)
            xs, ys = ray.xy(); ax.plot(xs, ys, color="k")
            # reflected part
            θr = -θ
            xs, ys = Ray(xs[-1], ys[-1], θr, 0.15).xy()
            ax.plot(xs, ys, color="k", ls="--")
        ax.legend(loc="lower right")

#──────────────────────────────────────────────────────────────────────────
# 4b Thin lens
#──────────────────────────────────────────────────────────────────────────
class ThinLens:
    def __init__(self, f=0.10):
        self.f = float(f)  # focal length +ve = convex

    def image_distance(self, u):
        return 1 / (1/self.f - 1/u)

    # three principal rays from object height h at distance u (>0 left side)
    def rays(self, u, h):
        rays = []
        # Parallel → focus
        θ = np.arctan(-h/self.f)
        rays.append(Ray(-u, h, 0, u))            # to lens
        rays.append(Ray(0, h, θ, 0.25))          # after lens
        # Through centre
        θ2 = np.arctan(h/u)
        rays.append(Ray(-u, h, θ2, u+0.25))
        # Through focal → parallel
        y_f = h * (1 - self.f/u)
        θ3 = np.arctan((h - y_f)/u)
        rays.append(Ray(-u, h, θ3, u))
        rays.append(Ray(0, y_f, 0, 0.25))
        return rays

    def demo(self, u=0.18, h=0.04, ax=None):
        if ax is None:
            ax = plt.gca()
        draw_axes(ax, xlim=(-0.25, 0.4))
        # lens
        ax.axvline(0, color="royalblue", lw=2)
        ax.scatter(-u, h, color="crimson", zorder=3)
        v = self.image_distance(u)
        y_img = -h * v/u                    # − sign = inverted if v>0
        ax.scatter(v, y_img, s=60, facecolors='none',
                   edgecolors='crimson', linewidths=1.3)
        for ray in self.rays(u, h):
            xs, ys = ray.xy()
            ax.plot(xs, ys, color="k")

#──────────────────────────────────────────────────────────────────────────
# 4c Spherical mirrors
#──────────────────────────────────────────────────────────────────────────
class SphericalMirror:
    def __init__(self, R=0.3, kind="concave"):
        self.R = np.sign({"concave":+1, "convex":-1}[kind]) * abs(R)
        self.kind = kind  # just for info
        self.f = self.R / 2

    def image_distance(self, u):
        return 1 / (2/self.R - 1/u)

    def demo(self, u=0.3, h=0.04, ax=None):
        if ax is None:
            ax = plt.gca()
        draw_axes(ax, xlim=(-0.1, 0.5))
        # mirror arc
        θ = np.linspace(-0.6, 0.6, 100)
        x = self.R * np.cos(θ)
        y = self.R * np.sin(θ)
        ax.plot(x, y, color="royalblue", lw=2)
        # principal rays
        ax.scatter(-u, h, color="crimson")
        v = self.image_distance(u)
        y_img = -h * v/u if self.kind == "concave" else h * v/u
        ax.scatter(v, y_img, s=60, facecolors='none', edgecolors='crimson')
        # 1. ray through C
        ax.plot([-u, self.R], [h, 0], color="k")
        ax.plot([self.R, v], [0, y_img], color="k", ls="--")
        # 2. Parallel then through f
        ax.plot([-u, 0], [h, h], color="k")
        ax.plot([0, self.f], [h, 0], color="k")
        ax.plot([self.f, v], [0, y_img], color="k", ls="--")
