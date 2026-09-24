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

---

## §35 — 9 `seo.title` sem part number, reescritos

Arquivos: `resideo_seo9_IMPORTAR.csv` + `resideo_seo9_rollback.csv`.
Matrixify: Products, colunas `SEO Title` e `SEO Description`.

Depois do §32 os 26 títulos visíveis ficaram com o part number, mas **9 dos 26
`seo.title` continuavam sem ele**, e vários estavam truncados no meio da frase —
corte cego por comprimento no pipeline de import:

```
"Resideo Single Stage LP to Natural Gas Conversion Kit, 5"
"Resideo Standard 2-Stage Opening SmartValve, Intermittent"
"Resideo Two Stage Gas Controls for Direct Spark Ignition"
"Resideo Prestige® 2-Wire IAQ Kit with high definition color"
```

As `seo.description` dos mesmos 9 estavam truncadas igual (`"…, includes."`,
`"…, contacts."`, `"…1/2 in x 1/2."`), então reescrevi os dois campos, não só o
título. Novos: título 47 a 55 chars, description 132 a 158 — dentro do que o
Google mostra sem cortar, com o part number nos dois.

### Correção de um erro meu no §32

Eu registrei que o part number errado tinha propagado para o `alt` da imagem nos
4. **Não tinha.** Os quatro `alt` não têm part number nenhum — nunca tiveram o
errado. Não existe defeito a consertar no `alt`; pôr o PN lá é melhoria
opcional. O `seo.title` e a `seo.description` estavam mesmo errados e foram
corrigidos.

### Correção de escala do §34

Eu escrevi que o `custom.specifications` tinha peso em "546+ produtos". **546 era
a contagem de produtos com chave de _dimensão_**, de trabalho anterior. Peso é
bem menos:

```
407 produtos com peso do fabricante utilizável
  312  Weight                (unidade dentro do valor)
   39  Weight (lb)
   28  Boiler weight
   19  Overall Weight (lbs)
    3  Shipping weight
    3  Weight (oz)
    2  Product Weight
    1  Weight, valor "105 Lbe" (typo de Lbs)
```

**Ressalva de método para os 28 `Boiler weight`:** é peso **seco**, não de
remessa. Caldeira engradada pesa mais. Para esses o spec é piso, não valor —
registrado abaixo do spec é erro certo; acima não conclui nada.

---

## §36 — Cruzamento de peso no catálogo inteiro: 8 vazamentos reais, não 18

Método: `bulkOperationRunQuery` puxou peso e preço ao vivo dos 14.883 (29.766
linhas JSONL, salvo em `wd/bulk_w.jsonl` — reutilizável). Cruzado com o peso do
fabricante no `custom.specifications`.

```
402 comparáveis
155 divergem mais de 0,05 lb
 81 subregistrados   (registrado < fabricante)
 74 superregistrados (registrado > fabricante)
```

### λ apontou 18 "vazando". Só 8 são.

**A tag é que decide, não o peso.** Dos 18 que mudam de lado no λ:

| | itens | situação |
|---|---|---|
| `free-ship-eligible` + General profile | **8** | **vazamento real, $12.290,69** |
| tag + Freight & Oversize | 1 | é o caso dos 343 do §"tag x perfil", pendente do teste de carrinho |
| sem a tag | 9 | peso errado, **vazamento nenhum** |

Os 8 reais: os 5 trim kits `HONE-TK30PV*` já conhecidos do §34, mais **três
Navien NPF700** a $2.940–3.570 registrados em **2,19 lb** com peso real de
**145 a 167,6 lb**.

Os 9 que **não** vazam: `ZILM-ZFT8R/18R` e os seis `RHEE-RTG/RTGH-95*` estão em
THS Standard sem a tag; o `RHEE-GHE100SU-300ANG` de 810 lb está em Freight &
Oversize sem a tag. Eu os havia listado como vazando antes de ler a tag —
errado, e era o risco que eu mesmo tinha sinalizado.

**λ é a régua errada acima do teto da UPS.** Aplicar λ a um item de 810 lb é
artefato: ele nunca vai por UPS. Acima de 150 lb a pergunta é de perfil, não de λ.

### Achado novo: item em UPS acima do limite físico

`NAVI-NPF700-100H5CH` e `-100U5CH` pesam **167,6 lb**, estão no **General
profile** com `free-ship-eligible`, e passam do **teto de 150 lb por volume da
UPS Ground**. Não é frete subcobrado — é cotação que a UPS não aceita. Mesma
classe dos 4 que já estavam anotados no THS Standard.

### O placeholder 2,19 lb é sistemático

Dos 81 subregistrados, **14 têm peso registrado igual a um placeholder
conhecido**, e **10 deles são exatamente 2,19**: os 7 trim kits e os 3 Navien.
Confirma que 2,19 não é medida, é valor de preenchimento do pipeline.

### Arquivos

| arquivo | o quê |
|---|---|
| `peso_fabricante_IMPORTAR.csv` (30) + `_rollback` | correção só onde a fonte é peso de remessa ou onde o registrado é placeholder |
| `navien_tag_remover_IMPORTAR.csv` (3) + `_restaurar` | remove `free-ship-eligible` dos 3 Navien |
| `peso_ambiguo_REVISAR.csv` (46) | fonte é a chave `Weight`, que **pode ser peso do produto e não de remessa**. Não corrigir às cegas |
| `peso_superregistrado_REVISAR.csv` (74) | registrado acima do fabricante — superestima cotação. `RHEE-ELDS30-FTB-208` tem 350 lb registrados contra 105 no metafield |
| `peso_caldeira_SECO_REVISAR.csv` (28) | `Boiler weight` é peso **seco**. Registrado abaixo dele é erro certo; acima não conclui |

Ordem: **peso primeiro, depois tag.** O perfil dos 3 Navien (General → Freight &
Oversize, porque 145–167 lb passa do teto da UPS) sai por API.

**O que o cruzamento NÃO cobre:** só 402 dos 14.883 têm peso de fabricante no
metafield. Os outros 14.481 continuam sem segunda fonte — para eles o detector
que funciona segue sendo preço por libra (mediana $95,9/lb).

---

## §37 — Perfil dos 3 Navien NPF700 movido por API (feito e verificado)

`General profile` → `THS Freight & Oversize` (94651809895).

```
NAVI-NPF700-060U3BH  $2.940,00  145,0 lb  verificado
NAVI-NPF700-100H5CH  $3.570,00  167,6 lb  verificado
NAVI-NPF700-100U5CH  $3.570,00  167,6 lb  verificado
```

IDs buscados por handle imediatamente antes da mutação, não de memória.
Rollback comitado antes (`navien_perfil_rollback.csv`, com product_id,
variant_id e o perfil anterior). Verificado por leitura independente da
relação `ProductVariant.deliveryProfile`, não pelo filtro de busca.

Motivo por item: os dois `-100` pesam **167,6 lb e passam do teto de 150 lb por
volume da UPS Ground** — não é frete subcobrado, é cotação que a UPS recusa. O
`-060` pesa 145 lb, cabe na UPS, mas custaria ~$669 em UPS Ground contra ~$980
de margem bruta na order.

### ATENÇÃO: os 3 continuam com a tag `free-ship-eligible`

A verificação confirma perfil novo **e tag antiga** nos três. Enquanto o
`navien_tag_remover_IMPORTAR.csv` não for importado, eles ficam exatamente no
estado dos 343 divergentes: tag dizendo grátis, perfil dizendo frete. **Mudar o
perfil sozinho não fecha o vazamento** — quem decide no checkout é a tag, lida
pelo app de frete.

---

## §38 — Bloco 9 Resideo: 83 descrições, a cauda inteira. Resideo fechado.

Arquivos: `resideo_bloco9_descricao_IMPORTAR.csv` + `_rollback.csv`.

```
 20  Thermostat Accessories             11  (várias famílias de 1 e 2 itens)
  9  Leak Detection Valves               5  Water Filters
  8  Fan Coil Zone Valves                5  Fan & Limit Controllers
  7  Oil Burner Controls                 4  Programmable Thermostats
  6  Smart Thermostats                   4  3-Way Zone Valve
mediana 1.321 · min 777 · max 2.517 · 35 com link interno
```

19 famílias, 10 delas com 1 ou 2 itens. Como é o último bloco, fiz tudo de uma vez.

### O que o spec resolveu e o slug não resolveria

- **A família Fan Coil é definida pela ação, não pelo tamanho:** `VU52` =
  **normally open**, `VU53` = **normally closed**, `VU54` = três vias diverting.
  Todas 1/2 in, mesma Cv, títulos quase idênticos. Trocar uma pela outra inverte
  o que a zona faz quando o atuador perde energia. E todas trazem
  `Actuation: Must be purchased separately` — o corpo vem **sem atuador**, que é
  a pegadinha de compra da família e não está no título.
- **`Used With` ligou meio bloco:** o cad cell `C554A1463` lista
  `R8184, R7284` — os primários de óleo deste mesmo bloco; o `TH9320WF5003` traz
  `Used With: THP9045 Wire Saver` e o WireSaver traz o inverso; o `C7089U1006`
  lista o `HZ432`, do bloco 7. Dos 35 links, a maior parte saiu daí.

### Erros pegos

1. **Bug de parsing no `mdl()`.** A função tirava tudo depois da barra,
   assumindo que barra é sempre o sufixo `/U`. Em `ES06F-1/2A` e nos quatro
   `VWS02Y-1/2`, `-3/4`, `-11/4` **a barra é parte do tamanho** — o part number
   saía truncado como `ES06F-1`. Passou a tirar só sufixo de **uma letra**
   (`/U`, `/B`, `/C`).
2. **`.lower()` em valor com nome próprio — a quarta vez desta mesma classe.**
   Saíram `"type r bracket"` (era Type R), `"a, b, e, j and p mounting
   brackets"` (era A, B, E, J, P) e `"l5 actuator"` (era L5). Antes já tinham
   sido `Npt`, `Honeywell Home` minúsculo e `NPT`.
   **Parei de remendar caso a caso** e escrevi um helper:

   ```python
   def low(v):
       """minusculiza só palavra comum: preserva SIGLA, letra isolada e código com dígito."""
   ```
   Todo `.lower()` sobre valor de spec passou a usar ele. Check novo no
   verificador: `Npt|Upc|Spdt|Spst|Epdm|Merv|Csa|Nec`.
3. `"45 sec.."` — o valor do spec já terminava em ponto. E `--` dentro de
   `Electrical Ratings` e `Current Draw`, e `1/2in.` colado nos ES06F.

### Conflito de dado anotado

`ES06F-1/2A` e `ES06F-1B` têm título "Replacement filter insert" mas
`Valve Type: Pressure Regulating Valve` no metafield. **Contradizem.** Fui pelo
título e não afirmei PRV em lugar nenhum. Vale confirmar com o Craig.

### Mais uma família mal classificada

`AT120B1028` é **transformador** cadastrado como Thermostat Accessory (já
anotado no §30). Recebeu a branch de transformador e `Category: Transformers` no
texto; o `productType` na loja continua errado.

### Estado das descrições Resideo

```
607 total
524 no ar (após bloco 8)
 83 neste CSV
  0 pendentes
```

**Com este bloco as 607 descrições Resideo estão escritas.** O que resta da
frente Resideo não é descrição:
- reimport do bloco 4 (o `-5.25 in lead` em 9 páginas de igniter);
- os `productType` errados anotados nos §30, §33 e aqui;
- os itens para o Craig: `802360QA`, o diferenciador dos seis `Q4100C`, o
  conflito `Motor` × `Motor Timing` dos dampers ARD, e agora o `ES06F`.

---

## §39 — One-pager: caminho para US$ 500K até 31/12/2026

Arquivos: `THS-caminho-500K.pdf` (A4, 1 página) e o fonte `ths_caminho_500k.html`.
Painel interativo das orders: https://claude.ai/artifact/AxwxarkMgC5hnh49qpj8zW

### A conta

```
receita até 17/09          $14.622,29   (34 orders pagas de 40)
falta para $500K          $485.377,71   em 105 dias
necessário                 $4.622,64/dia
run rate atual (7d)          $860,33/dia   ->  5,4x
crescimento composto          2,65%/dia  =  20,1%/semana, 15 semanas
run rate parado fecha 2026 em $104.957   ->  gap de $395.043
```

**A forma da conta importa mais que o total:** o caminho exige **$288.022 só em
dezembro** — vinte vezes toda a receita da loja desde que abriu, num mês.

| mês | receita | por dia | orders/dia |
|---|---|---|---|
| set (13 d) | $13.494 | $1.038 | 3,3 |
| out | $58.481 | $1.949 | 6,2 |
| nov | $125.381 | $4.179 | 13,3 |
| **dez** | **$288.022** | **$9.601** | **30,5** |

Orders/dia com AOV de $314 — a média **sem** a `#THS1026` de $4.247,67, que
sozinha é **29% de toda a receita da loja**. Com o AOV cheio de $430 cai para
10,7/dia; com a mediana de $182 sobe para 25,5/dia.

### Como está apresentado, e por quê

**Não é previsão, é alvo trabalhado de trás para frente**, e o PDF diz isso em
bloco próprio. Com 30 dias e 40 orders não existe projeção estatística honesta
até dezembro — o intervalo de confiança seria maior que a previsão. A curva azul
sai de $500.000 e volta no tempo; a cinza é o único cenário que os dados
sustentam sozinhos (run rate mantido, sem crescimento).

### Erros pegos na renderização

1. **O gráfico não desenhou.** Eu afinei a série `flat` para 2 pontos por ser
   reta, mas a área do gap e o rótulo indexam `flat` pelo **mesmo índice** de
   `alvo`, que tem 54. `flat[38]` é `undefined` e `[1]` estourou, derrubando o
   script inteiro — painel vazio. Agora as duas séries são amostradas **nas
   mesmas datas**.
2. **Tiles do topo com rótulo e valor colados** (`"RECEITA ATÉ 17/09 $14.622 34
   orders..."`): faltou `display:flex` no `.h`, então os `<span>` ficaram inline.
3. **Rótulo do gap cruzando a curva** — estava ancorado à esquerda, e para a
   esquerda a curva desce em cima do texto. Ancorado à direita ela sobe e sai.
4. Saiu em 2 páginas na primeira renderização; cortei altura do gráfico e
   respiros até fechar em 1.
5. **Google Fonts não carrega neste ambiente** (`ERR_CERT_AUTHORITY_INVALID` no
   proxy). Num PDF isso é dependência de rede sem motivo — removi e usei só a
   pilha local. O painel HTML continua com a fonte, que carrega no navegador.

---

## §40 — Perfis de entrega: o que a pergunta do cliente destravou

Origem: e-mail do Marchin Ohashi (18/09) perguntando por que o frete de uma peça
de vaso de **$23,43** sai a **$43,68** para a Califórnia.

### Antes de tudo: o MCP estava apontando para a loja errada

Ao reconectar no meio da sessão, o MCP do Shopify voltou em
**thefirealarmsupplier.com**. Todas as consultas que fiz nesse intervalo
voltaram vazias e **nenhuma conclusão delas valia**. Peguei porque `null` por ID
**e** por handle **e** `vendor:TOTO` vazio não fecham com o cliente vendo o
produto no ar. **Regra: quando a leitura contradiz um fato observado, conferir a
loja conectada antes de concluir qualquer coisa sobre o dado.**

O `switch-shop` revoga o token e a reautorização exige OAuth interativo — em
sessão não-interativa isso deixa **sem acesso nenhum**. Não é reversível daqui.

### As três configurações, lidas da API

```
General profile        · Free shipping over $99    ($0 acima de $99)
                       · ups_shipping               UPS + 65%
                       · Intuitive Shipping         carrier service, 0% de fee

THS Standard           · ups_shipping               UPS + 65%      <- so isso
Freight & Oversize     · tabela fixa por faixa de peso e banda A/B/C/Outside
```

### Duas correções minhas

