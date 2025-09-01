#!/usr/bin/env bash


# ffmpeg -i Galton_box.webm.1080p.vp9.webm -c:v libx264 -c:a aac -strict experimental ./Galton_box.mp4
# ffmpeg -ss 0 -t 30 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Galton_Box_More.mp4
# ffmpeg -ss 48 -t 5 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Student_Heights.mp4
# ffmpeg -ss 256 -t 64 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./General_Idea_CLT.mp4
# ffmpeg -ss 383 -t 103 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Dices_4Exps.mp4
# ffmpeg -ss 1381 -t 55 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Increase_Samples.mp4
# ffmpeg -ss 1436 -t 407 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Assumptions_CLT.mp4
ffmpeg -ss 705 -t 86 -i ./CLT_3Blue1Brown.webm -c:v libx264 -c:a aac -strict experimental ./Mean_Variance.mp4
