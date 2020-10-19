# This is a dataset downloader for the countix700 dataset
We took a liberty to create a downloader for this [dataset](https://deepmind.com/research/open-source/kinetics)

### Requirements:
`ffmpeg`, `openssl` (check your certs before running, fix if needed)

### Installation
* This project requires Python 3.7
* Start by cloning this project to folder of your choice:
```sh
$ git clone https://github.com/koljanos/dataset_downloader
```
* Then cd into it:

```sh
$ cd dataset_downloader
```
* Then create and actiavate new virtualenv

```sh
$ virtualenv venv
$ source /venv/bin/activate
```

* Install requirements.txt

```sh
$ pip3 install -r requirements.txt
```

* You can change the `config.py` file to your liking:

```py
spisok = ["push up"] # its alist with the classes needed to download
number = 10 # its the number of videos
folders = ["train", "val"] # its the list of folders needed to be populated
```

* Finally run `run.py`

```sh
$ python run.py
```

## Enjoy your pc doing your job for ya!