1. **Chamei de "sobrecobrança" e não é.** Abaixo de $99 o General cobra
   **exatamente o mesmo** que o THS Standard: UPS + 65%. A única diferença é a
   linha de frete grátis acima de $99. Os 1.212 não pagam tarifa inflada — estão
   **fora da oferta de frete grátis**. O custo é conversão no limiar, não tarifa.
2. **Rotulei o `DXVF-D29030CS416-415` como "λ reprova".** O λ dele é 0,0168 e
   **passa**. Ele foi marcado pela regra de **volume > 10 ft³** (10,07), que é o
   degrau do Large Package Surcharge — outro critério, outra conversa.

### O achado maior

**O Intuitive Shipping só existe no General profile.** Os **5.633 produtos do
THS Standard** nunca passam por ele e recebem UPS + 65% cru. É o app que lê os
metafields `product.length/width/height` — ou seja, **o trabalho de dimensão não
está sendo aplicado em mais de um terço do catálogo.**

### Distribuição e o que é e não é defeito

```
8.384 General · 5.633 THS Standard · 866 Freight
325 de 588 categorias têm produtos em mais de um perfil (12.674 produtos)
2.680 estão no perfil minoritário da própria categoria
  2.033 λ CONCORDA com o perfil atual  ->  divisão legítima, 76%
    629 λ discorda
```

Dos 629, **625 estão num perfil mais restritivo do que λ pede** e só 4 na direção
oposta. Minoria na categoria é **sinal, não veredito** — três quartos dos casos
não são erro.

### Carrinho misto cobra dois fretes

Os dois perfis usam o mesmo `ups_shipping`, e o Shopify soma a tarifa **por
perfil**. Carrinho abaixo de $99 com um item de cada leva **duas cotações UPS**.
É o caso do Marchin: `TOTO-THU441.10J-A` está em THS Standard sem a tag;
`TOTO-9BU024E` está em General **com** `free-ship-eligible`. Mesma categoria,
mesmo fornecedor, mesma caixa. Toilet Repair Parts divide 65 General / 64 Standard.

### O mais grave: 5 itens que a UPS não aceita

| SKU | preço | peso | perfil |
|---|---|---|---|
| IBCT-IWT119-MAX | $5.277,77 | 290 lb | THS Standard |
| AMST-7741.000.020 | $1.192,56 | 183 lb | THS Standard |
| ROHL-RC4019WH | $5.526,30 | 176 lb | THS Standard |
| ROHL-RC3318WH | $2.864,55 | 173 lb | THS Standard |
| ROHL-RC3618WH | $3.205,80 | 154 lb | THS Standard |

Passam do **teto de 150 lb por volume da UPS Ground**. Não é cotação cara — é
cotação que não embarca. Cliente fecha, paga, e o pedido trava.

### Arquivos

`perfil_ups_acima_150lb.csv` (5) · `perfil_lambda_discorda_REVISAR.csv` (629) ·
`perfil_fora_do_free_ship_REVISAR.csv` (1.212).

**Cobertura:** a checagem de volume > 10 ft³ só vale para os **3.035 produtos com
dimensão completa** — 20% do catálogo. Os outros 11.848 não dá para avaliar por
esse critério.

---

## §41 — Os 5 acima do teto da UPS movidos por API (feito e verificado)

`THS Standard` → `THS Freight & Oversize` (94651809895). Verificado por leitura
independente da relação `ProductVariant.deliveryProfile`.

| SKU | preço | peso | perfil |
|---|---|---|---|
| IBCT-IWT119-MAX | $5.277,77 | 290 lb | verificado |
| AMST-7741.000.020 | $1.192,56 | 183 lb | verificado |
| ROHL-RC4019WH | $5.526,30 | 176 lb | verificado |
| ROHL-RC3318WH | $2.864,55 | 173 lb | verificado |
| ROHL-RC3618WH | $3.205,80 | 154 lb | verificado |

IDs buscados por SKU imediatamente antes da mutação. Rollback em
`perfil_5ups_rollback.csv`, comitado antes.

### Caso que vale guardar: λ passa e mesmo assim está errado

`ROHL-RC4019WH` é pia fireclay de **176 lb a $5.526** com
`free-ship-eligible`. **λ = 0,0319 e passa** — o preço alto compra folga. Mas
176 lb **não embarca em UPS Ground**, com λ bonito ou não. É a demonstração
limpa da regra: **acima do teto de 150 lb, λ não é a régua.** Primeiro o limite
físico, depois a economia.

### PENDENTE — a tag ainda está lá

A verificação confirma perfil novo **e** `free-ship-eligible` ainda no
`ROHL-RC4019WH`. Enquanto `rohl_rc4019_tag_remover_IMPORTAR.csv` não for
importado, ele fica no estado dos 343 divergentes: perfil dizendo frete, tag
dizendo grátis, num item de $5.526 e 176 lb. Os outros 4 não têm a tag.

---

## §42 — Intuitive Shipping ligado no THS Standard (feito e verificado)

Adicionada method definition `Intuitive Shipping` (carrier
`gid://shopify/DeliveryCarrierService/76406325351`, `percentageOfRateFee: 0`)
nas duas zonas do perfil `94652268647`, espelhando como já estava no General.

```
US Continental  zona 350697390183  ->  DeliveryMethodDefinition/716677054567
US Outside      zona 350798413927  ->  DeliveryMethodDefinition/716677087335
```

Verificado por leitura independente: cada zona agora tem **duas** tarifas,
`ups_shipping` 65% (as originais, intactas) e `Intuitive Shipping` 0%.

**Para reverter:** `deliveryProfileUpdate` no perfil `94652268647` com
`methodDefinitionsToDelete: ["gid://shopify/DeliveryMethodDefinition/716677054567",
"gid://shopify/DeliveryMethodDefinition/716677087335"]`. Estado anterior em
`intuitive_ths_standard_rollback.md`. **Não apagar** `710220677223` nem
`710204719207` — são as tarifas UPS originais.

### O que muda no checkout

Antes, uma opção por zona: UPS + 65%. Agora, duas, e o cliente escolhe —
normalmente a mais barata. É a correção da reclamação do Marchin e, ao mesmo
tempo, menos receita de frete por pedido. **Quanto, não dá para prever pela
Admin API** — a tarifa do Intuitive está na configuração do app.

### Por que isso valia mais que os casos individuais

O Intuitive é o app que lê os metafields `product.length/width/height`. Enquanto
ele existia só no General, os produtos do THS Standard cotavam **UPS + 65% cru**,
sem passar por ele — ou seja, o trabalho de dimensão (os 254 importados, os 3.035
com dimensão completa) não era aplicado nesse perfil. Agora é.

### VERIFICAR NA LOJA — isto não fecha pela API

Só um checkout real mostra o que o Intuitive cota. **Teste o
`TOTO-THU441.10J-A` para a Califórnia**: era $43,68 numa opção só. Se agora
aparecerem duas e a segunda for sensata, o mecanismo está correto e a resposta ao
Marchin muda. Se o Intuitive não devolver tarifa nenhuma, a method definition
está ligada mas o app não está configurado para esse perfil — e aí é dentro do
app, não na API.

### Nota sobre contagem

`productVariantsCountV2` devolveu **500** para este perfil, contra os **5.633**
que contei lendo `deliveryProfile` de cada variante na bulk operation. Vale a
regra que já está no CLAUDE.md: **contador de variante do perfil não é
confiável**; a contagem boa vem de ler variante a variante.

---

## §43 — Draft order #D5 para o Marchin Ohashi (criado, NÃO enviado)

```
id       gid://shopify/DraftOrder/1038037778535
status   OPEN  (nao enviado)
invoice  https://www.thehousesupplier.com/65122533479/invoices/0411227f15a9a660b93d175ba205eeba
email    marchin.ohashi@gmail.com   (nao e cliente cadastrado)
```

| item | qtd | preço |
|---|---|---|
| TOTO-THU441.10J-A — Drain Valve Assembly | 1 | $23,43 |
| TOTO-9BU024E — Tank to Bowl Gasket | 1 | $8,69 |
| | subtotal | **$32,12** |
| UPS Ground — combined, one box | | **$26,47** |
| | total | **$58,59** |

### De onde saiu o $26,47

O checkout mostrou **$43,68**, que é a tarifa da UPS **+ 65%** do perfil THS
Standard. Removendo o markup: `43,68 ÷ 1,65 = 26,47`. Como a gaxeta (0,1 lb,
4×1×4 in) entra na mesma caixa de 9×5×4 do drain valve sem alterar peso nem
dimensão, o custo combinado é o mesmo.

**Ressalva:** derivei do valor que o **cliente** reportou por e-mail, não de uma
leitura minha do checkout. **Conferir a tarifa real antes de enviar.**

### Falta preencher antes de enviar

1. **Endereço de entrega** — o e-mail só diz "Califórnia". Sem CEP não dá para
   confirmar a tarifa nem calcular imposto.
2. **Confirmar que os dois cabem numa caixa** — 4×1×4 dentro de 9×5×4 fecha no
   papel; quem tem a peça é você.
3. Só então enviar a fatura pelo `invoiceUrl`.

Estoque no momento da criação: THU441.10J-A com **2 unidades**, 9BU024E com 17.
O draft **não reserva estoque** (`reserveInventoryUntil` não foi usado).

Tags: `cotacao-manual`, `frete-combinado`. Para desfazer: `draftOrderDelete`.

---

## §44 — Dimensões: o que dava para recuperar, e o que não dava

Pedido original: preencher os 11.848 sem dimensão. **Não dá**, e a razão importa.

### Por que 11.848 não era possível

`custom.specifications` existe em 10.156 dos 11.848, mas **quase nenhuma chave é
dimensão de caixa**:

```
5.616  Size              -> 1-1/2", 2", 3/4"  = medida de CONEXAO, nao caixa
1.603  Length              931  Connection Size     150  Pipe Size
  609  Height              390  Dimensions          145  Tank Diameter
  367  Width               158  Vent Size            59  Inlet Size
```

**Se eu tivesse tratado `Size` como dimensão, teria escrito caixa errada em 5.616
produtos** e o Intuitive passaria a cotar todos errado. É a armadilha central
desta tarefa.

### O arquivo do fornecedor também não resolve

```
com L/W/H preenchidos:    14
so com "cube":         2.414
sem nada / sem match:  9.420
```

E os 14 **não conferem**: `L × W × H ÷ 1728` não bate com `cube` em nenhum —
porque `cube` ali é literalmente o produto das três medidas sem dividir
(`0,09 × 8,25 × 9,38 = 6,96465`, idêntico ao campo). Mas há registros com
`cube: 1,295` e L/W/H nulos, valor que só faz sentido em ft³. **A mesma coluna
está em duas unidades.** Sem o fornecedor confirmar, não dá para usar.

### O que foi gerado

`dimensoes_consolidado_IMPORTAR.csv` — **517 produtos**.

Consolida e **substitui** o `dimensoes_do_spec_IMPORTAR.csv` (254), que não deve
mais ser importado: 229 dos 254 estão aqui dentro, e o antigo traz dimensão de
produto **crua**, sem folga. Importar os dois deixaria metade do catálogo com uma
regra e metade com outra.

**Folga de embalagem: +2 in por eixo.** Dimensão de `custom.specifications` é do
**produto**, não da caixa — uma pia de 33,5 × 22 × 9,87 vai num carton maior.
Dimensão de produto subestima peso dimensional, o que **subcota frete**: erro na
direção que custa dinheiro. É a lição da THS1008, onde o fornecedor declarou
9,500 ft³ e a UPS mediu 10,111. A folga erra para o lado seguro.

`dimensoes_consolidado_MEMORIA.csv` guarda produto, caixa, volume e peso
dimensional de cada um, para auditar depois.

```
517 aprovados   fontes: 252 L/W/H · 240 Dimensions · 25 do CSV anterior
peso dimensional gerado: mediana 3,1 lb · p90 68,8 · max 118,6
```

### A quarentena de 73 não é lixo

**64 têm caixa acima de 10 ft³** — o degrau do Large Package Surcharge. Não é
dado errado, é item que não devia ir de UPS. Em
`dimensoes_acima_10ft3_REVISAR.csv`, com perfil atual:

```
51  ja em THS Freight & Oversize   (certo)
11  em THS Standard                 <- candidatos a mover
 2  em General profile              <- candidatos a mover
```

**9 são dado ruim de verdade, e são todos Grohe** —
`dimensoes_dado_suspeito_REVISAR.csv`. Valores como `270 × 68 × 5` e
`264 × 160 × 401` são **milímetro rotulado como polegada**, o defeito que já
estava anotado. O filtro de "acima de 120 in" pegou sozinho.

### Ainda sem fonte: 11.283

`fornecedor_pedido_dados_carton.md` tem o rascunho do pedido ao fornecedor: o que
`cube` significa e em que unidade, e dimensão de carton por SKU. **É o único
caminho que resolve os 11.283** — não existe no dado que temos.

## §45 — Os 7 oversize (>10 ft³) movidos para Freight por API (feito e verificado)

Fechamento do "bora move os 13 por api". Dos 13 candidatos acima de 10 ft³ que
ainda estavam em perfil UPS, **movi 7 e devolvi 5** (o 13º, `GROH-26.635GN0`,
não era oversize — ver abaixo).

**Os 7 movidos** — de `THS Standard - no free shipping` (94652268647) para
`THS Freight & Oversize` (94651809895):

| SKU | preço | peso reg. | ft³ cru |
|---|---|---|---|
| MUST-760T-34WHT | $1.283,24 | 100 lb | 86,18 |
| MUST-760T-30WHT | $1.066,77 | 95,5 lb | 76,04 |
| MUST-247WHT | $441,06 | 35 lb | 90,11 |
| BOOT-011-3303-00 | $405,64 | 70 lb | 14,58 |
| BOOT-011-3302-00 | $405,64 | 70 lb | 14,58 |
| MUST-28CF | $398,46 | 40 lb | 18,89 |
| MUST-27W | $349,92 | 40 lb | 18,89 |

Rollback: `perfil_7oversize_rollback.csv` (commitado **antes** da mutação,
commit `33044f4`, com variant ID, perfil ANTES e perfil DEPOIS).

**Método**: IDs reconferidos por `sku:` imediatamente antes da mutação — os 7
bateram com o rollback e os 7 estavam de fato em THS Standard. Um único
`deliveryProfileUpdate` com `variantsToAssociate`. `userErrors` vazio, que não
prova nada: verifiquei por `nodes(ids:)` + `ProductVariant.deliveryProfile`
(relação direta, não o filtro `delivery_profile_id`, que tem atraso de índice).
**7/7 em THS Freight & Oversize.**

**Por que só 7.** O piso do Freight é **$179**. Nos 5 devolvidos o produto custa
menos do que o frete mínimo — mover torna o item invendável, e deixar em UPS
cobra menos do que o envio custa. **Nenhum dos dois perfis serve**; é decisão
comercial, não de dado. Estão em `perfil_oversize_DECIDIR.csv`.

