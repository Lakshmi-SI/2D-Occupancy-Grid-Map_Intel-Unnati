import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ImageListener(Node):

    def __init__(self):
        super().__init__('image_listener')
        self.bridge = CvBridge()


        # List of camera topics and corresponding frame IDs
        self.camera_topics = [
            '/overhead_camera/overhead_camera1/image_raw',
            '/overhead_camera/overhead_camera2/image_raw',
            '/overhead_camera/overhead_camera3/image_raw',
            '/overhead_camera/overhead_camera4/image_raw'
        ]

        # Create a subscription for each camera topic
        self.camera_subscriptions = []
        for i, topic in enumerate(self.camera_topics):
            subscription = self.create_subscription(
                Image,
                topic,
                lambda msg, idx=i: self.listener_callback(msg, idx),
                10)
            self.camera_subscriptions.append(subscription)

    def listener_callback(self, msg, camera_index):
        self.get_logger().info(f'Receiving image from camera {camera_index + 1}')
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow(f"Camera {camera_index + 1} Image", cv_image)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = ImageListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

