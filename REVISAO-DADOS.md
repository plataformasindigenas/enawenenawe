# Revisão dos dados

Questões encontradas na revisão dos dados de 2026-11 (fase 0 do novo modelo dos sites). Nada
aqui foi alterado automaticamente: cada item precisa de alguém que conheça a língua ou a
origem do material. Ao resolver um item, apague a linha.

## 1. Palavras repetidas sem número de homônimo (11)

A mesma palavra aparece em mais de uma linha, sem número. Se forem palavras diferentes
(homônimos), numere-as na coluna `homonym` (1, 2, …) para que apareçam como *kuri*¹, *kuri*².
Se forem a mesma palavra, junte as definições numa linha e apague a outra.

| palavra | id | definição |
|---|---|---|
| ahotene | 14 | plantar |
| ahotene | 15 | plantar, enterrar |
| atoli | 64 | avô |
| atoli | 65 | avô |
| hokwa | 166 | ciúme |
| hokwa | 167 | rede (de dormir) -- forma não possuída. |
| horatero | 172 | maduro |
| horatero | 173 | verde |
| hotaka | 176 | desaparecer |
| hotaka | 177 | perder |
| kotaha | 265 | cagar |
| kotaha | 266 | defecar |
| one | 307 | água |
| one | 308 | rio |
| wase | 366 | cego, cegar |
| wase | 367 | amendoim |
| wata | 368 | calor |
| wata | 369 | quente, esquentar |
| wesera | 396 | beber |
| wesera | 397 | beber |
| yalawi | 439 | araruta |
| yalawi | 440 | cego, cegar |

## 2. Palavras com letras fora do alfabeto (9)

O alfabeto do dicionário está em `CULTURA.md`. Estas palavras usam outras letras: pode ser
um empréstimo (tudo bem), um erro de digitação, ou uma palavra em português na coluna da
palavra (troque as colunas).

| id | palavra | letras | definição |
|---|---|---|---|
| 83 | awudali | u | saudável |
| 84 | casa | c | hakolo |
| 85 | cortar | c | erekiotene |
| 86 | criança | c ç | diwa |
| 134 | fechar | c f | aitowa |
| 182 | huiratero | u | azul |
| 290 | muñakalõ | u | virgem |
| 347 | trabalhar | b | kiwakali |
| 381 | wayakaJaiti | j | janela, espelho |

Também com o português na coluna da palavra, embora só usem letras do alfabeto: **302** *olho*
(definição *doseti*) e **332** *téwe* (definição *anta*; confira qual coluna é qual).

## 3. Imagens sem crédito: Fauna (77)

Estas imagens aparecem sem autor nem licença. Preencha em `data/fauna.yaml`, abaixo de `pic_link`:
`pic_credit: "© Nome, CC BY-SA 4.0, via Wikimedia Commons"` e `pic_source: "https://..."`. Se a
origem não puder ser encontrada, troque a imagem por uma de origem conhecida (Wikimedia Commons
e iNaturalist mostram autor e licença) ou apague `pic_link`. Fotos da comunidade:
`pic_credit: "Acervo da comunidade"`, ou o nome de quem fotografou, se ela concordar. Os créditos
que puderam ser comprovados já foram preenchidos.

