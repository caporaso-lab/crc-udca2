# SRA submission and retrieval notes

This directory contains notes on how the data for this project was prepared for submission to SRA, and how the data from this project can be retrieved from SRA and loaded into QIIME 2 (tested with QIIME 2 2019.1).

These notes aren't extremely detailed, but they may serve as a useful reference.

The files in this directory are as follows:

- `download-and-import-sra-data.ipynb` : Jupyter notebook illustrating how to load downloaded SRA data into QIIME 2 2019.1 for this project. The development of this workflow was informed by the [SRA documentation](https://www.ncbi.nlm.nih.gov/sra/docs/sradownload/).
- `human-filter-single-end-reads-for-submission.ipynb` : Jupyter notebook illustrating how the human read filter (removal of human reads) was performed for this study. The development of this workflow was informed by [Qiita's host filtering workflow](https://github.com/qiita-spots/qp-shogun/blob/c1f3183c8003c809a8b7fd3cf2bdc082233c372d/notebooks/host_filtering.rst), and the [bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml), [samtools](http://samtools.sourceforge.net/), and [bedtools](https://bedtools.readthedocs.io/en/latest/) documentation.
- `sra-submission-sheet.tsv` : the sample metadata in SRA format. Note that this is also a properly formatting QIIME 2 metadata file.
- `human-filter-environment.yml` : the exported conda environment where the human read filtering steps were run.
