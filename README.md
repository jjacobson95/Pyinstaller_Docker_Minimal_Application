# Pyinstaller_Docker_Minimal_Application

Repository created in response to issue https://github.com/pyinstaller/pyinstaller/issues/7255.


Required: 
Windows PC - Windows 10 Enterprise
Docker Desktop 4.14.1 (Previously tried 4.13 and 4.11 with same result)




More info:


Active pip packages:
brotlipy               0.7.0
certifi                2022.9.24
cffi                   1.15.0
charset-normalizer     2.0.4
colorama               0.4.4
conda                  22.9.0
conda-content-trust    0+unknown
conda-package-handling 1.8.1
contourpy              1.0.6
cryptography           36.0.0
cycler                 0.11.0
docker                 6.0.1
fonttools              4.38.0
idna                   3.3
kiwisolver             1.4.4
libmambapy             0.25.0
mamba                  0.25.0
matplotlib             3.6.2
menuinst               1.4.18
mkl-fft                1.3.1
mkl-random             1.2.2
mkl-service            2.4.0
numpy                  1.23.1
packaging              21.3
pandas                 1.5.1
Pillow                 9.3.0
pip                    21.2.4
pycosat                0.6.3
pycparser              2.21
PyMuPDF                1.21.0
pyOpenSSL              22.0.0
pyparsing              3.0.9
pypiwin32              223
PySocks                1.7.1
python-dateutil        2.8.2
pytz                   2022.6
pywin32                305
pywin32-ctypes         0.2.0
requests               2.27.1
ruamel-yaml-conda      0.15.100
setuptools             61.2.0
six                    1.16.0
tkPDFViewer            0.1
toolz                  0.11.2
tqdm                   4.63.0
ttkthemes              3.2.2
urllib3                1.26.8
websocket-client       1.4.2
wheel                  0.37.1
win-inet-pton          1.1.0
wincertstore           0.2

Active Conda Packages:
blas                      1.0                         mkl
brotlipy                  0.7.0           py39h2bbff1b_1003
bzip2                     1.0.8                h8ffe710_4    conda-forge
ca-certificates           2022.10.11           haa95532_0
certifi                   2022.9.24        py39haa95532_0
cffi                      1.15.0           py39h2bbff1b_1
charset-normalizer        2.0.4              pyhd3eb1b0_0
colorama                  0.4.4              pyhd3eb1b0_0
conda                     22.9.0           py39haa95532_0
conda-content-trust       0.1.1              pyhd3eb1b0_0
conda-package-handling    1.8.1            py39h8cc25b3_0
console_shortcut          0.1.1                         4
contourpy                 1.0.6                    pypi_0    pypi
cryptography              36.0.0           py39h21b164f_0
cycler                    0.11.0                   pypi_0    pypi
docker                    6.0.1                    pypi_0    pypi
fonttools                 4.38.0                   pypi_0    pypi
git                       2.34.1               haa95532_0
idna                      3.3                pyhd3eb1b0_0
intel-openmp              2021.4.0          haa95532_3556
kiwisolver                1.4.4                    pypi_0    pypi
libarchive                3.5.2                hb45042f_3    conda-forge
libcurl                   7.84.0               h86230a5_0
libiconv                  1.17                 h8ffe710_0    conda-forge
libmamba                  0.25.0               h81a967f_1    conda-forge
libmambapy                0.25.0           py39h4126fcf_1    conda-forge
libsolv                   0.7.22               h7755175_0    conda-forge
libssh2                   1.10.0               h680486a_2    conda-forge
libxml2                   2.9.14               h0ad7f3c_0
libzlib                   1.2.12               h8ffe710_2    conda-forge
lz4-c                     1.9.3                h8ffe710_1    conda-forge
lzo                       2.10              he774522_1000    conda-forge
mamba                     0.25.0           py39hb3d9227_1    conda-forge
matplotlib                3.6.2                    pypi_0    pypi
menuinst                  1.4.18           py39h59b6b97_0
mkl                       2021.4.0           haa95532_640
mkl-service               2.4.0            py39h2bbff1b_0
mkl_fft                   1.3.1            py39h277e83a_0
mkl_random                1.2.2            py39hf11a4ad_0
numpy                     1.23.1           py39h7a0a035_0
numpy-base                1.23.1           py39hca35cd5_0
openssl                   1.1.1s               h2bbff1b_0
packaging                 21.3                     pypi_0    pypi
pandas                    1.5.1                    pypi_0    pypi
pillow                    9.3.0                    pypi_0    pypi
pip                       21.2.4           py39haa95532_0
powershell_shortcut       0.0.1                         3
pybind11-abi              4                    hd8ed1ab_3    conda-forge
pycosat                   0.6.3            py39h2bbff1b_0
pycparser                 2.21               pyhd3eb1b0_0
pymupdf                   1.21.0                   pypi_0    pypi
pyopenssl                 22.0.0             pyhd3eb1b0_0
pyparsing                 3.0.9                    pypi_0    pypi
pypiwin32                 223                      pypi_0    pypi
pysocks                   1.7.1            py39haa95532_0
python                    3.9.12               h6244533_0
python-dateutil           2.8.2                    pypi_0    pypi
python_abi                3.9                      2_cp39    conda-forge
pytz                      2022.6                   pypi_0    pypi
pywin32                   305                      pypi_0    pypi
pywin32-ctypes            0.2.0                    pypi_0    pypi
reproc                    14.2.4               hd77b12b_1
reproc-cpp                14.2.4               hd77b12b_1
requests                  2.27.1             pyhd3eb1b0_0
ruamel_yaml               0.15.100         py39h2bbff1b_0
setuptools                61.2.0           py39haa95532_0
six                       1.16.0             pyhd3eb1b0_1
sqlite                    3.38.2               h2bbff1b_0
tkpdfviewer               0.1                      pypi_0    pypi
toolz                     0.11.2             pyhd3eb1b0_0
tqdm                      4.63.0             pyhd3eb1b0_0
ttkthemes                 3.2.2                    pypi_0    pypi
tzdata                    2022a                hda174b7_0
urllib3                   1.26.8             pyhd3eb1b0_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
websocket-client          1.4.2                    pypi_0    pypi
wheel                     0.37.1             pyhd3eb1b0_0
win_inet_pton             1.1.0            py39haa95532_0
wincertstore              0.2              py39haa95532_2
xz                        5.2.5                h62dcd97_1    conda-forge
yaml                      0.2.5                he774522_0
yaml-cpp                  0.7.0                h0e60522_1    conda-forge
zlib                      1.2.12               h8ffe710_2    conda-forge
zstd                      1.5.2                h6255e5f_3    conda-forge


