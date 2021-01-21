


### 1. 先安装如下版本
python3.8.6

pyinstaller==4.0
pypiwin32==223
PyQt5==5.15.1
PyQt5-sip==4.19.17

### 2.打包

- 使用动态库打包  
pyinstaller --hidden-import=pkg_resources -F E:\My_Git_PROJ\pyQT5-tutorial-code\10_案例\2_眼皮占卜.py

- 带图标打包: 
pyinstaller --hidden-import=pkg_resources -F --i "E:\\My_Git_PROJ\\pyQT5-tutorial-code\\10_案例\\eyejump.ico" E:\My_Git_PROJ\pyQT5-tutorial-code\10_案例\2_眼皮占卜.py

- 不显示命令行窗口的打包:  
pyinstaller --hidden-import=pkg_resources -F -w E:\My_Git_PROJ\pyQT5-tutorial-code\10_案例\2_眼皮占卜.py

-- 带图标 不显示命令行:  
pyinstaller --hidden-import=pkg_resources -F -w --i "E:\\My_Git_PROJ\\pyQT5-tutorial-code\\10_案例\\eyejump.ico" E:\My_Git_PROJ\pyQT5-tutorial-code\10_案例\2_眼皮占卜.py
