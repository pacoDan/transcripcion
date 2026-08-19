install en linux
```sh
conda create -n whisper
conda activate whisper
conda install pip -y
pip install -U openai-whisper
conda install -c conda-forge ffmpeg
```
sino primero antes:
```sh
conda config --set always_yes true
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```
para borrar el entorno y las dependencias:
```sh
conda remove --name whisper --all -y # Eliminar el entorno y sus paquetes asociados
conda clean --all -y # Limpiar el caché de Conda (Crucial para recuperar espacio)

```
https://github.com/openai/whisper#:~:text=pip%20install%20setuptools%2Drust

ver luego:
https://github.com/jhdeov/whisper-to-textgrid-batch/
https://github.com/benmaster82/writher

de http a ssh para push:
```sh

git remote set-url origin git@github.com:pacodan/transcripcion.git
```

```~~ 
```
