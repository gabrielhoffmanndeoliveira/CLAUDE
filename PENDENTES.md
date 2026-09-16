# Pendentes — THS

Atualizado em 16/set/2026 (frete e dimensão). Ordem = prioridade.

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

### Em execução agora

- **Tag `free-ship-eligible` importando** — 8.762 produtos,
  `tag_free_ship_IMPORTAR.csv`, `Tags Command: MERGE`. Verificado nos 12
  primeiros que as tags originais sobrevivem. Rollback:
  `tag_free_ship_rollback.csv`.
- **Dimensões em metafield importando** — 3.035 produtos,
  `dimensoes_metafield_IMPORTAR.csv`. As três definições (`product.length`,
  `product.width`, `product.height`, tipo `dimension`) já existem e estão
  mapeadas no Intuitive. Rollback: `dimensoes_metafield_rollback.csv`.

**Quando os dois terminarem:**
1. `Import catalog` no Intuitive, para ele puxar dimensão e tag.
2. Rodar `delivery_profile_id:89783402599 AND tag_not:free-ship-eligible` —
   devolve em uma chamada a lista exata do que está no frete grátis e não
   deveria. Substitui o snapshot `general_skus.json`, que é velho.
3. Montar o cenário no Intuitive em **`Status: Testing`** (ele nasce
   `Published`). Falta ver a lista de condições que o app oferece — o print do
   dropdown `Add condition` decide se é 1 cenário (se aceitar fórmula) ou 7
   (um por faixa de valor).

### A lógica do frete grátis, em três camadas

1. **Por item:** tag `free-ship-eligible`, dada por λ ≤ 0,0337. Todo item do
   carrinho precisa ter.
2. **Por carrinho:** o SmartBoxing do Intuitive empacota e devolve o peso
   faturável da **caixa**, não a soma dos itens. É o que fecha o furo do
   THS1013 — 36 termostatos, cada um passando na λ com folga, e a caixa custou
   $125,58 num pedido que cobrou $0,00.
3. **Teto que cresce com o valor:** peso_faturável ≤ (0,303 × subtotal − 14,98) / 4,51.

   | Subtotal | Peso faturável máx |
   |---|---|
   | $99–149 | 3,3 lb |
   | $150–199 | 6,7 lb |
   | $200–299 | 10,1 lb |
   | $300–499 | 16,8 lb |
   | $500–999 | 30,2 lb |
   | $1.000–1.999 | 63,8 lb |
   | $2.000+ | 131 lb |

   Usando o piso de cada faixa, que é conservador por construção.

4. **Três vetos absolutos**, independentes de valor: caixa ≥ **10 ft³**,
   comprimento + cintura > **130 in**, ou volume > **150 lb** (teto da UPS
   Ground). Falhar não bloqueia a compra — só esconde o frete grátis e mostra a
   tarifa UPS normal.

### Itens perigosos ainda no frete grátis

Medido contra snapshot anterior à execução da λ, então **carece de releitura**
(o passo 2 acima resolve). Os que sobreviveram à conferência:

| SKU | Volume | Peso no Shopify | Peso dimensional | Preço |
|---|---|---|---|---|
| `ELKA-LZSTL8WSLK` | 13,63 ft³ | 2,0 lb | **169,5 lb** | $3.676,80 |
| `ZOEL-915-0005` | 10,08 ft³ | 60,0 lb | **125,4 lb** | $2.024,89 |
| `ELKA-LZS8WSLK` | 9,97 ft³ | 2,0 lb | **123,9 lb** | $2.636,87 |
| `AMST-6400.001.020` | 9,31 ft³ | 1,0 lb | **115,7 lb** | $749,82 |
| `ELKA-LZSTL8WSLP` | 8,94 ft³ | 2,0 lb | **111,1 lb** | $3.817,65 |

Caldeiras Burnham de 300 a 502 lb (`BURN-205EN-G0` a `BURN-208EN-G0`) também
reprovam na λ — e estão acima do teto de 150 lb da UPS Ground.

### Faturas UPS — sangramento medido

**THS1008 (pia Blanco), fatura 000022K7Y8366, $675,26.** Declarado 38×27×16 in
= 9,500 ft³; auditado 39×28×16 = 10,111 ft³. Cruzou o degrau de 10 ft³:
+$331,00 de Large Package Surcharge, +$76,96 de combustível, +$42,52 de audit
fee. Custo real $657,02 contra $0,00 cobrado. Peso real 55 lb, cobrado 126.

**Fatura 00000022K7Y8376, $224,84** — quatro pedidos, todos `Inbound/Third
Party` (fornecedor despachando direto na conta da THS):

| Order | Rastreio | Cobrado | Pago à UPS | Resultado |
|---|---|---|---|---|
| THS1013 | 1Z7873030392581089 | $0,00 | $125,58 | −$125,58 |
| THS1014 | 1ZH1146Y0333123072 | $0,00 | $36,56 | −$36,56 |
| THS1012 | 1Z9515X00332116138 | $15,00 | $33,85 | −$18,85 |
| THS1015 | 1Z7873030393686492 | $15,00 | $21,14 | −$6,14 |

