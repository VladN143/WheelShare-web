# WheelShare

WheelShare este o platformă dedicată închirierilor auto, care se adresează atât dealerilor care doresc să își promoveze ofertele, cât și utilizatorilor aflați în căutarea unei mașini. Aplicația facilitează listarea și rezervarea autoturismelor, oferind un proces simplificat de închiriere, opțiuni variate și filtre intuitive pentru căutare.

## Funcționalități Principale

* **Sistem de Conturi:** Utilizarea platformei (pentru listare sau închiriere) necesită autentificare și înregistrare, conturile fiind împărțite în două categorii: client și dealer.


* **Motor de Căutare:** Platforma include un motor de căutare care permite utilizatorilor să filtreze mașinile disponibile în funcție de preț (minim/maxim) și anul fabricației.


* **Pagini Detaliate pentru Mașini:** Fiecare vehicul are o pagină dedicată care afișează modelul, anul fabricației, prețul pe zi, specificațiile și recenziile lăsate de alți utilizatori.


* **Sistem de Recenzii și Rating:** După închiriere, utilizatorii pot adăuga o descriere și pot acorda un rating de la 1 la 5 stele, recenziile devenind vizibile pe pagina publică a mașinii.



## Fluxuri de Utilizare (Use Cases)

* **Managementul Contului:** Utilizatorul introduce datele personale (username, nume, email, parolă, tip cont) pentru a se înregistra. Sistemul validează informațiile, iar la autentificarea cu succes, redirecționează utilizatorul către dashboard.


* **Adăugare Ofertă (Dealer):** Un dealer poate lista un autoturism completând un formular cu modelul, anul de fabricație, prețul, detalii tehnice și încărcând o imagine a mașinii. Datele sunt validate și salvate în baza de date.


* **Închiriere și Istoric (Client):** Utilizatorul filtrează ofertele, selectează o mașină și inițiază rezervarea. Toate mașinile închiriate pot fi vizualizate ulterior direct din profilul acestuia.



## Arhitectura Bazei de Date

Aplicația folosește un model de bază de date relațională structurat în patru entități principale:

* **CustomUser:** Stochează datele utilizatorilor (id, nume, email, parolă, tipCont, telefon).


* **Car:** Gestionează informațiile mașinilor (id, model, an_fabricație, preț, detalii) și include un Foreign Key către dealerul care a adăugat-o. Relația dintre dealer și mașini este de tip 1:N.


* **Review:** Asociază un id de utilizator cu un id de mașină (cheie primară compusă), conținând rating-ul și descrierea. Această entitate descompune relația N:M dintre utilizatori și mașini într-o relație 1:N (utilizator-recenzii) și N:1 (recenzii-mașină).


* **CarRented:** Păstrează istoricul închirierilor, legând utilizatorul de mașina închiriată și înregistrând data și ora rezervării.



## Infrastructură și Deployment

În stadiul inițial, serverul aplicației este configurat să funcționeze local. Pentru un mediu de producție, arhitectura suportă migrarea către servicii de cloud computing precum Google Cloud sau Microsoft Azure. Ca alternativă tehnică, sistemul poate fi găzduit pe un server dedicat rulând un sistem de operare Linux integrat cu o bază de date MySQL.
