#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void onButtonClicked();  // 버튼 클릭 시 호출되는 함수

private:
    Ui::MainWindow *ui;
    rclcpp::Node::SharedPtr node;  // ROS2 노드
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher;  // ROS2 퍼블리셔
};

#endif  // MAINWINDOW_H

