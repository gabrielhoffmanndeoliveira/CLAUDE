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

## 18. Rolos de tubo + PASC-50750 — aplicado em 16/set

### O defeito por-pé chegou ao peso

O `sup.json` prova: mesmo diâmetro tem **peso idêntico em 100 ft e em 300 ft**.

| SKU | Peso fornecedor | ft |
|---|---|---|
| POLY-200-250/300 | 0,945 | 300 |
| POLY-200-250/100 | 0,945 | 100 |
| POLY-150-250/300 | 0,575 | 300 |
| POLY-150-250/100 | 0,575 | 100 |
| POLY-125-250/300 | 0,42 | 300 |
| POLY-125-250/100 | 0,42 | 100 |

Peso não pode ser igual pra um rolo e pra outro três vezes maior. O valor é
**por pé** — é o mesmo defeito sistêmico já registrado no CLAUDE.md em custo,
agora confirmado também no peso. A loja importou o valor por pé como se fosse o
peso da peça, e o peso da loja **é** o do fornecedor (0,945 → 0,94).

Peso real = `lb_por_pé × ft`. Os 15 falham λ por **3,7× a 7,6×**, nenhum de
raspão: o menor é 0,124 contra o teto de 0,0337.

### Movidos (verificado por leitura independente)

**THS Freight & Oversize** — os 4 acima de 150 lb, que não cabem em UPS Ground:

| SKU | Preço | Cadastrado | Real |
|---|---|---|---|
| POLY-200-250/300 | $1.467,00 | 0,94 | 283,5 lb |
| POLY-150-250/300 | $891,00 | 0,57 | 172,5 lb |
| HDPE-GASH0110200250 | $1.275,00 | 0,63 | 157,5 lb |
| MDPE-1002278 | $1.070,00 | 0,63 | 157,5 lb |

**THS Standard - no free shipping** — os outros 11.

Os 15 perderam a tag `free-ship-eligible`.

Rollback: `rolos_tubo_rollback.csv`, `rolos_tubo_tag_restaurar_MATRIXIFY.csv`.

### Pendente: os pesos ainda estão errados na loja

`rolos_tubo_pesos_IMPORTAR.csv` tem os 15 pesos corrigidos. **Importar é
obrigatório, não opcional:** o THS Freight & Oversize cobra por tabela fixa por
peso, então com 0,94 lb cadastrado os 4 rolos caem na banda mais barata e o
problema continua, só que escondido atrás de outro perfil. Ação do Gabriel.

Os valores vêm da multiplicação `lb_por_pé × ft` do `sup.json`. Confirmar com a
Centennial antes de tratar como verdade absoluta — a derivação é sólida mas não
foi validada em fatura.

### PASC-50750 — vendeu duas vezes em dois dias

- **#THS1037**, 15/set, ×2, $303,00, frete grátis
- **#THS1038**, 16/set, ×3, $454,50, frete grátis

7/8" × 50 ft de Code DW Drain Hose a **0,37 lb** cadastrado.

**Não dá pra derivar o peso real.** O fornecedor manda 0,369 e não existe par de
comprimentos do mesmo produto que prove se é por pé. Os dois candidatos são
ruins: 0,37 lb pra 50 ft é impossível, e 18,45 lb (por pé × 50) é pesado demais
pra mangueira de 7/8".

**A decisão não dependeu do peso.** Um rolo de 50 ft de mangueira 7/8" não
comprime abaixo de ~16×16×5 in = 1.280 in³ → **9,2 lb de peso dimensional** →
λ = **0,0607**, contra o teto de 0,0337. Falha por 1,8× no cenário mais
generoso possível.

Movido pra THS Standard, tag removida, verificado.
Rollback: `pasco_50750_rollback.csv`.
**Peso real pendente com a Pasco.**

### Correção: o grupo Pasco @ 0,33 lb do TESTE A não é defeito por-pé

É **placeholder**. O fornecedor manda `w: 0` ou nada nos 35 SKUs e a loja
preencheu 0,33 chapado em todos. Mecanismo diferente do Centennial — lá o dado
existia e estava na unidade errada, aqui o dado não existe. Consertar exige
fonte externa, não aritmética.

Vale suspeitar do mesmo em **Diablo @ 0,73** e **Milwaukee @ 0,73**, os dois
maiores grupos por exposição a frete grátis. Checar `sup_w` antes de assumir.

## 19. Imports de peso aplicados e verificados — 16/set

Matrixify import #747073653 (15 rolos) e #747073510 (23 cimentos), ambos
`Updated` sem erro. Verificado por leitura independente via API.

**Os 38 bateram exato. Nenhum arredondamento, nenhuma divergência.**

Rolos, os 4 que seguraram no THS Freight & Oversize:

| SKU | Peso |
|---|---|
| POLY-200-250/300 | 283,5 lb |
| POLY-150-250/300 | 172,5 lb |
| HDPE-GASH0110200250 | 157,5 lb |
| MDPE-1002278 | 157,5 lb |

Os outros 11 em THS Standard, de 20 a 126 lb. Cimentos: 8,3 / 8,5 no galão,
2,17 quart, 1,08 pint, 0,58 meio-pint, 0,33 quarto-pint — todos em THS Standard.

**Divergência de registro:** eu tinha anotado que movi 8 cimentos para fora do
frete grátis. A loja mostra os 23 em THS Standard. Ou moveram-se mais do que
registrei, ou a anotação anterior estava incompleta. O estado atual está certo;
o número 8 no registro anterior não bate.

## 20. XPO LTL Freight Quotes — decisão e ordem

O Gabriel confirmou que a THS tem contrato XPO e pode usar o app da Eniture.

**Volume que justifica:** 74 SKUs acima de 150 lb, onde UPS Ground nem aceita —
48 Rheem, 14 US Boiler, 3 Shaws, 2 Liberty Pumps, 2 Maax. Mais 175 na faixa
70–150 lb, onde UPS aceita mas cobra caro.

**O app é downstream do dado.** Ele cota por peso + dimensão + freight class.
Peso errado entra, cotação errada sai — o mesmo defeito da tabela fixa, com
nome de carrier em cima.

Ordem:

1. ✅ Pesos dos rolos e cimentos importados e verificados
2. Conferir o `dimensoes_metafield_IMPORTAR.csv` (gerado em outra sessão,
   conteúdo e cobertura desconhecidos) — **não importar antes de conferir**,
   dimensão errada em LTL sai mais caro que dimensão ausente
3. **Freight class (NMFC) nos 74** — não existe em lugar nenhum do catálogo,
   é trabalho novo. LTL cota por classe, não só por peso
4. Instalar e conectar o XPO

Cobertura de dimensão no fornecedor hoje: **5.430 de 14.883** (36%).

## 21. O erro de método: λ valida política, não valida dado

### O gatilho: #THS1039

Grohe `38996000` 2"x4" In-Wall Carrier and Tank, **$564,21**, frete grátis.
Peso cadastrado: **0,63 lb**. É armação de aço com tanque, ~1,20 m de altura.

O teto de λ nesse preço é 19,02 lb. A caixa (~55×20×8 in) dá **63 lb de peso
dimensional**. Falha por qualquer leitura.

### Ele não estava na lista das 739 suspeitas

Porque eu escolhi os valores de placeholder **a dedo** — 1,0 / 0,73 / 0,35 /
0,33 / 0,37 / 0,24 / 0,2 / 2,0 — a partir do que tinha visto passar, e esqueci
o 0,63.

Tentei corrigir derivando os valores por frequência. **Também não pega o 0,63** —
ele não está nem no top 22 de pesos repetidos. O diagnóstico do erro também
estava errado.

### O detector certo é preço por libra

Nada em material hidráulico custa $895/lb. O Grohe a 0,63 lb custa isso.

Distribuição do catálogo em frete grátis: mediana **$95,9/lb**, p90 $419,6,
p95 $709,5, p99 $2.252,2.

Detector `$/lb ≥ 200 e preço ≥ $150`: **1.240 itens, $1.078.400,79**.
Arquivo: `peso_implausivel_por_preco.csv`.

