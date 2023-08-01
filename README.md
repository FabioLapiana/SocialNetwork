# README - Social Network con Django

Questo progetto è un social network sviluppato utilizzando Django, un framework web potente e flessibile per Python. Il social network ha diverse capacità avanzate, tra cui:

- Autenticazione: Abbiamo implementato l'autenticazione utilizzando il framework di autenticazione di Django per garantire che gli utenti possano accedere e gestire il proprio account in modo sicuro.

- Estensione del modello utente: Abbiamo esteso il modello utente predefinito di Django con un modello utente personalizzato per includere ulteriori informazioni nel profilo dell'utente.

- Utilizzo del framework di messaggi di Django: Abbiamo integrato il framework di messaggi di Django per consentire agli utenti di comunicare e ricevere notifiche all'interno dell'applicazione.

- Backend di autenticazione personalizzato: Abbiamo costruito un backend di autenticazione personalizzato per consentire metodi di accesso alternativi e personalizzati.

- Autenticazione social: Abbiamo implementato l'autenticazione social utilizzando Python Social Auth, consentendo agli utenti di accedere al social network tramite account Facebook e Google con OAuth2.

- Server di sviluppo HTTPS: Abbiamo utilizzato django-extensions per eseguire il server di sviluppo tramite HTTPS, aumentando la sicurezza delle comunicazioni durante lo sviluppo.

- Relazioni many-to-many nei modelli: Abbiamo implementato relazioni many-to-many tra gli utenti per consentire di stabilire collegamenti tra utenti e le risorse condivise.

- Richieste HTTP asincrone: Abbiamo aggiunto richieste HTTP asincrone tramite il JavaScript Fetch API e Django per migliorare la reattività dell'interfaccia utente.

- Paginazione con infinite scroll: Abbiamo implementato la paginazione con infinite scroll per migliorare l'esperienza di navigazione degli utenti attraverso il contenuto del social network.

- Sistema di follow degli utenti: Abbiamo costruito un sistema di follow degli utenti per consentire agli utenti di seguire le attività di altri utenti e ricevere aggiornamenti pertinenti.

- Attività dell'utente: Abbiamo creato uno stream di attività dell'utente per visualizzare le azioni e le interazioni recenti degli utenti, ottimizzando l'uso di QuerySets per garantire alte prestazioni e tempi di risposta veloci.

Requisiti di sistema:

Python 3.11
Django 4.1.7

Installazione e avvio:

Assicurarsi di avere Python 3.x installato sul proprio sistema.
Clonare questo repository sul proprio computer.
Aprire il terminale nella directory principale del progetto.
Installare le dipendenze eseguendo il comando pip install -r requirements.txt.
Eseguire le migrazioni del database con il comando python manage.py migrate.
Avviare il server di sviluppo con il comando python manage.py runserver.
Visitare http://localhost:8000/ nel browser per accedere al social network.
Nota finale:

Questo progetto è stato sviluppato per dimostrare capacità avanzate di Django e per illustrare le funzionalità di un social network. Il codice è rilasciato con una licenza aperta ed è liberamente accessibile sul nostro repository GitHub (inserire il link al repository qui). Ci auguriamo che questo progetto possa essere una risorsa utile per chiunque sia interessato a imparare e migliorare le proprie competenze con Django e lo sviluppo di social network dinamici e interattivi.
