# bib-cost-saver
Automatisch die medien verlöngern


## prolong

	https://metropol-mediensuche.de/services/de/metropolcard/prolong

    post {"libraryId":8726,"recordId":"0734206004","steps":[{"actionId":0}]}
    response {"status":"CONFIRMATION_NEEDED","actionId":0,"details":[{"text":"Neues vom Räuber Hotzenplotz","label":"Titel"},{"text":"08.05.2023","label":"Aktuelle Frist"},{"text":"12.06.2023","label":"Neue Frist nach Verlängerung"},{"text":"keine","label":"Gebühren"}]}

    Check response and send another request to https://metropol-mediensuche.de/services/de/metropolcard/prolong
    post: {"libraryId":8726,"recordId":"0734206004","steps":[{"actionId":0},{"actionId":2}]} // clicked on ok
    Response: {"status":"OK","actionId":0}

    send get to https://metropol-mediensuche.de/services/de/metropolcard/account/info