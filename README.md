# CPO-2025  
The Computational Physics Olympiad – a joint entry between Daniel + Rafi

---

# BPhO Computational Challenge 2025 – *Geometric Optics*

**Main task:** ≤ 3 min screencast showing your working: code, plots, interactive demos, and concise explanations. Aim for **Gold** by completing all tasks in code, adding GUI/app elements, and a short LaTeX write‑up of key results to Question pack.

We are using Overleaf. That is literally non-negotiable. 

---

## Tasks

### 1. **Dispersion models (Tasks 1a, 1b)**

- **Sellmeier formula** for crown glass:  
  $$n^2(\lambda) = 1 + \sum_{i=1}^3 \frac{B_i \lambda^{2}}{\lambda^{2} - C_i}$$  
  • Show $n(\lambda)$ decreases smoothly from ≈1.53 at 400 nm to ≈1.51 at 800 nm.  

- **Empirical fit** for water:  
  $$n(f) = A + B f^{2} + C f^{4}$$  
  • Convert wavelength ↔ frequency; plot refractive index vs frequency, discuss validity range.

---

### 2. **Thin‑lens equation (Task 2)**

- Equation:  
  $$\frac{1}{u} + \frac{1}{v} = \frac{1}{f}$$

- **Demonstrate** by:
  - Computing $x = \frac{1}{u}$, $y = \frac{1}{v}$ from data  
  - Fitting $y = mx + c$; show $m \approx 1$, $c \approx \frac{1}{f}$  
  - Extract $f$ and discuss residuals (e.g. measurement error or lens aberrations)

---

### 3. **Fermat’s principle (Tasks 3, 4)**

- **Reflection**:  
  $$t(x) = \frac{\sqrt{(x - x_{A})^2 + y_{A^2}} + \sqrt{(x_B - x)^2 + y_B^2}}{c}$$  
  • Show $\frac{dt}{dx} = 0 \Rightarrow \theta_{i} = \theta_{r}$

- **Refraction** (with speeds $c_1$, $c_2$):  
  $$t(x) = \frac{\sqrt{(x - x_{A})^2 + y_{A^2}}}{c_1} + \frac{\sqrt{(x_B - x)^2 + y_B^2}}{c_2}$$  
  • Show $\frac{dt}{dx} = 0 \Rightarrow n_1 \sin\theta_{1} = n_2 \sin\theta_{2}$  

- **Visualization:** numeric plot of $t(x)$ with annotated minimum

---

### 4. **Image formation (Tasks 5–9)**

- **Plane mirror (Task 5)**:  
  $$(x, y) \to (-x, y)$$  
  • Demonstrate correct virtual image behind mirror plane

- **Thin lens**  
  - Real, inverted image (outside focal length)  
  - Virtual, upright magnified image (inside focal length)  
  • Use ray‑construction: parallel, central, focal rays

- **Spherical mirrors**  
  - **Concave**: real image of a distant object (radius = $2f$)  
  - **Convex**: virtual, reduced image  
  • Use mirror equation:  
    $$\frac{1}{u} + \frac{1}{v} = \frac{2}{R}$$

---

### 5. **Anamorphic mapping (Task 10)**

- Fit object into unit disk, then remap coordinates to circular sector of angle $\alpha$ and radius $R_{f}$  
- Show how cylindrical mirror “unrolls” this sector into a recognisable image

---

### 6. **Rainbow angles (Task 11)**

- **Descartes’ model** for a spherical droplet of radius $a$  
- Deviation function:  
  $$δ(\theta) = \pi + 2\theta - 4\varphi (\theta),\quad \varphi = \arcsin\left(\frac{\sin \theta}{n}\right)$$  
- Find stationary points: $\frac{d\delta}{d\theta} = 0$ for primary (order 1) and secondary (order 2) bows  
- Plot elevation $\varepsilon = π - δ$ vs $n$ or vs solar elevation

---

### 7. **Prism dispersion (Task 12)**

- Triangular prism apex angle $\alpha$  
- For each $\lambda$: compute $n(λ)$ and apply Snell’s law at entry and exit  
- Compute emergent angle $\delta(λ)$; animate rainbow fan

---

## Extensions for “Gold+”

- **LaTeX write‑up:** 2–3 pages summarising theory, methods, uncertainties and applications  
- **Interactive GUI/app:** real‑time sliders for $u$, $f$, mirror radius, refractive index  
- **Vision simulator:** model corrective lenses; slider alters focal plane relative to retina

---
