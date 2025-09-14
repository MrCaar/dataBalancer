from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="smart-mix-split",
    version="1.0.0",
    author="Smart Mix Split Contributors",
    author_email="",
    description="Havalimanı yorumlarını akıllı örnekleme ve veri analizi aracı",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrcaar/smartMixSplit",
    project_urls={
        "Bug Tracker": "https://github.com/mrcaar/smartMixSplit/issues",
        "Documentation": "https://github.com/mrcaar/smartMixSplit#readme",
        "Source Code": "https://github.com/mrcaar/smartMixSplit",
        "Changelog": "https://github.com/mrcaar/smartMixSplit/blob/main/CHANGELOG.md",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="data-science, sampling, csv, pandas, airport-reviews, stratified-sampling, data-analysis",
    py_modules=["smart_mix_split"],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.8",
            "black>=21.0",
            "bandit>=1.7",
            "safety>=1.10",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "smart-mix-split=smart_mix_split:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["README.md", "LICENSE", "CHANGELOG.md", "requirements.txt"],
    },
    zip_safe=False,
)