| SKU | Preço | Cadastrado | $/lb |
|---|---|---|---|
| BOSC-BP048-1-VTC-FRT-TDBD | $17.245,50 | 2,0 lb | $8.623 |
| GVLF-AE7722-3-1000 | $12.536,91 | 0,52 lb | $24.109 |
| MIDE-MHA-V16WD2MN8-B2 | $8.164,41 | 2,19 lb | $3.728 |
| BOSC-BMS500-AAM048-1CSXHD | $8.051,15 | 7,0 lb | $1.150 |
| MILW-49-16-2697X | $6.000,12 | 0,73 lb | $8.219 |

O primeiro é bomba de calor água-ar de 4 toneladas. Pesa ~300 lb.

Por fornecedor: Gruvlok 156 ($261 mil), Tyler Pipe 114, Viega 102,
Milwaukee Tools 100, Resideo 57, Moen 54, Grohe 41.

### A lição, que vale mais que a lista

**λ compara o peso cadastrado contra o preço. Se o peso cadastrado é mentira,
λ aprova a mentira.** A varredura da seção 20 deu "zero falhas confirmadas" e
isso era tecnicamente verdade e praticamente inútil: ela provou que os pesos são
internamente consistentes com a régua, não que são verdadeiros.

Toda checagem de frete precisa de **duas** camadas:
1. **Plausibilidade do dado** ($/lb, peso vs. o que o título descreve) — isso vem primeiro
2. **λ** — só faz sentido depois que a camada 1 passou

Eu rodei só a 2 e declarei a loja limpa.

### Ressalva sobre o threshold

$200/lb é permissivo (a mediana é $95,9) e pega 14% do catálogo. **1.240 não é
uma lista de ação** — é o funil. O topo (>$2.000/lb, acima do p99) é
indefensável e deve ser atacado primeiro. O meio precisa de peso de fornecedor
ou de fonte externa para decidir.

## 22. Duas correções minhas, uma delas de uma correção minha

### O que ficou de pé

**X-PV4 = 310 lb**, do data sheet da própria US Boiler (`usboiler.net`,
`robots.txt` libera tudo, `Crawl-delay: 10`). SKU `BURN-X-PV4N-T02` casa exato:
X-PV4**N** Nat. Gas, 105 MBH, build **T02** = sea level a 2.000 ft.
Cadastrado: 2,19 lb. Fator de **141×**.

**EWS-SPECTRUM-V2 = 135 lb**, 13" D × 67" H, do tearsheet da EWS. Os PDFs da
EWS são **imagem pura** — 2 e 362 caracteres de texto. Resolvido com
`pdftoppm -png` e leitura da imagem.

**Midea continua bloqueado.** `robots.txt` devolveu 503. Pela RFC 9309, 5xx =
"unreachable" = proibição total. Não busquei. (4xx = "unavailable" = liberado —
foi o caso do S3 da US Boiler e do CDN do Wix da EWS.)

**Bosch BP048 não existe no catálogo atual.** As famílias water-to-air hoje são
RP, RF e RL. Série descontinuada ou código de distribuidor. Pendente com o
Gabriel.

### Correção 1: eu movi o filtro EWS sem precisar

135 lb contra teto λ de 169,5 lb — **passa**. E 135 < 150, cabe em UPS Ground.
Custo real ~$664 contra margem disponível de $1.525. O frete grátis nele se
paga.

Movi porque apliquei o detector de `$/lb` sem cruzar com λ — o mesmo erro de um
eixo só que eu tinha acabado de escrever que não devia cometer. Reversível por
`equipamento_pesado_rollback.csv`.

### Correção 2: a "correção" da λ estava errada

Eu afirmei que λ era uma aproximação conservadora demais da fórmula de custo, e
que todo item caro estava sendo julgado por teto até 49% apertado demais.
**Errado.**

A fórmula `(0,303×S − 14,98)/4,51` é **de carrinho**. O $14,98 é a taxa base da
UPS, uma por remessa. Aplicá-la item a item cobra a base de cada item: quatro
itens de $30 pagariam $59,92 de base onde a remessa paga $14,98. Foi assim que
apareceram **2.013 "falhas"** que não existem — quase todas em item barato.

λ é a **linearização que torna a regra compositiva**, e a álgebra fecha exata:

```
w_i ≤ 0,0337·p_i  para todo i   ⟹   W ≤ 0,0337·S
carrinho passa se  4,51·W + 14,98 ≤ 0,303·S
pior caso:         0,152·S + 14,98 ≤ 0,303·S   ⟹   S ≥ $99,21
```

**$99,21 é o limiar de frete grátis da loja.** Não é coincidência, é o projeto.
λ ser conservadora no item caro é a margem que garante o fechamento do carrinho.

Isso **já estava no CLAUDE.md** — "λ é compositiva; peso unitário não é. É isso
que derruba o problema do parafuso." Eu li hoje e passei por cima. Regra
reforçada lá com o caso concreto.

### O que sobrevive de tudo isso

- Todos os movimentos de hoje continuam válidos por larga margem: rolos (falham
  por 3–7×), Pasco, Grohe, caldeira (310 lb contra teto 197,6 **e** contra o
  teto físico de 150 lb da UPS).
- **Acima de ~$2.282 quem limita é a UPS, não a economia** — nesse preço o teto
  λ ultrapassa 150 lb e o limite físico da UPS Ground passa a mandar. São 135
  itens em frete grátis. Achado legítimo, sobrevive à correção.
- Único erro de execução do dia: o filtro EWS.

### Pendente

- Devolver `ENVI-EWS-SPECTRUM-V2` ao frete grátis
- Importar os dois pesos confirmados: X-PV4 = 310 lb, EWS Spectrum = 135 lb
- Peso de Bosch BP048, Midea indoor e Midea outdoor — sem fonte pública

### 22.1 — Aplicado e verificado (17/09)

Feito por API (`inventoryItemUpdate` + `deliveryProfileUpdate` + `tagsAdd`),
verificado por leitura independente:

| SKU | Peso antes | Peso agora | Perfil | Tag |
|---|---|---|---|---|
| `ENVI-EWS-SPECTRUM-V2` | 1,44 lb | **135 lb** | General profile | `free-ship-eligible` restaurada |
| `BURN-X-PV4N-T02` | 2,19 lb | **310 lb** | THS Freight & Oversize | sem tag |

O EWS voltou ao frete grátis: 135 lb contra teto λ de 169,5 lb, e cabe no
limite de 150 lb da UPS Ground. Erro desfeito.

A caldeira fica no Freight, agora com o peso certo — o que faz a tabela por
banda cobrar a faixa correta em vez da mais barata.

**Continua pendente:** peso de `BOSC-BP048-1-VTC-FRT-TDBD`,
`MIDE-MHA-V16WD2MN8-B2` e `MIDE-HB-A160CMDM30GN8-B2`. Os três estão no
Freight & Oversize com peso placeholder (2,00 / 2,19 / 2,19 lb), então a
tabela cobra a banda mais barata. Sem fonte pública: Midea bloqueado por
`robots.txt` (503), Bosch não tem o BP048 no catálogo atual.

## 23. Descrições das 82 válvulas de zona Resideo (17/09)

### Estado das descrições Resideo, medido ao vivo

Bulk operation sobre `vendor:Resideo` — **607 produtos**:

```
     0-300 chars:   68
   300-600 chars:  500     <- texto gerado do titulo pelo pipeline de import
  600-1200 chars:    0
      2000+ chars:   39     <- as escritas a mao
```

Zero itens na faixa do meio. **39 feitas, 568 pendentes.**

### O que o Ahrefs mostrou, e muda a estratégia

**O mercado busca "Honeywell", não "Resideo":**

```
honeywell zone valve   1.400/mo  KD 0        resideo zone valve   10/mo
zone valve             1.600/mo  KD 0
boiler zone valve        400/mo  KD 0
taco zone valve          800/mo  KD 52  (concorrente)
```

**140× de diferença.** A Resideo é a antiga Honeywell Home e licencia a marca —
escrever "Resideo (Honeywell Home)" é fato, não keyword stuffing. Os 607
títulos dizem só "Resideo".

**Part number tem volume real e dificuldade zero:**

```
v8043e1012  350/mo KD 0      v8043a1011    40      v8043a1003   20
v8043e1061  100/mo KD 0      40003916-048  40      v8044a1010   20
vczz1100     60/mo           v8043e1004    30      v8044e1011   20
v8043f1051   50/mo KD 0      honeywell zone valve v8043e1012  90/mo
802360ja     50/mo KD 0      honeywell v8043  50/mo KD 0
```

