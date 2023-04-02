# Wav2Lip-HD: High-Fidelity Lip-Syncing with Wav2Lip and Real-ESRGAN

This repository contains code for achieving high-fidelity lip-syncing in videos, using the [Wav2Lip algorithm](https://github.com/Rudrabha/Wav2Lip) for lip-syncing and the [Real-ESRGAN algorithm](https://github.com/xinntao/Real-ESRGAN) for super-resolution. The combination of these two algorithms allows for the creation of lip-synced videos that are both highly accurate and visually stunning.

## Acknowledgements

We would like to thank the following repositories and libraries for their contributions to our work:

1. The [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) repository, which is the core model of our algorithm that performs lip-sync.
2. The [face-parsing.PyTorch](https://github.com/zllrunning/face-parsing.PyTorch) repository, which provides us with a model for face segmentation.
3. The [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) repository, which provides the super resolution component for our algorithm.
4. [ffmpeg](https://ffmpeg.org), which we use for converting frames to video.
