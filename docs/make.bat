@ECHO OFF
setlocal EnableExtensions EnableDelayedExpansion

pushd "%~dp0" || exit /b 1

REM Command file for Sphinx documentation

if "%SPHINXBUILD%"=="" set "SPHINXBUILD=sphinx-build"
set "SOURCEDIR=."
set "BUILDDIR=_build"

REM Check sphinx-build exists
"%SPHINXBUILD%" --version >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found.
	echo.Install it with: python -m pip install sphinx
	echo.Or set SPHINXBUILD to the full path of sphinx-build.exe
	echo.
	popd
	endlocal
	exit /b 1
)

if "%~1"=="" goto help

REM Target is first arg; pass the rest through to sphinx via SPHINXOPTS
set "TARGET=%~1"
shift

"%SPHINXBUILD%" -M "%TARGET%" "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O% %*
set "RC=%ERRORLEVEL%"

popd
endlocal & exit /b %RC%

:help
"%SPHINXBUILD%" -M help "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
set "RC=%ERRORLEVEL%"
popd
endlocal & exit /b %RC%
