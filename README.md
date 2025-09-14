# 🎓 SAV3D @ ICIAP2025

## 🖥 Repository for the ICIAP25 Tutorial: 3D Shape Analysis for Virtual Humans

Acquiring and synthesizing avatars in different **identities, poses, clothes**, and possibly interacting with **physical objects** has caused a dramatic explosion of interest in both **academia** and **industry**.  
While the popularity of such data grows, it comes with the challenge of developing robust techniques to **process** and **learn** from them.

In this tutorial, we aim to introduce the foundations of **3D Virtual Humans** and tools from **spectral shape analysis**, deploying them in practical use cases.  
In particular, we combine the two worlds to develop a **compact but effective 3D Human Registration pipeline**.  
Finally, we review the latest trends and **open challenges** in the Virtual Humans field.

---

## 📚 Tutorial Overview

- **Part 1: Introduction to SMPL**
  - ✨ Motivation
  - 🧍 Modeling the identities
  - 🤸 Modeling the poses
  - 🔧 Extensions (SMPL-H, SMPL-X, ...)
  - 💻 Hands-on Coding

- **Part 2: Spectral Shape Analysis**
  - ✨ Motivation
  - 📈 Spectral Graph Theory: the Graph Laplacian
  - ⚙️ Applications of the Graph Laplacian
  - 📊 Spectral Analysis on 3D Shapes
  - 🔗 Shape Matching
  - 💻 Hands-on Coding

- **Part 3: 3D Humans Registration**
  - 🎯 Problem Definition
  - ⚖️ Losses and Regularizations
  - 🏆 State-of-the-art
  - 💻 Hands-on Coding

- **Part 4: Interacting 3D Virtual Humans**
  - 🏗 3D Human-Object Interaction
  - 🎬 3D Humans in motion
  - 🖐 Conclusions

---

## 💻 Code & Environment Setup
```
conda create -n sav3d python=3.9
conda activate sav3d

conda install -c conda-forge libstdcxx-ng
pip install smplx[all] open3d plyfile moderngl-window==2.4.6 pyglet aitviewer robust_laplacian scikit-learn pandas

pip install git+https://github.com/mattloper/chumpy@9b045ff5d6588a24a0bab52c83f032e2ba433e17
pip install git+https://github.com/facebookresearch/pytorch3d.git@75ebeeaea0908c5527e7b1e305fbc7681382db47


