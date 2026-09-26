# Pedido de dados ao fornecedor — dimensões de carton e o campo `cube`

Rascunho em inglês americano. Preencher o nome do contato e da empresa.
Contexto para o Gabriel: o arquivo mestre que recebemos (20.265 itens) tem as
colunas `L`, `H`, `W` e `cube`, mas **só 14 itens têm as três medidas
preenchidas**, e nesses 14 `L × W × H` bate exatamente com `cube` sem dividir
por 1728 — ou seja, `cube` ali é o produto das medidas, não pés cúbicos. Só que
outros 2.414 itens têm `cube` preenchido **com L/W/H nulos**, e valores como
1,295 que só fazem sentido em ft³. **A mesma coluna está em duas unidades.**

---

Subject: Carton dimensions and the `cube` field in the master item file

Hi [nome],

We're building out shipping calculation on our side and we've hit a gap in the
master item file. Two questions, and I'll be specific so this is quick for you.

**1. What does `cube` represent?**

In the file we have, `cube` is populated for about 2,400 items where `L`, `W`
and `H` are null. For the handful of items where all four are populated, `cube`
equals `L × W × H` exactly — so in those rows it reads as a raw product, not
cubic feet. But standalone values like `1.295` only make sense as cubic feet.

Could you confirm which it is, and whether it refers to the **carton** or the
**product**? If it's carton cubic feet, that single column solves most of what
we need.

**2. Can you provide carton dimensions per item?**

Right now `L`, `W` and `H` are populated on only 14 of the 20,265 items. What we
need for each SKU is the shipping carton: length, width, height, and the unit.

This matters because carriers rate small parcels on **dimensional weight**, not
actual weight. Without carton dimensions we're quoting from weight alone, which
overcharges customers on light items in large boxes and undercharges us on the
reverse. We recently had a customer question a $43.68 charge on a $23.43 part
for exactly this reason.

If carton data isn't available for the full catalog, a subset covering your
highest-volume items would already help, as would a general rule (for example,
standard carton sizes by product family).

Happy to take this in any format that's easy on your end — the same file with
the columns populated, or a separate extract keyed by part number.

Thanks,
[nome]
The House Supplier