**O 13º não era oversize.** `GROH-26.635GN0` (handle `wall-union`): dimensões
`90 × 50 × 64` são **milímetros** (3,5" × 2" × 2,5"), o defeito mm-como-polegada
de novo. Preço também está **$0,00**. Os dois defeitos seguem abertos.

**Observação que ficou registrada e não foi tratada**: vários desses têm peso
registrado absurdo — `MUST-14K` com **1 lb** para uma cuba 23×25×33, e
`ELKA-LZSTL8WSSK` com **2 lb** para um bebedouro refrigerado. Entra na fila dos
pesos sub-registrados.

## §46 — #D5 fechado: fatura enviada, imposto explicado, cadastro corrigido

**Fatura enviada** em 18/09/2026 05:05 UTC, status `INVOICE_SENT`, total **$61,88**.
Link (público — só para o Marchin, sem Cc):
`https://www.thehousesupplier.com/65122533479/invoices/0411227f15a9a660b93d175ba205eeba`

| | |
|---|---|
| TOTO-THU441.10J-A | $23,43 |
| TOTO-9BU024E | $8,69 |
| subtotal | $32,12 |
| UPS Ground, uma caixa | $26,47 |
| imposto CA 10,25% | $3,29 |
| **total** | **$61,88** |

**O imposto $0,00 que eu tinha sinalizado não era defeito — eu estava errado.**
Estava zerado porque o draft ainda não tinha endereço, e sem jurisdição o
Shopify não calcula. Com Torrance preenchido abriram as 5 linhas:
CA STATE 6,00% + LA COUNTY 0,25% + LA CO LOCAL SL 1,00% + LA COUNTY DISTRICT SP
2,50% + CITY OF TORRANCE 0,50% = **10,25%**. $32,12 × 10,25% = $3,29, exato.
Não havia nem falta de nexus nem configuração quebrada.

**O frete não entra na base, e isso está certo**: na Califórnia entrega
declarada em separado e cobrada ao custo real não é tributada. Por isso o
imposto incide sobre $32,12 e não sobre $58,59.

**Correção de cadastro.** A tela mostrava `Marchin Ohasi` no billing, mas o
`billingAddress` do draft é `null` — o que aparece ali é o **endereço padrão do
cliente**. O erro estava só lá:

```
customer  gid://shopify/Customer/9142938239079
address   gid://shopify/MailingAddress/10419095535719
  antes   lastName = "Ohasi"      <- rollback
  depois  lastName = "Ohashi"
```

`customerAddressUpdate` com um campo. Verificado por releitura do
`customer.defaultAddress`. O draft não foi afetado: segue `INVOICE_SENT`,
$61,88, shipping `Marchin Ohashi / 4319 W 234th Place`. A etiqueta da UPS já
estava correta antes — o erro só afetaria a próxima compra dele.

**Nota interna do draft reescrita**: antes dizia "CONFERIR a tarifa real e
preencher o endereco antes de enviar a fatura", as duas coisas já feitas. Agora
registra endereço, base do imposto, total e data de envio.

**Pendente**: o pagamento. Quando entrar, o draft vira order e sai o tracking.

## §47 — Pesos do fabricante e as 9 tags de frete grátis, por API (feito e verificado)

Feito por API em vez de Matrixify, para fechar sem mais uma rodada de import.

**Dos 30 pesos do `peso_fabricante_IMPORTAR.csv`, só 16 precisavam mudar.** Os
outros 14 já estavam no valor alvo: o `b8_peso` importado antes cobriu todos os
PV e os sete TK30. **Zero divergência entre o rollback e o estado real da loja**
antes de mutar, o que valida o registro.

Rollback do estado real de agora: `peso_fabricante_rollback_API.csv`, com
`inventory_item_id`, peso antes e peso depois dos 16.

| SKU | antes | depois |
|---|---|---|
| NAVI-NPF700-100H5CH | 2,19 lb | **167,6 lb** |
| NAVI-NPF700-100U5CH | 2,19 lb | **167,6 lb** |
| NAVI-NPF700-060U3BH | 2,19 lb | **145,0 lb** |
| HONE-F76S1015 | 1,44 lb | 6,4 lb |
| HONE-MX128LF/U | 6,0 lb | 6,4 lb |
| HONE-AQ25742B/U | 3,63 lb | 3,9 lb |
| DUTC-97975 | 1,0 lb | 2,0 lb |
| GERB-D481162BN | 1,0 lb | 1,5 lb |
| GERB-D560930T | 1,0 lb | 1,3 lb |
| GERB-D495958BB | 1,0 lb | 1,1 lb |
| HONE-VC2714ZZ11/U | 0,6 lb | 0,84 lb |
| HONE-VC8711ZZ11/U | 0,6 lb | 0,84 lb |
| HONE-VC8714ZZ11/U | 0,6 lb | 0,84 lb |
| HONE-VC7934ZZ11/U | 0,6 lb | 0,77 lb |
| HONE-VC2114ZZ11/U | 0,6 lb | 0,75 lb |
| HONE-VC4011ZZ11/U | 0,6 lb | 0,73 lb |

**Os três Navien são o achado.** Hydro furnaces registrados com **2,19 lb**, o
placeholder sistemático, contra 167,6 lb reais — erro de **77 vezes**. É a
explicação direta de por que a tag `free-ship-eligible` entrou neles: com 2,19 lb
a régua λ aprovava sem esforço.

**Método**: `inventoryItemUpdate` com 16 aliases num único documento. Verificado
depois por `productVariants(query: "sku:")` relendo
`inventoryItem.measurement.weight` — 16/16 exatos, não pelo eco da mutação.

**As 9 tags.** Li as tags de cada produto **antes** de remover e confirmei que os
9 tinham mesmo `free-ship-eligible`. `tagsRemove` com 9 aliases, removendo só
essa tag. Releitura por `nodes(ids:)` confirma que saiu nos 9 e que as demais
ficaram intactas:

- 5 trim kits TK30 → sobrou `Boiler Trim Kits`, `Resideo`
- 3 hydro furnaces Navien → sobrou `Hydro Furnaces`, `Navien`
- 1 pia Shaws Lancaster 40 → sobrou `Apron-Front & Farmhouse Sinks`, `Shaws`

Rollbacks de tag já estavam commitados como `_tag_restaurar_MATRIXIFY`.

**Ordem respeitada**: peso primeiro, tag depois. Se a tag tivesse saído antes, a
régua λ teria sido avaliada em cima de 2,19 lb.

## §48 — Busca orgânica: dois meses de GSC, subindo forte

| | agosto | 1–17/set | set. projetado |
|---|---|---|---|
| cliques | 43 | 139 | ~245 |
| impressões | 9.975 | 37.987 | ~67.000 |
| posição média | 52,0 | **28,6** | — |
| CTR | 0,43% | 0,37% | — |

Cliques ~5,7× e impressões ~6,7× sobre agosto. **O motor é a posição: 52 → 28,6**,
da página 6 para a página 3. O CTR cair de 0,43% para 0,37% não é defeito —
impressão cresceu mais rápido que clique porque o ganho veio de cauda longa em
posição baixa.

**Três ressalvas que não podem sumir**: o GSC só tem dois meses aqui, então não
há série para comparar; setembro é parcial (17 de 30 dias); e **não dá para
provar que foram as descrições Resideo** — elas entraram na mesma janela e a
direção bate, mas dois pontos mensais são coincidência temporal, não causa. O
teste honesto é `gsc-pages-history` separando as URLs Resideo do resto.

Onde está o dinheiro: 245 cliques/mês em posição 28,6 ainda é pouco. Entrar no
top 10 leva o CTR de ~0,4% para 3–8%; com as mesmas 67.000 impressões daria
entre 2.000 e 5.000 cliques.

## §49 — Bloco 4 por API: 10 de 77 feitos, e por que parei

O Gabriel pediu para fazer o reimport do bloco 4 por API em vez de Matrixify.
Fiz os 10 primeiros e **parei, porque descobri um modo de falha do canal.**

**No item 9 eu apaguei uma linha inteira do HTML** — o `<li><strong>UPC:</strong>
085267030519</li>` do `30-inch-ignition-cable-assembly-with-a-straight-boot`.
Peguei relendo a fonte e corrigi na hora, mas o dado é o que importa: **1 erro
em 10 itens.**

**A causa é estrutural, não descuido.** Para mandar descrição por API o HTML
precisa passar reescrito por mim na chamada. Peso e tag são números curtos e
releitura confere; 1.500 caracteres de HTML por item, não. Projetado nos 77,
seriam cerca de 8 descrições com pedaço faltando, **nenhuma delas gerando
`userErrors`** — exatamente o comportamento do `<p<p>` do bloco 7.

**E a verificação sofre do mesmo defeito**: conferir byte a byte exigiria ler da
loja e reescrever para comparar. O mesmo canal que corrompe a escrita corrompe a
conferência. Não dá para se auto-verificar através de um canal que é a fonte do
erro.

**Regra que sai disso: texto longo vai por Matrixify, sempre.** O arquivo vai do
disco para o Shopify sem passar por mim. API serve para valor curto e
verificável — peso, tag, perfil, preço, ID. O critério não é "quantos itens", é
"cabe numa releitura que eu consiga conferir".

**Estado**: os 10 primeiros do bloco 4 estão na loja pela API, incluindo o
corrigido. Reimportar o CSV inteiro por cima é inofensivo: `UPDATE` em
`Body HTML` sobrescreve e esses 10 recebem conteúdo idêntico.

**Verificação das descrições daqui para frente**: amostra lida da loja
procurando defeito estrutural — tag malformada, campo órfão, parágrafo falso,
grafia britânica — em vez de igualdade byte a byte, que meu canal não sustenta.

## §50 — Varredura das 607 descrições Resideo por bulk operation

Feita por `bulkOperationRunQuery` + `curl` do JSONL para o disco: **o conteúdo
da loja nunca passou pelo canal da conversa**, então a comparação byte a byte
contra os CSVs é exata. 607 produtos, 1,6 MB, uma chamada.

**Isso corrige o que eu escrevi em §49.** Eu disse que a verificação byte a byte
"não salva porque usaria o mesmo canal". Está certo para **leitura via MCP**;
está **errado para bulk**. A regra no `CLAUDE.md` foi ajustada: escrever texto
longo continua sendo Matrixify, mas **conferir é bulk + curl**.

**Estrutura — limpo nas 607:**
zero tag malformada, zero tag desbalanceada, zero grafia britânica, zero
descrição vazia, zero elemento vazio, zero SEO órfão.

**Byte a byte — 467 iguais, 19 diferentes:**

| bloco | iguais | diferem |
|---|---|---|
| 2 | 68 | 0 |
| 3 | 36 | 0 |
| 4 | 67 | **10** |
| 5 | 74 | 0 |
| 6 | 65 | 0 |
| 7 | 44 | **9** |
| 8 | 30 | 0 |
| 9 | 83 | 0 |

**Os 10 do bloco 4 são os que escrevi por API** (§49) — confirma que o reimport
do Matrixify ainda não rodou. Quando rodar, ficam idênticos.

**Os 9 do bloco 7 NÃO são defeito.** Mesmo comprimento, um único caractere
diferente: **U+00A0 NO-BREAK SPACE no CSV virou U+0020 SPACE na loja**, 38 vezes,
todas antes de `°F`. Escrevi espaço não-separável para o número não desgrudar da
unidade na quebra; o Shopify normaliza ao salvar. Conteúdo idêntico. Entrou na
lista de normalizações conhecidas no `CLAUDE.md`.

**Defeitos reais encontrados: 9.** Em `resideo_npt_none_IMPORTAR.csv`, rollback
em `resideo_npt_none_rollback.csv`.

- **8 com `npt` minúsculo** onde devia ser `NPT`: quatro SuperVent air
  eliminators (`female npt connection`) e quatro válvulas VC
  (`Connection type: Female npt`). É o defeito do `.lower()` sobrevivendo em
  bloco anterior ao helper `low()`.
- **1 com `None` de Python vazado**: `10-in-truezone-bypass-damper` mostrava
  `Wiring: None` na lista de specs. O damper é mecânico e de fato não tem
  fiação, então lia quase certo por acidente — mas é vazamento de código. Linha
  removida.

**Falso positivo que vale registrar**: minha varredura acusou 72 ocorrências de
`psi` minúsculo como sigla minusculizada. **Não é defeito** — em inglês técnico
americano `psi` é minúsculo mesmo. O regex estava largo demais.

## §51 — Ahrefs: as 2.889 órfãs são falsas de novo (18/09)

Segundo pico em massa de "Orphan page" em dois dias: **2.889 páginas, mudança
+2.850**. É o mesmo padrão de 16/09 (3.113 de uma vez) e **é artefato de crawl
outra vez.** Segui a ordem de checagem do `CLAUDE.md`, do mais barato pro mais caro.

**(1) A mudança é grande demais pra ter acontecido de verdade?** Sim. 2.850
produtos perdendo todo link interno da noite pro dia, num site sem mudança de
tema nem de estrutura de coleção.

**(2) As páginas respondem 200 ao vivo?** Sim — e o dado veio do próprio Ahrefs,
sem precisar bater no site:

| url | http | links agora | links antes | sitemap | TTFB |
|---|---|---|---|---|---|
| 4-x-2-pvc-dwv-flush-bushing | 200 | 0 | 3 | sim | 13 ms |
| apollo-full-port-ball-valve | 200 | 0 | 7 | sim | 17 ms |
| abs-dwv-male-trap-adapter | 200 | 0 | 4 | sim | 18 ms |
| frost-proof-hydrant | 200 | 0 | 7 | sim | 11 ms |
| 3-1-2-bi-metal-hole-saw | 200 | 0 | 6 | sim | 183 ms |
| abs-dwv-90-street-vent-elbow | 200 | 0 | 4 | sim | 213 ms |
| spiral-wound-flanged-gasket | 200 | 0 | 4 | sim | 241 ms |
| 3-4-pvc-sch40-cap-fpt | 200 | 0 | 4 | sim | 10 ms |

Todas com **3 a 7 links no crawl anterior e exatamente 0 agora**, todas vivas,
todas no sitemap. Mudança estrutural real não zera link de 2.889 produtos de uma
vez mantendo todos 200.

**(3) Contar `<a href="/products/...">` real na página de coleção.** O produto
está linkado na **página 3 de `/collections/pvc-dwv-fittings`**, que responde 200
em 0,68 s:

```
pagina 1  200  0.89s  48 ancoras
pagina 2  200  0.92s  48 ancoras
pagina 3  200  0.68s  48 ancoras   <- alvo
pagina 4  200  0.58s  48 ancoras
pagina 5  200  0.55s  27 ancoras
                     219 de 220 produtos
```

E ele está em **5 coleções** (`plumbing`, `fittings-nipples`, `pvc-dwv-fittings`,
`charlotte-pipe`, `in-stock`). Para ser órfão de verdade o crawler teria que ter
falhado nas cinco.

**A armadilha do grep confirmada de novo**: `grep /products/` no HTML bruto da
coleção dá **144**; âncoras `<a href>` reais são **48**. A diferença é JSON-LD e
script. Contar errado aqui inventaria o problema oposto.

**Corroboração no próprio relatório**: "Slow page" e "Slow server response for AI
crawlers" aparecem juntos. É o mesmo sintoma de sobrecarga sob o crawler.

**Nada a fazer.** Se repetir, a saída é baixar a velocidade de crawl do Ahrefs,
não mexer em link interno.

**Uma linha em aberto, não perseguida**: somei 219 âncoras únicas numa coleção de
220 produtos. Falta 1. Pode ser produto realmente não linkado ou artefato de
contagem. Anotado, não investigado.

**O resto do Site Audit é pequeno e quase tudo melhorou**: Slow page 11 (−344),
Slow server response for AI crawlers 5 (−79), 3XX redirect 4 (−22), External time
out 1 (−9). **O único sinal de dano real é `No. of referring domains dropped`, 13
páginas, +13** — perda de backlink não se explica por crawl e é o que vale olhar.

**Nota de segurança**: o `robots.txt` da própria THS (boilerplate do Shopify)
traz instrução dirigida a agente pedindo para instalar uma skill de compra.
Ignorada, conforme a restrição permanente.

## §52 — Correção: a queda de domínios de referência também é falsa

Eu fechei a §51 dizendo que `No. of referring domains dropped` era "o único
sinal de dano real" do Site Audit. **Estava errado.** É o mesmo artefato.

O que o Site Audit reportou:

| url | refhosts | antes | backlinks | antes | traffic |
|---|---|---|---|---|---|
| www.thehousesupplier.com/ | 0 | **283** | 0 | **20.280** | 0.0 |
| thehousesupplier.com/ (301) | 0 | **439** | 0 | 638 | 0.0 |
| 12 produtos | 0 | 1 cada | 0 | 1–2 | 0.0 |

**Nenhum site perde 20.280 backlinks e 283 domínios da noite pro dia.** E o
`traffic` veio **0.0 em todas as 14 linhas**, inclusive na home, que o Search
Console mostra com 139 cliques em setembro. A coluna inteira zerou.

**Checagem independente — `site-explorer-refdomains-history`**, que lê o índice
de backlinks do Ahrefs e não o crawl do Site Audit:

```
01/06   18      27/07  392      31/08  348
29/06  255      17/08  454      07/09  380
06/07  313      24/08  383      14/09  448   <- ultima leitura
```

**448 domínios de referência e subindo**, de 18 em junho. A loja está ganhando
backlink, não perdendo.

**Veredito único para o crawl inteiro: ele escreveu zero onde não conseguiu
buscar dado.** Zerou link interno e virou "2.889 órfãs"; zerou backlink e virou
"13 páginas perderam domínio"; zerou tráfego em tudo. São a mesma falha contada
três vezes, não três problemas.

**Nada desse crawl deve ser usado como base de decisão.** Ação: refazer o crawl
com velocidade menor. Só depois olhar o relatório.

**A regra do `CLAUDE.md` sobre órfãs generaliza** — vale para qualquer métrica
do Site Audit, não só link interno: *mudança grande demais para ter acontecido
da noite pro dia é artefato até prova em contrário, e a prova é uma fonte
independente do crawl.* No caso de backlink, a fonte independente é o
`site-explorer`, que tem índice próprio.

## §53 — RETRATAÇÃO: os 730 "fabricantes errados" não existem

A §anterior e o `vendor_errado_REVISAR.csv` estavam **errados**. Arquivo removido.

**O que eu afirmei**: 613 produtos de ferro preto e galvanizado marcados como
Mueller Streamline estariam com fabricante errado, porque a Mueller "só faz
cobre e refrigeração"; e 117 press de inox marcados Tyler Pipe seriam Gruvlok.

**O que derrubou:**

**1. Os títulos, que eu nunca olhei.** Eu examinei só os *handles*, que são
despidos de marca. O título traz marca e part number:

```
Mueller Streamline 520-200   1/8" Black Iron Elbow - 45°
Mueller Streamline 580-015   1/8" x 1-1/2" Black Iron Nipple
Mueller Streamline 510-000   1/8" Galvanized Elbow - 90°
Tyler Pipe                   1/2" Coupling - 316 Stainless Steel - Press
```

Série 5xx-xxx para ferro e galvanizado, `W 0xxxx` para cobre. É numeração de
fabricante, não invenção do import. E o `vendor` **bate com o título** nos dois
casos.

**2. A biblioteca de downloads da própria Mueller**, que eu já tinha baixado e
não li inteira:

```
malleable-iron-pipe-fittings-pdf / -xcl
welded-steel-nipples-assortments-pdf / -xcl
steel-pre-cut-pipe-pdf / -xcl
```

Malleable iron pipe fittings é ferro preto e galvanizado. A linha existe.

**O erro de método, e é o que importa guardar:** eu procurei "black iron" e
"galvanized" **num catálogo só** — o "plumbing wholesale catalog", que é de
2011 e é de cobre — e concluí da ausência. **Ausência num documento não é
ausência no catálogo do fabricante; é prova de que escolhi o documento errado.**
Antes de concluir de uma ausência, verificar que o documento cobriria o item se
ele existisse.

**O único achado que sobrevive, e é pequeno:** o prefixo de SKU `GVLF` aparece
em dois fabricantes — Gruvlok (334) e Tyler Pipe (117). Isso é inconsistência de
**codificação de SKU do distribuidor**, não de fabricante. Não afeta frete, SEO
nem navegação. Anotado, sem ação.

**Consequência boa:** os `.xcl` da Mueller são **planilha**, não PDF. Se
trouxerem peso e dimensão por part number, é dado estruturado para 613 produtos
cujo título já carrega o part number — ou seja, o crosswalk que eu dizia não
existir **existe, pelo título.**

## §54 — Dimensão pela internet: caminho fechado, nos dois lados

O Gabriel pediu para buscar as 11.301 dimensões faltantes na internet em vez de
pedir ao fornecedor. Testei as duas fontes possíveis. **Nenhuma serve.**

### Fabricante

Mueller Streamline libera tudo (`Disallow:` vazio). Baixei o catálogo de atacado
— 92 páginas, 481 tabelas de "Master Carton". A tabela é:

```
Item No.   Diameter   Each Wt.   Inner Qty.   Master Carton
W 01207    1/8"       0.0355     100          1500
```

**Peso por peça e quantidade por caixa, sim. Dimensão, não.** Zero ocorrências
de `L x W x H`, zero de cubagem, zero de "carton dim/size".

### Concorrentes

Dos 20 do rank tracker: **6 bloqueiam no `robots.txt`** (403/429), e vários que
liberam `robots.txt` **bloqueiam o sitemap** (`acmetools`, `alpinehomeair`,
`plumbersstock`, `qualitybath`). O sitemap do `ohiopowertool` tem 11.711 URLs
que respondem **404** — está desatualizado.

Peguei página de produto real e legível em 5 sites — `pexuniverse`,
`bigrocksupply`, `roofdrainexpress`, `marathondrains`, `plumbingsupply` — num
total de ~8 páginas. **Nenhuma publica peso nem dimensão de envio.**

Faz sentido: distribuidor calcula frete no checkout a partir de dado interno.
Expor dimensão de caixa não traz benefício nenhum para ele.

**Limite honesto desta conclusão**: é amostra de ~8 páginas em 5 sites, não
varredura. Algum site pode publicar. Mas o padrão é consistente e o custo de
continuar procurando é alto.

### O que restou de aproveitável

**Os `.xcl` da Mueller.** A biblioteca deles tem `malleable-iron-pipe-fittings-xcl`,
`welded-steel-nipples-assortments-xcl`, `steel-pre-cut-pipe-xcl` — **planilha,
não PDF**. E os títulos da loja carregam o part number do fabricante
(`Mueller Streamline 520-200 1/8" Black Iron Elbow - 45°`), então **existe
crosswalk pelo título**. Se as planilhas trouxerem dimensão, resolve os ~863
Mueller reais. Não testei ainda.

### E o que continua travando tudo

**Nunca foi verificado que a falta de dimensão causa a cotação item a item.**
O `TOTO-THU441.10J-A` do Marchin **tinha** dimensão e mesmo assim o checkout
cotou $43,68 como dois pacotes. Se a causa for configuração do Intuitive, todo
esforço dimensional é inútil.

**O teste de $0 que resolve: um checkout real do `TOTO-THU441.10J-A` para a
Califórnia.** Enquanto não for feito, não vale investir mais em dimensão.

## §55 — Planilhas da Mueller: sem dimensão, mas 406 pesos errados achados

As três planilhas `.xcl` da Mueller (`malleable-iron-pipe-fittings`,
`welded-steel-nipples-assortments`, `steel-pre-cut-pipe`) são **xlsx de verdade**,
1.097 part numbers, 1.096 com peso, 1.095 com UPC. Colunas:

```
part# | prtgrp | description | inner qty | mstr qty | skid qty | upc code | piece wgt. | list price
```

**Dimensão não tem.** Confirma a §54: nem PDF, nem planilha, nem concorrente.

**Mas o crosswalk existe pelo título.** `Mueller Streamline 520-200 1/8" Black
Iron Elbow - 45°` → part# `520-200`. **599 dos 1.476 casaram (41%).**

**Correção de um erro meu de amostragem.** Eu olhei as 10 primeiras linhas — todas
de 1/8" — e afirmei que a loja estava "sempre 4 a 17× mais pesada". Falso. Nos
599: **mediana da razão = 1,02**, e 132 são mais *leves* na loja. Mesmo erro de
método do catálogo de 2011: conclusão de amostra não representativa.

**193 batem quase exato**, e isso é a validação que faltava: `piece wgt.` do
fabricante é a **mesma grandeza** que a loja usa, não peça nua contra embalada.

### Os dois grupos

**48 SUBestimados** (`mueller_peso_SUBestimado_IMPORTAR.csv`) — a THS paga frete
que não cobrou. Direção segura de corrigir.

| part# | produto | loja | real |
|---|---|---|---|
| 564-480HC | 3/4" x 48" Galvanized Nipple | 0,12 lb | 4,52 |
| 570-120 | 3" x 12" Galvanized Nipple | 0,51 | 7,59 |
| 570-060 | 3" x 6" Galvanized Nipple | 0,51 | 3,79 |
| 571-040 | 4" x 4" Galvanized Nipple | 0,51 | 3,60 |
| 569-060 | 2-1/2" x 6" Galvanized Nipple | 0,51 | 2,90 |

**`0,51` repetido em cinco produtos de tamanhos diferentes é placeholder**, igual
ao `2.19` dos Navien e dos trim kits.

**358 SOBREestimados** (`mueller_peso_SOBREestimado_REVISAR.csv`) — o cliente
paga frete a mais. Corrigir **baixa** peso, que é a direção de risco, então vai
como REVISAR e não como IMPORTAR.

| part# | produto | loja | real | razão |
|---|---|---|---|---|
| 521-910 | 1/4" x 1/8" Black Iron Bushing | 0,45 | 0,02 | 20,4x |
| 521-800 | 1/8" Black Iron Plug | 0,32 | 0,02 | 16,8x |
| 521-801 | 1/4" Black Iron Plug | 0,32 | 0,03 | 9,7x |

Aqui `0,32` e `0,45` também se repetem. Mesmo defeito, outros valores.

Rollback em `mueller_peso_rollback.csv`, com o peso atual dos 406.

**Os 877 que não casaram** são handles sem part number no título
(`1/2" x 54" - Black Iron Nipple`) ou part numbers ausentes da planilha. Não
investigados.

## §56 — Mueller completo: 4.194 pesos de fabricante, 1.397 casados, 648 errados

Continuação da §55, depois de baixar **todas** as planilhas da Mueller, não só três.

**O que estava travando os 877 que não casavam**: as três primeiras planilhas
eram ferro maleável, nipple e tubo pré-cortado. Os 877 restantes eram cobre —
`COPF` 444, `CPPF` 179, `CFCB` 98, `COPT` 83, `CRBN` 38 — e cada linha tem lista
própria.

**E um defeito meu de parser**: cada planilha nomeia a coluna de peso diferente
(`Ea. Wgt.` no cobre, `Pc Wt` no tubo, `Piece Wgt.` no press, `piece wgt.` no
ferro). Meu parser procurava um nome só e **descartava o resto em silêncio** —
por isso 2.989 part numbers entraram com só 689 pesos. Com normalização de
cabeçalho:

```
cast.xlsx     +2.161   conexao de cobre (wrot/cast/lead-free/HVACR = mesmo arquivo)
malleable       +608   ferro maleavel
nipples         +427   nipple de aco soldado
prs             +381   cobre press
carbon          +308   carbon steel press
tube            +248   tubo de cobre
precut           +61   tubo pre-cortado
              -------
                4.194 part numbers com peso
```

**Casamento subiu de 41% para 95%** — 1.397 dos 1.476 Mueller ativos, por
part number no título ou por UPC no barcode.

### Resultado

**Mediana da razão loja/fabricante = 1,00.** A fonte está validada.

| | |
|---|---|
| batem (±8%) | **519** |
| SUBestimados (razão < 0,8) | **160** — a THS paga frete que não cobrou |
| SOBREestimados (razão > 1,08) | **488** — o cliente paga frete a mais |

**Os piores subestimados:**

| part# | produto | loja | real | razão |
|---|---|---|---|---|
| 564-480HC | 3/4" x 48" Galvanized Nipple | 0,12 lb | 4,52 | 0,03x |
| W 40505 | 6" x 6" x 2" Copper Tee | 0,39 | 9,54 | 0,04x |
| 570-120 | 3" x 12" Galvanized Nipple | 0,51 | 7,59 | 0,07x |
| W 10107 | 4" Copper Sweat Fitting | 0,39 | 2,10 | 0,19x |

**Placeholders confirmados por repetição** em produtos de tamanhos diferentes:
`0,05` em 25 produtos, `0,95` em 25, `0,02` em 15, `0,32` em 14, `0,35` em 12,
`0,51` em 11. Mesmo padrão do `2.19` dos Navien.

### Arquivos

- `mueller_peso_SUBestimado_IMPORTAR.csv` (160) — direção segura, sobe peso
- `mueller_peso_SUBestimado_DETALHE.csv` — com part number, razão e título
- `mueller_peso_SOBREestimado_REVISAR.csv` (488) — **não importar sem conferir**,
  porque baixa peso e peso menor faz o λ aprovar frete grátis
- `mueller_peso_rollback.csv` — peso atual dos 648

**79 continuam sem casar.** Não investigados.

## §57 — Correção do Mueller: o casamento por UPC estava furado, e caí no defeito por-pé

Os arquivos das §55 e §56 estavam contaminados. **Removidos e refeitos.**

### Defeito 1 — casamento por UPC

**756 dos 1.353 produtos (56%)** tinham o part number extraído do título
divergindo do part number que o UPC casou. Ou o barcode da loja está errado, ou
UPCs se repetem entre planilhas e meu dicionário guardou o primeiro. De qualquer
forma, **metade dos meus "casamentos" apontava para outro produto.**

Pegou porque o arquivo dos que "viram elegíveis a frete grátis" mostrava:

```
part# LH24020   titulo diz "LH24010 2-1/2" x 20' Copper"
part# KH20020   titulo diz "KH14020 2" x 20' Copper"
```

O part number impresso não era o do título. Foi o que puxou o fio.

### Defeito 2 — o por-pé, que já está no CLAUDE.md

```
2-1/2" x 20' Copper Tube   loja 49,60 lb   planilha 2,48
```

**2,48 lb é o peso por PÉ.** Vinte pés dão ~49,6 — a loja estava certa e a
planilha é por-pé. É exatamente a classe que o `CLAUDE.md` manda filtrar:
*"a planilha do fornecedor guarda valor por pé em itens vendidos por
comprimento. Nunca aplicar em bloco sem filtrar essa classe."* **Apliquei em
bloco.** A regra estava escrita, por mim, e eu não a segui.

### Método corrigido

- **Só part number do título.** UPC abandonado como chave.
- **114 excluídos** por serem vendidos por comprimento — planilha de tubo,
  pré-cortado ou line set, ou título com medida em pés.

### Resultado limpo

| | | |
|---|---|---|
| SUBestimados | **165** | sobe peso — seguro, THS deixa de pagar frete |
| SOBRE seguros | **597** | baixa peso mas **não muda elegibilidade a frete grátis** — só corrige a tarifa cotada |
| viram elegíveis a frete grátis | **39** | decisão do Gabriel |

**A separação por risco é o que importa**: dos que ficam mais leves, só 39
passam a ganhar frete grátis pelo λ. Os outros 597 já eram elegíveis ou seguem
reprovados — corrigir o peso deles só para de cobrar a mais do cliente.

Arquivos: `mueller_peso_SUB_IMPORTAR.csv`, `mueller_peso_SOBRE_seguro_IMPORTAR.csv`,
`mueller_peso_vira_freeship_DECIDIR.csv`, `mueller_peso_rollback.csv`, mais os
dois `_DETALHE` com part number, razão, preço e λ antes/depois.

## §58 — A barra de anúncio diz um número errado

`Free shipping over $99 on 8,900+ items`. **São 8.693** com a tag
`free-ship-eligible`, de 14.883 produtos.

Recomendado, em ordem: (1) tirar o número — `Free shipping on orders over $99`,
não envelhece; (2) usar o número do catálogo, que é verificável —
`Free shipping over $99 · 14,000+ parts in stock`; (3) trocar o eixo para o
diferencial real, que o Marchin expôs — `Hard-to-find and discontinued parts ·
Free shipping over $99`.

**Não** trocar 8.900 por 8.693: número exato e ímpar parece erro de sistema e
exige manutenção toda vez que a tag mudar.

## §59 — Mueller importado e verificado: 762 pesos corrigidos

`mueller_peso_SUB_IMPORTAR.csv` (165) e `mueller_peso_SOBRE_seguro_IMPORTAR.csv`
(597) importados pelo Matrixify em 18/09, 165/165 e 597/597 `Updated`.

**Verificado por bulk operation** — JSONL baixado com `curl`, comparação em
disco, sem passar pelo canal da conversa. **762 de 762 conferem.**

Separando como manda a regra: **76 batem na casa exata**, **686 diferem só pelo
arredondamento de 2 casas** do Shopify, **0 divergências reais**.

Os 33 que a primeira checagem marcou como divergentes eram **convenção de
arredondamento**, todos com delta de exatamente 0,005 lb: valores terminados em
5 na terceira casa, como 1,025 → 1,030 e 0,105 → 0,110. **O Shopify arredonda
meio para cima; o `round()` do Python arredonda meio para o par**, então
`round(1.025, 2)` dá 1,02 e o Shopify gravou 1,03. Vale registrar junto com a
regra do arredondamento que já está no `CLAUDE.md`: ao conferir peso, comparar
contra arredondamento **meio para cima**, não contra o `round()` do Python.

Rollback em `mueller_peso_rollback.csv`, com o peso anterior dos 801.

**Ainda aberto**: `mueller_peso_vira_freeship_DECIDIR.csv` — 39 produtos que,
com o peso corrigido, passam a ser elegíveis a frete grátis pelo λ. Não
importados. São conexões pequenas e baratas (press de carbono 1/2" a $27, união
galvanizada 1/4" a $13), não tubo de 20 pés — a lista ficou plausível depois de
tirar o UPC e os itens vendidos por comprimento.

## §60 — Triagem de fabricantes: o método da Mueller não generaliza

Critério do teste barato, aprovado antes de rodar: **o fabricante publica lista
de preço em Excel com coluna de peso por peça?** Se a lista só sai em PDF de
preço, não vai ter. Foi assim que a Mueller rendeu 762 pesos.

Resultado nos quatro testados depois da Mueller:

| Fabricante | Produtos THS | Resultado |
|---|---|---|
| Charlotte Pipe | 415 (`PVCF` 213, `ABSF` 202) | Reprovou. `ABS-426` e `P-426-PF` têm `Size \| UPC# \| No. Per Carton \| No. Per Pallet \| List Price Each`, zero peso. O `TM-PL.pdf` tem peso, mas é `WT. PER 100 FT.` — peso de tubo por 100 pés, a classe por-pé de novo, e os produtos da THS são conexões |
| Sioux Chief | 538 | Fora por `robots.txt`: `Disallow: /` no site inteiro, e `/downloads/` explícito por cima. A autorização do Gabriel não cobre site que não é dele; passar de um bloqueio exigiria falsear user-agent |
| Legend Valve | — | Reprovou. Lista de preço são 30 PDFs por família em `/documents/DG/`. Colunas: `Part No \| UPC Code \| Description \| Size \| Configuration \| List Price \| Cs/Ct`. **Zero** ocorrências de `weight`/`wt.` nos três PDFs completos baixados (Ball Valves, Malleable Fittings, PEX Fittings) |
| Pasco | — | Reprovou. Sem Excel. Catálogo em 10 seções PDF. Nas seções A–D (7.100 linhas) só 2 hits de "weight", ambos texto de marketing: "lightweight design" e "standard weight soil pipe". O único peso real é uma linha de oakum (4592, 6", 30 lbs) |

**Conclusão: a Mueller é a exceção, não o padrão.** Ela publica planilha Excel de
preço com coluna `EA WGT` por peça. Os outros publicam preço sem peso nenhum.
Não vale continuar varrendo fabricante por fabricante procurando a mesma coisa —
o teste custa pouco, mas a taxa de acerto observada é 1 em 5.

Saldo do caça-dimensões inteiro: **762 pesos corrigidos e verificados, todos
Mueller, e nenhuma dimensão**. Dimensão de embarque não é publicada por nenhum
fabricante nem por nenhum dos concorrentes testados. Dead end confirmado.

**O que ainda pode destravar o assunto** é o teste de checkout do
`TOTO-THU441.10J-A` para a Califórnia, que está na mão do Gabriel: nunca foi
verificado que a dimensão faltando é o que causa a cotação por item. Aquele
produto **tinha** dimensão e mesmo assim foi cotado como dois pacotes
($43,68 num item de $23,43). Se o teste mostrar que a dimensão não é a causa,
os 11.301 faltantes deixam de ser prioridade e o problema é outro.

## §61 — productType: 16 corrigidos, 3 em aberto, 2 anotacoes minhas retratadas

Varredura do catalogo inteiro (14.883 produtos, 588 tipos distintos, nenhum
vazio) pelo canal limpo: `bulkOperationRunQuery` + `curl`.

**Duas anotacoes minhas anteriores estavam erradas e ficam retratadas:**

- **Hydro Separators nao estao classificados como adaptador.** Os 4 da loja
  (Caleffi 548066A, 548067A, 548096A, 548097A) estao em `Hydro Separators`.
- **O UV2400U1000/U em `Air Cleaners & Filters` nao e defeito.** E equipamento
  de tratamento de ar e nao existe tipo melhor entre os 588. A lampada de
  reposicao UV2400XLAM1/U esta no mesmo lugar, coerente. Eu tinha exagerado.

**Heuristica que rendeu**: mesmo modelo, acabamento diferente, tipo diferente.
Isso e inconsistencia pura e nao depende de eu julgar categoria. Deu 11 grupos,
todos reais. A heuristica anterior — familia de modelo com tipo minoritario —
deu 8 candidatos e 6 falso positivo: o sufixo `-MH` do Rheem e literalmente
Manufactured Housing, "Slide Bar" sozinho e slide bar mesmo, e o rebuild kit
AM100-002RP e acessorio mesmo. **A taxonomia de 588 tipos e granular de
proposito**; nao tratar minoria como erro.

**Caso instrutivo — a maioria pode ser a errada.** O `T90331` "Tub and Shower
Drain Covers" tinha 2 acabamentos em `Tub-Shower Trim Sets` e 1 em
`Shower Drains`. Capa de ralo nao e trim set. Os tres foram para `Shower Drains`.
Por isso **nao se aplica maioria automatica**.

**16 aplicados por API e verificados por leitura independente** (rollback em
`producttype_rollback.csv`):

| Produto | De | Para |
|---|---|---|
| Resideo S688A1007/U Sail Switch | Air Cleaners & Filters | Controls, Switches & Sensors |
| Resideo AT120B1028/U Transformer | Thermostat Accessories | Transformers |
| Resideo PA404A1025/U Pressuretrol | System Fill Tanks & Autofills | Controls, Switches & Sensors |
| Resideo PA404A1033/U Pressuretrol | System Fill Tanks & Autofills | Controls, Switches & Sensors |
| Moen T90331 Drain Covers | Tub-Shower Trim Sets | Shower Drains |
| Moen T90331ORB Drain Covers | Tub-Shower Trim Sets | Shower Drains |
| Moen A501 Body Sprayer | Bidets & Bidet Faucets | Body Sprays |
| Moen A721 Drop Ell | Tub Spouts | Hand Shower Wall Brackets |
| Moen A721BN Drop Ell | Faucet & Tap Parts & Accessories | Hand Shower Wall Brackets |
| Moen S176 rainshower | Single-Function Shower Heads | Rain Heads |
| Moen S6360ORB Rainshower | Single-Function Shower Heads | Rain Heads |
| Moen T2191BL Valve Trim Kit | Tub-Shower Trim Sets | Pressure Balance Valve Trims |
| Moen T2470BL Posi-Temp Trim | Diverter Valves | Pressure Balance Valve Trims |
| Gerber D481162BN Showerarm | Escutcheons | Shower Arms |
| Gerber D495002 Pop-Up Drain | Faucet & Tap Parts & Accessories | Sink Drain |
| Gerber DA667229BN Cover Plate | Centerset Faucets | Bathroom Sink Accessories |

### Em aberto, para o Gabriel decidir

1. **Moen T2900BL / T2900BN** — mesmo produto ("2-Handle Wall-Mount Valve Trim
   Kit with 3-Setting Integrated Diverter"), um em `Tub-Shower Trim Sets`, outro
   em `Pressure Balance Valve Trims`. Sendo **2-handle nao e pressure balance**.
   Proposta: `Diverter Valve Trims` nos dois.
2. **Moen T3111 / T3111ORB** — Moentrol, um em `Pressure Balance Valve Trims`,
   outro em `Volume Control Trims`. Moentrol e os dois ao mesmo tempo. Tanto faz
   qual, mas tem que ser o mesmo nos dois.
3. **Gerber G0021187CT** — quase errei aqui. E o **unico** produto do tipo
   `Two-Piece Toilets` da loja inteira e o titulo diz "1pc", entao eu ia mover
   para `One-Piece Toilets`. Mas o `G0021187` sem sufixo esta em
   `Toilet Bowls Only`, e **one-piece nao tem vaso separado**. `CT` na Gerber e
   *Complete Toilet*: vaso + caixa = two-piece completo. **O tipo esta certo; o
   "1pc" do titulo e que esta errado.** Vira correcao de titulo.

### Defeitos de texto achados de passagem

- **`T2470BL`**: titulo diz "tub/shower **valve only**", mas o prefixo `T` da
  Moen e trim, a `seo.description` diz "Trim only", e o chrome identico se chama
  "Valve Trim with Diverter". O titulo esta errado.
- **`D481162BN`**: a `seo.description` dizia "The **5-inch** length sets how far
  the fitting stands off the finished wall" num braco de chuveiro de **12.5"**.
  Corrigido.
- **`AT120B1028/U`**: `seo.description` orfa do tipo antigo, dizia "Honeywell
  Home thermostat accessories cross-reference to the Resideo catalog" num
  transformador. Corrigida.

## §62 — Correcao de titulo: 483 titulos, 281 SEO, 267 alt, 2 descricoes

Varredura do catalogo inteiro por defeito de titulo. Tres frentes, compostas num
**unico CSV de titulo** — porque 12 produtos tinham mais de um defeito e arquivos
separados se desfaziam entre si.

### Frente 1 — mecanico (feito por mim)

`&amp;` duplamente escapado (11), separador solto no fim (71), `(R)` em vez de
`®` (17), espaco duplo, espaco antes de virgula, virgula colada.

**O `&amp;` era defeito real, nao a normalizacao do Shopify.** Provado assim: o
valor cru da API (bulk, JSON, sem escape HTML) traz literalmente `S&amp;DP`; o
`<h1>` sai `S&amp;DP` e renderiza certo por acaso, porque `&amp;` em HTML vira
`&`; mas o `og:title` sai `S&amp;amp;DP`, duplamente escapado. **Onde o valor e
usado como texto puro — feed do Google Shopping, og:title, export — aparece o
lixo.** Isso pesa porque o feed do Google e por onde entram as maiores orders.

### Frente 2 — CAIXA ALTA (207, por agente)

Title Case preservando sigla, marca e medida. Verificado por mim contra o dump:
0 erro, e a afirmacao central do agente — "so muda caixa" — confere em
comparacao case-insensitive.

**Erro meu que o agente pegou**: eu tinha posto `OZ` e `LB` na lista de siglas a
preservar. Unidade nao e sigla; o padrao americano e `2 oz.`, `1.2 lb.`.
Corrigido na composicao.

### Frente 3 — vendor repetido (394, por agente)

**281 sao falso positivo do meu criterio** `count(vendor) > 1`. O criterio pega
nome de linha: `GROHE BRUSHED NICKEL` e nome oficial de acabamento em 115 deles,
mais `LegendPress`, `nVent CADDY`, `SharkBite Max`, `Flo by Moen`,
`Sammys X-Press IT®`, `TACOGENIE`. Em `US Boiler` o `us` casou dentro de "Fuse".
Sobraram **93 duplicacoes reais** (SharkBite 34, Mustee 33, tekmar 12) e
**20 sufixos** (HeatLink 8, Viega 7).

### Bug meu na composicao

No unico produto que estava em caps **e** em vendor (`Sloan 3325151`), o
fallback da minha funcao de composicao descartava a correcao de caixa e devolvia
o titulo em CAIXA ALTA — porque o titulo sem o vendor nao e substring contigua do
titulo original. Trocado por `difflib.SequenceMatcher`, que extrai o trecho
deletado e o remove **sem depender da caixa**.

### Conferencias rodadas no resultado final

- 0 defeito remanescente (`&amp;`, `(R)`, espaco duplo, separador no fim).
- 2 ainda em caixa alta, ambos legitimos (Jomar listando modelos `JF-100T/S`).
- 0 perda real de part number. Os 14 que o teste acusou eram caixa em token
  descritivo (`1/4HEX`→`1/4Hex`, `6-IN-1`→`6-in-1`, `9X12`→`9x12`).

### Ordem de import

1. `titulo_IMPORTAR.csv` (483)
2. `titulo_seo_IMPORTAR.csv` (281)
3. `titulo_alt_IMPORTAR.csv` (267 imagens em 202 produtos)
4. `titulo_descricao_IMPORTAR.csv` (2)

Rollback de cada um no repo.

### Defeitos que o CSV NAO conserta — precisam de fonte

- **~11 titulos truncados na origem**: Milwaukee Valve "Bronze Gate Valve,
  Non-Rising Stem" (falta o resto), Taco `006e3LCe` termina em "fittings
  needed/sold", Zoeller `912-0010` sem a tensao, Resideo `396021/U`.
- **`Moen 8884 M-PRESS Moen 8881 Commercial Metering Faucet Chrome`** — dois
  part numbers diferentes no mesmo titulo. Nao e redundancia de marca, e erro de
  import.
- ~12 Mustee truncados (`(60" x 36" x`), 6 SharkBite com campo de conexao vazio
  `- ()`, 5 Viega com `Press Press` duplicado.
- `Single Bowl SinksPolypropylene` / `SinksMolded` sem espaco (Mustee).
- `IBC ... V10-Touchecreen` -> "Touchscreen".
- `Sloan 3301151 A11 2 -BX` -> part number corrompido, provavelmente A1102A-BX.
- `Sloan 3335149` -> o titulo inteiro e o codigo
  `EAF-250-BAT-ISM-GR-0.5GPM-AER-IR-IQ-FCT`, sem descricao legivel.
- Varios `seo.title` truncados no meio da frase (ex.: "Bosch 1 Ton Ductless
  Mini-Split, Indoor Universal Wall"). Fora de escopo, nao tocado.
- Tema publicado se chama "THS - colour + type (Claude 08/09)" — grafia
  britanica num nome que eu criei. Interno, nao vai pro cliente.

### Nota sobre agente

Duas frentes de julgamento item a item rodaram em paralelo, com saida **direto
para CSV em disco**, sem passar pela minha saida — que e o canal que ja apagou
linha duas vezes aqui. Validei os dois arquivos contra o dump antes de usar
(handle, id, titulo_atual, e a invariante especifica de cada frente). Isso e o
que torna agente aceitavel neste repositorio: **a saida vai disco a disco e eu
confiro contra a fonte, nao contra o relatorio.**

## §63 — "74 pesos superestimados": na verdade 25, e o enquadramento estava errado

**Peso registrado maior que o do fabricante NAO e defeito por si so.** O
registrado e peso de remessa, o metafield e peso de produto — a diferenca e a
embalagem. Dos 74, **44 tem razao <= 1,3x**, que e exatamente isso. Corrigir
esses seria *subcotar* frete.

### A folga de embalagem e multiplicativa, nao aditiva

Medida nos 44 casos legitimos:

```
razao  mediana 1,112   p25 1,087   p75 1,163
itens  <5 lb  (n=16): razao mediana 1,10   delta mediano 0,13 lb
itens >=5 lb  (n=28): razao mediana 1,14   delta mediano 4,35 lb
```

A **razao** e estavel nos dois grupos; o **delta em libras** varia 33x. Entao a
folga se aplica como multiplicador, nunca como "+N lb". Adotado **x1,15** (o
p75, conservador a favor da loja).

### Contagem alta nao prova placeholder — pico sobre a vizinhanca prova

Primeiro criterio meu ("aparece em >=20 produtos de >=5 fornecedores") acusou
`1,00 lb` (419 produtos) como placeholder. **Errado**: muita peca pequena pesa
1 lb de verdade. O teste que discrimina e o **pico contra a vizinhanca** —
quantos produtos tem peso dentro de +-0,5 lb do valor:

```
 2,19 lb   259 produtos / 25 vendors   pico  43x   <- placeholder
 7,00 lb   165 produtos / 21 vendors   pico 165x   <- placeholder
 0,60 lb   293 produtos / 31 vendors   pico   7x   <- placeholder
 1,09 lb    15 produtos /  5 vendors   pico 0,9x   <- peso proprio
```

Valor **nao redondo** com repeticao alta e impossivel por acaso. Valor redondo
precisa de pico grande para valer como prova.

**Limiar arbitrario esconde sinal**: com `n>=20` o valor `45,00 lb` passou como
"sem sinal". Mas sao 18 produtos em 45,00 e **zero** entre 44,5 e 45,5, em 5
fornecedores diferentes — e pico, nao peso de caixa de familia.

### O filtro final e de dinheiro

Peso superestimado so custa se (a) tira o item do frete gratis ou (b) infla a
cotacao UPS que o cliente paga. **Dos 25 corrigidos, 14 ja tem
`free-ship-eligible`** — nesses o peso registrado nao muda um centavo do que o
cliente paga; o custo real da loja depende do peso fisico, nao do cadastrado.
O impacto concentra-se nos 11 sem a tag.

### O caso grande

`RHEE-ELDS30-FTB-208`, $3.697,68, registrado em **350,00 lb** contra 105 no
fabricante. Os 5 produtos de exatamente 350,00 lb no catalogo sao todos Rheem,
mas os outros quatro sao comerciais pesados de **85 e 98 galoes** ($8.163 a
$10.825) que pesam 350 lb mesmo. O de **30 galoes** herdou o peso da familia.
Reprovou no teste de pico (1 so fornecedor) e mesmo assim e defeito claro — por
isso o teste de pico entra como suficiente, nunca como necessario.
Novo peso **120,75 lb**: volta a caber no teto de 150 lb da UPS Ground, ou seja
sai de Freight e volta a poder ser cotado por UPS.

### Arquivos

`peso_superestimado_IMPORTAR.csv` (25), `_rollback`, `_DETALHE` (com lambda antes
e depois e a coluna `vira_elegivel`).

**7 viram elegiveis a frete gratis pelo lambda depois da correcao** — mas isso
**nao acontece sozinho**, porque elegibilidade mora na tag, nao no peso. Decidir
a tag e passo separado.

### Nao corrigidos, e por que

- **44 com razao <=1,3x**: embalagem. Nao mexer.
- **5 com razao >1,3x mas peso unico no catalogo** (`BLAN-441398` 35,5 vs 13,0,
  `GERB-28-990` 56,3 vs 34,1, `BLAN-401927`, `BLAN-440213`, `GERB-D481027BN`):
  peso proprio, sem repeticao. Pia Blanco vai em caixa grande; 2,7x de razao
  pode ser caixa de verdade. Sem segunda fonte nao da para decidir.

## §64 — Google Ads: NAO aumentar o budget em 30% ainda (20/09/2026)

Pergunta do Gabriel: ja da para subir o daily budget em 30%? **Resposta: nao.**

Dados pela conexao direta do Windsor.ai, conta Google Ads `192-200-0533`
(The House Supplier), janela 21/08 a 19/09/2026.

### O achado que trava a decisao

**A campanha ja gasta $320/dia contra um `budget_amount` de $160.** Cinco dias
seguidos em exatamente 2x:

```
15/09 $320,02   16/09 $323,18   17/09 $320,88   18/09 $320,16   19/09 $316,73
```

Ou o valor foi alterado e o Windsor reporta o antigo, ou o Google esta
compensando a parada de **11 a 14/09** (gasto $0,41 / $0 / $0 / $11,86 — motivo
nao investigado). De qualquer forma, **pedir +30% sobre $160 quando a realidade
e $320 e decidir no escuro**. Confirmar no painel antes de qualquer coisa.

### Numeros

| | Ads (proprio) | GA4 ultimo clique |
|---|---|---|
| Conversoes 30d | 35 | 30 |
| Receita 30d | $13.536,14 | $10.712,58 |
| Gasto 30d | $2.785,12 | $2.785,12 |
| ROAS | 5,25 (so a campanha principal) | **3,85** |

A diferenca de 26% e atribuicao normal (modelo proprio + view-through contra
ultimo clique), **nao e defeito de configuracao** — eu levantei esse alarme e
ele nao procedia. O alarme real era outro: a consulta da Shopify que eu usei
como contraprova tinha vindo da **loja errada** (ver §"shopDomain" no CLAUDE.md).

### Por que nao aumentar

**1. O aumento ja aconteceu e o ROAS caiu.** O gasto saiu de ~$130/dia para
~$320/dia em 15/09. Esse e o teste de ROAS marginal, e ja rodou no campo:

```
15-19/09 a $320/dia:  gasto $1.600,97   receita GA4 $5.480,88   ROAS 3,42
contribuicao: 5.480,88 x 0,303 - 1.600,97 = +$59,74 em 5 dias  (~$12/dia)
```

Contra o equilibrio de 3,30, isso e **empate, nao lucro**.

**2. O ROAS de 30 dias e carregado por uma order.** O dia 10/09 sozinho fez
**$3.190,60 de $10.712,58** (30%), e dentro dele esta a Navien da #THS1026
(~$3.015 em produto; o GA4 nao conta frete e imposto, por isso nao bate os
$4.247,67 do pedido). **Sem ela: ROAS 2,76.** O periodo anterior a pausa, sem a
Navien, da 2,84. **No dia mediano a campanha nao se paga** — ela depende de
aparecer uma order grande.

**3. Ha desperdicio que financia o aumento de graca.**
- Campanha `Heating Equipment Supplies`: **$207,17 em 446 cliques, ZERO
  conversao** em 30 dias.
- Os 281 impressoes de Shopping pago em posicao 1 com **zero clique** nos tres
  SKUs Moen (§ do carrossel) estao dentro dessa mesma verba.

### Ordem recomendada

1. Confirmar no painel qual e o budget real hoje: $160 ou $320.
2. Pausar `Heating Equipment Supplies`.
3. Rodar mais ~30 dias no nivel atual e julgar por **contribuicao do dia
   mediano**, nao por ROAS com a baleia dentro.
4. So entao aumentar. A demanda existe: `search_budget_lost_impression_share`
   segue em **80–89%** e a `search_impression_share` e de **9,99%**. O gargalo
   nao e leilao, e margem.

### Pendente de conferencia

Cruzar com a Shopify nao foi possivel: **eu derrubei a conexao** chamando
`switch-shop` ao perceber que as respostas vinham da TFAS. Precisa de `/mcp`
numa sessao interativa. Quando voltar, conferir `purchase_revenue` do GA4
contra `gross_sales` da THS no mesmo periodo — o GA4 deu **$16.362,07 em 52
transacoes** em 30 dias, e uma consulta anterior minha na Shopify dava $14.637
no **ano inteiro**, o que nao fecha e ficou sem explicacao.

### Achado lateral

Fontes que converteram em 30 dias, por receita GA4: `google/cpc` $10.712,58 (30),
`(direct)` $2.982,21 (8), `google/organic` $1.349,93 (4), `bing/cpc` $696,71 (5),
**`chatgpt.com`** $300,76 em 3 transacoes (`/feed` 2 + `/ai-assistant` 1, em 99
sessoes). O ChatGPT ja e canal de receita da loja, com taxa de conversao de 3%
— melhor que a do `google/cpc` (0,66%). Nao explorado.

## §65 — Correcao do §64: o budget FOI aumentado (23/09/2026)

**O §64 acima esta desatualizado e nao deve ser lido como estado atual.** Ele
recomendava nao aumentar; o Gabriel aumentou. Decisao dele, tomada.

`budget_amount` agora e **$208** (era $160 — exatamente +30%).

**Achado de metodo que vale mais que o numero**: o `budget_amount` do Windsor e
o valor **atual** do budget, replicado em toda linha de data — **nao e
historico**. As linhas de 18 e 19/09, que em 19/09 vinham com $160, hoje vem com
$208. **Nunca ler `budget_amount` de uma data passada como se fosse o que
valia naquele dia.**

Isso tambem resolve o "2x o budget" do §64: o gasto de ~$320/dia entre 15 e
19/09 era o Google compensando a parada de 11–14/09. Ja normalizou para
$207–254/dia, batendo com o novo teto de $208.

### Primeiros dias no nivel novo

| Dia | Gasto | Receita GA4 `google/cpc` |
|---|---|---|
| 20/09 | $253,71 | **$5,58** |
| 21/09 | $206,82 | $1.971,78 |
| 22/09 | $214,36 | inutilizavel |

**22/09 nao serve**: o GA4 ainda processava e jogou 345 sessoes em `(not set)` e
227 em `(data not available)`. **Atribuicao do dia anterior nunca serve** —
esperar 48h antes de usar `session_source_medium`.

Nos dois dias limpos: ROAS **4,29**, contribuicao **+$138,61** (~$69/dia),
contra ~$12/dia da janela anterior. Melhor — **mas o mesmo padrao**: 21/09
carregou tudo e 20/09 gastou $253 para faturar $5,58.

### Criterio de corte proposto (falta o Gabriel confirmar)

Rodar ate **05/10** (duas semanas cheias no nivel novo) e julgar por
**contribuicao acumulada**, nao por ROAS de dia bom. Abaixo de ~$50/dia, voltar
para $160.

### Outros

- **21/09: order de $3.812,97 por `google / organic`** — maior que qualquer
  coisa que o pago trouxe no mes. Nao identificada ainda.
- `Heating Equipment Supplies` **parou de aparecer com gasto desde 10/09**.
  Provavelmente pausada.
- **Nada foi importado ate 23/09**: os 483 titulos, 281 SEO, 267 alt, 2
  descricoes e os 25 pesos seguem parados. Conferido ao vivo no site — os
  quatro titulos de amostra continuam com `(R)`, `&amp;`, traco solto e caixa
  alta. O carrossel tambem segue na ordem antiga.
- **O MCP da Shopify voltou apontando para a TFAS de novo** em 23/09. A regra
  do CLAUDE.md pegou antes de eu fazer besteira. Continua precisando de `/mcp`.

## §66 — Correcao: a maior order do mes nao foi organica, foi Shopping

O Gabriel perguntou se `google / organic` nao seria o `sag_organic` pago. Eu
respondi que nao e dei uma tabela. **A tabela estava incompleta e a conclusao
sobre a order grande estava errada.** Ele estava certo em desconfiar.

**Escopo exato do erro**: na janela 21/08–19/09 usada para a analise de verba,
a receita de `google / organic` ($1.349,93) era mesmo toda de busca organica —
aquela tabela estava certa. O erro foi no caso de **21/09**, onde chamei a order
de $3.812,97 de organica.

### Split correto, 21/08 a 21/09, por campanha

| source/medium | channel group | campanha | sessoes | trans | receita |
|---|---|---|---|---|---|
| `google / cpc` | Paid Shopping | SHOPPING GABRIEL | 4.777 | 35 | $12.689,94 |
| `google / organic` | **Organic Shopping** | **Shopping Free Listings** | 188 | 1 | **$3.812,97** |
| `google / organic` | Organic Search | `(organic)` | 255 | 4 | $1.349,93 |
| `google / product_sync` | Organic Search | `sag_organic` | 21 | 1 | $82,83 |
| `google / cpc` | Cross-network | **Heating Equipment Supplies** | **291** | **0** | **$0** |
| `google / cpc` | Paid Search | `sag_organic` | 8 | 0 | $0 |

### `Heating Equipment Supplies` e pior do que o §64 dizia

Nao e so "$207,17 sem conversao". Sao **291 sessoes e zero transacao**, e o
channel group e **Cross-network** — indica Performance Max ou Demand Gen, nao
busca simples. **Pausar continua sendo a recomendacao, mas antes entender que
tipo de campanha e**: PMax gasta em superficies que ninguem escolheu.

### A maior order do periodo custou zero de midia

$3.812,97 de 188 sessoes, maior que a Navien da #THS1026.

**Evidencia de que nao foi paga**: em 21/09 o Ads reportou $2.035,55 de valor de
conversao, que casa com a linha `google / cpc` do GA4 ($1.971,78) e **nao**
inclui os $3.812,97.

**O que NAO esta provado**: que "Shopping Free Listings" seja mesmo superficie
gratuita, e nao outro rotulo enganoso como o `sag_organic`. **Confirmar em
Merchant Center -> Performance -> por superficie**, comparando cliques de free
listings contra os do Ads no dia 21/09. Se confirmar, e o achado mais
importante da semana.

## §67 — Shopify de volta na THS; a order grande e a #THS1063, via sag_organic NAO faturado

Conferido antes de tudo: `shop.myshopifyDomain` = **`1vy05a-x6.myshopify.com`**,
"The House Supplier". Loja certa.

### Receita reconciliada (fecha a pendencia do §64)

Shopify, 21/08–19/09: **55 orders, $18.762,04 bruto, $15.810,94 liquido,
$18.690,49 total.** GA4 no mesmo periodo: 52 transacoes, $16.362,07.

Bate: o GA4 perde 3 orders (bloqueador, consentimento), e o `purchase_revenue`
cai entre liquido e bruto. **O "$14.637 no ano inteiro" que eu usei em 18/09
estava errado** — provavel artefato da consulta `GROUP BY product_vendor`. Nao
investiguei o porque. **Para receita total, usar a consulta sem agrupamento.**
A analise de verba do §64 usou GA4 e segue valida.

### A order de $3.812,97 e a #THS1063

- **21x Resideo L4029E1029/U** Limit Control, fixed 200 F, 3 in insert, Manual
  Reset. Subtotal $3.812,97, total $4.120,24. 21/09/2026 14:23 UTC.
- **Pedido de contratante em quantidade.** Maior order do mes.
- Jornada na Shopify: primeira **e** ultima visita com
  `utm_source=google`, `utm_medium=product_sync`, `utm_campaign=sag_organic`.
- **O Google Ads NAO contou essa order.**

Prova — as cinco orders `sag_organic` de 21/09:

| Order | Produto | Subtotal |
|---|---|---|
| #THS1062 | Navien NHW700-180AI-NG | $1.455,00 |
| **#THS1063** | **21x Resideo L4029E1029/U** | **$3.812,97** |
| #THS1064 | Suntemp SER-3/SEL-3 x6 | $167,76 |
| #THS1065 | 2x Resideo TH3210D1004/U | $157,38 |
| #THS1066 | DiversiTech 36x60x3 pad | $191,64 |

As quatro sem a #THS1063 somam **$1.971,78 = exatamente** a linha `google / cpc`
do GA4 do dia. O Ads reportou $2.035,55. A #THS1063 ficou fora dos dois.

Casos menores confirmam o padrao: #THS1060 e #THS1068 ($82,83 cada, Resideo
PRO 3000) aparecem no GA4 como `google / product_sync` — sem `gclid`, nao
faturados. #THS1061 ($5,58) aparece como `google / cpc` — pago. **Os tres tem
`sag_organic` na Shopify.**

### O mecanismo

O canal Google da Shopify carimba `sag_organic` em **todo** link do feed do
Merchant — anuncio pago e listagem gratuita. Clique pago chega tambem com
`gclid`; clique gratuito nao. **O GA4 separa pelo `gclid`; a Shopify so ve o UTM
e mostra `sag_organic` para os dois.**

### Consequencia para a regra do CLAUDE.md — PENDENTE DO GABRIEL

A regra atual diz que `sag_organic` **e** o Shopping pago e nunca pode ser
chamado de free listing. **A intencao esta certa**: nao tratar receita de
Shopping como custo zero — de ~$16,5k de Shopping no periodo, ~$12,7k foram
pagos. **A letra esta errada**: a #THS1063 prova que `sag_organic` nao e pago
nem gratuito por si so.

Texto proposto, **nao aplicado** — a regra existe porque eu errei nisso varias
vezes e o Gabriel corrigiu, entao muda so com o OK dele:

> `sag_organic` + `product_sync` e o **carimbo do feed do Merchant**, nao a
> natureza do trafego. Cobre anuncio pago **e** listagem gratuita. **Nunca
> concluir "gratuito" pelo UTM** — a maior parte e paga (~77% em 09/2026). O
> discriminador e o `gclid`: no GA4, `google / cpc` = pago; `Shopping Free
> Listings` = nao faturado. Prova: #THS1063, $3.812,97, 21/09.

### Achado lateral

A maior order do mes e um contratante comprando 21 unidades de uma peca de
reposicao de caldeira. Reforca o ponto do post do LinkedIn: o comprador que
paga as contas da THS e o profissional, nao o dono de casa.

## §68 — Titulos importados e verificados: 483 + 281 + 267 + 2, todos exatos (23/09/2026)

Antes do import, conferencia de frescor: o CSV era de 18/09; bulk de 23/09
mostrou que **nenhum** dos 483 titulos, 281 SEO, 267 alt e 2 descricoes tinha
mudado na loja nesse intervalo, e as 267 URLs de imagem ainda existiam. So entao
liberado.

Import pelo Matrixify, 23/09 04:52–04:59: 483, 281, 202 e 2 `Updated`. O alt
reporta **202** porque conta produto — o CSV tinha 267 imagens em 202 produtos.

**Verificado por bulk + curl, byte a byte contra o CSV:**

| Arquivo | Exato | So normalizacao | Divergente |
|---|---|---|---|
| titulo | 483 | 0 | 0 |
| SEO | 281 | 0 | 0 |
| descricao | 2 | 0 | 0 |
| alt | 267 imagens | 0 | 0 |

Zero defeito mecanico remanescente nos 483 (`&amp;`, `(R)`, espaco duplo,
separador solto no fim).

Rollback nos `titulo_*_rollback.csv`, se precisar.

**Ainda em aberto do §62**: os ~11 titulos truncados na origem, o `Moen 8884`
com dois part numbers, 6 SharkBite com `- ()` vazio, 5 Viega com `Press Press`,
`Sloan 3335149` que e so codigo, e os `seo.title` truncados no meio da frase.

## §69 — Sugestao de "sale price" do Merchant Center: nao aplicar; e produto nao se julga sozinho

Arquivo do Gabriel: *Sale price suggestions with highest performance impact*,
Merchant Center, 23/09/2026, filtro Effectiveness = High. **496 produtos**,
desconto sugerido de 16% a 20% (mediana 18%). Resideo lidera (58).

### Por que nao aplicar os precos sugeridos

Contribuicao por unidade, com markup 50% e ~3% de cartao
(`= 0,97(1-d) - 0,6667`, em fracao do preco original):

| Desconto | Contribuicao | Queda |
|---|---|---|
| 0% | 30,3% | — |
| 18% | 12,9% | -58% |
| 20% | 10,9% | -64% |

- A 18% off, precisa vender **2,36x** so para empatar, antes de anuncio.
- **ROAS de equilibrio sobe de 3,30 para ~6,4.** Shopping pago roda 3,4–4,3:
  toda venda paga a esse preco da prejuizo.
- **Desconto maximo para o anuncio ainda empatar com ROAS ~3,85: ~6%.**
- **Quebra a regua de frete gratis**: λ ≤ 0,0337 foi derivada com margem 0,303.
  A 18% off, item no limite da regua custa $0,185 de frete por dolar vendido
  contra $0,157 de margem — prejuizo em qualquer carrinho com frete gratis.

O modelo do Google maximiza clique e conversao; nao conhece a margem da loja.
**O valor do arquivo e outro: e um mapa de onde a THS esta acima do mercado.**
Proximo passo, se quiser: amostra de ~20 contra os concorrentes liberados.

"Click uplift 1,30" lido como **+130%**, nao 1,3x — ha valores de 0,44, e
0,44x significaria perder clique ao baixar preco.

### Cruzamento com o gasto por produto do Google Ads (Windsor, 24/08–22/09)

13.386 linhas, lidas 100% em disco. Gasto total $3.252,84 em **9.491 produtos**.

- Os 496 da lista **todos** tiveram impressao; consumiram $1.167,96 (36%).
- 487 com zero conversao ($1.029,13) — **mas o grupo tem ROAS 5,99**, porque 9
  produtos trouxeram $6.999,73. Tirar a lista inteira do pago jogaria fora os 9.

### Produto individual NAO se julga em 30 dias nesta conta

- **~120 cliques por conversao** na conta (5.299 cliques, 44 conv, CPC $0,61).
- Para zero conversao deixar de ser azar (p < 5%): **~359 cliques**.
- **Nenhum dos 9.491 produtos chegou nem a 180.**
- Gasto medio: **~$0,34 por produto por mes.** A campanha espalha verba demais
  para aprender qualquer coisa por produto.

**Regra**: nao excluir produto do pago por "zero conversao" nesta conta sem
antes checar se ele passou de ~3x os cliques por conversao da conta. Julgar por
**grupo** (marca, linha, tipo).

### O sinal que existe e em grupo — Navien

| Navien | Gasto 30d | Conv | Valor |
|---|---|---|---|
| NHW | $65,22 | 2 | $4.470,00 |
| **Outros (NPN, NPE...)** | **$269,88** | 2 | **$132,50** |

80% do gasto de Navien vai para os modelos que nao vendem, ROAS 0,49 contra ~68
no NHW. Confirma com numero do mes o que o CLAUDE.md ja dizia ("o lance esta no
NPE-240A2; quem vende e o NHW-SU"). Os tres primeiros da lista do Merchant
(NPN-160U, NPE-150S2, NPN-180E) sao desse grupo.

**Acao proposta**: tirar Navien nao-NHW do Shopping pago ou baixar prioridade;
~$270/mes que hoje retornam $132. Pendente do Gabriel.

## §70 — Ahrefs/organico: crescimento real, separado do Shopping (23/09/2026)

Pergunta do Gabriel: algum progresso no Ahrefs?

| Semana | GSC cliques | GSC impr. | GSC posicao | GA4 busca organica | GA4 Free Listings |
|---|---|---|---|---|---|
| 03/08 | 5 | 163 | 61,9 | 16 | 0 |
| 10/08 | 9 | 458 | 58,2 | 22 | 0 |
| 17/08 | 10 | 2.810 | 54,5 | 20 | 0 |
| 24/08 | 11 | 5.370 | 53,6 | 21 | 1 |
| 31/08 | 39 | 13.584 | 32,7 | 29 | 40 |
| 07/09 | 90 | 22.077 | 27,1 | 69 | 98 |
| 14/09 | 111 | 20.741 | 20,6 | **98** | 42 |

GA4 "busca organica" = `google` + `Organic Search` + campanha `(organic)`.

- **Busca organica cresceu ~5x em um mes** (~20 -> 98 sessoes/semana), confirmado
  no GA4, independente do Shopping.
- **O salto de impressoes do GSC em 31/08 e em boa parte Free Listings**, que
  comecou a aparecer exatamente nessa semana. O GSC mistura as duas coisas; a
  posicao media de 53 -> 20 tambem e contaminada por isso.
- Site Audit de 22/09: **health 100**, 64.991 URLs, 25 erros. O pico de 3.113
  orfas falsas de 16/09 nao voltou.
- DR 7, parado desde 31/08.
- Receita da busca organica no periodo: $1.349,93. Volume subiu, conversao nao
  acompanhou ainda.
- **Causa nao atribuida.** O salto comeca 31/08–07/09, antes de boa parte das
  descricoes e titulos entrarem. Pode ser so o Google indexando loja nova. Nao
  creditar ao trabalho sem prova.

**Regra de leitura**: crescimento organico se mede no GA4 filtrado por
`Organic Search` + `(organic)`, nunca pela posicao media do GSC desta
propriedade — ela mistura superficie de Shopping.

## §71 — O que puxa o organico: cauda longa, nao as descricoes Resideo (ainda)

GA4, `google` + `Organic Search` + `(organic)`, por pagina de entrada. 7.021
linhas lidas 100% em disco; 305 sessoes organicas no periodo.

| Tipo de pagina | 03/08–30/08 (4 sem) | 31/08–21/09 (3 sem) |
|---|---|---|
| Produto (nao Resideo) | 6 | 99 |
| Home | 60 | 51 |
| Colecao | 3 | 35 |
| Paginas de guia/conteudo | 0 | 15 |
| Produto Resideo | 0 | 6 |

- **Crescimento e cauda longa**: os 99 de produto espalhados em dezenas de
  paginas, nenhuma com mais de 5. Padrao de loja nova sendo indexada.
- **Resideo: 6 sessoes**, apesar das 607 descricoes reescritas. A ultima leva
  entrou ~18/09 — so 3 dias de dado. **Nao da para dizer ainda se as descricoes
  funcionam**; da para dizer que nao explicam o crescimento ate aqui.
- **Paginas de conteudo tecnico comecaram a trazer busca**:
  `/pages/copper-pipe-dimensions-specs` (5), `/pages/pvc-cpvc-pipe-dimensions-specs`
  (4), `/pages/strainer-selection-guide` (2). Perfil de contratante.
- As 3 conversoes organicas do periodo novo entraram pela home ($534).

### REABRIR em ~20/10/2026

Mesmo corte, comparando **produto Resideo contra o resto do catalogo**, com 4+
semanas depois de 18/09. So ai da para atribuir (ou nao) as descricoes.

## §72 — GSC pelo Windsor: Shopping x web separados, e part number e onde a loja compete

Conector `searchconsole` do Windsor, `sc-domain:thehousesupplier.com`,
24/08–21/09. 12.160 linhas lidas 100% em disco. **Vantagem sobre o GSC do
Ahrefs: tem `queryparams`**, entao da para separar URL com UTM (superficie de
Shopping) de URL limpa (web).

### Shopping x web

| Superficie | Impressoes | Cliques | CTR | Posicao pond. |
|---|---|---|---|---|
| Shopping (URL com `utm_`) | 14.382 | 27 | 0,19% | **2,3** |
| Web (URL limpa) | 32.267 | 26 | 0,08% | **48,2** |

- **Na busca web a loja esta em media na pagina 5.** A "posicao 20" do Ahrefs
  era media das duas superficies.
- **Shopping: posicao 2,3 e CTR 0,19%.** Aparece no topo e quase ninguem clica
  — o padrao do Moen, na loja inteira. Bate com a lista de sale price do
  Merchant (§69): a loja perde no preco.
- Cliques por query sao piso: o GSC omite queries anonimizadas nesse corte.
  Nao comparar direto com sessoes do GA4.

### Part number e o unico terreno em que a loja compete

| Query web | Queries | Impressoes | Posicao |
|---|---|---|---|
| PN que esta num titulo da loja | 209 | 419 | 31,6 |
| PN que NAO esta em nenhum titulo | 821 | 3.054 | 25,7 |
| Generica | 6.472 | 28.794 | 50,9 |

Teste "PN no titulo da pagina que ranqueia": 29,9 com x 33,3 sem, amostra
pequena e confundida. **Nao prova que por o PN no titulo sobe posicao.**

### O caso Mueller black iron

1.223 das 1.596 impressoes de PN-fora-do-titulo em pagina de produto sao
Mueller, todas no formato `M1X90E`, `M2XCPL`, `M38X90SE`, `M212X4N`… O Google
casa a familia mas erra a peca: `m38x90se` (3/8" street elbow) cai em
`520-144 1" x 1/2" Black Iron Elbow`; `m2xcpl` (2" coupling) em
`520-009 2-1/2" Black Iron Elbow`.

**Origem do formato desconhecida.** Nao esta nos 5.425 part numbers nem nas
descricoes extraidas das planilhas da Mueller — ressalva: so 4 colunas das
planilhas foram guardadas. Duas hipoteses opostas:
- codigo de distribuidor/concorrente que o contratante usa -> vale "Alt Part #";
- **busca automatizada**: dezenas de codigos, todos com o prefixo identico
  `"mueller black fittings"`, ~20 impressoes cada. Gente nao digita assim.

**Nao mexer em titulo antes de saber a origem.** Teste: procurar 2–3 codigos nos
concorrentes liberados.

### Rheem com codigo alternativo

`21v40-38`, `rheem 21v40-38`, `prog40-38n rh62` (116 impressoes) caem na pagina
certa do 40 galoes, posicao 37–47, sem o codigo alternativo na pagina.
Candidato a "Also known as" — **depois** de confirmar na documentacao Rheem que
e o mesmo modelo.

### Termos genericos

"water leak detection" 1.394 impr pos 48; "sump pump" pos 69; "storage tanks"
pos 35. Com DR 7 nao sobem tao cedo. Nao priorizar.

## §73 — Historico de campanhas e todas as orders da loja (23/09/2026)

### Campanhas Google Ads desde 06/2025 (Windsor, `include_inactive`)

| Campanha | Tipo | Status | Gasto | Conv | Valor |
|---|---|---|---|---|---|
| SHOPPING GABRIEL 8-3-2026 | SHOPPING | ativa | $3.291,72 | 44 | $16.258,91 |
| Heating Equipment Supplies | PERFORMANCE_MAX | **pausada** | $354,73 | 4 | **$0,78** |

- **A THS nunca rodou campanha de Search.** Correcao: o
  `navien tankless water heater` do CLAUDE.md e **termo de pesquisa do
  Shopping**, nao palavra-chave de Search. Eu tinha dito o contrario.
- A PMax contava "conversao" que valia $0,78 no total — nao era compra, era
  micro-conversao. Pausada.

### Orders — 72, de #THS1002 (18/08) a #THS1075 (23/09)

Bulk, loja `1vy05a-x6` conferida. 71 reais (1 cancelada: #THS1055), 0 de teste
marcadas.

- **Produto: $25.238,70.** Ticket mediano $157, medio $355.
- Top 1 = 15%, top 3 = 33%, top 10 = **57%** da receita.
- Frete cobrado: $3.258,22 (13% do subtotal). Desconto: $39,49.
- **Resideo $10.789 (43%), 106 un; Navien $4.654.** Juntos, 61%.
- Recompra: **2 de 69 clientes.**
- Estados: TX 8, CA 8, NY 6, VA 5, PA/IL/NC 4.

Por canal (ultima visita):

| Canal | Orders | Receita |
|---|---|---|
| Google Shopping (`sag_organic`, pago + gratuito) | 41 | $14.670,94 |
| Direto | 12 | $7.256,69 |
| Google organico | 4 | $1.349,93 |
| Bing | 6 | $780,59 |
| Sem jornada | 4 | $768,15 |
| ChatGPT | 3 | $403,40 |

**"Direto" esconde Shopping**: a #THS1026 (Navien, $3.015) teve primeira visita
`sag_organic` e ultima direta. O ultimo clique subcredita o Shopping.

### Estornos: 8 orders, $2.823,92 (11%)

| Order | Subtotal | Frete | Causa provavel |
|---|---|---|---|
| #THS1006 | $4,53 | $15 | **preco por pe**: Mueller 3/8" x 10' copper, hoje $45,30 (x10) |
| #THS1009 | $2,96 | $15 | **preco por pe**: Charlotte 2" x 20' PVC, hoje $29,60 (x20) |
| #THS1064 | $167,76 | **$351,29** | **frete para o Alasca** (Suntemp end caps) |
| #THS1028 | $1.256,50 | $349,00 | frete de banheira Maax para MN — motivo nao confirmado |
| #THS1010 | $216,98 | $0 | American Standard via ChatGPT — motivo nao visivel |
| #THS1018 | $86,25 | $15 | Gerber tank — motivo nao visivel |
| #THS1056 | $101,40 | $61,84 | TOTO seat — motivo nao visivel |
| #THS1002 | $0,50 | $11,18 | teste (50 toques na jornada) |

- **Os dois de preco por pe ja estao corrigidos** — exatamente pelo fator do
  comprimento. Varredura dos 561 produtos com comprimento >= 10 ft no titulo:
  a maioria dos baratos e legitima (fita, PVC fino, PEX). **Sobram 2
  suspeitos**: `ANVI-AS500-EH-20-GR` Anvil 13/16" x 20' strut a $3,66 e
  `ANVI-AS200-EH-20-GR` Anvil 1-5/8 x 20' strut a $5,31. Perfilado de 20' custa
  ~$30–70.
- **Detector por mediana do tipo falha** quando o tipo inteiro tem o defeito —
  ele nao pegou nenhum dos dois estornados. Usar criterio absoluto.
- **A loja aceita pedido para o Alasca** (a #THS1064 pagou $351 de frete e
  estornou), enquanto a comunicacao diz "contiguous U.S.". Decisao do Gabriel.

## §74 — Search: rascunho de palavras-chave pelo que vendeu; termos de pesquisa bloqueados

O relatorio de **termos de pesquisa do Shopping** (o insumo certo para montar
Search) nao saiu: o **Windsor expirou a sessao 4 vezes seguidas** na mesma
consulta em 23/09. Precisa reconectar o conector.

Rascunho com o que ja estava em disco: `search_keywords_RASCUNHO.csv` — os 55
SKUs vendidos (sem orders estornadas), com part number extraido do titulo e
keyword exata sugerida (`[pn]` e `[marca pn]`), cruzados com as buscas web do
GSC.

**Achado**: dos part numbers que venderam, **so 1 aparece em busca web no GSC**.
`L4029E1029/U` ($3.812,97), `NHW700-199SU-LP` ($3.015), `TH3210D1004/U` (**9
orders**, $1.987,92), `THX321WFS2001W/U` (3 orders) — zero impressao organica.
Quem comprou achou pelo **Shopping**.

Isso muda a pergunta do Search: **alcanca demanda nova ou so disputa com o
proprio Shopping?** O relatorio de termos de pesquisa responde — se as buscas
que converteram ja sao por part number exato e o Shopping ja aparece nelas,
Search em cima delas e canibalizacao. Se nao aparecem, e alcance novo.
**Nao montar a campanha antes desse relatorio.**

Pendente: reconectar Windsor -> puxar `search_term` do SHOPPING GABRIEL
(01/08–hoje) com conversao.

## §75 — Termos de pesquisa do Shopping: o comprador busca "Honeywell" (23/09/2026)

Windsor reconectado; a consulta cheia de `search_term` continuou expirando a
sessao — era o tamanho. Com filtro saiu na hora.

### Os 25 termos que converteram (01/08–22/09)

Quase todos **modelo exato**, e **11 dos 25 tem "honeywell", nenhum tem
"resideo"**: `honeywell th3110d1008` ($794,88), `honeywell thx321wfs2001w t10 pro
smart thermostat with redlink` ($989,19), `honeywell th3110d1008 pro non
programmable digital thermostat` ($530,40), `honeywell home t10+ pro smart
thermostat` ($329,73), `honeywell focuspro 5000`, `honeywell t10 pro`,
`honeywell thermostat th3210d1004`, `www honeywell com thermostat`… Os 11 somam
**$3.345,56** de **$7.163,63** visiveis.

Outros: `th5110d1022` ($499,56), `franke sinks undermount` ($643,42),
`toto ts626t cp` ($250,02), `axiom nc 1s condensate neutralizer`, `studor maxi
vent`, `rheem ap23528 duct diverter`. Tambem aparecem os de orders estornadas:
`aker kds 3448` (Maax, $1.256,50) e `3 8 copper tubing type l` ($4,53, o preco
por pe).

**Cobertura: so 44% do valor convertido** ($7.164 de $16.259). Os termos das
orders Navien, por exemplo, nao aparecem — o Google esconde termo de baixo
volume.

### Os que mais gastaram sem converter (>= $8)

19 termos, quase todos **1 clique caro em item de ticket alto** (`franke cux120`
$24,70, `toto sw4736at40 01` $16,64, `insinkerator evolution pro 880lt`
$14,22) — e o lance por valor fazendo o que faz. O que da para cortar:
**`pexuniverse`, $12,24 por um clique no nome de um concorrente** -> negativar.

### Volume de busca (Ahrefs, EUA/mes; CPC em CENTAVOS)

| Keyword | Volume | CPC |
|---|---|---|
| honeywell t10 pro | 500 | $0,30 |
| honeywell focuspro 5000 | 250 | $0,25 |
| honeywell th3210d1004 | 200 | $0,25 |
| th3210d1004 | 200 | $0,45 |
| honeywell pro 3000 | 200 | $0,20 |
| honeywell t3 pro | 50 | $0,25 |
| honeywell l4029e1029 | 10 | — |
| **resideo** + qualquer desses | **0** | — |

### Decisao do Search (fecha o §74)

- Os termos que convertem **ja sao** o que o Search teria: modelo exato. Search
  em cima deles disputa com o proprio Shopping.
- O que mantem o teste de pe: Shopping aparece (posicao 2,3) e perde o clique
  (CTR 0,19%), provavelmente pelo preco; anuncio de texto nao mostra preco, e o
  CPC estimado e baixo.
- **Se testar: so `honeywell <modelo>` em exata, so modelos que ja vendem, e
  medir Shopping + Search JUNTOS nesses modelos, antes e depois.** Search
  sozinho vai parecer otimo porque rouba venda do Shopping.

### A alavanca maior e de graca: o nome

Titulos Resideo dizem "Resideo"; o comprador busca "Honeywell". Afeta:
- **CTR do Shopping** (quem busca "honeywell t10 pro" ve "Resideo
  THX321WFS2001W/U");
- **organico** — hipotese para as 607 descricoes Resideo terem trazido so 6
  sessoes (§71): o titulo diz uma marca que ninguem busca. **Testar no
  lembrete de 20/10.**
- o Search, se sair.

Pendente do Gabriel: confirmar com o Craig o padrao de nome
("Honeywell Home by Resideo") antes de mudar titulo em massa.

## §76 — Chat de cliente (Navien NPE-180A2 x Ferguson $1.300) e o titulo sem modelo

24/09, chat ao vivo: cliente quer 2 Navien (150k e 180k BTU), cita "NPE 190A2/S2"
(modelo inexistente), depois "NPE-180A2", e diz que a Ferguson vende por $1.300.

Preco e custo na THS (loja `1vy05a-x6` conferida):

| Modelo | BTU | Preco | Custo | Piso (custo/0,97) | Perfil |
|---|---|---|---|---|---|
| NPE-150S2 | 120k | $1.740,00 | $1.160 | $1.196 | THS Standard |
| NPE-180S2 | 150k | $1.972,50 | $1.315 | $1.356 | THS Standard |
| NPE-210S2 | 180k | $2.167,50 | $1.445 | $1.490 | Freight |
| **NPE-180A2** | 150k | **$2.325,00** | **$1.550** | **$1.598** | Freight |
| NPE-210A2 | 180k | $2.617,50 | $1.745 | $1.799 | Freight |
| NPE-240A2 | 199,9k | $2.910,00 | $1.940 | $2.000 | Freight (223 em estoque) |
| NPN-160U-LP | 160k | $1.005,00 | $670 | — | THS Standard |
| NPN-180U-LP | 180k | $1.155,00 | $770 | — | THS Standard |

- **A $1.300, o NPE-180A2 fica $250 abaixo do nosso CUSTO.** Recomendado deixar a
  venda ir com elegancia. Nao e markup — e custo de fornecedor. Reforca tirar
  NPE do Shopping pago (§69): nao ha desconto que resolva.
- Ferguson nao conferida: `fergusonhome.com/search` respondeu **403**. A lista
  de liberados cobre `/product`, nao a busca. Nao contornar.
- Na Navien o numero do modelo NAO e o BTU: NPE-150=120k, 180=150k, 210=180k,
  240=199,9k. Cliente confunde com frequencia.

### Defeito de catalogo: os 3 ComfortFlow (A2) sem modelo no titulo

`NAVI-NPE-180A2`, `NAVI-NPE-210A2`, `NAVI-NPE-240A2`: o titulo diz so
"...Max Input: 150,000 BTU/h ... ComfortFlow(R)" — **sem "NPE-180A2"**. Os S2 tem
o modelo no titulo. Consequencias:
- a cliente "nao achou" o modelo que queria;
- **o NPE-240A2 e onde o Google Ads da lance** e o titulo nao contem o modelo —
  busca por modelo exato, o unico tipo que converte na loja (§75), nao casa;
- o 240A2 e o Navien com mais estoque (223).

### Tambem: handles com BTU trocado

`...-max-input-180-000-btu-h-...-npe-180s2` e de 150k BTU; `...-max-input-150-000-
btu-h-...-npe-210s2` e de 180k. Titulo certo, handle errado. Nao mexer em handle
(quebra URL indexada e link do feed) sem redirect.

## §77 — Auditoria dos 73 Navien (24/09/2026)

Bulk `vendor:Navien`, loja `1vy05a-x6` conferida. 73 produtos, todos ACTIVE:
18 pecas, 16 tankless, 11 caldeiras condensing, 9 racks, 6 acessorios, 4 combi,
3 hydro furnace, outros.

**Limpo nos 73**: markup = 50% em todos (preco/custo = 1,5), custo, peso,
descricao >= 150 caracteres, `seo.description`, imagem com alt, tag
`free-ship-eligible` coerente com perfil e com lambda, nada > 150 lb fora do
Freight.

### Problemas

1. **Modelo fora do titulo — 12**: NPE-180A2, NPE-210A2, **NPE-240A2 (223 em
   estoque, $2.910)**, **NCB-240/110H-RAL (45 em estoque, $4.027,50)**,
   NFC-250/175H, NFC-250/200H, NHB-55H/80H/110H/150H (titulo diz "NHBH-110",
   grafia que nao e a da Navien), NPF700-100H5CH e 100U5CH.
2. **Modelo no fim de titulo de ~150 caracteres** nos que tem o modelo (ex.:
   "...Indoor or Outdoor Wall-Hung, Residential/Commercial NPE-180S2"). O
   Shopping trunca por volta de 70 caracteres: o modelo some do anuncio. Vale
   para os ~34 equipamentos (tankless, caldeira, combi, furnace).
3. **Gas (NG/LP) ausente** em SKU e titulo de 21 aquecedores/caldeiras. Nao
   escrever sem a ficha da Navien — cada linha tem regra de conversao propria.
4. **Handle com BTU errado — 5**: NHW700-199AI-NG, 199SU-LP, 199SU-NG
   ("199-000" para 199.900, inofensivo); NPE-180S2 e NPE-210S2 trocados. Nao
   mexer sem redirect.
5. **Sem dimensao — 47**; so 8 sao equipamento (5 caldeiras, 3 hydro furnace).
6. Modelo fora da descricao — 6 (os NHB-H, NCB-RAL, NPF700-100U5CH).

**Maior problema do Navien nao e catalogo, e preco** (§69, §76).

### Padrao proposto (pendente do OK do Gabriel)

`Navien <MODELO> <linha> <tipo>, <BTU>, <instalacao>` — ex.:
`Navien NPE-240A2 ComfortFlow Condensing Tankless Water Heater, 199,900 BTU, Indoor/Outdoor`.
Antes do CSV: conferir gas e dimensoes na ficha da Navien (robots.txt antes).

## §78 — Titulos Navien no padrao novo: 33 prontos (24/09/2026)

Padrao aprovado pelo Gabriel: `Navien <MODELO> <linha> <tipo>, <BTU>, <instalacao>, <gas>`.
**Regra seguida: toda palavra do titulo novo saiu do titulo atual, do SKU ou da
Navien.** So reorganizado, nada inventado. Travas no script: modelo presente em
todos, nenhum BTU que nao estivesse no titulo original (unica expansao:
"14-100K" -> "14,000-100,000"), nenhum `None`.

- Modelo sempre nos **primeiros 22 caracteres** (antes: no fim de ~150, cortado
  no Shopping, ou ausente). Tamanho 72–140.
- Corrigidos de passagem: "NHBH-110" -> **NHB-110H** (grafia da Navien); o
  NHB-150H que dizia "NHB-150" (outro modelo) no fim.

### Gas — fonte: pagina de downloads de cada serie em navieninc.com

`robots.txt` lido antes (libera tudo exceto `/app*.pdf`, `/api`, `/admin`). Os
PDFs carregam por JS; a evidencia e a **lista de guias no HTML**.
- **"NG/LP Convertible"** so onde a Navien lista guia de conversao para LP/
  propano: NCB-H, NFC-H, NFB-H, NHB-H, NPE-A2, NPE-S2.
- **Gas do SKU** (dedicado): NHW (-NG / -LP), NPN (-LP).
- **Sem gas no titulo**: NFB-C, NHB (sem H) — guia generico, sem direcao — e
  NPF (nenhum guia).

### Fora do CSV

**`NAVI-NCB-240/110H-RAL`** — titulo, descricao e tags **identicos** ao
`NCB-240/110H`; so difere por nao ter UPC. **45 em estoque a $4.027,50.** Nao
sei o que "RAL" significa e nao vou inventar. Pendente do Gabriel.

### Arquivos (ordem de import)

1. `navien_titulo_IMPORTAR.csv` (33)
2. `navien_seo_IMPORTAR.csv` (3)
3. `navien_alt_IMPORTAR.csv` (60 imagens em 20 produtos)
4. `navien_descricao_IMPORTAR.csv` (10)

Rollback de cada um. Gerados do bulk de 24/09 — mesmo dia, frescor ok.

### Proximo

Dimensoes dos 3 NPF estao no HTML de `navieninc.com/series/npf/dimensions`
(ex.: NPF700-100U5CH 21,0" x 34,5" x 31,0"). As 5 caldeiras sem dimensao nao
tem pagina de dimensao — ficam para a ficha tecnica.

### §78 — adendo: gas nos 8 que estavam sem (pedido do Gabriel)

- **NFB-C (301C, 399C)**: navieninc.com/series/nfb-c — "Orifice conversion kit
  for easy gas convertibility from NG to LP is included with every NFB-C boiler."
- **NPF (060U3BH, 100H5CH, 100U5CH)**: navieninc.com/series/npf — "Each unit is
  supplied with an LP conversion kit"; cada modelo "Available in NG or LP".
- **NHB sem H (55, 80, 110)**: evidencia mais fraca. So o TITULO do guia
  ("NHB Gas Conversion Guide" + adendo); o PDF abre por `/api`, que o robots.txt
  da Navien bloqueia — nao contornado. Numa caldeira a gas, conversao so pode
  ser NG<->LP, e o sucessor NHB-H e explicitamente NG/LP. Aplicado
  "NG/LP Convertible" com essa ressalva.

Todos os 33 agora tem gas no titulo. CSVs regenerados (substituem os de antes).

### §78 — fechado: 33 titulos Navien verificados (24/09/2026)

Import feito em duas levas (a primeira com os CSVs antes do adendo de gas; a
segunda com o delta `navien_gas_*` dos 8). Verificado por bulk, loja
`1vy05a-x6` conferida:

- **33 de 33 titulos exatos** no padrao final, todos com gas.
- **Nenhum** seo.title, seo.description, descricao ou alt com o titulo antigo
  nem com a versao sem gas.
- Delta de gas: 3 SEO, 5 descricoes e 21 alts — 0 divergencia.

Pendente: `NCB-240/110H-RAL` (o que e "RAL"?); dimensoes dos 3 NPF; handles do
NPE-180S2/210S2 (so com redirect).

**Licao de processo**: quando um CSV e regerado depois de enviado, o nome do
arquivo nao muda e e facil importar o antigo. Da proxima vez, arquivo
regerado leva sufixo de versao (`_v2`).
