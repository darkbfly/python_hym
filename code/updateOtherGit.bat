@echo off
setlocal

call :DownloadAndRename "https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/%E5%96%9C%E7%88%B1%E5%B8%AE.py" "xiaiban.py" "xiaiban.py"
exit /b

:DownloadAndRename
rem ����1��Ҫ���ص��ļ�URL
rem ����2������·��
rem ����3�����ļ���

set "url=%~1"
set "outputPath=%~2"
set "newName=%~3"

curl -o "%outputPath%" "%url%"

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