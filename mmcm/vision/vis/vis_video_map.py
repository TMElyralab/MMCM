# -*- encoding: utf-8 -*-
import sys
import json

import cv2
from moviepy.editor import VideoFileClip


def vis_video_map(video_path, video_map, save_path):
    # raise NotImplementedError("This function is not implemented yet.")
    if isinstance(video_map, str):
        video_map = json.load(open(video_map, encoding="UTF-8"))
    face_detections = []
    for i in video_map["face_detections"]:
        if i["faces"] and len(i["faces"]) > 0:
            face_detections.append(i)
    video_path = video_map["video_path"]
    # Capture video
    video = VideoFileClip(video_path)
    video = video.crop(*video_map["content_box"])
    fps = video.fps
    duration = video.duration
    width, height = video.size
    print("fps, duration, width, height:", fps, duration, width, height)
    vid_writer = cv2.VideoWriter(
        save_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        video_map["detect_fps"],
        (width, height),
    )
    frame_idx = 0
    face_idx = 0
    for im in video.iter_frames(fps=video_map["sample_fps"]):
        if face_idx == len(face_detections):
            break
        if frame_idx == 50000:
            break
        if frame_idx == face_detections[face_idx]["frame_idx"]:
            print(frame_idx)
            pred = face_detections[face_idx]["faces"]
            im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
            # TODO: to visualize the face detection results
            # Stream results
        frame_idx += 1
