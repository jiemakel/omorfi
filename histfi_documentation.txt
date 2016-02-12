Dokumentaatio varhaisnykysuomen OMORFi-säännöistä:

*Leksikaaliset muutokset*

Leksikaaliset muutokset on koottu lexemes-arc.tsv -tiedostoon. Ne muodostuvat:

1) OMORFin itsenäisinä lekseemeinä kuvaamien johdosten murteellisista johdinvarianteista tuotetuista muodoista. Lisätyt muotoryhmät:
	1.1) ottaa/oittaa -verbit (esim. kirjottaa, kirjoittaa)
	1.2) inen/nen -nominit. (esim. kärpänen, kärpäinen)

Ryhmä on koottu hakemalla OMORFin vakiosanalistasta (lexemes.tsv) johtimia vastaavat sanamuodot ja tuotettu niistä murrevariantilliset muodot. Tämä on johtanut siihen, että sanalistassa on todennäköisesti muotoja, joita ei ole koskaan esiintynyt, eli sanoja, jotka ovat ilmaantuneet yleiskieleen vasta sen jälkeen johdinvariaatio on vakiintunut.

Tähän ryhmään kuuluvat sanat on lexemes-arc.tsv -tiedostossa merkitty koodilla "aok".

2) Muista (historiallisista) lähteistä saatua autenttista murteellista tai varhaisnykysuomen kauden sanastoa. Merkitään koodilla, joka viittaa lähteeseen.

3) Vakiintumattoman tai vanhanaikainen ortografian tuottamista muodoista, joita ei voi kuvata muuten kuin sanakohtaisesti. Koodataan myös viittauksella lähteeseen.

*Tunnuksiin, päätteisiin ja kliitteihin liittyvät muutokset*

Taivutukseen liittyvät muutokset on koottu continuations/inflections-arc.tsv -tiedostoon. Ne muodostuvat:

1) Murteellisten tai vanhanaikaisten vartalovarianttien liitoksista OMORFin taivutussäännöstöihin.

esimerkiksi:

NOUN_BACK_WEAK_PLURALS_ARCHAIC	Uarch		NOUN_BACK_WEAK_PLURALS

2) Murteellisista tai vanhanaikaisista taivutuspäätteistä. Lisätyt muotoryhmät:
	2.1) Inessiivi
		2.1.1) Yksinäis-s:lliset inessiivit ("autosa")
		2.1.2) Loppuheitolliset inessiivit ("autos")
	2.2) Illatiivi
		2.2.1) Yksinäis-e:lliset een-illatiivit ("harmaasen")
	2.3) Allatiivi
		2.3.1) loppu-n:lliset illatiivit ("autollen")
	2.4) Adessiivi
		2.4.1) loppuheitolliset adessiivit ("autol")

3) Murteellisista tai vanhanaikaisista liitepartikkeleista
	3.1) loppuheitolliset muodot ("autolleki")
	


*Vartalotaivutukseen liittyvät muutokset*

1) t:n heikko aste
	1.1) katomuodot (sota -> sodan / soan)
	1.2) j-variantti (sota -> sodan / sojan)

2) k:n heikko aste
	2.1) g-variantti (alku -> alun / algun)
	2.2) '-variantti i:n jälkeen (aika -> ajan / a'an)
	2.3) h-variantti s:n edellä (haaksi -> haaksen / haahen)

3) eA-adjektiivit
	3.1) ee-variantti (korkea / korkee)

*Sananjohtamiseen liittyvät muutokset*

HistOMORFi pyrkii käsittelemään sananmuodostusta hivenen morfologislähtöisemmin kuin OMORFin nykysuomen pääversio, ja tulkitsee johdetuiksi sanoiksi sellaisia muotoja, jotka nyky-OMORFi käsittelee leksikaalisina yksiköinä. Tämä on välttämätöntä, sillä varhaisnykysuomessa tuotettiin paljon uusia sanoja käyttämällä sananjohdosmorfologiaa, eivätkä monetkaan näistä sanoista vakiintuneet käyttöön. Tästä huolimatta nykysuomen puhuja joka tapauksee analysoi näiden sanojen johdossuhteet ja merkityksen yleensä oikein.

Tämä on toteutettu niin, että continuations/stems-arc.tsv -tiedostoon on avattu jokaiselle relevantille vartalotyypille rivi ja lisätty mahdollisten johtimien lista. Johtimet itsessään on kuvattu continuations/derivations-arc.tsv -tiedostossa.

1) Tekijännimijohtimet
	1.1) jA - lisätty säännöstö, joka osaa tuottaa mistä tahansa verbistä jA-tekijännimijohdoksen
	
	




