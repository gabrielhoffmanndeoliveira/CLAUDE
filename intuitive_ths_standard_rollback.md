# Rollback — Intuitive Shipping no perfil THS Standard

Estado **ANTES** da mutação, lido da API em 18/09/2026.

```
DeliveryProfile      gid://shopify/DeliveryProfile/94652268647   "THS Standard - no free shipping"
DeliveryLocationGroup gid://shopify/DeliveryLocationGroup/95566332007
  location            gid://shopify/Location/77868040295  "The House Supplier"
```

Cada zona tinha **exatamente uma** method definition:

| zona | id da zona | method definition | participant | carrier | fee |
|---|---|---|---|---|---|
| US Continental (48 estados) | `350697390183` | `gid://shopify/DeliveryMethodDefinition/710220677223` | `gid://shopify/DeliveryParticipant/67513712743` | `ups_shipping` (`75774066791`) | 65% |
| US Outside (AK, HI, territórios) | `350798413927` | `gid://shopify/DeliveryMethodDefinition/710204719207` | `gid://shopify/DeliveryParticipant/67513516135` | `ups_shipping` (`75774066791`) | 65% |

Carrier adicionado: **Intuitive Shipping** `gid://shopify/DeliveryCarrierService/76406325351`,
`percentageOfRateFee: 0`, espelhando como já está no General profile.

## Como reverter

`deliveryProfileUpdate` no perfil `94652268647` com `methodDefinitionsToDelete:
[<ids das duas novas>]`. Os ids novos ficam registrados no §42 do PENDENTES
depois da mutação. **Não apagar** `710220677223` nem `710204719207` — essas são
as tarifas UPS originais.

## Efeito no checkout

Antes: uma opção por zona (UPS + 65%). Depois: duas, e o cliente escolhe —
normalmente a mais barata. Pode reduzir o frete cobrado nos 5.633 produtos do
perfil. Quanto, não dá para prever pela Admin API: a tarifa do Intuitive está na
configuração do app.
