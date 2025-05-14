# Projekts automatizācija
<br/>

## Python tēmu meklētājs ar Cheat Sheet funkcionalitāti
<br/>

### Projekta uzdevums 

Projekts automatizēti meklē un izgūst informāciju par Python programmēšanas valodas tēmām no tīmekļa lapas [(https://www.w3schools.com/python/default.asp)] Lietotājs ievada meklēšanas tēmas nosaukumu, un programma: 

* meklē atbilstošās tēmas.
* izgūst atbilstošo lapu saturus. 
* saglabā to lokāli, .txt failā, kā "Python cheat sheet".


## Izmantotās Python bibliotēkas 
<br/>

**selenium** – pārlūka programmas darbības automatizēšanai, ļauj atvērt un kontrolēt tīmekļa lapas, un iegūt vajadzīo informāciju no HTML tagiem. <br/>
**time** – nodrošina pauzes, lai lapa pilnībā ielādētos pirms tālākas darbības. <br/>
**bs4** – tiek izmantota HTML elementu analīzei un vajadzīgās informācijas izvilkšanai no lapas. Tā kā vietnes izkārtojums ir sarežģīts un satur daudz  tagu. <br/>

 

## Pašizveidotās datu struktūras 
<br/>

Projektā tiek izmantots binārais meklēšana koks(BST) un node(atzara) Objekts. Projektam tika izvēlētas tieši šīs datu struktūras jo binārais meklēšanas koks nodrošina ātru meklēšanu sakārtotiem datiem **O(loh(n))**. Tā kā koks tiek veidots no esoša saraksta, un nav paredzēts jaunu atzaru pievienošanai un esošu atzaru dzēšanai, binārais meklēšanas koks atbilda programmatūras prasībām. Tajā tirk glabāti tēmu nosaukumi un linki uz tēmām, tēmu nosaukumi  ir sakārtoti alfabētiskā secībā ātrākai meklēšanai. Node objekts glabā norādes uz nākošajiem atzariem un vērtības par atzaru. 
<br/> 

Node Metodes: 
* Initialize()- inicializē jaunu node objektu kas satur vērtības left, right, value, key un link.
  
<br/>

Node objekts satur atribūtus 
* left – norāde uz kreiso apakškoku 
* right – norāde uz labo apakškoku 
* value – indekss sarakstā  
* key – tēmas nosaukums 
* link – saite uz tēmas lapu 
<br/>

Koda fragments: 

"   " 
<br/>

BST ir binārais meklēšanas koks ar šādām metodēm: 
* __init__() – Inicializē jaunu tukšu koku 
* insert_node(value, key) – Pievieno jaunu Node objektu kokam 
* create_tree(list) – Izveido līdzsvarotu koku no sakārtota saraksta 
* contains(value) – Meklē, vai ievadītā vērtība atrodas kokā, un atgriež tās saiti
<br/> 
Koda fragments: 

"   " 


## Programmatūras izmantošana 
<br/>

Pirms programmatūru iespējams izmantot, nepieciešams: uzinstalēta bibliotēka selenium, bs4. <br/>

1. Instalēšana: 

pip install selenium <br/>
pip install bs4 <br/>
Palaid programmu.  <br/>

2. Rezultāts:
   
** ĻOTI ILGI JĀGAIDA **, kad webdraiveris tiks galā ar pārlūkprogrammas lapu. <br/>
Tiek izvadīts izvēles tēmas no kurām var izvēlēties.  <br/>
Konsolē tiek parādīta atbilstošā tēma. <br/>
Tiek izgūts lapas saturs. <br/>
Saturs tiek saglabāts teksta failā " python_cheat_sheet .txt". <br/>
