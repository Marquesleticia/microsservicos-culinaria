# 🍲 Projeto Culinária: Aplicação com Microserviços em Python e Docker

Este projeto é uma demonstração prática de uma arquitetura de microserviços, desenvolvida como um exercício de aprendizado. A aplicação simula um pequeno portal de culinária, onde é possível consultar receitas e obter sugestões de ingredientes.

---

## 🚀 Sobre o Projeto

O objetivo principal é demonstrar a separação de responsabilidades e a comunicação entre diferentes serviços, cada um rodando em seu próprio container Docker.

A arquitetura é composta por três serviços independentes:

- **Serviço de Receitas**: Um microserviço em Python com Flask que expõe uma API para fornecer uma lista de receitas.
- **Serviço de Ingredientes**: Outro microserviço em Python com Flask que sugere um ingrediente aleatório a cada chamada.
- **Serviço de Frontend**: Uma interface de usuário simples em HTML, CSS e JavaScript, servida por um container Nginx, que consome os dados dos outros dois serviços de forma dinâmica.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.9, Flask  
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)  
- **Conteinerização e Orquestração**: Docker, Docker Compose  
- **Servidor Web (Frontend)**: Nginx  
- **Comunicação**: API REST  

---

## ▶️ Como Executar o Projeto

> **Pré-requisitos**:  
> Certifique-se de ter o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/) instalados em sua máquina.

1. Clone este repositório:

```bash
git clone git clone https://github.com/Marquesleticia/microsservicos-culinaria.git