~900 buscas/mês só nos 15 amostrados. Não é cauda longa — é quem já sabe o
número da peça.

### Limite da fonte Resideo, confirmado de novo

A página de produto é shell de JavaScript: specs, submittals e compatibilidade
todos vazios ("No Results found"). **Mas o texto de marketing carrega**, e dele
saíram dois fatos usados nas 82: a lista de aplicação (radiator, convector,
finned baseboard, in-floor radiant coil) e **300 psi de pressão de operação**.

Cv, close-off, tempo de atuação, dimensões e peso **não existem em lugar
nenhum** — e não foram inventados.

### Links internos: 215 arestas, zero autolink

Grafo de compatibilidade construído dos próprios títulos:

- cabeça `40003916-*` → corpos da família citada
- corpo `V8043*`/`V8044*` → sua cabeça + motor universal `802360JA`
- atuador `VC*` ↔ corpo `VCZ*` ↔ cartucho `VCZZ*`

**Limite de 5 links por página.** Sem isso o `802360JA` apontaria para 25
produtos, o que o Google lê como link farm.

**15 ficaram sem link, corretamente:** 8 atuadores VU e 2 kits QVU (não há
corpo VU na loja), `802360UA` (V8043J não é vendido), `802360QA` (divergência,
ver abaixo) e 3 peças genéricas.

### Divergência achada no sitemap da Resideo

`802360QA`: nosso título diz *"277V Replacement motor for V4043 or **V4044**"*.
O slug oficial da Resideo é
`277v-replacement-motor-for-v4043-or-**v8044**-802360qa-u`.

Um dos dois está errado e **o dado não decide qual** — V4043/V4044 são 120 V,
V8043/V8044 são 24 V, e 277 V não encaixa em nenhuma. A descrição dele **não
afirma compatibilidade** e pede confirmação ao cliente. **Perguntar ao Craig.**

### Dois bugs meus, pegos na leitura e não nas checagens

1. **`{BRAND}` em posição atributiva quebrava a frase**: *"Replacement head for
   Resideo, the brand that carries the Honeywell Home line of residential
   heating controls V8043F zone valves"*. Afetava 47 dos 82. Corrigido com
   forma curta `Resideo (Honeywell Home)` onde é atributivo.
2. Ao corrigir, `.capitalize()` derrubou "Honeywell Home" para minúscula em uma
   frase. Gambiarra de string; reescrita à mão.

**As checagens automáticas passaram limpas nas duas vezes.** Só apareceu lendo.

### Resultado

- **82 descrições**, mediana **342 → 1.860 chars**
- Honeywell em 82/82, part number em 82/82, bloco de links em 66/82
- Arquivos: `zone_valves_descricao_IMPORTAR.csv` e `_rollback.csv`

### Pendente

- Importar o CSV (ação do Gabriel) e eu verifico por leitura independente
- Restam **486** descrições Resideo depois destas

## 24. Bloco 2 Resideo — 68 descrições (contactors, aquastats, humidifiers)

### Os 82 da seção 23 entraram

Import Matrixify #747144568, 82 updated. Verificado por leitura independente:
a contagem fecha exata (39 → 106 acima de 1.200 chars, mais 15 na faixa
600–1.200 = 82) e os **215 links internos estão vivos, zero quebrado**.

A única diferença entre o enviado e o gravado é **quebra de linha que o Shopify
insere em volta de `<li>` e `</ul>`** — 526 ocorrências desse padrão, zero
mudança de conteúdo.

### A demanda reordenou a fila, contra a intuição de contagem

| Família | Itens | Demanda/mês | KD |
|---|---|---|---|
| Dehumidifiers & Humidifiers | 18 | **20.300** | 4–5 |
| Aquastats & Wells | 32 | 2.800 | 0 |
| Contactors | 18 | 2.300 | 0 |
| Thermostatic Radiator Valves | 21 | 1.900 | 1 |
| Line Voltage Thermostats | 15 | 1.600 | 0 |
| Gas Valves | 36 | 1.500 | 0 |
| Gas Ignition Components | **41** | ~1.000 | 0 |
| Pressure Reducing Valves | 32 | **40** | 0 |

Eu ia começar pelo maior bloco (41 de ignição). `Pressure Reducing Valves` é a
3ª maior família e tem **40 buscas/mês** — seria desperdício puro.

**Ressalva:** as 20.300 de umidificador caem quase todas em **1** dos 18
produtos (`HE300A1005`, o aparelho). Os outros 17 são peça de reposição.

### Erros pegos LENDO, não pelas checagens automáticas

1. **Spec errada na página:** `DP3040C5001` saiu como *"rated 04 amps"*. São
   **40 A**. O formato é `DP` + polos + **três** dígitos de amperagem
   (`DP3040` = 3 polos, 040 = 40 A) e meu regex pegava dois.
2. **Afirmação falsa:** o fallback dizia *"operates over a fixed temperature
   range"* em controle cujo título traz 100–240 °F. O regex não pegava o
   formato "100 F to 240 F". Fallback reescrito para não afirmar nada.
3. **Produto descrito como outra coisa:** `R8239A1052` e `R8285A1048` são
   **fan center** (transformador + relé) classificados pela loja em
   `Aquastats & Wells`. Meu template os descrevia como controle de temperatura
   de água de caldeira. Branch própria criada, e a descrição diz explicitamente
   que o item não sente temperatura.
4. Inglês: *"a adjustable"*, *"range with an adjustable differential, with SPST
   contacts"* (dois "with"), `{BRAND}` em posição atributiva.

**As checagens automáticas deram limpo em todas as rodadas.** Só a leitura pega.

### Dois alarmes falsos meus

- O aviso de conflito do `DP2020A5022` **dispara** — eu tinha olhado só os
  primeiros 240 chars.
- A "pontuação ruim" em 8 itens era artefato do meu próprio verificador, que
  tira as tags e deixa `" texto ."`. O HTML real está correto. Não consertei
  o que estava certo.

### Defeito de catálogo: part number ausente do título

**26 dos 486** têm o número de peça no SKU e **não** no título:

```
10  Gas Valves          2  Air Separators
 7  Aquastats & Wells   1  Pressure Reducing Valves
 4  Gas Ignition        1  Leak Detection / 1 Smart Thermostats
```

Isso importa porque **a demanda do bloco está nos part numbers** e é o título
que ranqueia. Resolvido nas descrições (modelo puxado do SKU), mas **a correção
de título é trabalho separado**.

### Divergência nova para o Craig

```
SKU:     HONE-DS06-102-DU**P**-LF/U
Título:  Resideo DS06-102-DU**T**-LF/U
```

Uma letra, e são referências diferentes na Resideo. Vai junto com o `802360QA`
da seção 23.

### Resultado

- **68 descrições**, mediana **1.581 chars** (contactors 1.619, aquastats 1.602,
  humidifiers 1.387)
- Checagens finais: 0 artigo errado, 0 "with" duplo, 0 palavra duplicada,
  0 sem SKU, 0 placeholder
- Arquivos: `resideo_bloco2_descricao_IMPORTAR.csv` e `_rollback.csv`

### Estado das descrições Resideo

```
607 total
121 feitas (39 iniciais + 82 valvulas de zona)
 68 prontas neste bloco, aguardando import
418 pendentes
```

### 24.1 — UPC e peso nas especificações (17/09)

O texto antigo gerado pelo pipeline trazia dois campos que eu não estava
incluindo: **UPC** e **Shipping Weight**. O UPC é dado de busca real — quem
escaneia um código na obra procura por ele.

**O peso é armadilha, e quase entrou.** Primeiro item da amostra:

```
HONE-120650/U   Heat Conductive Grease 1/2 oz   →   1,4 lb
```

Graxa de meia onça (0,03 lb) cadastrada a 1,4 lb. E 59 dos 68 pesos do bloco
estão em três valores só: **1,4 (23), 7,0 (18), 2,19 (18)** — 7,0 é o mesmo
placeholder Resideo que o TESTE A já tinha apontado.

