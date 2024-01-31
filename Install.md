# Installation of FunTB V.0.0.1

Last updated: Jan 31, 2024

FunTB is an open source standalone tool available for academic purposes. For commercial use of FunTB please contact: industrial.genomics@gmail.com

Please feel free to post on **Issues** or contact axel.ramos3737@gmail.com

## 1.- FunTB requirements

 * Python: 3.11.5
 * Pandas: 2.0.2
 * Numpy: 1.24.3
 * Matplotlib: 3.7.1
 * Networkx: 3.1
 * Seaborn: 0.13.0
 * Scipy: 1.11.1

### 1.1 Install dependencies

```bash
# Install Python 3.11.5
```
[Python (windows)](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe) v.3.11.5

# Install Mamba package manager (faster!)
conda install mamba -n base -c conda-forge

# Create FunGAP environment and install dependencies using Mamba
conda create -y -n fungap
conda activate fungap
mamba install \
  braker2=2.1.5 trinity=2.12.0 repeatmodeler=2.0.1 hisat2=2.2.1 pfam_scan=1.6 busco=5.1.2 \
  -c bioconda -c conda-forge

# Install Python and Perl modules (within fungap environment)
pip install biopython bcbio-gff markdown2 matplotlib
cpanm YAML Hash::Merge Logger::Simple Parallel::ForkManager MCE::Mutex Thread::Queue threads

# Install Maker using Mamba (Maker installation is conflict with Busco)
conda deactivate
conda create -y -n maker
conda activate maker
mamba install maker=3.01.03 -c bioconda -c conda-forge
```

 
