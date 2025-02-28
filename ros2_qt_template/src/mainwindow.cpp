#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow) {
    ui->setupUi(this);

    // ROS2 노드 생성
    node = rclcpp::Node::make_shared("qt_gui_node");
    publisher = node->create_publisher<std_msgs::msg::String>("/chatter", 10);

    // 버튼 클릭 시 onButtonClicked() 슬롯 호출
    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::onButtonClicked);
}

MainWindow::~MainWindow() {
    delete ui;
}

// 버튼 클릭 시 실행되는 함수 (ROS2 메시지 퍼블리시)
void MainWindow::onButtonClicked() {
    auto message = std_msgs::msg::String();
    message.data = "Hello from Qt!";
    publisher->publish(message);
    RCLCPP_INFO(node->get_logger(), "Published: %s", message.data.c_str());
}

