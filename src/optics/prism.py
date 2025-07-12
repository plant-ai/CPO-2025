import numpy as np

__all__ = ["deviation", "spectrum", "animation"]

def deviation(alpha, n, i1):
    r1 = np.arcsin(np.sin(i1) / n)
    r2 = alpha - r1
    i2 = np.arcsin(n * np.sin(r2))
    return i1 + i2 - alpha

def spectrum(alpha=np.deg2rad(60),
             i1=np.deg2rad(15),
             lambdas=np.linspace(400,700,151),
             sellmeier=None):
    if sellmeier is None:
        from .dispersion import sellmeier
    nλ = sellmeier(lambdas)
    δλ = deviation(alpha, nλ, i1)
    return lambdas, δλ

def animation(filename="prism.mp4"):
    import matplotlib.pyplot as plt
    import matplotlib.animation as anim

    lambdas, δλ = spectrum()
    fig, ax = plt.subplots(figsize=(5,3))
    ax.axvline(0, color="k")
    ax.set(xlim=(-0.05,0.35), ylim=(-0.1,0.1), xticks=[], yticks=[])

    lines = [ax.plot([],[])[0] for _ in lambdas[::10]]

    def init():
        return lines

    def update(i):
        lam = lambdas[i]
        δ   = δλ[i]
        color = plt.cm.hsv((lam-400)/300)
        lines[i//10].set_data([0, 0.3*np.cos(δ)],
                              [0, 0.3*np.sin(δ)])
        lines[i//10].set_color(color)
        lines[i//10].set_alpha(0.9)
        return lines[i//10],

    ani = anim.FuncAnimation(
        fig, update, frames=len(lambdas),
        init_func=init, blit=True, interval=40
    )
    ani.save(filename, dpi=150)
    plt.close(fig)
