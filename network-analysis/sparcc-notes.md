
Creation of SparCC conda environment
```
$ conda create --name sparcc python=2.6.9
$ conda activate sparcc
$ conda install numpy=1.9.2 pandas=0.16.2
$ conda list
# packages in environment at xxx/envs/sparcc:
#
# Name                    Version                   Build  Channel
ca-certificates           2018.03.07                    0
libcxx                    4.0.1                h579ed51_0
libcxxabi                 4.0.1                hebd6815_0
libedit                   3.1.20170329         hb402a30_2
ncurses                   6.1                  h0a44026_0
numpy                     1.9.2                    py26_0
openssl                   1.0.2p               h1de35cc_0
pandas                    0.16.2               np19py26_0
pip                       7.1.0                    py26_0
python                    2.6.9                         0
python-dateutil           2.4.2                    py26_0
pytz                      2015.4                   py26_0
readline                  6.2                           2
setuptools                18.0.1                   py26_0
six                       1.9.0                    py26_0
sqlite                    3.24.0               ha441bb4_0
tk                        8.5.18                        0
zlib                      1.2.11               hf3cbc9b_2
```

SparCC was then downloaded on 16 August 2018 (commit: 05f4d3f), and commands were executed from within the resulting directory.

The `run-sparcc.py` script in this directory was used to execute SparCC, get bootstrap tables, and then compute p-values.
