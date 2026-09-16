# Pendentes — THS

Atualizado em 16/set/2026. Ordem = prioridade.

## 1. Card testing ativo (urgente)

**159 checkouts abandonados, 101 contas falsas, ainda rodando.** Último em
15/set 08:22 UTC.

Assinatura: nome sempre `james anderson`, e-mail gerado (`nome+numero@`),
quantidade sempre 1, sempre um de **dois SKUs** — `Pasco 1224 Tube Sure Grip
Flange` ou `Dearborn P9801 Flanged Strainer Tailpiece` — em dois valores-alvo,
**$46,09–$46,47** e **$1,24–$1,26**. Cadência ~1h, 24h por dia, desde 26/ago.
Domínios: aol, outlook, proton.me, protonmail, yandex, mail.com, gmail, icloud,
yahoo, hotmail.

Prejuízo direto até agora: **zero**, nenhuma virou pedido. O risco é a taxa de
aprovação e a posição junto ao Shopify Payments.

**Bot protection em Settings é exclusivo do Plus** — não existe no Advanced.
O que existe: proteção nativa automática (já ativa, sem toggle) e Shopify
Protect em Settings → Payments.

**Ação:** abrir ticket no Shopify Support com os dados acima. Eles têm
ferramentas (proxy detection, bloqueio por padrão) que só o suporte aciona.
CSV das 101 contas ainda não foi gerado — pedir quando for abrir o ticket.
Não deletar as contas, são evidência; marcar com tag.

## 2. ads_redirect no Merchant Center

Regra de feed, ação do Gabriel (não tenho escrita no Merchant Center —
Windsor retorna lista vazia de ações).

Merchant Center → Products → Feeds → Feed rules → Create rule:
- atributo de destino: `ads_redirect`
- data source: `link`
- find and replace: `utm_medium=product_sync` → `utm_medium=cpc`
- find and replace: `sag_organic` → `shopping_paid`

Find-and-replace em vez de montar URL do zero porque o domínio precisa bater
exatamente com o do `link` — é requisito do Google, e substituindo pedaços da
própria URL isso é garantido por construção.

Propaga em 24–48h, não é retroativo. O GA4 **já separa hoje** (lê `gclid`),
então isso resolve só a atribuição dentro do Shopify.

## 3. Peso e frete

- **43 pesagens** de conexões PEX de $1,67 a $2,44, todas com o placeholder de
  0,05 lb (22,7 g) e peso crítico entre 25 e 37 g. São os únicos da régua λ com
  folga apertada e peso não verificado. Balança de cozinha, 15 minutos.
- **Intuitive Shipping — trial de 15 dias em andamento.** Plano Growth, $70/mês,
  500 pedidos, SmartBoxing incluso, 30¢/pedido de excedente. Resolve o box
  packing dos **1.262 subcotados por volume** — buraco que nenhuma régua
  conserta, é a mecânica dos $276,82 perdidos na pia Blanco.
  - Unidades já corrigidas para **in / lb / mi** (estava cm/kg/km). Dimensão do
    fornecedor (`cube`) é em polegada cúbica e o divisor dimensional da UPS
    (139) é em polegada — trocar a unidade invalidaria tudo.
  - Confirmado na tela de edição de produto: o app **puxa o peso do Shopify**
    e aceita **override de dimensão por produto** (Shipping dimensions em
    polegadas, em branco = usa a plataforma). Logo o caminho de carga em massa
    é o **Import** da tela Products.
  - **Próximo passo: exportar o CSV da tela Products** e mandar o cabeçalho.
    Preciso da ordem das colunas, se a chave é SKU ou ID do Shopify, e como ele
    nomeia comprimento/largura/altura. Tenho pronto para carregar: **3.795
    itens com L/H/W completos** do arquivo do fornecedor, mais **2.917 que só
    têm `cube`** (volume), que precisam de tratamento à parte porque o app quer
    três medidas separadas.
  - Cenário novo nasce com `Status = Published`. Pôr em **Testing** antes de
    salvar, senão entra no checkout ao vivo.
  - Elegibilidade a frete grátis: usar **Product tag** em vez de perfil do
    Shopify. Tag entra por Matrixify; perfil de entrega só sai por API.
  - Três testes do trial: (1) de onde ele lê dimensão; (2) pia Blanco — Shopify
    cota $380,20 e a UPS fatura $657,02, se ele devolver ~$657 funciona;
    (3) o AND — grátis acima de $99 **E** abaixo de X lb.
