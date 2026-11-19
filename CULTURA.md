# Cultura visual do Enawenê-Nawê

O Enawenê-Nawê usa a mesma interface das outras plataformas, mas com elementos visuais próprios. Este
arquivo diz de onde eles vêm, o que fica de fora de propósito e quem os aprovou. Os elementos de
um povo **não são usados no site de outro**.

## Os elementos do site (versão 2)

O novo modelo do site (versão 2, em prévia em <https://previews.terradoc.org/enawenenawe/v2/>)
tem três elementos visuais: as cores, uma faixa e uma textura de fundo. **Não há emblema.**
Os elementos foram desenhados por nós a partir da pesquisa publicada, como abstrações: nenhum
copia um objeto, um enfeite ou um trançado. O site também funciona e parece acabado só com as
cores, e qualquer elemento pode sair a qualquer momento sem quebrar nada.

- **Onde estão:** as cores em `theme.palette` (`terradoc.yaml`); a faixa e a textura em
  `config/templates/v2/motifs/enawene/` (desenhos em SVG, com fontes e aprovação repetidas em
  `pack.yaml`).
- **Aprovação:** desenhados em 2026-11-18 e aprovados pelo coordenador sob a aprovação geral da
  comunidade (2026-11-17). A comunidade pode pedir mudanças a qualquer momento.

### Cores

Cinco cores com papéis fixos, cada uma com o nome do material de onde vem.

| Papel | Cor | Material |
|---|---|---|
| fundo | `#FAF3E8` | fibra de buriti, algodão |
| texto | `#2C1810` | castanho escuro neutro, sem material |
| títulos, links e botões | `#A83220` | urucum, *ahete* (Barra 2010, p. 113) |
| faixas e destaques | `#D4A81E` | urucum amarelo, penas da tapiragem |
| texto secundário | `#6B5E4F` | castanho acinzentado neutro |

- O par vermelho e amarelo segue o "urucum amarelo-gualdo com traços destacados em
  vermelho-sangue" (Mendes dos Santos 2006, citado por Barra 2010, p. 60).
- O preto do jenipapo não vira cor do site: nas fontes ele é ritual e ligado aos Yakairiti.
  Pela mesma razão não há um esquema de lama e argila branca.
- O dourado do site atual deixa de ser a cor dos links e títulos, porque não tinha contraste
  suficiente para leitura (2,0:1); fica só nas faixas.
- Todas as combinações usadas passam o contraste mínimo de leitura (4,5:1); o `terradoc check`
  recusa uma paleta que não passe.

### Faixa: fio com contas

Um fio amarelo com contas redondas vermelhas, iguais e espaçadas, sob o cabeçalho e entre as
seções. Abstrai as faixas de algodão que as mulheres tecem e os enfeites de contas do dia a dia
(IPHAN, p. 148; ISA), nas cores do urucum. Não reproduz nenhum enfeite em particular, nem a
jarreteira das mulheres (*barese*).

### Textura: trama dos caminhos

Fios diagonais muito claros que se cruzam por cima e por baixo, no fundo da página. Abstrai a
ideia, registrada no dossiê do IPHAN (p. 182), de que esteiras e cestos são trançados por
analogia com os caminhos: as palhas que se cruzam registram o território.

- Não é um cesto nem a peneira. As fontes não trazem nomes de padrões de trançado, e o
  trançado é especialidade de clã, por isso a trama é genérica.
- Também não se chama "waitiwina": o termo, de notas antigas do projeto, não aparece nas
  fontes (a barragem de pesca é *waiti*).

### O que fica de fora, de propósito

A casa do Yãkwa, as flautas, os Yakairiti e os *dakoti*, a tatuagem *ihota* e a jarreteira
*barese*, e qualquer coisa ligada aos mortos. A casa do Yãkwa é pública e aparece nas fotos
do IPHAN e da UNESCO, mas é a casa dos clãs e das flautas; usá-la como enfeite repetido
trataria um centro ritual como decoração.

### Fotos

A foto da página inicial é uma paisagem, sem pessoas (`theme.hero_people: false`), como
decidido para este site. Falta o crédito (`theme.hero_credit`); a equipe deve preenchê-lo,
e confirmar de onde é a foto, antes da migração. Qualquer foto pode ser retirada a pedido.

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
  trate como variante de **l**. A busca da versão 2 trata l/r e w/b como a mesma letra e
  procura u como o (`search_folds` em `terradoc.yaml`).
- Ficam fora: **u** (3 palavras; o IPHAN e Zorthêa a tratam como variante de o), **b**, e as
  letras que só aparecem em linhas com o português na coluna da palavra (veja
  `REVISAO-DADOS.md`).
- Vale perguntar à OPAN se há hoje um alfabeto usado na escola.
- **Onde está:** `alphabet` e `search_folds` em `terradoc.yaml`. Pesquisa completa:
  `meta/domains/plataformas/research/2026-11-17-template-redesign/alphabets.md`.
- **Aprovação:** proposta de 2026-11-18, aprovada pelo coordenador sob a aprovação geral da
  comunidade ao ser incorporada. A comunidade pode pedir mudanças a qualquer momento.

## O site atual (versão 1, até a migração)

O site publicado hoje ainda usa o modelo antigo, com o padrão `lattice`: uma **trama de linhas
diagonais cruzadas** e um **pequeno triângulo**, no fundo animado da página inicial, na
moldura das fotos, no divisor, no selo ao lado dos títulos e na textura de fundo.

- A trama é a mesma ideia dos caminhos (IPHAN, p. 182), e continua na versão 2 como textura.
- O triângulo lembrava a casa do Yãkwa, que guarda as flautas e é a casa dos clãs (e é
  cônica, não triangular). Na versão 2 ele sai.
- **Onde está:** `config/templates/motifs/lattice/`; cores em `theme.colors`, fotos em
  `theme.hero_images`.
- **Aprovação:** aprovado (registro do coordenador, 2026-11-14).

## Fontes

Pesquisa completa, com o que cada fonte diz e o que não foi possível consultar:
`meta/domains/plataformas/research/2026-11-17-template-redesign/enawene.md` (elementos e
cores), `alphabets.md` (alfabeto) e `palettes.md` (cores e contraste).

- IPHAN / OPAN. *Dossiê IPHAN: Ritual Yaokwa, Povo Enawene Nawe.* Processo
  01450.011160/2006-42; registrado no Livro das Celebrações em 2010.
  <https://www.ipatrimonio.org/wp-content/uploads/2017/05/Dossie_Yaokwa.pdf.pdf>
- Instituto Socioambiental (ISA). "Enawenê-nawê." *Povos Indígenas no Brasil*.
  <https://pib.socioambiental.org/pt/Povo:Enawenê-nawê>
- Barra, M. C. A. (2010). *Transformações dos corpos: um estudo do conceito de corpo enawene
  nawe.* Dissertação de mestrado, UFMG.
- Mendes dos Santos, G. (2006). *Da cultura à natureza: um estudo do cosmos e da ecologia dos
  Enawene-Nawe.* Tese de doutorado, USP. Não lida diretamente; citada por Barra (2010), Souza
  (2011) e o ISA.
- Almeida, J. de (2015). *Enawene-Nawe Wixo: diferença e convivialidade na gestão
  sociopolítica do cosmos.* Dissertação de mestrado, UFAM.
- Souza, E. R. de (2011). *Sociocosmologia do espaço Enawene Nawe.* Dissertação de mestrado,
  UFBA.
- Lacerda, R. (2019). "Os banquetes do Yaokwa: potencialidades e limites do cinema e do
  património entre os Enawenê-nawê." *Sociedade e Cultura* 22(2): 60–83.
- Carvalho, R. da C. (2024). *Monitoramento da Atividade Pesqueira na Terra Indígena
  Enawenê-Nawê.* Relatório técnico, OPAN (o termo *waiti*).

Consultados entre 2026-11-17 e 2026-11-18.

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
