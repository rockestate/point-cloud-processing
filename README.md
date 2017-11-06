# point-cloud-processing
Point cloud processing slides

Static presentation available [here](https://www.rockestate.be/point-cloud-processing/presentation/)

Notebook available [here](https://github.com/rockestate/point-cloud-processing/blob/master/notebooks/point-cloud-processing.ipynb)

## Initial setup

Will work on linux, may work on macOS. [Get in touch](mailto:hello@rockestate.be) if you'd like to give us a hand to make it run on Windows.

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