- **Limiar de freight grátis estilo Ferguson**, ~$1.744 (Banda C), no perfil
  Freight. Ferguson usa $49 parcel / $1.499 freight.
- **Travar `Variant Weight` no import do fornecedor** — senão os 2.790 pesos
  aplicados voltam atrás. *Ainda não sei se o import é agendado ou manual.*
- **629 itens do Standard** passam no λ mas não têm dimensão conhecida.
  Destravam sozinhos quando houver dimensão.

## 4. Fornecedor

Um pacote só, com três listas:
- **54 segurados** pelo piso físico (`pesos_segurados_suspeitos.csv`) — inclui
  a sentinela `0.0001 lb`, que aparece 14 vezes com valor idêntico
- **130 tubos** sem peso resolvível (`pesos_tubo_pendentes.csv`)
- **294 custos por pé** (`custos_por_pe_incorretos.csv`) — o campo `unitCost`
  guarda custo **por pé** e o preço é da peça inteira. Corrompe o relatório de
  lucro do Shopify em $123.989 de catálogo.

Pergunta objetiva para o fornecedor: **o campo `weight` é por pé ou pela peça
inteira?** Já está comprovado que para tubo é por pé.

## 5. SEO

Resta **1** da lista original: `pipe-straps-brackets-hooks` (64 produtos).
19 coleções no ar, 238 títulos corrigidos.

## 6. Mídia — revista de associação (em espera)

**PHCC** é a associação certa: público é contratante e dono, que é quem compra.
**ASPE é público errado** — engenheiro especifica, não compra material.

| Publicação | Alcance | Frequência |
|---|---|---|
| PHCC Nacional | ~3.500 decisores | trimestral |
| PHCC Minnesota | 5.200 | estadual |
| PHCC Maryland | 3.300 | estadual |
| PHC News (não é da associação) | 200 mil impressões/mês | mensal |

Valores de anúncio **não obtidos** — media kits 2026 não apareceram na busca.

**Recomendação: fazer o Craig antes.** Ele ofereceu compartilhar post da THS
para 4.000 contratantes e donos no LinkedIn, de graça. É mais gente que a
revista nacional, sai essa semana em vez do próximo trimestre, e dá para medir
com UTM. Se gerar pedido, aí a revista se decide com número.

## 7. Menores

- `Single Hole Faucets` (10) vs `Single-Hole Faucets` (97) — dois product types
  para a mesma coisa, 107 produtos separados por um hífen
- Gruvlok `GVLF-617-300-EN` e `GVLF-617-400-EN` titulados "Coupling (Reducing)"
  com um só tamanho — provavelmente couplings retos rotulados errado
- Títulos Gruvlok não trazem número de figura, que é como o contratante
  especifica. Confirmar com o representante.
- `living-room` (95) é termostato e aquecedor — deletar + 301
- Oatey 42044 ($11,12) e 42093 ($16,66) — descrições idênticas, UPCs
  diferentes, 50% de diferença de preço. Possível duplicata.
- 142 títulos em caixa alta
- Barra de anúncio diz "8.900+ items", são 14.845 ativos
- Gap não explicado: em 15/set o GA4 capturou 42% dos cliques do Google Ads
  (135 de 322). Até 10/set capturava 94–103%. Vale olhar o tag do GA4 no tema.
