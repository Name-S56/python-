@echo off
:: 检查是否以管理员身份运行
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo 正在以管理员身份重新启动...
    powershell -Command "Start-Process cmd -ArgumentList '/c py main_t.py' -Verb RunAs"
)

echo  支持快捷键：
echo   Alt + H 隐藏/显示窗口
echo   Ctrl + Enter 翻译
echo   Ctrl + S 保存
:: 以管理员身份运行 Python 脚本
py main_t.py