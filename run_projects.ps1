# Script PowerShell para executar os projetos de Redes Neurais

function Show-Menu {
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  REDES NEURAIS - EXECUTAR PROJETOS" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Escolha um projeto para executar:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Iris - Setosa" -ForegroundColor Green
    Write-Host "2. Iris - Versicolor" -ForegroundColor Green
    Write-Host "3. Iris - Virginica" -ForegroundColor Green
    Write-Host "4. Wine - Classificacao Principal" -ForegroundColor Magenta
    Write-Host "5. Wine - Classe 1" -ForegroundColor Magenta
    Write-Host "6. Wine - Classe 2" -ForegroundColor Magenta
    Write-Host "7. Breast Cancer" -ForegroundColor Red
    Write-Host "8. Magazine Luiza (Series Temporais)" -ForegroundColor Blue
    Write-Host "9. Testar Instalacao" -ForegroundColor DarkYellow
    Write-Host "0. Sair" -ForegroundColor Gray
    Write-Host ""
}

function Run-Project {
    param (
        [string]$ProjectName,
        [string]$ProjectPath
    )
    
    Write-Host "Executando $ProjectName..." -ForegroundColor Yellow
    Write-Host "Caminho: $ProjectPath" -ForegroundColor Gray
    Write-Host ""
    
    try {
        & "C:/Program Files/Python313/python.exe" $ProjectPath
        Write-Host ""
        Write-Host "✅ Projeto executado com sucesso!" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Erro ao executar o projeto: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host ""
    Write-Host "Pressione qualquer tecla para continuar..."
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}

# Loop principal
do {
    Clear-Host
    Show-Menu
    $choice = Read-Host "Digite sua escolha (0-9)"
    
    switch ($choice) {
        "1" {
            Run-Project "Iris Setosa" "#1 Íris/setosa.py"
        }
        "2" {
            Run-Project "Iris Versicolor" "#1 Íris/versicolor.py"
        }
        "3" {
            Run-Project "Iris Virginica" "#1 Íris/virginica.py"
        }
        "4" {
            Run-Project "Wine Principal" "#2 Wine/wine.py"
        }
        "5" {
            Run-Project "Wine Classe 1" "#2 Wine/wine_class_1.py"
        }
        "6" {
            Run-Project "Wine Classe 2" "#2 Wine/wine_class_2.py"
        }
        "7" {
            Run-Project "Breast Cancer" "#3 Breast cancer/breast_cancer.py"
        }
        "8" {
            Run-Project "Magazine Luiza" "#4 Previsão de séries temporais/magazine_luiza.py"
        }
        "9" {
            Run-Project "Teste de Instalação" "test_conversion.py"
        }
        "0" {
            Write-Host ""
            Write-Host "Obrigado por usar o sistema!" -ForegroundColor Green
            Write-Host "👋 Até logo!" -ForegroundColor Yellow
            break
        }
        default {
            Write-Host "Opção inválida! Tente novamente." -ForegroundColor Red
            Start-Sleep -Seconds 2
        }
    }
} while ($choice -ne "0")
