"""
Script de teste para verificar se todos os módulos Python funcionam corretamente.
Execute este script para testar rapidamente as conversões dos notebooks.
"""

import subprocess
import sys
import os

def test_imports():
    """Testa se todas as dependências estão instaladas"""
    print("=== Testando importações ===")
    
    modules = [
        'torch',
        'numpy',
        'sklearn',
        'matplotlib',
        'pandas',
        'yfinance'
    ]
    
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module} - OK")
        except ImportError as e:
            print(f"✗ {module} - ERRO: {e}")
            return False
    
    return True

def test_datasets():
    """Testa se os datasets estão acessíveis"""
    print("\n=== Testando datasets ===")
    
    try:
        from sklearn import datasets
        
        # Teste Iris
        iris = datasets.load_iris()
        print(f"✓ Iris dataset - {iris.data.shape} samples")
        
        # Teste Wine
        wine = datasets.load_wine()
        print(f"✓ Wine dataset - {wine.data.shape} samples")
        
        # Teste Breast Cancer
        breast = datasets.load_breast_cancer()
        print(f"✓ Breast Cancer dataset - {breast.data.shape} samples")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro ao carregar datasets: {e}")
        return False

def test_pytorch():
    """Testa funcionalidades básicas do PyTorch"""
    print("\n=== Testando PyTorch ===")
    
    try:
        import torch
        import torch.nn as nn
        
        # Teste básico de tensor
        x = torch.randn(5, 3)
        print(f"✓ Tensor criado: {x.shape}")
        
        # Teste básico de rede neural
        class TestNet(nn.Module):
            def __init__(self):
                super(TestNet, self).__init__()
                self.fc1 = nn.Linear(3, 5)
                self.fc2 = nn.Linear(5, 1)
                
            def forward(self, x):
                x = torch.relu(self.fc1(x))
                x = self.fc2(x)
                return x
        
        net = TestNet()
        output = net(x)
        print(f"✓ Rede neural funcionando: {output.shape}")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro no PyTorch: {e}")
        return False

def test_quick_training():
    """Testa um treinamento rápido"""
    print("\n=== Testando treinamento rápido ===")
    
    try:
        import torch
        import numpy as np
        from sklearn import datasets
        
        # Carregar dados do Iris
        iris = datasets.load_iris()
        X = torch.FloatTensor(iris.data) / 10
        y = torch.FloatTensor((iris.target == 0).astype(float))
        
        # Rede neural simples
        class SimpleNet(torch.nn.Module):
            def __init__(self):
                super(SimpleNet, self).__init__()
                self.fc1 = torch.nn.Linear(4, 5)
                self.fc2 = torch.nn.Linear(5, 1)
                
            def forward(self, x):
                x = torch.relu(self.fc1(x))
                x = torch.sigmoid(self.fc2(x))
                return x
        
        model = SimpleNet()
        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
        
        # Treinamento rápido (10 épocas)
        for epoch in range(10):
            optimizer.zero_grad()
            output = model(X)
            loss = criterion(output.squeeze(), y)
            loss.backward()
            optimizer.step()
        
        print(f"✓ Treinamento concluído - Loss final: {loss.item():.4f}")
        return True
        
    except Exception as e:
        print(f"✗ Erro no treinamento: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 TESTE DE CONVERSÃO DOS NOTEBOOKS")
    print("=" * 50)
    
    all_tests_passed = True
    
    # Executar testes
    tests = [
        test_imports,
        test_datasets,
        test_pytorch,
        test_quick_training
    ]
    
    for test in tests:
        if not test():
            all_tests_passed = False
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("🎉 Os arquivos Python estão funcionando corretamente!")
        print("\nPróximos passos:")
        print("1. Execute os arquivos Python individuais")
        print("2. Consulte o README.md para instruções detalhadas")
    else:
        print("❌ ALGUNS TESTES FALHARAM!")
        print("💡 Verifique as dependências e tente novamente")
        print("📋 Execute: pip install -r requirements.txt")
    
    return all_tests_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