Cobrado $30,00, pago $187,63. **−$157,63 numa fatura só.** Vale puxar a aba
`Adjustments` dos últimos 6 meses: se a taxa de correção de 13,4% for
consistente, é dinheiro recorrente e argumento para cobrar do fornecedor.

### Ainda abertos

- **43 pesagens** de conexões PEX de $1,67 a $2,44, todas com o placeholder de
  0,05 lb (22,7 g) e peso crítico entre 25 e 37 g. São os únicos da régua λ com
  folga apertada e peso não verificado. Balança de cozinha, 15 minutos.
- **579 itens segurados** (`tag_free_ship_segurados_sem_dimensao.csv`): passam
  na λ só pelo peso real, sem nenhuma noção de volume, e hoje estão fora do
  General. Destravam quando houver dimensão.
- **2.414 itens têm só `cube`** (volume) e não as três medidas. O Intuitive
  exige comprimento, largura e altura juntos — volume sozinho não serve.
  Pedir as três ao fornecedor.
- **Intuitive Shipping** — trial de 15 dias, plano Growth $70/mês, 500 pedidos,
  SmartBoxing incluso, 30¢/pedido de excedente. Unidades já em **in/lb/mi**.
- **Limiar de freight grátis estilo Ferguson**, ~$1.744 (Banda C), no perfil
  Freight. Ferguson usa $49 parcel / $1.499 freight.
- **Travar `Variant Weight` no import do fornecedor** — senão os 2.790 pesos
  aplicados voltam atrás. *Ainda não sei se o import é agendado ou manual.*
- **Perguntar ao Master Source** por que a dimensão declarada da Blanco deu
  exatamente 9,500 ft³, na casa decimal do limiar de 10.

## 4. Benchmark SupplyHouse — o frete deles não é uma regra, é a malha

Testado em 15/set, deslogado, com o `TH1210U4001` (FocusPRO N100, $43,26),
36 unidades, ~18 lb — mesmo peso do THS1013, que nos custou **$125,58**.

| CEP | Resultado | Entrega |
|---|---|---|
| 19056 Levittown PA (destino real do THS1013) | **FREE** | 1 dia, FastTrack |
| 95008 Campbell CA (travessia de país) | **FREE** | **dividido em 2**: 25 un. em 17/set, 11 un. em 21/set |

**O split é a descoberta.** Eles não têm tarifa UPS melhor — têm **estoque
distribuído**, e quebram o pedido para cada parte sair do armazém mais perto do
cliente. Frete grátis é consequência de zona baixa, não generosidade. E
absorvem **duas** remessas sem repassar nada.

Regra declarada deles: frete terrestre grátis acima de $99; acima de **100 lb**
normalmente vira freight carrier. Bate perto do teto de 131 lb que a nossa
fórmula dá para carrinho de $2.000+.

| | THS1013 | SupplyHouse |
|---|---|---|
| Subtotal | $1.144,80 | $1.557,36 |
| Custo de frete | **$125,58** | estimado $40–60 |
| **% do pedido** | **11,0%** | **~3%** |

11% come um terço da margem bruta de 33,3%. 3% não faz cócegas.

**Consequências:**

1. **Não copiar a regra deles.** A THS despacha de origem única via fornecedor,
   sem controle de onde sai. "$99 e pronto" é o sintoma de uma máquina que não
   temos.
2. **A régua λ está certa por isso.** Não é conservadora demais — é a
   ferramenta adequada para origem única e distante.
3. **A alavanca é a origem, não a régua.** Nosso $111,48 de base para 18 lb é
   tarifa de zona 7–8. **Perguntar ao fornecedor de qual centro de distribuição
   cada SKU sai, e se dá para rotear pelo mais próximo do cliente.** Vale mais
   que qualquer ajuste de limiar.
4. **Split delivery é capacidade, não defeito.** O cliente aceita duas datas.
   Abre espaço para a THS fazer igual quando o carrinho misturar origens, em vez
   de segurar tudo esperando o item mais lento.

**Ressalva:** dólar contra dólar não é maçã com maçã — origens diferentes. O que
o teste mede bem é o comportamento, e isso é independente de zona.

Comparação de preço, de passagem: estamos mais caros nos três itens conferidos.

| Nosso SKU | Nosso preço | Equivalente na SH |
|---|---|---|
| `HONE-TH3210D1004/U` | $82,83 | $70,00 |
| `HONE-TH3210U2004/U` | $46,28 | $43,26 (sucessor `TH1210U4001`) |
| `HONE-TH3110U2008/U` | $30,00 | $27,79 (sucessor `TH1110U4000`) |

## 5. Preço — não conseguimos competir em commodity residencial

Descoberto no teste de frete de 15/set. O aquecedor de 40 galões:

| | Valor |
|---|---|
| **Nosso custo de compra** (`unitCost`) | **$1.018,85** |
| **Preço de varejo da SupplyHouse** (Ruud `PROG40S-40N-RU62`) | **$1.060,14** |
| Nosso preço de venda (`RHEE-PRO+G40S-40N-RH62`) | $1.528,28 |