| id | nome | nome científico | imagem |
|---|---|---|---|
| 1 | Tahoto (Queixada) | *Tayassu pecari* | `images/fauna_001_tahoto.jpg` |
| 3 | Eixine dotalinase (Onça parda) | *Puma concolor* | `images/fauna_003_eixine_dotalinase.jpg` |
| 4 | Alitine (gavião real) | *Harpia harpyja* | `images/fauna_004_alitine.jpg` |
| 6 | Kololo hekali (paca) | *Cuniculus paca* | `images/fauna_006_kololo_hekali.jpg` |
| 7 | Erinãli (veado catingueiro) | *Mazama gouazoubira* | `images/fauna_007_erinãli.jpg` |
| 8 | Erinãli kawera kionere (veado mateiro) | *Mazama americana* | `images/fauna_008_erinãli_kawera_kionere.jpg` |
| 9 | Erinãli kakotawerali (cervo do pantanal) | *Blastocerus dichotomus* | `images/fauna_009_erinãli_kakotawerali.jpg` |
| 10 | Erinãli olokwalikwali (veado campeiro) | *Blastocerus campestris* | `images/fauna_010_erinãli_olokwalikwali.jpg` |
| 11 | Yolina (raposa do campo) | *Lycalopex vetulus* | `images/fauna_011_yolina.jpg` |
| 12 | Detekwalahe (lobo guará) | *Chrysocyon brachyurus* | `images/fauna_012_detekwalahe.jpg` |
| 14 | Hota hotãnaloli (macaco-prego) | *Simia apella* | `images/fauna_014_hota_hotãnaloli.jpg` |
| 17 | Atikioli (tamanduá-bandeira) | *Myrmecophaga tridactyla* | `images/fauna_017_atikioli.jpg` |
| 19 | Kahe (quati) | *Nasua nasua* | `images/fauna_019_kahe.jpg` |
| 22 | Anaxowa (tamanduá-mirim) | *Tamandua tetradactyla* | `images/fauna_022_anaxowa.jpg` |
| 24 | Malola ewete (tatu-canastra) | *Priodontes maximus* | `images/fauna_024_malola_ewete.jpg` |
| 25 | Malolase (tatu-galinha) | *Dasypus novemcinctus* | `images/fauna_025_malolase.jpg` |
| 26 | Hotoxe (rato preto) | *Rattus rattus* | `images/fauna_026_hotoxe.jpg` |
| 27 | Kolohe kodohe (lagarto verde) | *Ameiva ameiva* | `images/fauna_027_kolohe_kodohe.jpg` |
| 28 | Tihowe (arara-canindé) | *Ara ararauna* | `images/fauna_028_tihowe.jpg` |
| 29 | Towada (araracanga) | *Ara macao* | `images/fauna_029_towada.jpg` |
| 30 | Kakerenali (arara-vermelha) | *Ara chloropterus* | `images/fauna_030_kakerenali.jpg` |
| 31 | Olotawa (papagaio-verdadeiro) | *Amazona aestiva* | `images/fauna_031_olotawa.jpg` |
| 33 | Haweti (mutum cavalo) | *Mitu tuberosum* | `images/fauna_033_haweti.jpg` |
| 34 | Tawekiolo (chora-chuva-preto) | *Monasa nigrifrons* | `images/fauna_034_tawekiolo.jpg` |
| 36 | Kotayalihe (tesourina-do-campo) | *Tyrannus savana* | `images/fauna_036_kotayalihe.jpg` |
| 37 | Oloweto (rolinha roxa) | *Columbina talpacoti* | `images/fauna_037_oloweto.jpg` |
| 39 | Koñaho (anu preto) | *Crotophaga ani* | `images/fauna_039_koñaho.jpg` |
| 45 | Towayako (bacurau-comum) | *Nyctidromus albicollis* | `images/fauna_045_towayako.jpg` |
| 47 | Totokoli (pomba trocal) | *Patagioenas speciosa* | `images/fauna_047_totokoli.jpg` |
| 48 | Makalo (garça vaqueira) | *Bubulcus ibis* | `images/fauna_048_makalo.jpg` |
| 50 | Olokwe (papagaio moleiro) | *Amazona farinosa* | `images/fauna_050_olokwe.jpg` |
| 55 | Wayalata (tiriba-de-barriga-vermelha) | *Pyrrhura perlata* | `images/fauna_055_wayalata.jpg` |
| 57 | Kakase (maracanã-verdadeiro) | *Primolius maracana* | `images/fauna_057_kakase.jpg` |
| 58 | Wakowa (acauã) | *Herpetotheres cachinnans* | `images/fauna_058_wakowa.jpg` |
| 59 | Oloho (urubu-de-cabeça-vermelha) | *Cathartes aura* | `images/fauna_059_oloho.jpg` |
| 60 | Oloho eyowalioli, herenewa xewere (urubu-rei) | *Sarcoramphus papa* | `images/fauna_060_oloho_eyowalioli_herenewa_xewere.jpg` |
| 61 | Wayalanese (urubuzinho) | *Chelidoptera tenebrosa* | `images/fauna_061_wayalanese.jpg` |
| 63 | Hõse (coruja buraqueira) | *Athene cunicularia* | `images/fauna_063_hõse.jpg` |
| 64 | Tewatewali (macuru-de-barriga-castanha) | *Notharchus swainsoni* | `images/fauna_064_tewatewali.jpg` |
| 65 | Xalala (martim-pescador-verde) | *Chloroceryle amazona* | `images/fauna_065_xalala.jpg` |
| 66 | Towehe (inhambu chororó) | *Crypturellus parvirostris* | `images/fauna_066_towehe.jpg` |
| 67 | Xirese (periquito-de-encontro-amarelo) | *Brotogeris chiriri* | `images/fauna_067_xirese.jpg` |
| 68 | Yotikia (ariramba-bronzeada) | *Galbula leucogastra* | `images/fauna_068_yotikia.jpg` |
| 69 | Xolaxola (inhambu anhangá) | *Crypturellus variegatus* | `images/fauna_069_xolaxola.jpg` |
| 71 | Onoli (socó-boi-baio) | *Botaurus pinnatus* | `images/fauna_071_onoli.jpg` |
| 72 | Maña (jaó) | *Crypturellus undulatus* | `images/fauna_072_maña.jpg` |
| 74 | Totokwalili (pica-pau-grande-americano) | *Dryocopus pileatus* | `images/fauna_074_totokwalili.jpg` |
| 77 | Awere (ariranha) | *Pteronura brasiliensis* | `images/fauna_077_awere.jpg` |
| 79 | Okwamada (gavião-de-rabo-branco) | *Buteo albicaudatus (Vieillot, 1816)* | `images/fauna_079_okwamada.jpg` |
| 80 | Kota (saúva) | *Atta cephalotes* | `images/fauna_080_kota.jpg` |
| 81 | Waoli (borboleta) | *Ordem: Lepidoptera* | `images/fauna_081_waoli.jpg` |
| 82 | Malaeta (Maranduvá) |  | `images/fauna_082_malaeta.jpg` |
| 83 | Hõi (Iguana verde) | *guana iguana* | `images/fauna_083_hõi.jpg` |
| 84 | Akola (escorpião) | *Ordem: Scorpiones* | `images/fauna_084_akola.jpg` |
| 85 | Kariri (cascavel) | *Família: Viperidae* | `images/fauna_085_kariri.jpg` |
| 86 | Koloalo (Sapo) | *Ordem: Anura* | `images/fauna_086_koloalo.jpg` |
| 87 | Torilori (abelha) | *Subfamília: Anthophila* | `images/fauna_087_torilori.jpg` |
| 88 | Dekwalahĩ (cachorro-vinagre) | *Speothos venaticus* | `images/fauna_088_dekwalahĩ.jpg` |
| 91 | Kohase atoke awo / Dokose (boto-cor-de-rosa) | *Inia geoffrensis* | `images/fauna_091_kohase_atoke_awo_dokose.jpg` |
| 92 | Menese (sucuri) | *Género: Eunectes* | `images/fauna_092_menese.jpg` |
| 93 | Xaweyali (caititu) | *Pecari tajacu* | `images/fauna_093_xaweyali.jpg` |
| 94 | Kolixihi (caxinguelê) | *Guerlinguetus brasiliensis* | `images/fauna_094_kolixihi.jpg` |
| 95 | Akioli (jabuti) | *Chelonoidis carbonaria / Cheleonoidis denticulata* | `images/fauna_095_akioli.jpg` |
| 98 | ahete (urucum) | *Bixa orellana* | `images/fauna_098_ahete.jpg` |
| 100 | waloriki (bacaba) | *Oenocarpus bacaba* | `images/fauna_100_waloriki.jpg` |
| 101 | wase (amendoim) | *Arachis hypogaea* | `images/fauna_101_wase.jpg` |
| 102 | waxarikwaihi (máscara ritual) | *Euterpe oleracea* | `images/fauna_102_waxarikwaihi.jpg` |
| 103 | wayokwata (joaninha) | *Família: Coccinellidae* | `images/fauna_103_wayokwata.jpg` |
| 105 | wotohõ (macaco zogue-zogue) | *Callicebus personatus* | `images/fauna_105_wotohõ.jpg` |
| 106 | xihiya (jacamim) | *Família: Psophiidae* | `images/fauna_106_xihiya.jpg` |
| 107 | yahõ (jaú) | *Zungaro zungaro* | `images/fauna_107_yahõ.jpg` |
| 108 | yalawi (araruta) | *Maranta arundinacea* | `images/fauna_108_yalawi.jpg` |
| 109 | halila (tucunaré) | *Género: Cichla* | `images/fauna_109_halila.jpg` |
| 110 | hoserese (coruja-buraqueira) | *Athene cunicularia* | `images/fauna_110_hoserese.jpg` |
| 111 | wisowisohi (caiarara) | *Gênero: Cebus* | `images/fauna_111_wisowisohi.jpg` |
| 113 | kolohi (bico-doce (calango)) | *Ameiva ameiva* | `images/fauna_113_kolohi.jpg` |
| 115 | kayali (pacu) | *Família: Myleinae* | `images/fauna_115_kayali.jpg` |

