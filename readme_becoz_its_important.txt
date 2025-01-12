for the github codespace

/// first you have to type this command for an issue with the cv2 library (OpenCV),
 specifically its dependency on libGL.so.1. This means that the OpenGL library 
 required by OpenCV is missing or not correctly configured in your environment.

sudo apt update

sudo apt install libgl1-mesa-glx

/// here another issue arise "Also, ensure that ffmpeg is installed on your system and available in your PATH"

sudo apt update
sudo apt install ffmpeg

/// then Please make sure you have the latest version of pytube and ffmpeg-python installed.

pip install --upgrade pytube ffmpeg-python

/// This request was detected as a bot. Use `use_po_token=True` to view. See more details at https://github.com/JuanBindez/pytubefix/pull/209

use_po_token ="MlPY1DjNnpOh9NjopK52MqjiZGtpFmoDeFcU42BKUe5WTSleAEd1w2krjF3AJXr3bc58usiicn3Lh8PDPzthnVeMEgi7LoUu2W99a-rYDsz7hx7EQg=="
visitorData= "CgtWcDM5RkN4bVlOdyiN-o28BjIKCgJJThIEGgAgWg%3D%3D"