**O varejo deles está 4,1% acima do nosso atacado.** Vendendo a preço de custo
ficaríamos $41 abaixo, com margem zero, e ainda perderíamos em prazo e malha.
Com os 50% de markup do catálogo, ficamos **44% acima**.

Rheem e Ruud são a mesma fabricante — mesmo aparelho, etiqueta diferente.

Nos termostatos o gap era 7–18%. Aqui 44%. Eles compram melhor do que nós.

**31% do catálogo está em concorrência direta:** 4.590 itens ACTIVE em marcas
que a SupplyHouse carrega, de 14.883.

| Marca | Nossos itens | Mediana |
|---|---|---|
| Viega | 955 | $57,60 |
| Milwaukee | 764 | $57,89 |
| Honeywell/Resideo | 606 | $110,59 |
| Sioux Chief | 538 | $13,44 |
| Legend Valve | 295 | $21,73 |
| MrPEX | 289 | $26,61 |
| **Rheem/Ruud** | 278 | **$1.255,47** |
| Taco | 119 | $287,00 |
| Navien | 73 | $1.155,00 |
| Watts | 74 | $399,57 |

### Onde eles NÃO estão

Três de três itens testados que a SupplyHouse não carrega:

| Item | Categoria |
|---|---|
| `NAVI-30010747A` | acessório OEM Navien |
| `HGRI-454005` | nVent CADDY |
| `SIOU-851-36T` | cleanout comercial 6" |

Eles são fortes em **commodity residencial**, que é onde estamos 7% a 44% mais
caros. Não estão em **peça OEM, item comercial e tamanho grande** — onde a THS
tem catálogo e o cliente não tem comparação fácil de preço.

**Conclusão prática:** competir em termostato Resideo e aquecedor Rheem é perder
por construção. A margem está no sortimento que sobra. E, por coincidência útil,
é lá que os itens são pesados e volumosos — ou seja, onde a régua λ e o box
packing mais importam.

### Amostragem em andamento

`amostra_preco_supplyhouse.csv` — 82 itens estratificados por marca × faixa de
preço (item mediano de cada célula, só com MPN conhecido), com nosso preço,
nosso custo e markup real. Duas colunas em branco para o preço deles e o gap.

Executar por lote, cada MPN é uma busca. **Lote 1:** os 10 de maior impacto —
Rheem e Navien nas faixas altas, mais Taco e Watts, itens de $400 a $12.000.

## 6. Termostatos Honeywell descontinuados (comercial, urgente)

**Os 3 SKUs da série T3 Pro / PRO 3000 que temos estão ACTIVE na loja e a
série foi descontinuada pelo fabricante.**

| Nosso SKU | Preço | Descontinuado | Sucessor |
|---|---|---|---|
| `HONE-TH3210D1004/U` | $82,83 | **a confirmar** — busca diz que sim, mas apareceu preço ativo de $70,00 | `TH1320U4002` |
| `HONE-TH3210U2004/U` | $46,28 | 26/nov/2025 | `TH1210U4001` |
| `HONE-TH3110U2008/U` | $30,00 | 30/set/2025 | `TH1110U4000` |

São o carro-chefe dos pedidos recentes: **$2.655,20 em 4 pedidos** —
THS1032 (hoje, 10 un.), THS1024 (4 un.), THS1022 (6 un.), THS1013 (36 un.).

**Ações:**
- **O THS1032 saiu hoje, 10 unidades, e ainda não tem fulfillment.** Confirmar
  com o fornecedor se consegue as 10 antes de prometer prazo.
- Confirmar o status do `TH3210D1004` abrindo a página da SupplyHouse.
- Cadastrar os 3 sucessores. O `TH1110U4000` tem 5.502 unidades no estoque da
  distribuição.
- THS1022 e THS1032 foram os dois para **Newark, DE 19711** — mesmo cliente,
  recomprando termostato. É o primeiro para avisar quando os sucessores
  entrarem.
- **Não investigado ainda:** se o padrão se repete em outras marcas. Quantos
  SKUs ACTIVE nossos já morreram no fabricante?

## 7. Fornecedor

Um pacote só, com três listas:
- **54 segurados** pelo piso físico (`pesos_segurados_suspeitos.csv`) — inclui
  a sentinela `0.0001 lb`, que aparece 14 vezes com valor idêntico
- **130 tubos** sem peso resolvível (`pesos_tubo_pendentes.csv`)
- **294 custos por pé** (`custos_por_pe_incorretos.csv`) — o campo `unitCost`
  guarda custo **por pé** e o preço é da peça inteira. Corrompe o relatório de
  lucro do Shopify em $123.989 de catálogo.

Pergunta objetiva para o fornecedor: **o campo `weight` é por pé ou pela peça
inteira?** Já está comprovado que para tubo é por pé.

## 8. SEO

Resta **1** da lista original: `pipe-straps-brackets-hooks` (64 produtos).
19 coleções no ar, 238 títulos corrigidos.

## 9. Mídia — revista de associação (em espera)

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

## 10. Menores

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
