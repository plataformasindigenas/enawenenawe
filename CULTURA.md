# Cultura visual do Enawenê-Nawê

O Enawenê-Nawê usa a mesma interface das outras plataformas, mas com elementos visuais próprios. Este
arquivo diz de onde eles vêm e quem os aprovou. Os elementos de um povo **não são usados no site
de outro**.

## O padrão (`lattice`)

Uma **trama de linhas diagonais cruzadas** e um **pequeno triângulo** aparecem no fundo animado
da página inicial, na moldura das fotos, no divisor, no selo ao lado dos títulos e na textura de
fundo.

- **A trama (caminhos):** segundo o dossiê do IPHAN sobre o Yaokwa (p. 182), esteiras e cestos são
  trançados por analogia com os caminhos: as palhas que se cruzam registram o território. A trama
  do site é uma abstração disso, não a cópia de nenhum cesto em particular. (Notas antigas
  chamavam a trama de "waitiwina"; o termo não aparece nas fontes. A barragem de pesca é *waiti*.)
- **O triângulo:** a casa do Yãkwa guarda as flautas e é a casa dos clãs; além disso, é cônica, não
  triangular. No redesenho do site o triângulo sai, e fica só a trama.

**Fontes:** IPHAN/OPAN, *Dossiê Ritual Yaokwa*,
<https://www.ipatrimonio.org/wp-content/uploads/2017/05/Dossie_Yaokwa.pdf.pdf>; ISA, *Povos
Indígenas no Brasil*, "Enawenê-nawê", <https://pib.socioambiental.org/pt/Povo:Enawenê-nawê>;
OPAN, relatório de pesca 2024 (termo *waiti*). Consultados em 2026-11-17.

- **Onde está:** `config/templates/motifs/lattice/`; escolhido em `terradoc.yaml` (`theme`).
- **Aprovação:** aprovado (registro do coordenador, 2026-11-14).

As cores (`theme.colors`) e as fotos da página inicial (`theme.hero_images`) também fazem
parte da identidade do site; os créditos das fotos ficam junto delas.

## O alfabeto do dicionário

O dicionário agrupa e ordena as palavras por este alfabeto:

a, d, e, h, i, k, l, m, n, ñ, o, r, s, t, w, x, y

- **ñ** é uma letra, depois de **n**. As vogais nasais **ã ẽ ĩ õ** ficam junto da vogal simples.
  **kw** não tem aba própria (nenhuma palavra começa com kw).
- **Fontes.** A tabela de letras de Mendes dos Santos (2006), reproduzida por Barra (2010,
  UFMG, pp. 11–12); o dossiê do IPHAN sobre o Yaokwa ("Notas sobre a grafia enawene nawe",
  p. 8), que diz que c, f, g, j, p, q, v, z e u não fazem parte da grafia e que l/r e b/w
  variam. Todas as fontes dizem que a grafia muda desde os anos 1990 e segue o modo como os
  próprios Enawenê-Nawê escrevem; a lista mais recente que encontrei é de 2006.
- **r** fica, porque está na tabela de Barra e em 138 palavras dos dados, embora o IPHAN o
  trate como variante de **l**. A busca deve tratar l/r e w/b como a mesma letra (no novo
  modelo do site).
- Ficam fora: **u** (3 palavras; o IPHAN e Zorthêa a tratam como variante de o), **b**, e as
  letras que só aparecem em linhas com o português na coluna da palavra (veja
  `REVISAO-DADOS.md`).
- Vale perguntar à OPAN se há hoje um alfabeto usado na escola.
- **Onde está:** `alphabet` em `terradoc.yaml`. Pesquisa completa:
  `meta/domains/plataformas/research/2026-11-17-template-redesign/alphabets.md`.
- **Aprovação:** proposta de 2026-11-18, aprovada pelo coordenador sob a aprovação geral da
  comunidade ao ser incorporada. A comunidade pode pedir mudanças a qualquer momento.

## Conhecimento restrito

Este repositório e todas as prévias são **públicos**. Conhecimento restrito (rituais,
conhecimento de clã ou de gênero, os mortos, imagens de pessoas sem autorização) **nunca entra
aqui**, nem num ramo de teste: o histórico do git guarda tudo, e apagar depois não resolve. Um
campo "oculto" não protegeria nada, porque o arquivo continuaria legível no GitHub.

- **Quem aprova:** a comunidade Enawenê-Nawê, por meio de quem coordena a plataforma com ela.
- **Situação em 2026-11-14:** todo o conteúdo publicado até esta data está aprovado
  (registro do coordenador, Tiago Tresoldi).
- **Retirar algo:** avise o Tiago. Ele tira o material do site na hora (todas as versões e
  prévias) e remove-o do repositório; a remoção do histórico é pedida ao suporte do GitHub.
  Até lá, o material continua acessível a quem tiver o endereço exato do commit.
