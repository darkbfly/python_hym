@echo off
setlocal

call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/ϲ����.py" "xiaiban.py" "xiaiban.py"
call :DownloadAndRename "https://raw.githubusercontent.com/meetclover/JavaScript/main/mcyp.py" "mcyp.py" "mcyp.py"
call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/�ε�.py" "didi.py" "didi.py"
exit /b

:DownloadAndRename
rem ����1��Ҫ���ص��ļ�URL
rem ����2������·��
rem ����3�����ļ���

set "url=%~1"
set "outputPath=%~2"
set "newName=%~3"

curl --proxy 127.0.0.1:7890  -o "%outputPath%" "%url%"

if %errorlevel% neq 0 (
    echo ����ʧ�ܣ�
    exit /b
)

if "%newName%" neq "%outputPath%" (
    del "%newName%"
    rename "%outputPath%" "%newName%"
    echo �ļ������ز�������Ϊ %newName%
) 
exit /b