## 4. Imagens sem crédito: Etnobotânica (22)

Estas imagens aparecem sem autor nem licença. Preencha em `data/ethnobotany.yaml`, abaixo de `pic_link`:
`pic_credit: "© Nome, CC BY-SA 4.0, via Wikimedia Commons"` e `pic_source: "https://..."`. Se a
origem não puder ser encontrada, troque a imagem por uma de origem conhecida (Wikimedia Commons
e iNaturalist mostram autor e licença) ou apague `pic_link`. Fotos da comunidade:
`pic_credit: "Acervo da comunidade"`, ou o nome de quem fotografou, se ela concordar. Os créditos
que puderam ser comprovados já foram preenchidos.

| id | nome | nome científico | imagem |
|---|---|---|---|
| 2 | lolokwatehi (açaí) | *Euterpe oleracea* | `images/ethnobotany_002_lolokwatehi.jpg` |
| 3 | Yodairiro (cará roxo) | *?* | `images/ethnobotany_003_yodairiro.jpg` |
| 4 | walolike (bacaba) | *Oenocarpus bacaba* | `images/ethnobotany_004_walolike.jpg` |
| 5 | hakali (cara) | *Dioscorea trifida* | `images/ethnobotany_005_hakali.jpg` |
| 6 | kolowali (pequí) | *Caryocar coriaceum* | `images/ethnobotany_006_kolowali.jpg` |
| 7 | kolito (milho) | *Zea mays* | `images/ethnobotany_007_kolito.jpg` |
| 8 | Ahete (urucum) | *Bixa orellana* | `images/ethnobotany_008_ahete.jpg` |
| 10 | Ketese (Mandioca) | *Manihot esculenta* | `images/ethnobotany_010_ketese.jpg` |
| 11 | Halata kate (babaçu) | *Attalea speciosa* | `images/ethnobotany_011_halata_kate.jpg` |
| 12 | Konohi (Algodão) | *Género: Gossypium* | `images/ethnobotany_012_konohi.jpg` |
| 15 | Amayo (Batata doce) | *Ipomoea batatas* | `images/ethnobotany_015_amayo.jpg` |
| 16 | dolohi (bambu) | *Subfamília: 	Bambusoideae* | `images/ethnobotany_016_dolohi.jpg` |
| 17 | Ohata (Palmeira sete perna) | *Socratea exorrhiza* | `images/ethnobotany_017_ohata.jpg` |
| 18 | akiona (timbó) | *familias: leguminosas e sapindáceas* | `images/ethnobotany_018_akiona.jpg` |
| 21 | Hetire (Cabaça) | *Porongo* | `images/ethnobotany_021_hetire.jpg` |
| 23 | kowatairo (feijão de corda) | *Vigna unguiculata* | `images/ethnobotany_023_kowatairo.png` |
| 25 | kowatase (feijão fava) | *Vicia faba* | `images/ethnobotany_025_kowatase.jpg` |
| 29 | kalana (mauritiella armata) | *Mauritiella* | `images/ethnobotany_029_kalana.jpg` |
| 31 | halata (inaja) | *Attalea maripa* | `images/ethnobotany_031_halata.jpg` |
| 32 | katehe (cogumelo) |  | `images/ethnobotany_032_katehe.jpg` |
| 34 | eyolo yokolali (Anona) | *Annona muricata (Graviola)* | `images/ethnobotany_034_eyolo_yokolali.jpg` |
| 35 | eyolo yokolali (Annona squamosa Ateira) | *Annona squamosa Ateira* | `images/ethnobotany_035_eyolo_yokolali.jpg` |
