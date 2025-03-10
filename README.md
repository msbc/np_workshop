# NumPy Done Right: Speed, Efficiency, and Best Practices

These are jupyter notebooks for an introductory course on NumPy, vectorization and optimization.

## Based on/Forked from

[Vineet Bansal's Introduction to Numpy](https://github.com/vineetbansal/np_workshop)

## Before the workshop

...And by "before the workshop", I just expect you to do this right now. Hopefully, you already have a place where you've used the Anaconda package manager for Python before. If not, you can install it now.

### Clone This Repository

Please clone this repository to your local machine before the workshop. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/msbc/np_workshop.git
```

### Anaconda Python Distribution

We will be using the [Anaconda Python Distribution](https://www.anaconda.com/download) for this course. Anaconda is a popular software that gives us everything we need to get started in Python - the Python 3 interpreter, common Python libraries for scientific computing, plotting and analysis, jupyter Notebooks, and a lightweight IDE (Integrated Development Environment) for more advanced users.

Please ensure that you follow the instructions posted at:
https://researchcomputing.princeton.edu/learn/workshops-live-training/requirements-picscie-virtual-workshops#jupyter

and validate your setup using the sample notebook available as part of the instructions.

Advanced users may just choose to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Create a Virtual Environment

It is a good practice to create a virtual environment for each project you work on. This way, you can install the specific versions of the libraries you need for that project without affecting other projects you are working on.

The specification for the environment is in the `environment.yml` file. If you already have an envireonment with `numpy` and `jupyter` (and optionally `matplotlib`), that is sufficent. You can create the environment by running the following command in your terminal:

```bash
conda env create -f environment.yml
```

This will create a new environment called `np_workshop`. You can activate the environment by running:

```bash
conda activate np_workshop
```

If you're still having trouble with launching the notebooks locally on your computer, try Github codespaces. You can launch the notebooks in a browser without installing anything on your computer. Just click on the green button "Code" and select "Open with Codespaces".

## Suggested Code Editors

Picking a code editor is a *very* personal choice. Below are some suggetions that I have personally used. I will be using Visual Studio Code for this workshop.

- [Visual Studio Code](https://code.visualstudio.com/) (my goto editor)
  - See also [RC's VS Code help page](https://researchcomputing.princeton.edu/support/knowledge-base/vs-code)
- [Vim](https://www.vim.org/) (my goto command line editor, steep learning curve)
  - [MacVim](https://macvim.org/) (for MacOS only)
- [PyCharm](https://www.jetbrains.com/pycharm/) (great for Python only code bases)
