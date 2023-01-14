# PMR demo on Probabilistic Graphical Models (2023-2024)

This is a repository for tutorial on Probabilistic Graphical Models (PGMs) of Probabilistic Modelling and Reasoning (2023/2024) - a University of Edinburgh master's course.

The tutorial notebook with exercises is in [Heckerman car start model.ipynb](./Heckerman%20car%20start%20model.ipynb) and uses a Python package for (discrete) probabilistic graphical modelling, [pgmpy](https://github.com/pgmpy/pgmpy).

[Heckerman car start model with solutions.ipynb](./Heckerman%20car%20start%20model%20with%20solutions.ipynb) contains the solutions to the exercises, but we recommend first attempting to solve the exercises on your own.

## Environment setup

Perhaps the easiest way to run the demo is to use Google Colab, which is outlined below. Alternatively, you can use conda on your local machine to set up the Python environment and run the Jupyter notebook locally (see below).

### Google Colab

You can run the notebook on Google Colab directly via this link <http://colab.research.google.com/github/vsimkus/pmr2024-pgm-demo>.

More details on running notebooks from github on Google Colab can be found at <https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=WzIRIt9d2huC>.

### Setup on your machine (conda)

Alternatively you can setup the environment locally with conda. You will need to open terminal on your machine and then follow the below instructions

* Install git ([linux](https://git-scm.com/download/linux), [macOS](https://git-scm.com/download/mac), [windows](https://git-scm.com/download/win)) to access the repository if you don't have it already
* Clone the git repository on your machine by running `git clone` in the terminal (you can find a guide [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
* Once you've cloned the repository, step into the directory by entering `cd pmr2024-pgm-demo` into the terminal
* If you don’t already have it also install miniconda  ([linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html), [macOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html), [windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)), which will allow you to manage all python dependencies per project
* You can now create the `pmr` conda environment by typing `conda env create -f environment.yml`. This step may take a while to complete since it has to download large binaries and you should better be connected to a good internet connection.

#### Starting the Jupyter server

Once you have the environment prepared you can start your jupyter notebook

* Activate the conda environment with `conda activate pmr`
* Now you will be able to start your jupyter server by typing `jupyter notebook`, which will start the server and open a browser to access the tutorial notebook. Click tutorial link in the browser window. You can stop the server by pressing <kbd>Ctrl</kbd>+<kbd>c</kbd> (or <kbd>Cmd</kbd>+<kbd>c</kbd>) in the terminal when you are done with it.

## Attributions

The course is taught by [Michael Gutmann](https://michaelgutmann.github.io/) and [Chris Williams](https://homepages.inf.ed.ac.uk/ckiw/), and this tutorial was created by [Vaidotas Šimkus](https://github.com/vsimkus).

