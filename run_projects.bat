@echo off
echo ========================================
echo  REDES NEURAIS - EXECUTAR PROJETOS
echo ========================================
echo.

:menu
echo Escolha um projeto para executar:
echo.
echo 1. Iris - Setosa
echo 2. Iris - Versicolor  
echo 3. Iris - Virginica
echo 4. Wine - Classificacao Principal
echo 5. Wine - Classe 1
echo 6. Wine - Classe 2
echo 7. Breast Cancer
echo 8. Magazine Luiza (Series Temporais)
echo 9. Testar Instalacao
echo 0. Sair
echo.
set /p choice="Digite sua escolha (0-9): "

if "%choice%"=="1" goto iris_setosa
if "%choice%"=="2" goto iris_versicolor
if "%choice%"=="3" goto iris_virginica
if "%choice%"=="4" goto wine_main
if "%choice%"=="5" goto wine_class1
if "%choice%"=="6" goto wine_class2
if "%choice%"=="7" goto breast_cancer
if "%choice%"=="8" goto magazine_luiza
if "%choice%"=="9" goto test_install
if "%choice%"=="0" goto exit

echo Opcao invalida!
pause
goto menu

:iris_setosa
echo Executando Iris Setosa...
"C:/Program Files/Python313/python.exe" "#1 Iris/setosa.py"
pause
goto menu

:iris_versicolor
echo Executando Iris Versicolor...
"C:/Program Files/Python313/python.exe" "#1 Iris/versicolor.py"
pause
goto menu

:iris_virginica
echo Executando Iris Virginica...
"C:/Program Files/Python313/python.exe" "#1 Iris/virginica.py"
pause
goto menu

:wine_main
echo Executando Wine Principal...
"C:/Program Files/Python313/python.exe" "#2 Wine/wine.py"
pause
goto menu

:wine_class1
echo Executando Wine Classe 1...
"C:/Program Files/Python313/python.exe" "#2 Wine/wine_class_1.py"
pause
goto menu

:wine_class2
echo Executando Wine Classe 2...
"C:/Program Files/Python313/python.exe" "#2 Wine/wine_class_2.py"
pause
goto menu

:breast_cancer
echo Executando Breast Cancer...
"C:/Program Files/Python313/python.exe" "#3 Breast cancer/breast_cancer.py"
pause
goto menu

:magazine_luiza
echo Executando Magazine Luiza...
"C:/Program Files/Python313/python.exe" "#4 Previsao de series temporais/magazine_luiza.py"
pause
goto menu

:test_install
echo Testando instalacao...
"C:/Program Files/Python313/python.exe" test_conversion.py
pause
goto menu

:exit
echo.
echo Obrigado por usar o sistema!
pause
exit
