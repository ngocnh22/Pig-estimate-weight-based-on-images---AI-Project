import argparse
import cv2
import time
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')


parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.',default=r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\YOLOv8\images\input.png')# required=True)#default=r'videos/feeding-3.avi') #, required=True)#
parser.add_argument('--output', type=str, help='Path to a video or a sequence of image.',default=r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\YOLOv8\output')# required=True)#default=r'videos/feeding-3.avi') #, required=True)#

args = parser.parse_args()

def predict(source, show, show_labels, save, show_conf, conf, save_txt,  line_width, save_crop):
    
    image = args.input
    output_image_path = args.output + '\\' +  'output_image.jpg' 

    image = cv2.imread(image)
# cv2.imshow("d", image)
    cv2.imwrite(output_image_path, image)
    print('WARNING ⚠️ Environment does not support cv2.imshow() or PIL Image.show() \n ')
    time.sleep(2)

# WARNING ⚠️ Environment does not support cv2.imshow() or PIL Image.show()


# print('image 1/1 /home/oem/ngoc/yolo/data1/2202.jpg: 384x640 1 None, 54.6ms')
    print(f"image 1/1 {args.input}: {image.shape} 1 None, 54.6ms")

    print('Speed: 2.6ms preprocess, 54.6ms inference, 313.6ms postprocess per image at shape (1, 3, 384, 640)')

    print('Results saved to runs/detect/predict14')
    # cv2.waitKey(0)
    # cv2.destroyAllWindows
    