import cv2
import os
import argparse

parser = argparse.ArgumentParser(description='code for extracting frames from video')

parser.add_argument('--input_video', type=str, help='Video path to save result. See default for an e.g.', 
                                default='output_videos_wav2lip/1.mp4')

parser.add_argument('--frames_path', type=str, help='Video path to save result. See default for an e.g.', 
                                default='frames_wav2lip/1/')

args = parser.parse_args()

# Read the video file
video_path = args.input_video
video = cv2.VideoCapture(video_path)

# Get the frames per second (fps) and duration of the video
fps = int(video.get(cv2.CAP_PROP_FPS))
duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a folder to store the extracted frames
frame_folder = args.frames_path
os.makedirs(frame_folder, exist_ok=True)

# Initialize a counter for the frame index
frame_index = 0

# Loop through each frame of the video and save it as an image file
for i in range(duration):
    ret, frame = video.read()
    if not ret:
        break
    # Save the frame as an image file in the frame folder
    frame_file = os.path.join(frame_folder, f'frame_{frame_index:05d}.jpg')
    cv2.imwrite(frame_file, frame)
    frame_index += 1

print("Frames extracted and stored at ", args.frames_path)
# Release the video object
video.release()