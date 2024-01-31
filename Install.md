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

##### Python v.3.11.5

[Windows](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)
[Linux](https://www.python.org/ftp/python/3.11.5/Python-3.11.5.tgz)
[macOS](https://www.python.org/ftp/python/3.11.5/python-3.11.5-macos11.pkg)

##### Pandas 2.0.2
```bash
# Pip: Run pip install pandas == <version>
pip install pandas == 2.0.2
```
```bash
# Anaconda: Run conda install pandas = <version>
conda install pandas = 2.0.2
```
##### Numpy 1.24.3
```bash 
# Pip: Run pip install numpy == <version>
pip install numpy == 1.24.3
```
```bash
# Anaconda: Run conda install numpy = <version>
conda install numpy = 1.24.3
```

> [!Note]
> If you have already installed a specific version of NumPy and want to install another version, use "--force-reinstall" e.g., "pip install -- force-reinstall numpy== version". Or, if you have a virtual env and want to override the installation without uninstalling, use "--ignore-installed", e.g., "pip install --ignore-installed numpy== version".

##### Matplotlib 3.7.1
```bash 
# Pip: Run pip install matplotlib == <version>
pip install matplotlib == 1.24.3
```
```bash
# Anaconda: Run conda install matplotlib = <version>
conda install matplotlib = 1.24.3
```
##### Networkx 3.1 
##### Seaborn 0.13.0
##### Scipy 1.11.1


# Install Mamba package manager (faster!)
conda install mamba -n base -c conda-forge


 
