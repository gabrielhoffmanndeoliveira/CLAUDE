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

### Leak detection — alvo trocado (16/set)

A `potable-water-leak-detection` tinha 321 impressões em `water leak detection`
na **posição 49, zero cliques**. Investiguei achando que era alavanca on-page.
Não era, por dois motivos que só apareceram medindo:

- **DR da THS é 7,0.** O menor DR no top 10 orgânico dessa query é **57**
  (prefeitura de Port Orange). Depois vêm Amazon 96, Home Depot 90, YouTube 99,
  Reddit 95, doityourself 77, minut 66. Distância que on-page não fecha.
- **A intenção é serviço.** Posição 1 é local pack de encanadores, posição 3 é
  caixa de perguntas sobre custo. O único espaço comprável é o carrossel de
  Shopping na posição 2 — que é o feed, não a página de coleção.

A página em si não tem defeito: title, meta, h1 únicos, 462 palavras boas,
23/23 produtos linkados, sem paginação, guia em `/pages/water-leak-detection-guide`
respondendo 200. **Impressão em posição 49 não é ativo, é ruído** — foi erro meu
priorizar por volume de impressão sem olhar DR e intenção antes.

### Feito (16/set) — três páginas mirando KD 0–5

| Página | Produtos | Alvo | Vol/mês | KD |
|---|---|---|---|---|
| `/collections/flo-by-moen` (nova) | 8 | `flo by moen` | 7.900 | 1 |
| `/collections/water-heater-shut-off-valves` (nova) | 4 | `water heater shut off valve` +2 | 1.550 | 0 |
| `/collections/floodstop` (reescrita) | 4 | `floodstop` | 400 | 0 |

Rollback em `colecoes_seo_rollback.csv`, commitado antes de mutar.

Duas lições da execução, ambas já valendo como regra:

- **Coleção nova não nasce publicada.** `collectionCreate` devolveu `userErrors`
  vazio e as duas páginas davam **404 no storefront**. Precisou de
  `publishablePublish` no `Publication/134723731559` (Online Store) em chamada
  separada. Conferir sempre por `resourcePublicationsV2`.
- **Regra automática > lista manual.** `TITLE contains "Flo by Moen"` puxou 8, não
  os 7 que eu tinha mapeado: `MOEN-935-001` Flo by Moen Service Kit tem
  `productType` diferente e não estava na coleção de leak detection.

Não confirmei a `flo-by-moen` pelo storefront — duas tentativas caíram no
**HTTP 429 / "Verifying your connection"** do Shopify depois de eu bater demais
no site. Não falseei user-agent. Confirmação existente é pela Admin API
(8 produtos, `isPublished: true` no Online Store). Abrir no navegador para fechar.

### Próximo na mesma veia

Alvos KD 0–5 já medidos onde a loja tem estoque e ainda não tem página:
`moen water leak detector` (1.400, KD 0), `best water leak detector` (900, KD 0),
`smart water leak detector` (900, KD 5), `underground water leak detector`
(700, KD 2). Pular Govee, Kidde e Ring — aparecem com KD 0 mas a THS não vende.

