# convert_ros2_qt.py

## 📌 Overview
`convert_ros2_qt.py` is a Python script that automates the creation of **ROS2 Qt GUI packages**.  
It copies a **template (`ros2_qt_template/`)**, renames files, and updates configurations.

## 📂 Project Structure
```
.
├── convert_ros2_qt.py        # Main script
├── ros2_qt_template          # ROS2 Qt package template
│   ├── CMakeLists.txt        # CMake configuration
│   ├── package.xml           # ROS2 package metadata
│   ├── include/qt_gui_template/
│   ├── src/
│   ├── ui/
```

## 🚀 Usage
1. **Run the script**
   ```bash
   python3 convert_ros2_qt.py
   ```
2. **Enter details**
   ```
   Enter the workspace path (default: ~/ROS2/Qt_ws/src): 
   Enter the new package name: my_qt_package
   ```
3. **Build and run the package**
   ```bash
   cd ~/ROS2/Qt_ws
   colcon build --packages-select my_qt_package
   source install/setup.bash
   ros2 run my_qt_package my_qt_package
   ```

## 🛠️ Features
✔ **Automatically renames package files and folders**  
✔ **Updates `CMakeLists.txt` and `package.xml`**  
✔ **Ensures correct Qt & ROS2 dependencies**  

## 📜 License
This project is licensed under the **MIT License**.
