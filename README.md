#  TaskTracker - Conteinerização e Deploy (Fase 3)

Aplicação CLI em Python 3 para gestão de tarefas, empacotada com Docker e orquestrada com Docker Compose.

---

## Como Executar

### 1. Como construir a imagem:
```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado:
```bash
docker run -it --rm tasktracker-app
```

### 3. Como rodar via orquestração (Recomendado):
```bash
docker compose run --rm tasktracker-app
```