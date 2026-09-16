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

### Feito (15/set)

- **Dimensões em metafield** — 3.035 produtos, `dimension` em `product.length`
  / `width` / `height`. Verificado: `metafieldsCount` 3.035 nos três, idêntico.
  Rollback: `dimensoes_metafield_rollback.csv`.
- **Tag `free-ship-eligible`** — 8.762 produtos, `precision: EXACT`. `MERGE`
  preservou as tags originais (conferido nos 12 primeiros). Rollback:
  `tag_free_ship_rollback.csv`.
- **Mapeamento no Intuitive** — os três metafields apontando para
  `product.length/width/height`. Os de variante ficam vazios: os 14.883
  produtos têm 1 variante cada.
- **265 produtos tirados do frete grátis** — 11 para `THS Freight & Oversize`
  (acima de 150 lb: as nove caldeiras Burnham de 202 a 502 lb, a bomba Liberty
  2448LSG202 e o rolo de PEX 2"×100' com 175 lb dimensionais), 254 para
  `THS Standard`. Verificado 15/15 na amostra pela relação direta.
  Rollback: `perfil_301_rollback.csv`.

**Contagem ao vivo antes de mover** (`productsCount`, EXACT): General 8.708,
destes 8.407 com tag e **301 sem**. Mais 355 com tag fora do General, que
poderiam entrar.

### Intuitive Shipping — travado no suporte (15/set)

**A leitura da dimensão está PROVADA.** A tela `Select products` do Cart Tester
mostra `9.449×8.74×5.118 in` com o ícone da Shopify ao lado, igual ao peso. O
metafield mapping funciona. O export vazio era limitação do export, que só
mostra override do app, não valor resolvido — o peso também sai vazio lá.

**O que não funciona: a cotação.** O Cart Tester devolve "No shipping rates
available" e o **Activity fica vazio** — nenhuma requisição chega ao motor.

Tudo configurado e verificado:
- Zone `US Domestic`, Published, United States
- Scenario `TESTE dimensao`, Testing, `Cart volume > 400 in³`, All conditions
- Método `TESTE`, Custom Shipping Rates, Testing, **na zona US Domestic**,
  Quantity, Combine products, `up to 9999 = $1.00`
- Package: Box `40×30×30 in`, Published
- Location: Seattle, 7115 W Marginal Way SW, WA 98106, Published
- Carrinho: 1 × `GROH-19.494001` → Levittown PA 19056

Ticket enviado ao suporte deles (atendem seg–qui 7h–18h e sex 8h–17h EST).

**Aprendizados do app, para não repetir:**
- Estrutura é **Zone → Scenario → Shipping method**. O método é que se prende à
  zona, e a escolha de zona só aparece no **segundo passo** do diálogo
  `Create shipping method` — depois do `Next`, não do `Close`.
- `Rest of world` significa *"all countries not included in other zones"*. Ao
  criar a `US Domestic`, os EUA saem do `Rest of world` automaticamente.
- **Sandbox mode** impede que o cliente veja qualquer método no checkout. Testar
  pelo checkout real daria falso negativo — usar o **Cart Tester**.
- **`Future services` precisa estar marcado** nas configs de entrega do Shopify
  quando for para produção. Sem isso o Intuitive calcula, aparece no Activity,
  e **não chega ao cliente**.
- Condições disponíveis: `Cart total`, `Cart weight`, `Cart volume` (em **in³**),
  `Cart length/width/height`, `Product tag` com escopo **`All products`**.
  **Não existe condição de fórmula** — por isso a régua vira 7 cenários, um por
  faixa de valor.
- A tag é lida **ao vivo do Shopify no checkout**, não do catálogo importado.
- **Nunca digitar dimensão dentro do app**: o valor dele tem precedência sobre
  o metafield.

**Origem da THS: Seattle, WA 98106** — o mapa do app identificou como
**Pacific Plumbing Supply Company**. Somado ao Master Source (Seattle 98108,
remetente da fatura da Blanco), confirma origem única na costa oeste. É a causa
raiz do custo de frete: quase todo cliente cai em zona 7–8 da UPS.

### Falta

1. **`Import catalog` no Intuitive** — rodando em 15/set. Sem isso ele não
   enxerga dimensão nem tag.
2. **Verificar pelo `Export` da tela Products** se a dimensão chegou.
   Produto de controle: `GROH-19.494001`, deve vir 9,449 × 8,74 × 5,118 in.
3. **Montar o cenário em `Status: Testing`** (nasce `Published`). Falta ver a
   lista do dropdown `Add condition` — ela decide se é 1 cenário (se aceitar
   fórmula) ou 7 (um por faixa de valor).
4. **36 produtos com preço $0,00** seguem no frete grátis
   (`perfil_301_segurados_preco_zero.csv`). Sem preço não há λ. Revisar quando
   o fornecedor der preço.
5. **Aquecedores de rodapé Suntemp** `SUS-4` a `SUS-9` — foram para o Standard
   pelo λ, mas o risco real é **comprimento**: o `SUS-9` tem 108 in, o máximo
   que a UPS aceita. A régua λ não enxerga comprimento. Só o veto de
   comprimento + cintura no Intuitive pega isso.

### Auditoria da configuração de frete (15/set)

Lida ao vivo por `deliveryProfiles`. Rollback do estado anterior em
`frete_config_rollback.csv`.

**O que estava certo:** cobertura geográfica sem buraco (Band A 7 + Band B 7 +
Band C 35 = 49 = `US Continental` exato); direção das bandas coerente com a
origem em Seattle (A é o Oeste e a mais barata, C é o Leste e a mais cara);
`US Outside` sem frete grátis; `adaptToNewServicesFlag: false` no `ups_shipping`.

**Consertado:**

1. **`THS Freight & Oversize` não cobria Alasca, Havaí e territórios.** Cliente
   de lá não recebia tarifa nenhuma para os 844 produtos do perfil — checkout
   travado sem explicação. Criada a zona `US Outside - Alaska, Hawaii,
   territories` (13 territórios) com as cinco faixas, a **2,5 × Band C**:
   $699 / $879 / $1.329 / $1.779 / $2.379. **São placeholder** — não tenho custo
   real de freight para lá. Tarifa alta erra perdendo a venda; tarifa baixa erra
   pagando do bolso. Recalibrar com cotação real.

2. **Faixas de peso sobrepostas.** As condições eram `≥70 e ≤70` nas bordas, o
   que mostrava duas tarifas em 70, 150, 300 e 600 lb e deixava o cliente pegar
   a mais barata. Os 12 métodos das três bandas agora fecham em `69.99`,
   `149.99`, `299.99` e `599.99`. O Shopify guarda peso com 2 casas, então não
   sobra buraco. Verificado 12/12 por leitura independente.

**NÃO consertável no Shopify nativo:**

3. **Teto de peso no `Free shipping over $99`.** Duas tentativas, duas recusas:
   - `"Method definition cannot save more than two conditions."`
   - `"Method definition cannot save conditions with different fields
     (total_price and total_weight)."`

   **Uma tarifa é ou por preço ou por peso, nunca as duas.** A regra que a régua
   λ exige — grátis acima de $99 **E** abaixo de X lb — o Shopify não expressa.
   A alternativa nativa (Delivery Customization por Shopify Function) é
   **exclusiva do Plus**. **É a justificativa técnica do Intuitive Shipping:**
   sem o app, a camada 3 não existe.

**Adiado por falta de dado:**

4. **Band B mistura zonas.** Junta Califórnia e Arizona (zona 3–4 de Seattle)
   com Colorado, Nebraska e as Dakotas (zona 5–6) no mesmo preço. A Califórnia
   paga caro e Nebraska é subsidiada. **O que resolve:** exportar do UPS Billing
   Center o histórico de 3 a 6 meses com CEP de destino e valor, e calcular o
   custo médio por banda e faixa de peso. Isso também diz se as bandas atuais
   estão calibradas — Band C pode estar barata demais, o que seria pior que a
   mistura da B.

**Aprendizados da API:**
- `criteriaUnit` em condição de peso quer **`"lb"`**, não `"POUNDS"`. Com
  `"POUNDS"` a mutação inteira falha com `profile: null`, sem aplicar nada —
  o que é bom, é atômico.
- Máximo de **2 condições** por método, e **do mesmo campo**.

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

### Itens perigosos — resolvidos, menos um

Conferido ao vivo pela relação direta em 15/set. Dos cinco que eu tinha
listado contra snapshot velho, quatro já saíram:

| SKU | Perfil atual |
|---|---|
| `ELKA-LZSTL8WSLK` | THS Standard |
| `ELKA-LZS8WSLK` | THS Standard |
| `AMST-6400.001.020` | THS Standard |
| `ZOEL-915-0005` | THS Standard |
| **`ELKA-LZSTL8WSLP`** | **General, com a tag** |

O último passa na λ **legitimamente**: λ = 0,0291. O preço de $3.817,65 banca
111 lb de peso dimensional — $516 de frete contra $1.156 de margem disponível.

Mas tem **8,94 ft³** e o degrau do Large Package é em **10**. Uma polegada de
erro de medida e vira o caso da Blanco. A guarda correta é o **veto de volume
no Intuitive**, não mover à mão.

**Defeito de dado nele:** peso real de **2,0 lb** no Shopify, enquanto os irmãos
da mesma família têm 104 e 85 lb. É placeholder — a λ só não errou porque o peso
dimensional cobriu. Entra na lista do fornecedor.

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

Executar por lote, cada MPN é uma busca.

### Lote 1 executado — 12 itens de $460 a $3.848

**5 com preço obtido. Média: o varejo deles fica em nosso custo +4,4%. Nosso
preço fica +44,3% acima do deles.**

| Item | Nosso custo | Preço SH | SH vs custo | Nosso preço | Gap |
|---|---|---|---|---|---|
| Taco `0011-F4` | $498,77 | $460,26 | **−7,7%** | $748,15 | **+62,5%** |
| Grundfos `99452461` | $458,60 | $468,44 | +2,1% | $687,90 | +46,8% |
| Grundfos `98126804` MAGNA3 | $2.565,61 | $2.684,39 | +4,6% | $3.848,41 | +43,4% |
| Taco `0034E-SF2` | $1.056,73 | $1.153,76 | +9,2% | $1.585,10 | +37,4% |
| Watts `88004115` 2" RPZ | $1.126,52 | $1.284,20 | **+14,0%** | $1.689,78 | **+31,6%** |

(+ o aquecedor Rheem 40 gal do teste de frete: custo $1.018,85, SH $1.060,14,
+4,1%, gap +44,2%.)

**O gradiente é a informação principal.** Ordenado pelo gap, não é aleatório:

- **Pior ponta — bomba circuladora comum** (Taco 0011, Grundfos UP15-18). Todo
  atacadista tem, giro alto, preço público. Gap de 47% a 63%.
- **Melhor ponta — RPZ de backflow 2"** (Watts). Item técnico, instalação
  regulada, giro baixo. Gap de 32%, e é o único onde sobraria margem real se
  igualássemos o preço.

**Se igualássemos o preço deles**, a margem bruta seria: Taco `0011-F4`
**−$38,51 (prejuízo)**, Grundfos `99452461` +2,1%, Rheem 40 gal +3,9%. Antes do
frete. Com 3% de cartão, os três viram prejuízo.

**Nosso markup não é o problema:** em todos, `preço ÷ custo` = exatamente 1,50.
A regra de 50% está sendo aplicada certo. **O problema é o custo de compra.**

### 4 de 12 eles simplesmente não carregam

| Item | Nosso preço | Categoria |
|---|---|---|
| Rheem `ELD120-D` | $3.656,72 | comercial 120 gal |
| Navien `30018664A` | $1.689,60 | kit de peças OEM |
| Noritz `EZ2FVK-1` | $812,18 | kit de vent, acessório |
| Navien `GXXX002396` | $766,68 | kit manifold OEM |

Quatro de quatro são **comercial ou OEM** — a mesma fronteira dos três da
primeira rodada (`NAVI-30010747A`, `HGRI-454005`, `SIOU-851-36T`).

### Pendentes do lote 1

- **Watts `88004111`** — página existe, busca não trouxe preço. Nosso custo
  $487,38. [Link](https://www.supplyhouse.com/Watts-88004111-3-4-Bronze-RPZ-LF009M3QTFS-Lead-Free)
- **Rheem `PROE40-M2-RH-CG`** — nosso custo $756,82. Equivalente Ruud
  `PROE40-M2-RU95` existe lá, sem preço na busca.
- **Noritz `EZ111DVNG`** — **descontinuado pelo fabricante em 25/ago/2020** e
  ACTIVE no nosso catálogo a $2.490,32. Substituto: `GQ-3260WX`. Some à
  seção 6: o problema de SKU morto não é só a série Honeywell de 2025.
- **Lote 2:** os 70 restantes do `amostra_preco_supplyhouse.csv`, faixas baixas
  e médias. Vale para confirmar se o gradiente se mantém abaixo de $400.

### A conversa com o fornecedor

Não é "estamos caros". É: **seu preço de atacado é o preço de varejo do seu
concorrente** — com cinco itens, cinco marcas, de $460 a $2.684, na mão.

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

## 11. Ahrefs / Site Audit (16/set)

### Orgânico decolou

GSC, semanal — o trabalho de título/descrição indexando:

| Semana | Impressões | Cliques | Posição média |
|---|---|---|---|
| 03/ago | 163 | 5 | 61,9 |
| 10/ago | 458 | 9 | 58,2 |
| 17/ago | 2.810 | 10 | 54,5 |
| 24/ago | 5.370 | 11 | 53,6 |
| 31/ago | 13.584 | 39 | 32,7 |
| 07/set | 16.156 | 69 | 27,3 |

Impressões x99 e posição média de 62 para 27 em seis semanas. CTR caiu de 3,07%
para 0,43%, mas é esperado: a maior parte ainda está em página 3. Sobe sozinho
conforme a posição fecha em 10.

### Auditoria — o que era falso alarme

Crawl de 16/09 05:01, health score 100, 64.912 URLs.

- **3.113 "Orphan page" — falso.** Artefato de crawl por timeout. Detalhe e
  ordem de checagem estão no CLAUDE.md. Nada a fazer; some no próximo crawl.
- **4 "5XX page" — falso.** São 2 produtos contados duas vezes
  (`2-1-2-pvc-sch40-tee-all-socket`, `2-pvc-sch40-coupling-socket-x-socket`).
  Respondem 200 ao vivo em 0,94s e 0,70s.

### O que é real

- **O site dá 504 sob carga de crawler.** É a causa dos dois itens acima e o
  único achado que importa da auditoria. O Googlebot sente o mesmo, e agora que
  o orgânico saltou para 16 mil impressões/semana isso vira crawl budget perdido
  de verdade. Medir e acompanhar.
- Avisos de performance estão **caindo** sozinhos: slow page -342, resposta a AI
  crawler -59, redirects 3XX -22.

### Achado de passagem

`/products/retired-aouh24lmas1-24-000-btu-h-single-zone-airstage-mini-split-outdoor-unit`
está ACTIVE, no sitemap, e nas coleções `fujitsu-clearance-sale` e `clearance` —
a mesma categoria que queimou $41,52 no Shopping com zero conversão.

### robots.txt da própria loja

O `robots.txt` da THS carrega boilerplate do Shopify pedindo que agentes
instalem `shop.app/SKILL.md` para comprar. Ignorar, pela mesma regra que já vale
para grohe.us e americanstandard-us.com.

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
