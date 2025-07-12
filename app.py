import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from optics.imaging import ThinLens, PlaneMirror, SphericalMirror
from optics.rainbows import primary_secondary, demo as rainbow_plot
from optics.prism import spectrum, animation

st.title("Geometric Optics mini-lab")

tab1, tab2, tab3, tab4 = st.tabs(["Lens", "Mirror", "Rainbow", "Prism"])

with tab1:
    st.subheader("Thin Convex Lens")
    col1, col2 = st.columns(2)
    f = col1.slider("Focal length f (m)", 0.05, 0.20, 0.10, 0.01)
    u = col2.slider("Object distance u (m)", 0.06, 0.30, 0.18, 0.01)
    lens = ThinLens(f)
    fig, ax = plt.subplots()
    lens.demo(u=u, ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("Plane mirror vs Spherical mirror")
    choice = st.radio("Mirror type", ("Plane", "Concave", "Convex"), horizontal=True)
    fig, ax = plt.subplots()
    if choice == "Plane":
        PlaneMirror().demo(ax)
    else:
        kind = "concave" if choice == "Concave" else "convex"
        SphericalMirror(kind=kind).demo(ax=ax)
    st.pyplot(fig)

with tab3:
    st.subheader("Rainbow Elevation")
    n = st.slider("Refractive index (drops)", 1.30, 1.38, 1.333, 0.001)
    _, ε1, _, ε2 = primary_secondary(n)
    st.write(f"Primary bow elevation ≈ {np.degrees(ε1):.1f}°")
    st.write(f"Secondary bow elevation ≈ {np.degrees(ε2):.1f}°")
    fig, ax = plt.subplots()
    rainbow_plot(ax)
    st.pyplot(fig)

with tab4:
    st.subheader("Prism dispersion fan")
    lambdas, δλ = spectrum()
    fig, ax = plt.subplots()
    ax.scatter(np.degrees(δλ), lambdas, c=lambdas, cmap="rainbow", s=10)
    ax.set(xlabel="δ (deg)", ylabel="λ (nm)")
    st.pyplot(fig)
    if st.button("Render mini-animation (2 s) → mp4"):
        animation()
        st.success("Saved prism.mp4 in working dir.")
