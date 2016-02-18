Dokumentaatio varhaisnykysuomen OMORFi-säännöistä:

## Leksikaaliset muutokset

Leksikaaliset muutokset on koottu lexemes-emf.tsv -tiedostoon. Ne muodostuvat:

1. OMORFin itsenäisinä lekseemeinä kuvaamien johdosten murteellisista johdinvarianteista tuotetuista muodoista. Lisätyt muotoryhmät:
  1. ottaa/oittaa -verbit (esim. kirjottaa, kirjoittaa)
  1. inen/nen -nominit. (esim. kärpänen, kärpäinen)

  Ryhmä on koottu hakemalla OMORFin vakiosanalistasta (lexemes.tsv) johtimia vastaavat sanamuodot ja tuotettu niistä murrevariantilliset muodot. Tämä on johtanut siihen, että sanalistassa on todennäköisesti muotoja, joita ei ole koskaan esiintynyt, eli sanoja, jotka ovat ilmaantuneet yleiskieleen vasta sen jälkeen johdinvariaatio on vakiintunut.

  Tähän ryhmään kuuluvat sanat on lexemes-emf.tsv -tiedostossa merkitty koodilla "aok".

1. Muista (historiallisista) lähteistä saatua autenttista murteellista tai varhaisnykysuomen kauden sanastoa. Merkitään koodilla, joka viittaa lähteeseen.

1. Vakiintumattoman tai vanhanaikainen ortografian tuottamista muodoista, joita ei voi kuvata muuten kuin sanakohtaisesti. Koodataan myös viittauksella lähteeseen.

## Tunnuksiin, päätteisiin ja kliitteihin liittyvät muutokset

Taivutukseen liittyvät muutokset on koottu continuations/inflections-emf.tsv -tiedostoon. Ne muodostuvat:

1. Murteellisten tai vanhanaikaisten vartalovarianttien liitoksista OMORFin taivutussäännöstöihin.

  esimerkiksi:

  NOUN_BACK_WEAK_PLURALS_ARCHAIC	Uarch		NOUN_BACK_WEAK_PLURALS

1. Murteellisista tai vanhanaikaisista taivutuspäätteistä. Lisätyt muotoryhmät:
  1. Inessiivi
    1. Yksinäis-s:lliset inessiivit ("autosa")
    1. Loppuheitolliset inessiivit ("autos")
  1. Illatiivi
    1. Yksinäis-e:lliset een-illatiivit ("harmaasen")
  1. Allatiivi
    1. loppu-n:lliset illatiivit ("autollen")
  1. Adessiivi
    1. loppuheitolliset adessiivit ("autol")

1. Murteellisista tai vanhanaikaisista liitepartikkeleista
  1. loppuheitolliset muodot ("autolleki")

## Vartalotaivutukseen liittyvät muutokset

1. t:n heikko aste
  1. katomuodot (sota -> sodan / soan)
  1. j-variantti (sota -> sodan / sojan)

1. k:n heikko aste
  1. g-variantti (alku -> alun / algun)
  1. '-variantti i:n jälkeen (aika -> ajan / a'an)
  1. h-variantti s:n edellä (haaksi -> haaksen / haahen)

1. eA-adjektiivit
  1. ee-variantti (korkea / korkee)

## Sananjohtamiseen liittyvät muutokset

HistOMORFi pyrkii käsittelemään sananmuodostusta hivenen morfologislähtöisemmin kuin OMORFin nykysuomen pääversio, ja tulkitsee johdetuiksi sanoiksi sellaisia muotoja, jotka nyky-OMORFi käsittelee leksikaalisina yksiköinä. Tämä on välttämätöntä, sillä varhaisnykysuomessa tuotettiin paljon uusia sanoja käyttämällä sananjohdosmorfologiaa, eivätkä monetkaan näistä sanoista vakiintuneet käyttöön. Tästä huolimatta nykysuomen puhuja joka tapauksee analysoi näiden sanojen johdossuhteet ja merkityksen yleensä oikein.

Tämä on toteutettu niin, että continuations/stems-emf.tsv -tiedostoon on avattu jokaiselle relevantille vartalotyypille rivi ja lisätty mahdollisten johtimien lista. Johtimet itsessään on kuvattu continuations/derivations-emf.tsv -tiedostossa.

1. Tekijännimijohtimet
  1. jA - lisätty säännöstö, joka osaa tuottaa mistä tahansa verbistä jA-tekijännimijohdoksen
	
	




