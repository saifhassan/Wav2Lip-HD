export filename=mona
export input_video=input_videos
export input_audio=input_audios/ai.wav
export frames_wav2lip=frames_wav2lip
export frames_hd=frames_hd
export output_videos_wav2lip=output_videos_wav2lip
export output_videos_hd=output_videos_hd
export back_dir=..

python3 inference.py --checkpoint_path "checkpoints/wav2lip_gan.pth" --segmentation_path "checkpoints/face_segmentation.pth" --sr_path "checkpoints/esrgan_yunying.pth" --face ${input_video}/${filename}.mp4 --audio ${input_audio} --save_frames --gt_path "data/gt" --pred_path "data/lq" --no_sr --no_segmentation --outfile ${output_videos_wav2lip}/${filename}.mp4
python video2frames.py --input_video ${output_videos_wav2lip}/${filename}.mp4 --frames_path ${frames_wav2lip}/${filename}
cd Real-ESRGAN
python inference_realesrgan.py -n RealESRGAN_x4plus -i ${back_dir}/${frames_wav2lip}/${filename} --output ${back_dir}/${frames_hd}/${filename} --outscale 3.5 --face_enhance
#ffmpeg -r 20 -i ${back_dir}/${frames_hd}/${filename}/frame_%05d_out.jpg -i ${back_dir}/${input_audios} -vcodec libx264 -crf 25 -preset veryslow -acodec copy ${back_dir}/${output_videos_hd}/${filename}.mkv