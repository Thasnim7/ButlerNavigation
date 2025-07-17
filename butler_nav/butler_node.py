import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ButlerNode(Node):
    def __init__(self):
        super().__init__('butler_node')
        self.subscription = self.create_subscription(
            String,
            'order_request',
            self.listener_callback,
            10
        )
        self.get_logger().info("🤖 Butler ready for orders...")

    def listener_callback(self, msg):
        table = msg.data
        self.get_logger().info(f'📦 Received order for {table}')
        self.get_logger().info(f'🚚 Delivering to {table}... Done!')

def main(args=None):
    rclpy.init(args=args)
    node = ButlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

