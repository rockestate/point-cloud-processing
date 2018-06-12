# point-cloud-processing
Point cloud processing slides

Static presentation available [here](https://www.rockestate.be/point-cloud-processing/presentation/)

Static notebook available [here](https://github.com/rockestate/point-cloud-processing/blob/master/notebooks/point-cloud-processing.ipynb) or try running it live in the browser with [Binder](https://mybinder.org/v2/gh/rockestate/point-cloud-processing/master)!

## Initial setup

Will work on Linux, macOS, and Windows.

Make sure you have `git` and [`conda`](https://conda.io/miniconda.html) installed and on your path.

```shell
git clone https://github.com/rockestate/point-cloud-processing
cd point-cloud-processing
conda env create -f environment.yml --force
```

## Running the notebook

```shell
source activate pcp-env
jupyter notebook
```

Then go to the `notebooks` folder and run `point-cloud-processing.ipynb`.

Don't forget to specify a region when presented with the leaflet maps.
