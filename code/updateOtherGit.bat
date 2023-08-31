@echo off
setlocal

call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/%E5%96%9C%E7%88%B1%E5%B8%AE.py" "xiaiban.py" "xiaiban.py"
exit /b

:DownloadAndRename
rem 参数1：要下载的文件URL
rem 参数2：保存路径
rem 参数3：新文件名

set "url=%~1"
set "outputPath=%~2"
set "newName=%~3"

curl -o "%outputPath%" "%url%"

if %errorlevel% neq 0 (
    echo 下载失败！
    exit /b
)

if "%newName%" neq "%outputPath%" (
    del "%newName%"
    rename "%outputPath%" "%newName%"
    echo 文件已下载并重命名为 %newName%
) 
exit /b