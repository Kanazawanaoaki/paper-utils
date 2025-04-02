import rospy
import rosbag
import argparse
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge
import cv2

def save_first_image(bag_path, image_topic):
    # rosbagを開く
    bag = rosbag.Bag(bag_path, 'r')

    print(bag_path, image_topic)

    bridge = CvBridge()
    first_image_saved = False

    for topic, msg, t in bag.read_messages(topics=[image_topic]):
        print(topic, t)
        cv_image = bridge.compressed_imgmsg_to_cv2(msg)
        # if isinstance(msg, CompressedImage):
        #     # 圧縮画像の場合
        #     cv_image = bridge.compressed_imgmsg_to_cv2(msg)
        # elif isinstance(msg, Image):
        #     # 未圧縮画像の場合
        #     cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # else:
        #     continue

        # 最初の画像を保存
        if not first_image_saved:
            filename = 'first_image.png'
            cv2.imwrite(filename, cv_image)
            print(f"画像が保存されました: {filename}")
            first_image_saved = True
            break

    bag.close()

if __name__ == '__main__':
    # 引数の解析
    parser = argparse.ArgumentParser(description="rosbagから最初の画像を保存するプログラム")
    parser.add_argument('bag_path', type=str, help="rosbagファイルのパス")
    parser.add_argument('image_topic', type=str, help="画像のトピック名")
    args = parser.parse_args()

    # 最初の画像を保存
    save_first_image(args.bag_path, args.image_topic)
