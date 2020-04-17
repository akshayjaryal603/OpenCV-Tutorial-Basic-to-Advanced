# import os
# import cv2

# def test_input_framerate():
# 	"""
# 	Testing "-input_framerate" special parameter provided by WriteGear(in Compression Mode) 
# 	"""
# 	stream = cv2.VideoCapture(0) #Open live webcam video stream on first index(i.e. 0) device    return_testvideo_path()
# 	test_video_framerate = stream.get(cv2.CAP_PROP_FPS)
# 	output_params = {"-input_framerate":test_video_framerate}
# 	writer = WriteGear(output_filename = 'Output_tif.mp4', custom_ffmpeg = return_static_ffmpeg(), **output_params) #Define writer 
# 	while True:
# 		(grabbed, frame) = stream.read()
# 		if not grabbed:
# 			break
# 		writer.write(frame) 
# 	stream.release()
# 	writer.close()
# 	output_video_framerate = getFrameRate(os.path.abspath('Output_tif.mp4'))
# 	assert test_video_framerate == output_video_framerate
# 	os.remove(os.path.abspath('Output_tif.mp4')) 

# test_input_framerate()

import cv2
if __name__ == '__main__' :

    video = cv2.VideoCapture(0);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    video.release()