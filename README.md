# MMT_experiments

Further experiments on the basis of "Probing the Need for Visual Context in Multimodal Machine Translation" (Caglayan et al, 2019) [1]

All experiments are implemented in nmtpytorch [2]. The included copy of the
nmtpytorch repository includes several changes to ensure compability with
pytorch 1.4 and CUDA 10.2. No model architectures were changed in
the process, but the att.ipynb scripts was severly changed to reintegrate in
the current nmtpytorch repository.

## Installation

nmtpytorch requires at least one GPU to work! 

Clone the repository:

```
git clone git@gitlab.cl.uni-heidelberg.de:hubert/mmt_experiments.git
```

We recommend the usage of a virtual environment:

```
python -m venv mmt_ex
source mmt_ex/bin/activate
```

install the requirements

```
pip install requirements.txt
```

and install the nmtpytorch package using the `setup.py` script

```
cd nmtpytorch/
python install setup.py
```

Do not use the pip installable nmtpytorch version, unless you use pytorch
<= 1.0!

Run 

```
nmtpy-install-extra
```

_once_ to download METEOR related files into your `${HOME}/.nmtpy` folder

If not configured, set your CUDA_VISIBLE_DEVICES environment variable, e. g.

```
export CUDA_VISIBLE_DEVICES=0
```


If you encounter trouble or wish to know more, consult the excellent nmtpytorch
wiki [3]


## Running experiments


### Preparation

First create the vocabularies for the models. Change into the directory
containng your dataset and run

```
nmtpy-build-vocab
```

Note that you only need to do this once.

If you wish to perform more experiments than training the models on the entire
dataset, you must first create the ablated and foiled datasets.
Firstly, edit the file- and pathnames in `constants.py` to suit your personal
setup. Then perform l2 normalisation as advised in [1]:

```
python create_l2.py
```

*Warning: This step takes at least 45 GB of RAM!*

* Progressive Masking: To create the progressively marked datasets, run

```
python mask_datasets.py
```

* Random Foil words: To create the randomly replaced datasets, run


```
python randomise_datasets.py
```

and if you want to replace words with words of the same Part-Of-Speech tags
run (both all tags and one specific tag)

```
python tag_text.py
python randomise_datasets_only_same_pos.py
```

### Model training

Simply run

```
nmtpy train -C <config file>
```

to train a model with the configuration given in the config file. We provide
all configuration files to repeat the experiments performed in the report.
For instance, run

```
nmtpy train -C mmt-task-en-fr-multimodalatt_random_pos_replacement4.conf
```

to train the MMT model on the dataset with for tokens randomly replaced with
tokens with the same Part-Of-Speech tag.

### Evaluation

```
nmtpy translate -k 12 -b 64 -s test_2017_flickr -o translate_mmt_random_pos4/mmt-task-en-fr-multimodalatt_random_pos_replacement4/{model-name}
nmtpy-coco-metrics translate_mmt_random_pos4.test_2017_flickr.beam12 -l fr -r ../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.fr 
```

to get the entire metric for the trained model.
Note that all relevant options are defined in the config file:

* model type
* model hyperparameters
* savepath
* datasets
* vocabulary


You may run various experiments with the same configuration, write the output to a text file and use `get_mean_and_std.py` to get the mean and standard deviation, after adapting the filenames.

### Visualisation

You may use the `att.ipynb` jupyter-ǹotebook to visualise the attention
patterns of your models.
Note that doing so requires a non-neglatable amount of RAM and an NVIDIA-GPU.

[1] http://arxiv.org/abs/1903.08678

[2] https://github.com/lium-lst/nmtpytorch

[3] https://github.com/lium-lst/nmtpytorch/wiki

