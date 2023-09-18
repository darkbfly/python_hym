@echo off
setlocal

call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/喜爱帮.py" "xiaiban.py" "xiaiban.py"
call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/滴滴.py" "didi.py" "didi.py"
call :DownloadAndRename "https://raw.githubusercontent.com/smallfawn/QLScriptPublic/main/卡萨帝签到提现.py" "kasadi.py" "kasadi.py"
call :DownloadAndRename "https://raw.githubusercontent.com/241793/bucai2/main/中健365.py" "zj.py" "zj.py"
call :DownloadAndRename "https://raw.githubusercontent.com/qianmo8/au01/main/gbyd.py" "gb.py" "gb.py"
call :DownloadAndRename "https://raw.githubusercontent.com/qianmo8/au01/main/xyy.py" "xyy.py" "xyy.py"
call :DownloadAndRename "https://raw.githubusercontent.com/Bidepanlong/ql/main/hqcsh.py" "hqcsh.py" "hqcsh.py"

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