# Wav2Lip-HD: High-Fidelity Lip-Syncing with Wav2Lip and Real-ESRGAN

This repository contains code for achieving high-fidelity lip-syncing in videos, using the [Wav2Lip algorithm](https://github.com/Rudrabha/Wav2Lip) for lip-syncing and the [Real-ESRGAN algorithm](https://github.com/xinntao/Real-ESRGAN) for super-resolution. The combination of these two algorithms allows for the creation of lip-synced videos that are both highly accurate and visually stunning.

## Acknowledgements

We would like to thank the following repositories and libraries for their contributions to our work:

1. The [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) repository, which is the core model of our algorithm that performs lip-sync.
2. The [face-parsing.PyTorch](https://github.com/zllrunning/face-parsing.PyTorch) repository, which provides us with a model for face segmentation.
3. The [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) repository, which provides the super resolution component for our algorithm.
4. [ffmpeg](https://ffmpeg.org), which we use for converting frames to video.

## Testing Model

To test the "Wav2Lip-HD" model, follow these steps:

1. Clone this repository and install requirements using following command:

    ```
    git clone https://github.com/saifhassan/Wav2Lip-HD.git
    cd Wav2Lip-HD
    pip install -r requirements.txt
    ```
    
### Downloading weights

| Model        | Directory           | Download Link  |
| :------------- |:-------------| :-----:|
| Wav2Lip           | [checkpoints/](checkpoints)   | [Link](https://drive.google.com/drive/folders/1tB_uz-TYMePRMZzrDMdShWUZZ0JK3SIZ?usp=sharing) |
| ESRGAN            | experiments/001_ESRGAN_x4_f64b23_custom16k_500k_B16G1_wandb/models/ | [Link](https://drive.google.com/file/d/1Al8lEpnx2K-kDX7zL2DBcAuDnSKXACPb/view?usp=sharing) |
| Face_Detection    | face_detection/detection/sfd/ | [Link](https://drive.google.com/file/d/1uNLYCPFFmO-og3WSHyFytJQLLYOwH5uY/view?usp=sharing) |
| Real-ESRGAN       | Real-ESRGAN/gfpgan/weights/   | [Link](https://drive.google.com/drive/folders/1BLx6aMpHgFt41fJ27_cRmT8bt53kVAYG?usp=sharing) |
| Real-ESRGAN       | Real-ESRGAN/weights/          | [Link](https://drive.google.com/file/d/1qNIf8cJl_dQo3ivelPJVWFkApyEAGnLi/view?usp=sharing) |


2. Put input video to `input_videos` directory and input audio to `input_audios` directory.
3. Open `run_final.sh` file and modify following parameters:
 
     `filename=kennedy` (just video file name without extension)
     
     `input_audio=input_audios/ai.wav` (audio filename with extension)

4. Execute `run_final.sh` using following command:

    ```
    bash run_final.sh
    ```
5. Output video file is stored at `output_videos_hd` directory.
