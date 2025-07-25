# Python SOLID Principles with Clean Architecture

Este projeto demonstra a aplicação dos princípios SOLID usando Clean Architecture em Python.

## Estrutura do Projeto

O projeto segue a arquitetura limpa (Clean Architecture) com as seguintes camadas:

```
src/
├── domain/           # Regras de negócio e interfaces
│   ├── entities/    # Entidades do domínio
│   │   ├── order.py
│   │   ├── payment.py
│   │   ├── shape.py
│   │   └── user.py
│   └── interfaces/  # Contratos e abstrações
│       ├── notification_service.py
│       ├── order_repository.py
│       ├── user_repository.py
│       └── use_case.py
├── application/     # Casos de uso e DTOs
│   ├── dto/        # Objetos de transferência de dados
│   │   ├── order_dto.py
│   │   └── user_dto.py
│   └── use_cases/  # Implementação dos casos de uso
│       ├── create_order_use_case.py
│       ├── create_user_use_case.py
│       └── notify_order_created_use_case.py
├── infrastructure/ # Implementações concretas
│   ├── repositories/
│   │   ├── memory_order_repository.py
│   │   └── memory_user_repository.py
│   └── services/
│       ├── email_notification_service.py
│       └── mock_notification_service.py
└── presentation/   # Controllers e interfaces de usuário
    └── controllers/
        ├── order_controller.py
        └── user_controller.py
```

## Princípios SOLID Demonstrados

1. **S - Single Responsibility Principle (SRP)**

   - Cada classe tem apenas uma razão para mudar
   - Exemplo: `User` em `domain/entities/user.py` é responsável apenas pelos dados e validações do usuário
   - Exemplo: `UserRepository` em `domain/interfaces/user_repository.py` define apenas operações de persistência

2. **O - Open/Closed Principle (OCP)**

   - Entidades devem estar abertas para extensão, mas fechadas para modificação
   - Exemplo: `PaymentProcessor` em `domain/entities/payment.py` permite adicionar novos métodos de pagamento sem modificar o código existente
   - Implementações: `CreditCardProcessor`, `PayPalProcessor`, `PixProcessor`

3. **L - Liskov Substitution Principle (LSP)**

   - Objetos de uma classe derivada devem poder substituir objetos da classe base
   - Exemplo: Hierarquia de `Shape` em `domain/entities/shape.py`
   - Classes `Rectangle`, `Square` e `Circle` podem ser usadas onde `Shape` é esperado

4. **I - Interface Segregation Principle (ISP)**

   - Clientes não devem ser forçados a depender de interfaces que não usam
   - Exemplo: Interfaces específicas em `domain/interfaces/`
   - `NotificationService`, `OrderRepository`, `UserRepository` são interfaces coesas e focadas

5. **D - Dependency Inversion Principle (DIP)**
   - Módulos de alto nível não devem depender de módulos de baixo nível
   - Exemplo: Use cases dependem de interfaces do domínio, não de implementações concretas
   - Implementações concretas em `infrastructure/` dependem das interfaces em `domain/interfaces/`

## Clean Architecture

O projeto segue os princípios da Clean Architecture:

1. **Camada de Domínio**

   - Contém as regras de negócio centrais
   - Define interfaces e contratos
   - Independente de frameworks e detalhes técnicos

2. **Camada de Aplicação**

   - Implementa casos de uso específicos
   - Orquestra o fluxo de dados usando as interfaces do domínio
   - Contém DTOs para transferência de dados

3. **Camada de Infraestrutura**

   - Implementa as interfaces definidas no domínio
   - Contém código específico de frameworks e bibliotecas
   - Adapta tecnologias externas para as interfaces do domínio

4. **Camada de Apresentação**
   - Controllers que coordenam os casos de uso
   - Converte dados entre o formato da API e DTOs
   - Gerencia a interação com o usuário

## Como Executar

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute os testes: `python -m pytest`

## Exemplos

Cada princípio SOLID tem seu próprio módulo com exemplos práticos e testes unitários demonstrando sua aplicação. Os exemplos incluem:

- Gerenciamento de usuários com validações
- Processamento de pedidos com diferentes formas de pagamento
- Sistema de notificações extensível
- Cálculos geométricos demonstrando LSP

## Contribuição

Sinta-se à vontade para contribuir com mais exemplos ou melhorias no código existente.
