# Registro de casos — índice

Os casos trabalhados do projeto TFAS, movidos **verbatim** do antigo CLAUDE.md único em
23 Sep 2026. Nada foi reescrito. O núcleo operativo fica em `/CLAUDE.md` (carregado
automaticamente); estes arquivos **não** são carregados sozinhos — leia sob demanda e
passe o caminho para os agentes.

**Como usar**

- Antes de montar um batch, leia os arquivos das marcas do batch e passe os caminhos no
  briefing. Para uma parte ou host específico, `grep -rl '<SKU ou host>' docs/registro/`
  — um caso que envolve várias marcas mora em **um** arquivo só (o da marca dominante),
  então o grep é mais confiável que o nome do arquivo.
- **É cronológico.** Entradas posteriores corrigem anteriores; em conflito vale a mais
  recente, e acima de tudo vale o núcleo.
- Caso novo: acrescente no fim do arquivo certo. Marca nova: arquivo novo + uma linha
  aqui. Se o caso muda uma regra, edite também a regra no núcleo.

## Por marca

| arquivo | conteúdo | casos |
|---|---|---|
| `edwards-kidde.md` | Edwards/EST, Kidde ES, Genesis, SIGA, EST3/EST4, LifeLines/myeddie, regra E/K | 55 |
| `honeywell-notifier.md` | Notifier, FlashScan/CLIP, `-IV`, gabinetes CAB-4/CAB-5, HPF-PS | 42 |
| `honeywell-system-sensor.md` | System Sensor, L-Series, pack counts `-BP`, bulletins M23.2SS | 36 |
| `honeywell-edam-rotas.md` | formatos de caminho do EDAM, fingerprints, revisões duplicadas | 16 |
| `honeywell-gamewell.md` | Gamewell-FCI, prefixo `GW`, Velociti | 12 |
| `honeywell-fire-lite.md` | Fire-Lite, LiteSpeed, H365/SD365 | 11 |
| `honeywell-silent-knight.md` | Silent Knight / Farenhyt | 3 |
| `simplex-autocall-ansul.md` | Simplex, Autocall, Ansul; hub JCI | 32 |
| `siemens.md` | Siemens/Cerberus, `/go/` A6V, frase de coexistência | 20 |
| `eaton-wheelock.md` | Eaton/Wheelock Eluxa, rota `urllib`, lente âmbar | 23 |
| `potter-rsg.md` | Potter, RSG, PAD, Thermotech, RMS | 23 |
| `gentex.md` | Gentex, S/C/SC/H, PLACE, carta de anúncio | 14 |
| `mircom-secutron.md` | Mircom, Secutron, OpenGN, QAA | 14 |
| `fiplex-bda.md` | Fiplex, Westell, Comba, RFS, BDA/DAS | 21 |
| `xtralis-vesda.md` | Xtralis, VESDA, OSID | 11 |
| `power-sonic.md` | Power-Sonic, capacidade por taxa, códigos de terminal | 12 |
| `sti.md` | STI, Sanity | 13 |
| `napco.md` | Napco, tag index, Aiphone | 10 |
| `hochiki.md` | Hochiki America/Europe | 9 |
| `resideo-brk.md` | Resideo, Honeywell Home, BRK | 9 |
| `rath-avire.md` | RATH / Avire | 9 |
| `kidde-fenwal.md` | Kidde Fenwal, CARDOX | 4 |
| `macurco.md` | Macurco, LADBS | 5 |
| `amerex.md` | Amerex | 2 |
| `det-tronics.md` | Det-Tronics | 2 |
| `outros-fabricantes.md` | Altronix, DITEK, Functional Devices, Bosch, APC, Space Age/SAFE, FFE, Apollo, Viking, E2S, Protectowire, demais | 41 |

## Por tema

| arquivo | conteúdo | casos |
|---|---|---|
| `metodo-geral.md` | regras de pesquisa e armadilhas de extração sem marca dominante | 57 |
| `coordenacao-e-incidentes.md` | erros do coordenador, briefings, builders, slices | 56 |
| `fotos.md` | pipeline de fotos, CSVs, dHash, look pass, cobertura por marca | 37 |
| `varreduras-e-auditorias.md` | scans por mecanismo, sweeps de verificação, censos | 26 |
| `pipeline-operacao.md` | texto operacional antigo da seção do pipeline (fila, arquivos, estilo) | 17 |
| `negocio-ads-medicao.md` | Ads, Merchant Center, ERP, demanda, coleções, fila, medição | 16 |
| `ordem-permanente.md` | ordem permanente, convenções e status do repositório (texto original) | 3 |
