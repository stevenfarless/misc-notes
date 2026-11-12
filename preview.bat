@echo off
setlocal
cd /d "%~dp0"

where ruby >nul 2>nul
if errorlevel 1 (
  echo Ruby is required. Install Ruby with DevKit from https://rubyinstaller.org/
  echo During installation, allow the MSYS2 development toolchain setup to finish.
  pause
  exit /b 1
)

where bundle >nul 2>nul
if errorlevel 1 (
  echo Bundler is missing. Install it with: gem install bundler
  pause
  exit /b 1
)

bundle check >nul 2>nul
if errorlevel 1 (
  echo Installing the local GitHub Pages dependencies...
  bundle install
  if errorlevel 1 (
    echo Dependency installation failed.
    pause
    exit /b 1
  )
)

echo.
echo Starting the local site at http://127.0.0.1:4000/
echo Press Ctrl+C to stop the preview.
echo.
bundle exec jekyll serve --livereload
