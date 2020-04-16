# Windows程序启动参数配置器

#### 介绍

该程序是一个轻量化的程序，旨在为用户在启动Windows应用时可以轻松地附加参数，无需繁琐地新建快捷方式。
“为程序启动添加参数”功能允许用户在启动Windows程序时键入自己需要的参数。
“为程序添加预设启动参数”允许用户按照预设的参数启动应用，并有管理器可以管理预设和目录。
本程序包含自动化配置脚本，在您修改代码后也可以轻松更新整个程序。
本程序使用Python3.7开发，仅可在Windows平台上运行。

#### 库版本

PyQt5 版本：5.11.3
pyinstaller 版本：3.6


#### 安装教程

自动安装（推荐）

1.  安装必须库
请先运行下列代码安装所需库。如果您已经安装了这些库，您可以跳过这一步。
```
pip3 install pyqt5
pip3 install pyinstaller
```

2.  配置注册列表
运行本程序根目录下的`setup.bat`，在提示是否允许对计算机进行修改时点击确定。
如果提示错误，请以管理员运行这个脚本。
如果您不能用'setup.bat'初始化您的程序，请您按照下述步骤手动配置。

手动安装

1.安装必须库
这一步骤和自动安装是相同的。

2.Python编译
如果您没有修改pyinstaller的配置，那么您可以直接利用下述代码使用pyinstaller将python脚本编译成为可执行文件。
```
cd 本程序目录
pyinstaller -Fw QuickStart.py
pyinstaller -Fw ConfigPre.py
```
生成的exe文件都保存在dist文件夹下。请不要移动它。

3.添加注册列表项
在注册列表中的HKEY_CLASSES_ROOT下的`*\\shell`目录下建立两个项，分别叫做`quick_start`和`quick_start_pre`。
编辑`quick_start`的值`MUIVerb`为 为程序启动添加参数
在`quick_start`下建立项，名为`command`。编辑`command`项的默认值为`"本程序根目录+ \dist\QuickStart.exe" "%1"`
编辑`quick_start_pre`的值`MUIVerb`为 为程序添加预设启动参数，`SubCommands`值为空。
在`quick_start_pre`下建立项，名为`Shell`。在`Shell`下建立项`add_pre`，值`MUIVerb`为 启动预设编辑器。
在`add_pre`下建立项，名为`command`。编辑`command`项的默认值为`"本程序根目录+ \dist\ConfigPre.exe" `

#### 注意事项

程序本身对目录的要求比较严格，请不要修改根目录下所有python脚本，bat脚本以及dist文件的位置。
本程序需要操作注册列表，请务必给予管理员权限。没有分配管理员权限可能导致不可预料的错误。
如果您误操作了本程序有关的注册列表，请重新安装即可。

如果您发现了bug，欢迎您即时发聩。我们也欢迎您对程序提供修改。
