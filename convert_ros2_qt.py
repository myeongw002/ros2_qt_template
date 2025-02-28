import os
import shutil

# Default template directory
TEMPLATE_DIR = "ros2_qt_template"

def replace_in_file(file_path, old_text, new_text):
    """Replace a specific string in a file with a new string."""
    with open(file_path, "r") as file:
        content = file.read()
    content = content.replace(old_text, new_text)
    with open(file_path, "w") as file:
        file.write(content)

def create_package(ws_path, package_name):
    """Create a new ROS2 Qt package based on the template."""
    package_path = os.path.join(ws_path, package_name)

    # Remove existing package if it already exists
    if os.path.exists(package_path):
        print(f"Removing existing package '{package_name}'...")
        shutil.rmtree(package_path)

    print(f"Creating ROS2 Qt package '{package_name}' in '{ws_path}' from template...")

    # Copy the template directory
    shutil.copytree(TEMPLATE_DIR, package_path)

    # 🔹 Update package name in CMakeLists.txt and package.xml
    replace_in_file(os.path.join(package_path, "CMakeLists.txt"), "qt_gui_template", package_name)
    replace_in_file(os.path.join(package_path, "package.xml"), "qt_gui_template", package_name)

    # 🔹 Rename the include directory
    old_include_dir = os.path.join(package_path, "include", "qt_gui_template")
    new_include_dir = os.path.join(package_path, "include", package_name)
    os.rename(old_include_dir, new_include_dir)

    # 🔹 Update namespace in C++ source files
    replace_in_file(os.path.join(package_path, "include", package_name, "mainwindow.h"), "qt_gui_template", package_name)
    replace_in_file(os.path.join(package_path, "src", "main.cpp"), "qt_gui_template", package_name)
    replace_in_file(os.path.join(package_path, "src", "mainwindow.cpp"), "qt_gui_template", package_name)

    print(f"Package '{package_name}' has been successfully created in '{ws_path}'! 🎉")

if __name__ == "__main__":
    # Get workspace path from user
    ws_path = input("Enter the workspace path (default: ~/ROS2/Qt_ws/src): ").strip()
    if not ws_path:
        ws_path = os.path.expanduser("~/ROS2/Qt_ws/src")

    # Get package name from user
    package_name = input("Enter the new package name: ").strip()

    if not package_name:
        print("Package name cannot be empty!")
    else:
        create_package(ws_path, package_name)