**Mas não é placeholder puro.** Onde existe peso de fornecedor para conferir
(11 itens), **os 11 batem** — inclusive dois aquastats L6006 a 1,4 lb. O 1,4 é
o peso real da família L6006, copiado por cima da graxa. O valor está
*contaminado*, não inventado: certo em alguns, errado em outros, e pelo número
sozinho não dá para separar.

**Regra adotada:**
- **UPC: sempre** (59/68 têm) — não tem como estar "meio certo"
- **Peso: só onde o fornecedor confirma** (11/68). Nos outros 57, omitido.

Publicar peso errado numa descrição é pior do que não publicar: hoje o erro
está num campo interno; na descrição vira spec pública que o cliente lê.

Mediana subiu para **1.6xx chars**. A graxa saiu corretamente sem peso.

**Nota para os próximos blocos:** UPC existe em **408 dos 486**. O peso do
catálogo Resideo inteiro tem a mesma contaminação — 7,0 lb em 61 itens,
2,19 em 56, 0,2 em 48. Mesma regra vale.

**Correção da 24.1:** a checagem acusou "upc invalido: 59", mas era o meu
verificador: o regex `(\S+)` capturava `085267005319</li>` com a tag junto.
Revalidado com extração correta — **os 59 são UPC-A de 12 dígitos e os 59
passam no dígito verificador**. Zero inválido.

Terceiro falso positivo do meu próprio verificador hoje (os outros: pontuação
com tag removida, e o aviso de conflito do DP2020A5022 que eu não tinha
procurado no texto inteiro). **O verificador erra nas duas direções** — deixa
passar erro de fato (amperagem 04, "fixed range" falso, fan center descrito
como aquastat) e acusa erro que não existe. Ele filtra, não decide.

## 25. Bloco 3 Resideo — 36 descrições (TRV + termostatos de linha)

### O sitemap da Resideo carrega spec que a página não tem

Achado novo e reaproveitável: **o slug do sitemap traz dado que o HTML
renderizado por JS não mostra.**

```
v110d1000  →  straight-pattern-1-2-in-high-capacity-valve-46-cv-...
v110f1010  →  horizontal-angle-pattern-3-4-in-high-capacity-valve-58-cv-...
th114-a-240d → line-volt-manual-t-stat-for-electric-heat-09f-accuracy-...
t498a1810  →  brush-gold-electric-heat-thermostat-vertical-mount-...
t301920w0  →  t301920w0-thera-6-radiator-thermostat-external-sensor-...
```

**36/36 casaram no sitemap.** Saíram daí: Cv de 6 corpos V110, precisão de
0,9 °F, montagem vertical, a linha Thera-6 e 50/60 Hz.

**O slug derruba a vírgula decimal:** `46-cv` é 4,6 Cv. Confirmado pela
progressão com a bitola — **1/2" = 4,6 · 3/4" = 5,8 · 1" = 7,0**, monotônica.
Lidos como literais seriam vazões de tubo de 4 polegadas numa válvula de
radiador.

### Compatibilidade de TRV: onde o risco estava

Três padrões de rosca convivem no bloco e ligar errado seria afirmar
compatibilidade falsa:

- `T3019DAW0NA` → **Danfoss RA**
- `T301920W0`, `T3019W0NA` → **M30x1.5**
- `T104*` (High Capacity) → corpos `V110*` (High Capacity)

A cabeça Danfoss ficou **sem bloco de links** e a descrição dela diz
explicitamente que **não serve** M30x1.5 nem as séries V110/V2040 da Resideo.

80 links internos, 0 quebrado, 0 autolink.

### Polos: 7 detectados, 8 omitidos de propósito

O sufixo do part number carrega o dado: `TH115-A-120**S**` = single-pole,
`TH115-A-240**D**` = double-pole. Conferido contra a ficha: **0 divergência**.

Os 8 sem indicação no título nem no modelo ficaram **sem afirmar polo**. Polo
em termostato de linha é spec de segurança elétrica — single-pole deixa uma
perna viva no aquecedor com o termostato desligado. Chutar ali é pior que
omitir.

### Quarto falso positivo do meu verificador

Acusei erro de detecção de polo em 5 itens. Era o diagnóstico: eu testei
`"double-pole" in texto`, e o parágrafo do **single-pole** cita "double-pole"
ao explicar a diferença. Conferido pelo campo `Poles` da ficha: os 7 corretos.

Contagem do dia: o verificador errou **4 vezes para mais** (pontuação, conflito
do DP2020A5022, 59 UPCs, polos) e **3 vezes para menos** (amperagem 04,
"fixed range" falso, fan center como aquastat).

### Resultado

- **36 descrições** — TRV mediana **2.067**, termostatos **1.696**
- Arquivos: `resideo_bloco3_descricao_IMPORTAR.csv` e `_rollback.csv`

### Estado das descrições Resideo

```
607 total
121 feitas e no ar
 68 bloco 2, aguardando import
 36 bloco 3, aguardando import
382 pendentes
```

### 25.1 — Erro de artigo que eu mesmo introduzi, e que foi ao ar

