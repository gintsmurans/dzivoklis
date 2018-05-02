Title: Elektrība 1. daļa - pieslēgums un plānošana
Date: 2016-12-04 03:15
Category: Sākums
Tags: Elektrība
Lang: lv

Kad sākām remontu par elektrību skaidrs bija tikai tas, ka vajag drošinātājus. Tagad pēc ļoti aktīvas googlēšanas un [Ģimenes māja](https://gimenesmaja.wordpress.com/) lasīšanas, šķiet, ka ir izkristalizējies ko gribu un ko nē.

Sākām ar elektriķa atrašanu, ieteica mums tādu Ivanu, kurš izrādās strādā sadales tīklos un tieši atbild par mūsu rajonu. Atnāca, izstāstīja, aizgāja. Sapratām, ka labāk būtu 3 fāzes, jo ieslēdzot plīti, tv un putekļusūcēju visticamāk, ka sitīs ārā drošinātājus. Ivans iedeva kontaktus sadales tīkliem, kur interesēties par pieslēguma maiņu. Uzzvanu sadales tīkliem, kur man paskaidro, ka labāk aizpildīt formu, ko var atrast viņu [mājaslapā](https://www.e-st.lv/lv/private/). Aizpildu, aizsūtu elektroniski parakstītu iesniegumu uz e-pastu par to, ka gribu palielināt jaudu uz 3 fāzēm un 20A, pēc kāda laika ir atbilde, ka tas ir iespējams, bet vajadzēs no namsaimnieka atļauju. Tālāk interesējos namsaimniekā un tiek norunāts, ka pie manis ieradīsies meistars kurš novērtēs esošo stāvokli. Meistars ierodas un novērtē, ka jāmaina viss stāvvads, 4x10mm vads. Pēc debatēm ar citiem un pašam savām pārdomām, nolemjam atstāt esošo pieslēgumu, tikai nomainīt jaunus vadus no skaitītāja līdz dzīvoklim, un vilkt jaunos vadus ar domu, ka kādreiz varētu būt 3 fāzes, ja ar vienu būs par maz. Un šķiet, ka es ar tām 20A mazliet pārspīlēju, varbūt mainot uz 3 fāzu 16A būtu ok ar tiem pašiem vadiem, bet tagad tas tiks atstāts uz vēlāku laiku jebkurā gadījumā. Prieks par to, ka šis viss neivlkās mēnešiem ilgi, bet notika diezgan raiti.


Vadu vilkšanas mazais plāns:

* Jāvelk visi vadi zvaigznes veidā, jeb katram gala patērētājam savs vads, pārsvarā pat divi vadi. Šādi kā Ernests saka, mēs atbrīvojamies no sadales kārbām. Un no sadales skapja ir iespēja automatizēt uz vella paraušanu. gribēsies pēkšņi pašam savu gudro māju taisīt, nebūs problēmas, jo visi vadi būs skapī kur kā reiz sēdēs arī interneta rūteris. Atliek tikai paprasīt Lattelecomam ārējo ip adresi un uzprogramēt saziņu telefonam ar kontrolieri.
* Gaismām 3x1.5 vadi, kontaktiem 3x2.5 vadi. Kontakti kur ir vairāk par 3 rozetēm jāvelk divi vadi. Gaismām vēl būs jārēķina cik daudz lampas var darbināt ar vienu vadu (led paneļi).
* Uz slēdžiem jau laikus jāsavelk divi vadi, ja, piemēram, gribas nomainīt slēdzi ar vienu pogu uz slēdzi ar divām tādējādi piešķirot vienam slēdzim vairākas funkcijas, vai arī, piemēram, papildus slēdzī ielikt arduino, lai tas būtu iespējams bez lieka čakara. Izmaksās mazliet vairāk, bet vēlāk nebūs liekas problēmas.
* Uz plīti jau laikus jāievelkt kārtīgs trīsfāzu kabelis.
* Uz katru istabu jāievelk vismaz viena ethernet kontaktligzda. Sākumā es domāju šo vispār nevilkt, jo ir tak wifi, kas mūsdienās ir pat ātrāks par ethernet'u, bet ja gadījumā arī tos vadus neizmantos kā tīkla vadus, tad varbūt kādā dzīves posmā sagribēšu katrā istabā ielikt kaut kādus sensorus, piemēram gaisa kvalitātes mērīšanai, vai pieslēgt kaut kadu ierīci kurai nav wifi, tad man nebūs pa jaunu jāvelk vadi.
* Lai vai kā liktos, ka nelikšu sev dzīvoklī apsardzi, tomēr labāk ievilkt apsardzes kabeļus priekš sensoriem, ja nu es tomēr izdomāju kaut vai pats savu apsardzes variantu, vai izdomāju ielikt kameras, vai tamlīdzīgas lietas. Apsardzes kabeļa vietā 6x0.22 nopirku cat5e vadu, kurš bija krietni lētāks.
* Rozetes tuvāk zemei un nekad nav par daudz, lai nebūtu jāizmanto pagarinātāji.
* Slēdži ~90cm augstumā.
* Paša elektrības skapja saturs īsti nav vēl skaidrs. Saprotu, ka vajag kaut kāud noplūdes automātu vannas istabai, bet it kā liekas lieki visur citur kā to Ernests lika. Gribētu atsevišķi drošinātājus uz: vannas istaba & tualete, lielā istaba, virtuve, 3xguļamistabas, plīts, veļļas mašīna, ledusskapis, TV kontakts (5 rozetes, divi vadi). Varbūt kaut kādu aizsardzību pret ienākošām pārslodzēm, bet arī nav pārliecība vai tiešām vajag.
* Vēl neesmu izlēmis vai vilkt optikas vadus vai nē. Daudz lielāks ātrums par ethernetu, bet diezgan liels čakars ar vadu savienošanu (metināšanu).
