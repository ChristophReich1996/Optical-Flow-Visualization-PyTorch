import setuptools

setuptools.setup(
    name="flow_vis_torch",
    packages=["flow_vis_torch"],
    version="0.1",
    license="MIT",
    author="Christoph Reich",
    description="Easy optical flow visualisation in Python (PyTorch).",
    url="https://github.com/ChristophReich1996/Optical-Flow-Visualization-PyTorch",
    keywords=["optical flow", "visualization", "motion"],
    install_requires=["torch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