**Problema maior que apareceu de lado:** `moen` (535 produtos),
`taco-comfort-solutions` (122) e a `floodstop` antiga estavam todas no **mesmo
template genérico** ("Shop X products in stock at The House Supplier. Fast U.S.
shipping on plumbing, HVAC, fittings, valves and more."). Não é problema de três
páginas, é de toda coleção de marca da loja.

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

## 12. Perfil de links, bots e atribuicao (16/set)

### O perfil de backlinks e 93% um link do proprio grupo

```
backlinks live      22.034
refdomains live        500
Domain Rating          7,0
```

**20.418 desses links (92,7%) sao um unico link**, na barra de anuncio do tema
do `thefirealarmsupplier.com` (site irmao da JEM Systems, projeto Ahrefs
7227233), renderizado em 20.431 paginas:

```
anchor:      "Need HVAC or plumbing parts? Visit our sister store The House Supplier ->"
url_to:      https://www.thehousesupplier.com/    (so a home)
dofollow:    20.418 de 20.418
is_content:  false      <- o Ahrefs classifica como boilerplate de template
refdomains:  1
```

Isso explica o DR 7 sozinho: link sitewide de dominio co-owned colapsa para
perto de um voto so. **A THS tem exatamente UM link editorial legitimo** no
perfil inteiro: `thefirealarmsupplier.com/pages/about-us`, ancora "The House
Supplier", `is_content: true`.

**A barra nao se paga:** 116 sessoes em 90 dias (0,18% do trafego) e **zero
orders**. Recomendacao dada: `rel="nofollow"` no link da barra. Mantem a barra
para o humano, elimina a pegada de 20 mil dofollow entre dominios do mesmo dono.
Manter o link do `/pages/about-us` dofollow.

### O resto do perfil e spam passivo, nao link comprado

Gabriel confirmou que nunca compraram link. As ancoras provam: sao paginas de
venda de PBN que geram uma pagina por dominio-alvo, do tipo *"High Quality
Dofollow Backlinks DA 50 PA 40 Premium PBN Network Service thehousesupplier.com
... Buy Backlinks Online Cheap"* (88 links, 42 dominios). Os dominios de maior
DR sao todos `traffic_domain: 0` — autoridade inflada, ninguem visitando.

As mesmas ancoras citam **`thefastsupplier.com`, `thehvacsupplier.com` e
`thesupplierhouse.com`** — se sao do grupo, estao levando o mesmo tratamento.

### 51.495 sessoes de bot — e isso contamina TUDO

Sessoes por dispositivo/pais, 90 dias:

| Dispositivo | Pais | Sessoes |
|---|---|---|
| **other** | **Seychelles** | **45.595** |
| mobile | United States | 4.330 |
| desktop | United States | 4.131 |
| **other** | Netherlands | 2.999 |
| **other** | Lithuania | 1.481 |
| **other** | United States | 1.420 |

`device_type: other` = nem mobile, nem desktop, nem tablet. E script.
**As 60.323 sessoes "direct" sao ~85% robo.**

Serie semanal das Seychelles — a onda comecou do nada e esta decaindo:

```
ate 24/ago        0
semana 31/ago  30.630
semana 07/set  13.654
semana 14/set   2.554
```

**Comecou exatamente na semana em que a campanha de Shopping escalou** (1.850
sessoes sag_organic na mesma semana de 31/ago). Correlacao forte com scraper de
preco de concorrente ou bot de fraude de clique seguindo exposicao nova de feed.

**Trafego humano real dos EUA: 8.461 sessoes em 90 dias.** Com 31 orders, a
conversao real e **0,37%**, nao os 0,05% que sai do relatorio bruto.

**Isso fecha o circulo com a secao 11:** 50 mil sessoes de script batendo no
site e o que faz o Shopify devolver **504 sob carga** — a causa dos 3.113
"orfaos" falsos e dos 2 "5XX" que respondem 200 ao vivo. Nao sao tres
problemas, e um.

### NAO existe buraco de atribuicao — eu errei

Eu afirmei que o trafego pago do Shopping nao estava sendo atribuido, olhando
`referrer_source`. Errado. O relatorio de `referrer_source` so nao classifica
medium de feed como "search google". Por UTM esta tudo la:

| utm_source | utm_medium | utm_campaign | Sessoes 90d |
|---|---|---|---|
| google | product_sync | sag_organic | 3.634 |
| bing | cpc | Shopping_Search_082626_085848 | 1.487 |
| *(vazio)* | feed | meta_catalog | 273 |
| tfas | announcement_bar | sister_store | 134 |
| chatgpt.com | feed | (e openai_catalog) | 43 |
| shop_app | | | 28 |

E a serie semanal fecha a conta que eu tinha deixado aberta: **a campanha de
Shopping so comecou pra valer em 24/ago**.

```
ate 27/jul     0
03/ago        80
10/ago         1
24/ago       415
31/ago     1.850
07/set       830
14/set       463
```

3.634 sessoes em 90 dias contra 3.411 cliques em 30 dias nao era discrepancia:
os dois numeros cobrem praticamente a mesma janela. **Atribuicao esta sa.**

Fica em pe o alerta ja anotado na seccao 10 sobre o GA4 (42% dos cliques em
15/set contra 94-103% ate 10/set) — esse e outro fenomeno e continua aberto.

### Achados de lado

- **Existe uma campanha de Bing Ads rodando** que nao apareceu em nenhuma
  conversa: `Shopping_Search_082626_085848`, 1.487 sessoes/90d, 3 orders,
  $443,92. Confirmar com o Gabriel se e conhecida e quem gerencia.
- **43 sessoes vindas do ChatGPT** (`chatgpt.com / feed`, incluindo
  `openai_catalog`). O feed ja aparece em superficie de IA.

### Proximo passo em link building

A THS nao tem link editorial. Revende Moen, Resideo, Navien, Taco, Charlotte
Pipe, FloodStop — *dealer locator* de fabricante e link legitimo, gratuito e
inexistente hoje. E o caminho mais limpo para sair do DR 7.

## 13. Zone dampers Resideo — familia inteira fora do frete gratis (16/set)

### O gatilho

A order **#THS1033** ($531,21) trouxe dois dampers no mesmo carrinho: o
`ZD10X16` (7 lb, THS Standard) e o `ZD10X18` (3 lb, General com
`free-ship-eligible`). Um damper 10x18 nao pesa menos que um 10x16 — isso
abriu a investigacao.

### O dado nao existia em lugar nenhum

- **Fornecedor:** os 19 SKUs `ZD##X##` tem `w = 0`, sem L/W/H, sem cube.
- **Loja:** os pesos sao placeholder — so existem dois valores, **3 lb ou 7 lb**,
  sem progressao por tamanho. Um 10x10 (100 in2) e um 12x20 (240 in2) pesavam
  "3 lb" os dois.
- **Nenhum dos 19 tem metafield de dimensao**, entao o peso dimensional nunca
  entrava no calculo do lambda.

A elegibilidade a frete gratis era **heranca de perfil, nao calculo**: a regra
de tagueacao marcava se lambda passasse **e** (tivesse dimensao **ou** ja
estivesse no General). Sem dimensao, so foram marcados os que ja estavam no
General por motivo historico. Prova: o `ZD10X16` tinha lambda 0,0326 (passa) e
estava no Standard, enquanto o `ZD24X10`, maior e mais arriscado, estava no
General.

### A geometria veio do submittal sheet

`33-00264.pdf` (ZD Series Damper Submittal Sheet) da os dois numeros que
faltavam:

- **"All ZD models are 4 in. thick"** — espessura confirmada para a familia toda
- **Projecao maxima do atuador: 4-31/32 in (126 mm)**

Os PDFs **nao trazem peso nem dimensao de caixa** — confirmado em
`33-00264`, `33-00038` e `33-00040`. As paginas de produto tambem nao.

### Calculo e veredito

Caixa assumida `(d1+2) x (d2+2) x 7,48 in` (1" de folga por lado, metade da
projecao do atuador na altura), divisor UPS 139:

| SKU | caixa in | in3 | dim lb | preco | lambda |
|---|---|---|---|---|---|
| ZD20X12 | 22x14x7,48 | 2.305 | 16,6 | 228,83 | 0,0725 |
| ZD12X20 | 14x22x7,48 | 2.305 | 16,6 | 267,34 | 0,0620 |
| ZD24X10 | 26x12x7,48 | 2.335 | 16,8 | 273,31 | 0,0615 |
| ZD10X18 | 12x20x7,48 | 1.796 | 12,9 | 232,38 | 0,0556 |
| ZD16X12 | 18x14x7,48 | 1.886 | 13,6 | 258,78 | 0,0524 |
| ZD12X12 | 14x14x7,48 | 1.467 | 10,6 | 264,41 | 0,0399 |
| ZD10X10 | 12x12x7,48 | 1.078 | 7,8 | 198,94 | 0,0390 |
| ZD16X8 | 18x10x7,48 | 1.347 | 9,7 | 257,20 | 0,0377 |

**Os 19 falham a regua.** O menor lambda da familia e 0,0377, contra limite
0,0337 — nem o mais favoravel passa. O peso declarado subestimava o faturavel
em **2 a 5 vezes**.

Quanto custava, no ZD24X10: custo UPS = 14,98 + 4,51 x 16,8 = **$90,74**,
contra lucro bruto de 273,31 x 33,3% = **$91,01**. Sobrava **$0,27** — e isso
antes de qualquer sobretaxa.

Ressalva: espessura e projecao do atuador sao **dado confirmado**; a caixa e
**suposicao conservadora**. Se a caixa real for maior, os lambda pioram.

### Feito

9 SKUs movidos de General para `THS Standard - no free shipping` e com a tag
`free-ship-eligible` removida, verificado por leitura independente (nao por
`userErrors`): `ZD10X10, ZD10X18, ZD12X12, ZD12X20, ZD14X12, ZD16X12, ZD16X8,
ZD18X10, ZD24X10`. Os outros 10 ja estavam no Standard. **A familia inteira
esta correta agora.** Rollback em `zone_dampers_rollback.csv` e
`zone_dampers_tag_restaurar_MATRIXIFY.csv`.

### Aberto

- **Perguntar ao Craig (Resideo) se existe planilha de peso de embarque.** Seria
  o dado exato no lugar do derivado, e cobriria os 607 SKUs Resideo da loja.
- **O submittal sheet cobre familias inteiras** — este resolveu 19 SKUs num PDF
  so. Extrair geometria dos submittals e um caminho viavel para os 607, mesmo
  sem peso.
- O mesmo buraco continua nos **2.414 itens so com cube** e nos **579 segurados
  sem dimensao**. Se o Craig entregar a planilha, vale pedir o mesmo aos outros
  fornecedores grandes.

## 14. Descricao de produto — piloto nos zone dampers (16/set)

### O buraco

O SEO ate agora cobriu **titulo, meta e colecao**. **Descricao de produto nunca
entrou.** O que esta nas paginas e a saida do pipeline de import:

```
The 10 in x 16 in Parallel Blade Damper by Resideo is part of our zone dampers selection.
Brand: Resideo / Manufacturer Part #: ZD10X16TZ/U / Category: Zone Dampers
```

Template: `The {titulo} by {marca} is part of our {categoria} selection.` mais
tres bullets. Cinco dos 19 dampers nem o paragrafo tinham, so os bullets.

Nao tenho percentual confiavel do catalogo — o dump local de 15/set tem 38.918
registros para 14.883 produtos e nao e 1:1. Contar ao vivo se precisar do numero.

### Feito — 19 zone dampers, no ar em 16/09/2026

De ~250 para **~2.600 caracteres** por produto. Import Matrixify #746917174,
Updated 19 / Total 19, verificado por leitura live: perfil de entrega, tags e
meta description intactos nos 19.

Texto **derivado do submittal sheet 33-00264 e reescrito**, nao copiado da
Resideo — evita duplicar com o site do fabricante e com os outros distribuidores
que colam o mesmo blurb. Cada SKU e genuinamente diferente: traz o tamanho, o
lado em que o atuador monta e o **SKU espelhado equivalente** (`ZD10X16` vs
`ZD16X10`), que e a confusao real que faz o instalador pedir errado.

Cinco secoes: o que e e o que faz, power close / spring open, sizing e
orientacao, eletrica e desempenho, construcao, atuador de reposicao.

### Dois erros que valem para os proximos 607

- **O gerador nao tratava `d1 == d2`.** Nos dois dampers quadrados o texto dizia
  *"a ZD10X10TZ is the same opening..."* — o produto comparado com ele mesmo.
  Corrigido por API depois do import; o caso quadrado virou informacao util
  ("no mirrored part number to confuse it with"). **Qualquer familia com
  tamanhos quadrados vai repetir isso.**
- **`productUpdate` usa `ProductUpdateInput`, nao `ProductInput`.**

### Proximo

Medir daqui a algumas semanas: impressao e clique dos 19 contra os produtos
Resideo nao tocados, no GSC. Se subir, escala para os 607 Resideo — o submittal
cobre familias inteiras, entao nao sao 607 requisicoes.

## 15. Descricao Resideo — termostatos e o que o teste estabeleceu (16/set)

### Feito

| Bloco | SKUs | Estado |
|---|---|---|
| Zone dampers ZD | 19 | no ar, verificado (import #746917174) |
| Termostatos T-series + PRO 1000/2000/3000 | 20 | no ar, verificado (import #746927781) |
| | **39 de 607** | ~6,4% do catalogo Resideo |

Nos 20 termostatos: texto novo em 20/20, **UPC preservado em 18**, **Shipping
Weight em 6**, zero sobra do template antigo, perfil de entrega e meta
description intactos, e os 4 links de colecao do texto respondem 200.

### O corte foi por demanda, e a demanda Resideo e minuscula

Vendas Resideo em 12 meses, por `product_type`:

```
Non-Programmable Thermostats   $2.673,23   5 orders
Smart Thermostats                $989,19   1 order
Zone Dampers                     $447,35   1 order
                               ---------
                               $4.109,77   7 orders no ano
```

So tres familias venderam. Ressalva: **e circular** — produto sem descricao nao
vende, entao demanda passada num catalogo mudo mede o estado atual, nao o
potencial. E a janela e enviesada: o Shopping so escalou em 24/ago.

### O que o teste estabeleceu sobre a fonte Resideo

**Ganho que vale para os 607:** o sitemap `https://www.resideo.com/us/en/sitemap.xml`
tem **6.368 URLs**, 518 de termostato, e **casa numero de modelo com o slug oficial**.
Os 20 modelos bateram 20/20. Acabou a adivinhacao de URL e a busca modelo a modelo.

**Limite, testado e nao suposto:**
- Paginas de **categoria** da Resideo sao renderizadas por JavaScript — as tres
  vieram com ~170 KB identicos e zero numero de modelo no HTML.
- Paginas de **produto** idem: 20 baixadas, ~121 KB cada, spec nenhuma no HTML.
- **Só 3 das 20 linkam PDF**, e nenhuma e modelo de volume (TH1110DV1009,
  TH4210U2002, TH6320U2008, TH6220WF2006, TH3210D1004, THX321WFS2001W: zero).

O damper deu certo porque a pagina dele carregava o submittal `33-00264.pdf` no
HTML. **Isso foi excecao.** Para a maior parte do catalogo nao havera spec
estruturada, e o texto sera do tipo dos termostatos (guia de compra ancorado no
que o titulo afirma) e nao do tipo dos dampers (ficha tecnica).

### Regra de escrita adotada

Nao inventar terminal, faixa de temperatura, tipo de pilha nem requisito de
C-wire. Termostato errado volta como devolucao — texto curto e melhor que numero
inventado. O valor entregue foi a **equivalencia de nomenclatura** (PRO 1000/2000/3000
sao os nomes antigos dos mesmos tiers que T1/T4/T3) e o **guia de estagios**
(casar com o equipamento, nao com o comodo; sobra de estagio funciona, falta nao).

### Preservar campos e obrigatorio

Diferente dos dampers, os termostatos carregavam **UPC e Shipping Weight dentro
da descricao** — dado real que um overwrite cego apagaria. O gerador le e repassa.
**Peso de embarque dentro da descricao e o dado que passamos o dia cacando**, no
campo errado.

### Aberto nesta linha

1. **Cinco titulos quebrados em line voltage — RESOLVIDO (16/set).** O SKU
   estava inserido entre "Line" e "Volt". Corrigidos os 5 por API, mais caixa
   normalizada. Rollback em `titulos_line_voltage_rollback.csv`.
2. **`YTH5320R1000/U` — RESOLVIDO, e ao contrario do que eu propus.** Eu ia
   reclassificar o `productType` achando que era um Equipment Interface Module.
   O sitemap da Resideo desmentiu: o slug e
   `focuspro-kit-for-truezoner-panels-yth5320r1000-u`, e um **kit FocusPRO para
   paineis TrueZONE**, e `Non-Programmable Thermostats` estava certo. Corrigi o
   **titulo** e os dois campos de SEO, que repetiam a informacao errada. A meta
   agora aponta para o termostato avulso (`TH5320R1002/U`, $195,39), que era a
   confusao que o titulo velho criava contra o kit de $405,97.
3. **Pesos conferidos — batem.** Dos 6 com peso declarado na descricao: 3 batem
   exato (0,5 lb) e 3 diferem so por arredondamento (0,811 na descricao contra
   0,81 no Shopify, que trunca em 2 casas). **Zero divergencia real.** Minha
   suspeita de que "o dado existe e nao foi usado" estava errada: o peso foi
   usado. Fechado.
4. Medir daqui a algumas semanas: GSC dos 39 tocados contra os Resideo intactos.

## 16. GA4 — key events contam carrinho como conversao (16/set, URGENTE)

### O achado

Tres eventos estao marcados como key event no GA4, 90 dias:

```
add_to_cart                       533   is_key_event: true
ads_conversion_Shopping_Cart_1    300   is_key_event: true
purchase                           32   is_key_event: true
                                  ---
                                  865   <- so 32 sao venda. 96% e carrinho.
```

**E ha duplicacao.** O mesmo `add_to_cart` aparece duas vezes no relatorio, com
342 (nao marcado) e 533 (marcado), mais o `ads_conversion_Shopping_Cart_1` com
300 — que e evento criado pelo proprio Google Ads, contando o mesmo carrinho por
um terceiro caminho. Um add-to-cart esta sendo contado ate tres vezes.

### Por que custa dinheiro

Se o Google Ads e o Bing otimizam contra esse sinal, estao comprando **carrinho
abandonado, nao venda**. Bate exatamente com a analise de termos de busca do
mesmo dia: 98,1% do gasto em termos com clique e zero conversao, e a campanha
seguia rodando como se funcionasse — o algoritmo estava sendo recompensado por
encher carrinho.

Funil real, 90 dias:

```
view_item        6.189
add_to_cart        342   (5,5% dos view_item)
begin_checkout     616   <- MAIOR que add_to_cart, tambem nao fecha
purchase            32   (0,5%)
```

### Recomendacao

Deixar **so `purchase`** como key event. Desmarcar `add_to_cart` e
`ads_conversion_Shopping_Cart_1`.

Duas ressalvas:
1. Desmarcar nao apaga historico, mas **quebra a serie** — as campanhas vao
   parecer despencar de 865 para 32. E contabil, nao real.
2. **O Google Ads pode estar importando esses eventos como conversao.** Se
   estiver, ajustar la tambem, senao o Ads continua otimizando pelo sinal velho.

E configuracao no GA4 e no Ads, fora da API. Acao do Gabriel.

### De quebra, o GA4 confirmou tres coisas por angulo independente

- **Os bots.** GA4 ve `(direct)` com **1.535 sessoes**; o Shopify contava 60.323.
  GA4 roda JavaScript e script simples nao executa JS. **GA4 e a fonte limpa** — e
  confirma o diagnostico de bot das Seychelles sem depender do ShopifyQL.
- **O Bing converte.** `bing / cpc`: 1.415 sessoes, 3 transacoes, $399,26 em 90
  dias — mais a #THS1036 de hoje, que ainda nao entrou no GA4 por atraso de
  processamento. Sao 4 no total.
- **A barra da TFAS nao se paga.** 147 sessoes, 1 transacao, **$0,50** de receita.
  Reforca o `rel="nofollow"` ja recomendado.

### Achado novo: o ChatGPT vendeu

```
chatgpt.com / ai-assistant     9 sessoes   1 transacao   $216,98
chatgpt.com / feed            30 sessoes   0 transacoes   9 key events
```

9 sessoes e 1 venda. Amostra minuscula, nao da para concluir nada
estatisticamente — mas e dinheiro real de superficie de IA, e ninguem cuida
desse canal.

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

## 17. Defeito de peso no catálogo — os dois testes (16/set)

### O gatilho: #THS1037

Pasco `50750`, 7/8" × **50 ft** de Drain Hose, 2 unidades, **$303,00**, frete
grátis. Peso cadastrado: **0,37 lb**. `length`/`width`/`height` nulos. 1.965 em
estoque, perfil General + tag `free-ship-eligible`.

50 pés de mangueira de 7/8" não pesam 0,37 lb — é rolo, é volume, e sem
dimensão o peso dimensional não existe pro cálculo. Mesmo defeito dos zone
dampers e dos cimentos, só que aqui o disfarce é o comprimento.

### TESTE B — peso implausível para o que o título descreve

Arquivo: `peso_implausivel_TESTE_B.csv`. **95 suspeitos, 54 no frete grátis.**

Regras (aplicadas sobre `sh.json` com pesos de `ver2.jsonl` sobrepostos):

- `≥10 ft` no título e `lb < ft × 0,02`
- `gallon` no título e `lb < 5`
- `quart` / `32 oz` / `32 fl` e `lb < 1,5`

Piores por preço unitário:

| Preço | Peso | SKU | Título diz |
|---|---|---|---|
| $2.141,12 | 0,73 lb | MILW-3154-20 | 75' câmera de dreno + PACKOUT |
| $1.467,00 | 0,94 lb | POLY-200-250/300 | 2" × 300' Poly Pipe |
| $1.405,90 | 0,48 lb | WATT-0792024 | Quart |
| $1.275,00 | 0,63 lb | HDPE-GASH0110200250 | 2" × 250' Gas Pipe HDPE |
| $1.070,00 | 0,63 lb | MDPE-1002278 | 250 ft |
| $959,61 | 3,5 lb | CALA-GMP4 | Glycol Make-Up 4-Gallon |
| $937,85 | 0,94 lb | MPEX-1330040 | 5/8" × 400' PEX-AL-PEX |
| $891,00 | 0,57 lb | POLY-150-250/300 | 1,5" × 300' |
| $726,03 | 1,0 lb | ELKA-ELGDULB3322WH0 | Quart |
| $651,00 | 0,42 lb | POLY-125-250/300 | 1,25" × 300' |

**Os rolos de tubo são o caso do THS1037 em escala.** Bobina de 250–400 ft é
volume puro: o peso real já passa de 50 lb e o dimensional passa muito mais.
Estão cadastrados abaixo de 1 lb, com frete grátis, a mais de $600 cada.

### TESTE A — peso idêntico em tamanhos diferentes

Arquivo: `peso_chapado_TESTE_A.csv`. **444 grupos `(fornecedor, peso)`** com
≥4 SKUs e ≥4 tokens de tamanho distintos no título. Somados, tocam **4.344 SKUs
em frete grátis** — esse é o teto do dano, não o dano; boa parte é leve de
verdade. O sinal é o peso repetido, não o peso baixo.

| Fornecedor @ peso | SKUs | Tamanhos | No frete grátis |
|---|---|---|---|
| Pasco @ 0,33 lb | 35 | 20 | **26** |
| Diablo @ 0,73 lb | 60 | 18 | **45** |
| Milwaukee @ 0,73 lb | 47 | 16 | **37** |
| Centrotherm @ 2,19 lb | 34 | 15 | 22 |
| Elkay @ 1,0 lb | 9 | 15 | 9 |
| Dearborn @ 0,96 lb | 29 | 17 | 9 |
| Resideo @ 7,0 lb | 44 | 22 | 5 |
| MrPEX @ 29,2 lb | 21 | 17 | 0 |

O 0,73 lb de Diablo e Milwaukee e o 0,33 da Pasco são peso-padrão chapado: o
importador preencheu um valor único pra família inteira. É o mesmo mecanismo do
1,21 lb dos cimentos.

### Ressalva obrigatória

Os dois CSVs vêm do snapshot de **15/set**. Nenhum deles autoriza mutação
direta: **reler cada SKU ao vivo por API antes de tocar**, conforme a regra de
nunca colar ID de memória.

### Ordem proposta

1. **Rolos de tubo** (Poly / HDPE / MDPE / MrPEX PEX-AL-PEX) — maior risco por
   unidade e o caso já comprovado em pedido real.
2. **Diablo @ 0,73 (45 em frete grátis)** e **Milwaukee @ 0,73 (37)** — maior
   número de itens expostos.
3. **Pasco @ 0,33 (26)** — a família do THS1037.
4. **Centrotherm @ 2,19 (22)** — chaminé, volumoso por natureza.

Cada bloco: buscar peso e dimensão reais no `sup.json` / fornecedor, gerar
rollback, recalcular λ do dado bruto e mover só quem falha.
