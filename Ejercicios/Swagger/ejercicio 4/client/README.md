
## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t edem_blackjack:latest .

# starting up a container
docker run -p 8080:8080 edem_blackjack
```

Methods:

Onboarding:
    - Json:
      - Alias
      - Ip
      - PictureUrl


StartGame:
    - Barajar Cartas
    - Dar mano a todos
      - Envío:
        - Carta
      - Retorno:
        - Operacion
        - Cantidad apostada
        - Cantidad restante
        - Cartas actuales



