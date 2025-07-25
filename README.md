# Python SOLID Principles with Clean Architecture

Este projeto demonstra a aplicação dos princípios SOLID usando Clean Architecture em Python.

## Estrutura do Projeto

O projeto segue a arquitetura limpa (Clean Architecture) com as seguintes camadas:

```
src/
├── domain/          # Entidades e regras de negócio
├── application/     # Casos de uso e interfaces
├── infrastructure/  # Implementações concretas
└── presentation/    # Controllers e interfaces de usuário
```

## Princípios SOLID Demonstrados

1. **S - Single Responsibility Principle (SRP)**

   - Cada classe deve ter apenas uma razão para mudar
   - Exemplo: `UserService` focado apenas em operações do usuário

2. **O - Open/Closed Principle (OCP)**

   - Entidades devem estar abertas para extensão, mas fechadas para modificação
   - Exemplo: `PaymentProcessor` com diferentes estratégias de pagamento

3. **L - Liskov Substitution Principle (LSP)**

   - Objetos de uma classe derivada devem poder substituir objetos da classe base
   - Exemplo: Hierarquia de `Shape` com diferentes formas geométricas

4. **I - Interface Segregation Principle (ISP)**

   - Clientes não devem ser forçados a depender de interfaces que não usam
   - Exemplo: Separação de interfaces para diferentes tipos de operações

5. **D - Dependency Inversion Principle (DIP)**
   - Módulos de alto nível não devem depender de módulos de baixo nível
   - Exemplo: Uso de injeção de dependência no `OrderService`

## Como Executar

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute os testes: `python -m pytest`

## Exemplos

Cada princípio SOLID tem seu próprio módulo com exemplos práticos e testes unitários demonstrando sua aplicação.

## Contribuição

Sinta-se à vontade para contribuir com mais exemplos ou melhorias no código existente.
