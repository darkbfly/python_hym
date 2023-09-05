@echo off
setlocal

rem call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/%E5%96%9C%E7%88%B1%E5%B8%AE.py" "xiaiban.py" "xiaiban.py"
rem call :DownloadAndRename "https://raw.githubusercontent.com/meetclover/JavaScript/main/mcyp.py" "mcyp.py" "mcyp.py"
call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/滴滴.py" "didi.py" "didi.py"
exit /b

:DownloadAndRename
rem 参数1：要下载的文件URL
rem 参数2：保存路径
rem 参数3：新文件名

set "url=%~1"
set "outputPath=%~2"
set "newName=%~3"

curl --proxy 127.0.0.1:7890  -o "%outputPath%" "%url%"

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