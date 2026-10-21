# IndexNow — chave da thehousesupplier.com

Gerada em 2026-09-16. 32 caracteres hex, dentro da regra da spec
(8–128 caracteres, apenas a-z A-Z 0-9 e hifen).

```
13670c9c7c9904b3df5188c447c180b6
```

**Esta chave e publica por design** — fica servida no site para o buscador
verificar a posse do host. Nao e credencial de acesso a nada.

## Onde ela precisa estar

O Shopify nao serve arquivo na raiz do dominio, entao usamos a opcao 2 da
spec: chave em qualquer lugar do mesmo host, declarada em `keyLocation`.

URL pretendida: `https://www.thehousesupplier.com/pages/indexnow`

## Como submeter

```
POST /indexnow HTTP/1.1
Host: api.indexnow.org
Content-Type: application/json; charset=utf-8

{ "host": "www.thehousesupplier.com",
  "key": "13670c9c7c9904b3df5188c447c180b6",
  "keyLocation": "https://www.thehousesupplier.com/pages/indexnow",
  "urlList": [ "..." ] }
```

Ate 10.000 URLs por requisicao. O backlog de 2.524 paginas cabe em uma.

## Pendente de teste

A pagina vai responder `text/html`, nao `text/plain`. A spec pede "text key
file". **Nao esta confirmado que o Bing aceita.** Testar com UMA url antes do
lote.