O bloco 2 (#747356983, 68 updated) entrou correto em tudo que eu tinha
verificado — amperagem, polos, tiers, UPC. **Mas ele subiu com um erro de
inglês que eu criei ao corrigir outro.**

```
"...frequent cycling on an unit that short-cycles..."
"...keeps an unit that is otherwise sound out of the landfill."
```

Quando corrigi o *"a adjustable"* do bloco 2, escrevi a regra por **letra**:
`a` + vogal → `an`. Artigo em inglês vai pelo **som**. "Unit" começa com som de
consoante (/juː/), então é *"a unit"* — como "a university", "a European". A
regra por letra também quebraria "an hour" e "an honest" no sentido inverso.

**23 dos 68 foram ao ar com o erro. O bloco 3 estava limpo** só porque os
templates dele não usam a palavra "unit".

Regra reescrita para tratar `uni-`, `use-`, `user-`, `usual-`, `utili-`,
`Euro-`, `one` e `ubiqui-` como som de consoante, e `hour`/`honest`/`honor`
como vogal. Zero ocorrência nos dois blocos depois.

**Os dois CSVs foram regravados.** O bloco 2 precisa de **reimport** — as 23
páginas estão no ar com o erro agora.

**Padrão que se repete:** cada correção minha de texto introduziu um erro novo
(`{BRAND}` atributivo → `.capitalize()` em minúscula; `a adjustable` →
`an unit`). Toda correção de string precisa de releitura, não só de recontagem.

### 25.2 — Verificação ao vivo dos blocos 2 e 3 (17/09)

Import #747404754: **bloco 3, 36 updated. Verificado: 36/36 idênticos.**

**O reimport corrigido do bloco 2 NÃO saiu.** Ao vivo:

```
bloco 2: 16 iguais, 52 ainda na versao antiga
paginas Resideo com "an unit" AO VIVO: 23
```

Só o bloco 3 foi importado. O arquivo corrigido do bloco 2 tem o mesmo nome de
antes (`resideo_bloco2_descricao_IMPORTAR.csv`) — provável que só um dos dois
tenha entrado.

**Pendente: reimportar o bloco 2.**

Estado do catálogo Resideo ao vivo:

```
607 total
225 escritas  (121 + 68 bloco 2 + 36 bloco 3)
382 pendentes
```

Próximos por demanda: **Gas Valves** (36 itens, 1.500/mo) e **Gas Ignition
Components** (41, ~1.000/mo) — juntos, 77 dos 382.

### 25.3 — Reimport do bloco 2 confirmado (17/09)

Import #747407572, 68 updated. Verificado ao vivo: **"a unit" correto** nas
páginas que tinham o erro, e "an air conditioning" / "an entire" seguem certos.
O erro de artigo saiu das 23 páginas.

**Catálogo Resideo: 225 de 607 escritas, 382 pendentes.** As três levas
(121 + 68 + 36) verificadas por leitura independente.

## 26. Bloco 4 em preparo — e uma correção minha antes de escrever

### Eu quase escrevi "standing pilot" em quatro válvulas de ignição direta

Varrendo as 36 válvulas de gás contra o sitemap da Resideo, achei 4 conflitos e
**reportei como se nossos títulos estivessem errados**, chamando de "o mais
grave dos três itens para o Craig".

Era o contrário. Os quatro slugs da Resideo são **a mesma string**:

```
VR8204H1006  →  single-stage-standing-pilot-1-2-in-x-1-2-in-24-v-ac-standard-opening
VR8205A2024  →  single-stage-standing-pilot-1-2-in-x-1-2-in-24-v-ac-standard-opening
VR8205Q2787T →  single-stage-standing-pilot-1-2-in-x-1-2-in-24-v-ac-standard-opening
VR8205Q2795T →  single-stage-standing-pilot-1-2-in-x-1-2-in-24-v-ac-standard-opening
```

Quatro part numbers distintos, um slug só. É **template**, não spec.

E o conteúdo dele contradiz a própria Resideo: **VR8205 é série de direct
ignition** na numeração da Honeywell, e o slug diz standing pilot.

**Teste que resolveu:** série → tipo de ignição declarado nos nossos títulos.

```
VR8200/VR4300 = standing pilot      COERENTE
VR8204/VR8304 = intermittent pilot  COERENTE
VR8205/8215/8305 = direct ignition  COERENTE
VR8245/VR8345 = intermittent+direct COERENTE
```

**Os títulos da loja estão certos.** `VR8205Q2795T` sai da lista do Craig.

Regra nova no CLAUDE.md: **slug idêntico entre part numbers diferentes não vale
como evidência**, e a numeração de série da Honeywell serve de verificação
cruzada.

### Conteúdo duplicado que o dado não resolve

Seis igniters `Q4100C` com título idêntico — "Silicon Carbide Hot Surface
Igniter -5.25 in Lead Length" — em 9054, 9056, 9060, 9062, 9066, 9068.

**O sitemap da Resideo também não diferencia**: 5 dos 6 slugs são iguais; só o
9068 ganha o prefixo `120-volt`. O diferenciador (suporte, aplicação OEM) não
existe em fonte pública.

Vou escrever a plataforma uma vez, diferenciar pelo que é conhecido
(comprimento de cabo, 120 V no 9068, montagem redonda no 9048) e dizer que os
part numbers diferem por suporte e aplicação OEM. **Os 5 vão ficar quase
idênticos — o conserto disso é dado, não texto.** Item para o Craig.

### Lista atual para o Craig

1. `802360QA` — 277 V, nosso título diz V4043/V4044, slug diz V4043/V8044
2. `DS06-102-DUP-LF` (SKU) vs `DS06-102-DUT-LF` (título)
3. Diferenciador dos 6 igniters `Q4100C` de 5,25 in

## 26.1 — Bloco 4 gerado: 77 descrições (válvulas de gás + ignição)

- **Gas Valves 36**, mediana **1.855 chars** — aviso de segurança em **36/36**
- **Gas Ignition Components 41**, mediana **1.364 chars**
- Checagens limpas; zero fallback genérico (os 41 caíram em branch específica)

Válvulas de gás levam bloco fixo de segurança: a válvula tem que casar com o
aparelho (sistema de ignição, capacidade, pressão de entrada, tipo de gás), a
troca é serviço de técnico licenciado, e quem decide é a lista de peças do
fabricante do aparelho — não o encaixe da rosca.

O tipo de ignição saiu da **numeração de série da Honeywell**, validada contra
os títulos: a `VR8205Q2795T` está descrita como **direct ignition**, que é o
que a série manda e o que o slug templated da Resideo teria me feito errar.

### Conteúdo duplicado: o limite do que texto resolve

Os seis igniters `Q4100C` de 5,25 in saíram **99,3% a 99,5% idênticos entre si**.

Usei o slug da Resideo para separar dois: `Q4100C9068` (120 V, caiu para 97,4%)
e `Q4100C9048` (montagem redonda, 94,9%). **Os cinco do meio continuam em
99,5%**, e o `Q4100C9042` também — comprimento de cabo diferente não move o
texto o bastante.

**Isso não tem solução por escrita.** Cinco páginas quase idênticas competem
entre si no índice. Os caminhos reais são dois, e os dois são decisão do
Gabriel:

1. **Pedir o diferenciador à Resideo** (suporte, aplicação OEM) — já está na
   lista do Craig
2. **Consolidar** os cinco num produto com variantes

Canonical não serve aqui: esconderia cinco SKUs distintos da busca.

### Estado

```
607 total
225 no ar
 77 bloco 4, aguardando import
305 pendentes
```

### 26.2 — Bloco 4 importado e um erro corrigido (17/09)

Import #747425667, 77 updated. Verificado: a `VR8205Q2795T` está no ar como
**direct ignition**, que é o correto — o slug templated da Resideo teria posto
"standing pilot" numa válvula de ignição direta.

**Erro encontrado na verificação:** *"with a **-5.25** in lead"* e
`Lead length: -5.25 in`. Comprimento negativo, em **9 páginas de igniter**.

Causa: o título é *"Igniter -5.25 in Lead Length"* e meu regex
`([\d./-]+)\s*in\s*Lead Length` incluía o hífen na classe de caracteres, então
capturava o traço separador junto com o número.

Corrigido, e a captura fracionária (`19-1/8 in`) continua funcionando.
**CSV regravado — precisa de reimport.**

**Erros deste bloco pegos só na verificação ao vivo, não nas checagens:** o
comprimento negativo passou por todas as checagens automáticas porque
`-5.25 in` é string bem formada.

## 27. Peso dimensional: o furo que λ não fecha sozinha (17/09)

### Gatilho: #THS1041

Franke Cube `FRAN-CUX11030`, pia undermount 31,5 × 17,7 in, **$643,42**, frete
grátis. Peso cadastrado **20,25 lb** — peso real, não placeholder.

**Pelo peso real ele passa:** teto λ a $643,42 é 21,68 lb, e 20,25 < 21,68.
Passou com 7% de folga.

**Pelo volume não.** A régua é `peso_efetivo = max(peso real, peso dimensional)`.
Só a cuba, sem caixa: 31,5 × 17,75 × 9 = 5.032 in³ → **36,2 lb**. Falha por
**1,7×** na leitura mais conservadora possível.

Primeiro caso do dia em que o peso real passa e o dimensional reprova. É
exatamente o furo que o CLAUDE.md nomeia.

### Fonte de dimensão nova: `custom.specifications`

Metafield que nunca tinha sido usado. Existe em **13.141 de 14.883** produtos
(88,3%), mas quase sempre com `Type`, `Size`, `Material`. Dimensão utilizável
em **546**, dos quais **266 não tinham** `product.length/width/height`.

Chaves que valem: `Length`, `Width`, `Height`, `Depth`, e para pia também
`Large Bowl Depth` / `Sink Basin Depth` — foi essa última que fez o Franke
aparecer, e sem ela a varredura passava batido nele.

**Fração em polegada** (`25-9/16"`, `6-9/16"`) exige parser próprio; a leitura
ingênua devolvia `16`.

### 31 pias fora do frete grátis — aplicado e verificado

**$19.661,71.** Dayton 18, Franke 10, mais Blanco, Elkay e Mustee.

```
MUST-14K    tanque de lavanderia 23x25x33 in   136,5 lb dim   teto 2,96   46x
DAYT-D-23322-4                                  34,3 lb dim   teto 13,29  2,6x
FRAN-CUX11030 (o do THS1041)                    36,2 lb dim   teto 21,68  1,7x
```

O Mustee a **46×** é o caso extremo: item de $87,81 que ocupa 11 ft³.

### Achado: perfil e tag divergiam em 12 dos 31

Na releitura ao vivo, **12 já estavam em THS Standard mas seguiam com a tag
`free-ship-eligible`**. Como a elegibilidade mora na tag e é ela que o app de
frete lê, esses 12 podiam estar dando frete grátis com o perfil correto.

**Vale varrer essa divergência no catálogo inteiro** — não foi feito ainda.

### CSV de dimensões: 254 produtos, Grohe excluída

`dimensoes_do_spec_IMPORTAR.csv` — 254 produtos ganham
`product.length/width/height` a partir do `custom.specifications`.

**A Grohe foi excluída inteira** (12 itens, em
`dimensoes_grohe_SUSPEITO_MM.csv`). Motivo: o `wall-union` (Grohe 26635GN0,
conexão de parede) traz "Height 64", Length 90", Width 50"" — que em mm dá
3,5 × 2 × 2,5 in, o tamanho real da peça. **São milímetros com aspas de
polegada.**

Mas é **misto**: os outros 11 Grohe têm valores plausíveis em polegada. Não dá
para separar item a item pelo número, então os 12 saíram. Onze bons ficaram de
fora para evitar um ruim — numa fonte única de verdade de frete, errar para
menos é o certo.

### Pendências abertas daqui

1. **53 produtos acima de 10 ft³** no CSV — degrau do *Large Package Surcharge*
   da UPS, o mesmo que custou $331 na THS1008. São box de acrílico de peça única
   (60 × 36 × 77 in = 96 ft³), reais. **Não verifiquei se estão em frete grátis.**
2. **Divergência perfil × tag** no catálogo inteiro
3. **Grohe em mm** — perguntar ao fornecedor ou corrigir no import
4. `GROH-26.635GN0` está com **preço $0,00**

### 27.1 — Os 52 acima de 10 ft³: nada errado (17/09)

Verificado ao vivo em amostra de 20 dos 52: **16 em THS Freight & Oversize,
4 em THS Standard, zero com a tag `free-ship-eligible`, zero em General
profile.**

São box de acrílico Maax de peça única (60 × 36 × 77 in = 96 ft³), paredes de
chuveiro Mustee, banheiras Bootz. **49 dos 52 passam ao mesmo tempo dos 130 in
de comprimento+cintura e dos 150 lb de peso dimensional** — UPS Ground não
aceita nenhum deles.

**Primeiro bloco do dia em que eu abro e não acho nada errado.** A classe mais
óbvia de risco já estava resolvida.

**Ressalva, e não é vazamento de dinheiro:** os 4 em THS Standard
(`MUST-247WHT` $441,06, `BOOT-011-3302-00` $405,64, `MUST-17FK` $143,97 e mais
um) estão num perfil que cota **UPS + 65%**, e esses itens estouram o limite
físico da UPS. Não dão frete grátis, mas oferecem no checkout uma transportadora
que vai recusar o volume. É erro de cotação, não de margem — deveriam estar em
Freight & Oversize junto com os outros 48.

## 28. Divergência tag × perfil no catálogo inteiro (17/09)

Varredura dos 14.883 pela relação `ProductVariant.deliveryProfile`:

```
 8.350  tag SIM / General profile          <- coerente
 5.366  tag NAO / THS Standard             <- coerente
   787  tag NAO / THS Freight & Oversize   <- coerente
   267  tag SIM / THS Standard             <- DIVERGENTE
    76  tag SIM / THS Freight & Oversize   <- DIVERGENTE
    37  tag NAO / General profile          <- divergente, mas soma $0,36
```

**343 divergências que importam, $111.759,68 de catálogo.** Moen 74, Delta 36,
Legend Valve 29, Charlotte Pipe 27, Milwaukee Tools 22.

Os 37 do outro sentido somam **$0,36** — produtos de preço zero ou centavos.

Arquivo: `divergencia_tag_perfil.csv`.

### Não consigo decidir qual vence, e não vou fingir que consigo

O CLAUDE.md diz que a elegibilidade mora na tag, mas isso descreve como cada
campo é **escrito**, não qual **vence no checkout**.

Cruzei os 343 com os 11 SKUs que efetivamente venderam nos últimos 30 pedidos:
**nenhum dos vendidos está na lista.** O histórico não testa a hipótese.

O que os pedidos provam é que o perfil funciona **quando não há conflito**:

```
THS1028  Maax shower  $1.256,50  ->  Freight 70 to 150 lb $349,00   (Freight, sem tag)
THS1026  Navien       $3.015,00  ->  UPS Ground $918,03             (Standard, sem tag)
THS1032  termostato   $  828,30  ->  Free shipping $0               (General, com tag)
```

**As duas hipóteses:**

- **Perfil vence:** os 343 já cobram certo, a tag é sujeira. Higiene, não urgência.
- **Tag vence:** $111.759,68 oferecendo frete grátis com perfil pago, incluindo
  **76 itens em Freight & Oversize** — justamente os volumosos.

**Teste que o Gabriel faz em 30 segundos e eu não consigo fazer:** colocar um
dos 343 no carrinho e ver o que o checkout oferece. Se aparecer "Free shipping
over $99", a tag vence e é urgente. Se aparecer UPS Ground, o perfil vence.

## 29. Bloco 5 — 74 descrições (PRV + mixing valves)

### Eu tinha descartado a maior oportunidade que restava

Em 17/09 medi `pressure reducing valve **boiler**` — **40/mo** — e concluí que
a família de 32 PRVs não valia a pena. Errado por um fator de ~500:

```
pressure reducing valve    5.400/mo  KD  7
water pressure regulator  16.000/mo  KD 12
```

**21.400 buscas/mês somadas.** Usei uma cauda longa como proxy da cabeça e
quase pulei a maior família restante do catálogo.

Demanda medida dos tipos que faltavam:

| Família | Itens | Demanda/mês | KD |
|---|---|---|---|
| **Pressure Reducing Valves** | 32 | **21.400** | 7–12 |
| Thermocouples & Thermopiles | 11 | 4.600 | 0 |
| Thermostat Accessories | 20 | 4.000 | 0 |
| Mixing Valves (todas) | 42 | 2.800 | 0–2 |
| Relays + Switching Relays | 24 | 2.200 | 0 |
| Transformers | 14 | 2.000 | 0 |
| Non-Programmable Thermostats | 16 | 1.800 | 0 |
| Leak Detection Valves | 9 | 1.320 | 14–22 |
| Air Cleaners & Filters | 24 | 500 | 0–15 |

`thermopile` sozinho faz **3.900/mo KD 0** em 11 produtos — a melhor razão
demanda por item da lista.

### Resolve o item 2 da lista do Craig

```
SKU:    HONE-DS06-102-DUP-LF/U
Titulo: "DS06-102-DUT-LF/U 1" DialSet Press Double Union PRV"
```

Na nomenclatura DS06 o sufixo é a conexão: `T` threaded, `S` sweat, `P` press.
O título **repete o número DUT mas descreve uma válvula Press**. O SKU está
certo, o título tem o part number errado e a descrição certa. **Erro de
digitação nosso, não ambiguidade da Resideo.** Vira correção de título.

### Segurança: as 6 válvulas heat-only

`AM101R` e `AM102R` (6 itens) são da série **R, para loop hidrônico** — não
para água potável. As descrições dizem isso explicitamente e a ficha traz
*"Heat-only mixing valve (not for potable water)"*.

**Erro pego na leitura:** a frase de abertura dessas 6 dizia *"lead-free
thermostatic mixing valve"*. Lead free existe por causa de potável — chamar
assim uma válvula que não é para potável é enganoso. Eu tinha suprimido o
parágrafo de lead-free mas esquecido da abertura. Corrigido para *"for hydronic
heating service"*.

**Terceiro erro de sigla do dia:** `.capitalize()` transformou `NPT` em `Npt` no
campo de conexão. Mesmo padrão do "honeywell home" e do `-5.25 in`.

### Resultado

- **74 descrições** — PRV mediana **2.096**, mixing valves ~1.550
- Checagens limpas; 6 heat-only marcados; 9 com a designação 1070
- Arquivos: `resideo_bloco5_descricao_IMPORTAR.csv` e `_rollback.csv`

### Estado

```
607 total
302 no ar
 74 bloco 5, aguardando import
231 pendentes
```

### 29.1 — Bloco 5 importado e verificado (17/09)

Import #747500543, 74 produtos. Verificado ao vivo na `AM101R-US-1`, que é uma
das 6 de segurança:

- abre com *"for **hydronic heating** service"*
- traz *"**not** for potable water"* em negrito no corpo
- ficha: `Type: Heat-only mixing valve (not for potable water)`
- **sem "lead-free" em lugar nenhum**

**Inconsistência cosmética anotada:** o campo `Connection` sai `sweat` em
minúscula ao lado de `NPT` e `ProPress`, que são maiúsculas por serem nome
próprio. Correto, mas desalinhado. Corrigir no próximo bloco, não vale reimport.

### Estado das descrições Resideo

```
607 total
376 no ar
231 pendentes
```

### Fila por demanda para o bloco 6

| Família | Itens | Demanda/mês |
|---|---|---|
| Thermocouples & Thermopiles | 11 | 4.600 |
| Thermostat Accessories | 20 | 4.000 |
| Relays + Switching Relays | 24 | 2.200 |
| Transformers | 14 | 2.000 |
| Non-Programmable Thermostats | 16 | 1.800 |

`thermopile` sozinho faz 3.900/mo KD 0 em 11 produtos — melhor razão demanda
por item de tudo que restou.

**Ressalva sobre Thermostat Accessories:** os 4.000/mo vêm de `thermostat wire`.
**Não confirmei que os 20 itens dessa família são fio** — podem ser placa de
parede e adaptador, e aí a demanda não é deles. Verificar antes de priorizar.

---

## §30 — Bloco 6 Resideo: 65 descrições (thermocouples, relays, transformers, non-programmable)

Arquivos: `resideo_bloco6_descricao_IMPORTAR.csv` + `resideo_bloco6_descricao_rollback.csv`.
Matrixify: Products / Body HTML, `Command: UPDATE`. Rollback tem o HTML anterior
dos 65 (nenhum veio vazio; média de 339 chars, o texto auto-gerado de sempre).

```
 16  Non-Programmable Thermostats     mediana 2.152
 14  Transformers                     mediana 1.554
 13  Relays                           mediana 1.188
 11  Switching Relays                 mediana 1.355
 11  Thermocouples & Thermopiles      mediana 1.423
min 870 · max 2.508 · 11 com link interno
```

**Thermostat Accessories ficou fora com razão.** Verifiquei a família: 10 placas
de cobertura, 2 guardas de termostato, 3 sensores, um range stop, um jogo de
chaves e um adaptador WireSaver de fio C. **Não é fio.** Os 4.000/mo de
`thermostat wire` não pertencem a ela. Anotado de passagem: `AT120B1028` é
transformador cadastrado como thermostat accessory.

### Erros pegos na leitura (o verificador automático deu LIMPO nos três)

1. **`T4398A1021`** — título *"Electric Heat Thermostat … Baseboard"* é line
   voltage, mas o regex exigia `120|277 V` **e** o nome da aplicação. Sem os
   volts, o item recebeu o parágrafo do **fio C** e o do **heat anticipator** —
   os dois falsos num stat de linha: não tem 24 V, não tem anticipator, não tem
   comum. `T4398B1029` caía no mesmo buraco pelo outro lado (tinha os volts, não
   tinha o nome). Regra nova: volts **ou** `Electric Heat|Baseboard|Line Volt`.
2. **`RC840`** — título diz *"Without Transformer"* e a descrição ignorava. É a
   pegadinha de compra da família: `RC840T-120` e `RC840T-240` são o mesmo relé
   **com** trafo. Agora tem parágrafo próprio, ficha `Internal transformer: No`
   e link cruzado nos dois sentidos.
3. **`AT150F1022` / `AT72D1683`** — saíam *"50 VA, multi mount mount"*: o campo
   já é "Multi Mount" e o gerador concatenava " mount" de novo.
4. `Category` dos Switching Relays saía como `Relays`; passou a usar o
   `productType` real.

**O `Connection` do §29.1 não se aplica aqui** — nenhum item do bloco 6 tem esse
campo. Fica para o bloco que tiver.

### Links internos (11)

`RC840` ↔ `RC840T-120`/`RC840T-240` · `TH5320R1002` ↔ `YTH5320R1000` ·
stats millivolt (`TS812A1007`, `T827K1009`) → termopilhas `Q313A1188`/`Q313A1139`
· termopilhas → stat millivolt. Todos apontam para handle do próprio bloco.

### Estado das descrições Resideo

```
607 total
376 no ar
 65 neste CSV
166 pendentes depois deste
```

---

## §31 — Bloco 7 Resideo: 53 descrições (ar — filtros, dampers, painéis, RedLINK)

Arquivos: `resideo_bloco7_descricao_IMPORTAR.csv` + `resideo_bloco7_descricao_rollback.csv`.
Matrixify: Products / Body HTML, `Command: UPDATE`.

```
 24  Air Cleaners & Filters               mediana 1.518
  9  Zone Dampers                         mediana 1.757
  8  RedLINK Accessories                  mediana 1.888
  6  Forced Air Zone Panels               mediana 2.800
  4  Ventilation Controls & Accessories   mediana 1.204
  2  Bypass Dampers                       mediana 1.172
min 871 · max 3.342 · 20 com link interno
```

### Mudança de método: a fonte passou a ser o metafield da própria loja

Os 53 têm `custom.specifications` preenchido, e ele é **mais rico que o sitemap
da Resideo**. O sitemap não discrimina os painéis (os três slugs são
`truezoner-hzXXX-panel`); o metafield dá zonas e estágios exatos:

| | Zonas | Estágios |
|---|---|---|
| HZ311 | 3 | 1 Heat / 1 Cool |
| HZ322 | 3 | 2 Heat / 2 Cool |
| HZ432 | 4 (expansível a 32 com painéis TAZ-4H) | 3 Heat / 2 Cool |

E o campo **`Used With` / `Includes` / `Replacement Filters` virou o gerador de
link interno** — evidência da loja, não inferência de slug. Dos 20 links, 6
saíram de casamento por **dimensão** entre a mídia de reposição e o gabinete
(`Dimensions` dos dois lados), que é o único caminho porque o `Used With` da
mídia é prosa sem part number.

### Demanda medida (Ahrefs, us)

`redlink` 1.300/mo KD 0 · `air separator` 1.000 KD 1 · `zone damper` 450 KD 1 ·
`automatic air vent` 450 KD 0 · `whole house air cleaner` 350 KD 15 ·
`bypass damper` 300 KD 0 · `honeywell air cleaner` 250 KD 2 ·
`thermostat wall plate` 200 KD 0.

**`furnace air filter` faz 2.100/mo com KD 96 — não é nossa, não mirar.** O
ganhável em Air Cleaners é part number, `media air filter` (100, KD 0) e
`honeywell air cleaner` (250, KD 2).

### Erros pegos antes de gerar o CSV

1. **Bug de tupla, o pior do bloco.**
   ```python
   MERVP=('<p>...</p>'
    '<p>...</p>')        # parênteses = concatenação, é UMA string
   b.append(MERVP[0]+MERVP[1])   # -> "<p"
   ```
   `MERVP[0]` é o caractere `<`. Os dois parágrafos sobre MERV **nunca
   entraram** em 20 itens e sobrou `<p<p>` no HTML. O mesmo em `RLP` nos 8
   RedLINK. **O teste de balanceamento passou** porque `<p<p>` tem um `<p>` e um
   `</p>`. Só apareceu lendo o HTML cru. Check novo: `<(?!/?(p|ul|li|strong|em|a)[ >])`.
2. `Terminals: Terminals: M1-Power…` — o valor do spec já começa com o rótulo.
3. `16 in. x 20 in.` virava `16in x 20in` — o regex comia o espaço, não o ponto.
4. HZ432K repetia "4 Zones (expandable to 32…)" **três vezes** no mesmo texto.
5. `10 in Diameter round` — redundante e com maiúscula no meio da frase.
6. `Voltage: 24V` na ficha contra "24 V" no corpo.

### Conflito de dados anotado (não corrigido)

Os dampers `ARD*` têm `Motor: Power closed, spring open` e
`Motor Timing: 30 seconds power open/10 seconds spring return` — **os dois
campos se contradizem na direção**. Usei só o `Motor` (que bate com o ARD ser
normalmente aberto) e **omiti os tempos**. Conferir com o Craig.

### Intrusos na família Air Cleaners & Filters

`S688A1007` é **sail switch** (prova de fluxo) e `UV2400U1000`/`UV2400XLAM1` são
**UV** (tratamento, não filtragem). Ganharam branch própria e `Category` fora de
filtros. A família em si é legítima — ao contrário do que eu suspeitava de
Thermostat Accessories no §30.

### Estado das descrições Resideo

```
607 total
441 no ar (após bloco 6)
 53 neste CSV
113 pendentes depois deste
```

**Bloco 8 (hidrônico), 30 itens:** Air Separators 12 + Boiler Trim Kits 7 +
System Fill Tanks & Autofills 6 + Hydro Separators 3 + Air Vents 2.

---

## §32 — 26 títulos Resideo sem part number (+ 4 com part number ERRADO)

Arquivos: `resideo_titulos_IMPORTAR.csv` (26) + `resideo_titulos_rollback.csv`,
e `resideo_pn_errado_seo_IMPORTAR.csv` (4) + `resideo_pn_errado_seo_rollback.csv`.
Matrixify: Products. Importar **o de títulos primeiro**.

Não são 26 do mesmo caso:

- **22 sem part number nenhum** — aquastats L4008/L6006/L6008, válvulas de gás
  VR/SV, pilot burners Q3450, o kit de conversão 395253-1 e o YTHX9421R7001WW.
  Correção: inserir o PN logo depois de "Resideo", que é o padrão dominante da
  loja. Maior título resultante: 163 chars.
- **4 com o part number ERRADO no título**, e nos quatro o **SKU é que está
  certo**:

| SKU | Título dizia | Evidência |
|---|---|---|
| `DS06-102-DUP-LF` | `DS06-102-DUT-LF/U` | slug `…-dup-lf-u` = **press** double union; `dut` = NPT fêmea, `dus` = sweat |
| `VB-SP02Y-003` | `VB-SP02Y-002` | slug `-003` = **power adaptor**; `-002` = replacement actuator |
| `PV125S` | `PV125/U` | slug `pv125s` = **sweat**; `pv125` = NPT |
| `PV150P` | `PV150/U` | slug `pv150p` = **press** |

Desta vez **os slugs discriminam** (part number diferente → slug diferente →
produto diferente), então valem como evidência — ao contrário das quatro
válvulas de gás do §29. E o próprio texto do nosso título confirma de forma
independente: "Press", "Sweat", "Power Adapter". Duas fontes concordando.

### O PN errado tinha propagado

Nos 4, o part number errado não estava só no título — estava também em
`seo.title`, `seo.description` e no `alt` da imagem:

```
PV125S  title: Resideo PV125/U 1-1/4" SuperVent Air Eliminator Sweat
        seo_t: Resideo PV125/U 1-1/4" SuperVent Air Eliminator Sweat
        seo_d: ... MPN PV125/U.
        alt  : 1-1/4" SuperVent Air Eliminator Sweat
```

Corrigir só o título deixaria part number errado em três campos indexados.
O CSV de SEO cobre `seo.title` e `seo.description`. **O `alt` dos 4 sai por
API**, não está em CSV.

### Nos outros 22 o MPN já estava no `seo.description`

Todos os 22 já trazem `"MPN L4008A1130/U."` na meta description — o part number
já é indexável. O que falta é ele no **título visível**, que é o H1 e o anchor
interno.

### Achado fora do escopo, anotado

Vários `seo.title` estão **truncados no meio da palavra**:
`"Resideo Single Stage LP to Natural Gas Conversion Kit, 5"` e
`"Resideo Pilot Burner, C- Mounting Bracket"` (comeu o "C-Style"). Parece corte
cego por comprimento no pipeline de import. Medir a extensão disso no catálogo
inteiro antes de propor conserto.

---

## §33 — Bloco 8 Resideo: 30 descrições (hidrônico)

Arquivos: `resideo_bloco8_descricao_IMPORTAR.csv` + `_rollback.csv`.

```
 12  Air Separators                 mediana 2.146
  7  Boiler Trim Kits               mediana 2.584
  6  System Fill Tanks & Autofills  mediana 1.942
  3  Hydro Separators               mediana   906
  2  Air Vents                      mediana 1.382
min 894 · max 2.629 · 7 com link interno
```

Os 7 links saem do campo `Includes` dos trim kits, que declara o conteúdo em
part number: `TK300-30, PV125S, SCV-050, NK300S-100` — três dos quatro são
produtos nossos.

### Erro pego na leitura

`PV-020RP` recebeu *"Universal fit across the SuperVent range"* porque o
`Connection Type` do metafield diz `Universal`. **O título diz
`(New Style 90 Degree)`** — as tampas do SuperVent mudaram de desenho e não são
intercambiáveis. Afirmar encaixe universal ali geraria devolução. Agora o texto
declara o estilo e manda casar com o que sai do corpo. O `PV-001RP`, cujo título
não contradiz, manteve o `Universal`.

Também corrigido: `Pipe Size` do `VF06-100-SUSUT` vinha malformado
(`"1/2 in. Inlet Size-- 1/2 in."`) e vazava pra frase de abertura; e
`Maximum temperature: 240 F Maximum`, com o rótulo repetido no valor.

### Duas famílias mal classificadas

- **Hydro Separators (3)** não são separadores — são **adaptadores de união NPT**
  (`Used With: HYDROSEP-104-U`). Recategorizados no texto como Hydronic
  Accessories; o `productType` na loja continua errado.
- **`PA404A1025` / `PA404A1033`** são **Pressuretrol**, controle de pressão de
  caldeira a vapor, arquivados em "System Fill Tanks & Autofills". A diferença
  entre os dois é real e vale descrever: diferencial **subtrativo** (cut-in é o
  ajuste, religa no ajuste menos o diferencial) contra **aditivo** (cut-out é o
  ajuste mais o diferencial). Mesmos números nas duas versões dão ciclos
  diferentes.

---

## §34 — Peso: 18 divergências achadas pelo metafield, 5 vazando frete grátis

Arquivos: `b8_peso_IMPORTAR.csv` (18) + `b8_peso_rollback.csv`,
`b8_tag_remover_IMPORTAR.csv` (5) + `b8_tag_restaurar_MATRIXIFY.csv`,
`b8_perfil_rollback.csv`.

O `custom.specifications` traz `Weight (lb)` do fabricante em 21 dos 30 itens do
bloco 8. Cruzado com o peso registrado: **18 divergem**.

**Os 7 boiler trim kits estão todos registrados em 2,19 lb** — valor da lista de
placeholders conhecidos — contra 16 a 19,2 lb declarados. Subregistro de 14 a
17 lb.

λ recalculado do dado bruto, preço lido ao vivo:

| SKU | preço | reg. | real | λ reg. | λ real | |
|---|---|---|---|---|---|---|
| TK30PV100SFM | $402,42 | 2,19 | 16,0 | 0,0054 | **0,0398** | vaza |
| TK30PV100SNK | $481,05 | 2,19 | 19,2 | 0,0046 | **0,0399** | vaza |
| TK30PV125FM | $416,72 | 2,19 | 16,8 | 0,0053 | **0,0403** | vaza |
| TK30PV125SFM | $416,72 | 2,19 | 16,8 | 0,0053 | **0,0403** | vaza |
| TK30PV125SNK | $493,78 | 2,19 | 19,2 | 0,0044 | **0,0389** | vaza |
| TK30PV100PNKP | $490,35 | 2,19 | 16,0 | 0,0045 | 0,0326 | passa |
| TK30PV125PNKP | $517,10 | 2,19 | 16,0 | 0,0042 | 0,0309 | passa |

**5 de 7 vazam; 2 passam porque o preço compra folga.** 16 lb reprova a $402 e
aprova a $490. É a mesma lição do Diablo/Milwaukee: ranquear por peso engana,
só λ decide. Custo UPS estimado nos que vazam: **$87 a $102 por remessa**, com
frete cobrado $0,00. Todos os 18 estão no General profile com
`free-ship-eligible`.

**Os 11 da família PV passam mesmo com o peso real.** O `PV150P` sobe de 2,50
para 6,10 lb e λ vai só a 0,0171. Corrigir o peso deles é precisão de cotação,
não vazamento. O `PV125S` está **super**registrado (6,00 contra 3,50 reais).

Ordem de importação: **peso primeiro**, depois tag. Perfil dos 5 (General →
THS Standard) sai por API, não por Matrixify.

**Método novo que isso abre:** o `custom.specifications` tem `Weight (lb)` em
546+ produtos do catálogo. Vale rodar o mesmo cruzamento no catálogo inteiro —
é peso do fabricante contra peso registrado, sem depender da planilha do
fornecedor.

### Estado das descrições Resideo

```
607 total
494 no ar (após bloco 7)
 30 neste CSV
 83 pendentes depois deste
```
