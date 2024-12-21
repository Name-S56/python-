@echo off
:: 检查是否以管理员身份运行
net session >nul 2>&1

:menu
echo 支持快捷键：
echo Alt + H 隐藏/显示窗口
echo Ctrl + Enter 翻译
echo Ctrl + S 保存
echo.
echo 1. 运行 main_t.py
echo 2. 运行 背单词小程序01.py
echo 3. 退出

set /p choice=请输入你的选择（1-3）:

if "%choice%"=="1" (
    py main_t.py
    goto menu
) else if "%choice%"=="2" (
    py 背单词小程序01.py
    goto menu
) else if "%choice%"=="3" (
    exit
) else (
    echo 无效输入，请重新选择。
    pause
    goto menu
)

pause