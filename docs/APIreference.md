---
title: API Reference
nav_order: 2
---

[Ensar Aydogan & Mirkan Ergün]
{: .label }

# [API reference]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

<br>

## REST
---
Die To-Do API ist eine Flask-RESTful API. Das bedeutet, dass die API so konzipiert ist, dass Sie Objekte mit den HTTP-Verben GET, POST, PATCH und DELETE abrufen, erstellen, aktualisieren und löschen können.

Anzeigen der Attribute einer Todo / Ändern der Todo Attribute / Löschen einer Todo

GET `/api/todos/<int:todo_id>` / PATCH `/api/todos/<int:todo_id>` / DELETE `/api/todos/<int:todo_id>`


<br>

Anzeigen aller Todos / Hinzufügen einer Todo:

GET `/api/todos/` / POST: `/api/todos/`

<br>



## JSON
---
Die To-Do API kommuniziert ausschließlich in JSON.

<br>

## HTTP Status Codes
---

| Status Code | Beschreibung                  | Fehlerbehebung |
|-------------|-------------------------------|----------------|
| 200         | OK - Erfolgreiche Anfrage     |        ---     |  
| 303         | Umleitung                     |        ---     | 
| 400         | Schlechte Anfrage - Fehlerhaft| Überprüfen Sie die Anfragedaten  | 
| 401         | Unautorisierter Zugriff       | Zugriff ohne Login nicht möglich |  
| 403         | Keine Zugriffsberechtigung    | Dieser Account kann auf den Inhalt nicht zugreifen | 
| 404         | Nicht gefunden                | Route oder Todo_id nicht vorhanden |
| 500         | Interner Serverfehler         |        ---     |

<br>

## API ENDPUNKTE
---

### Route: `/todos/`

**def():** `todos()`

**Purpose:** Zeigt alle `todos` des eingeloggten Benutzers an und ermöglicht das Erstellen neuer `todos` und deren Hinzufügen zur Datenbank.

<br>

**Exemplare:**

***Request:*** `GET`

***Response:*** 
{"todos":[
{"complete": false, "description": "Hausarbeit schreiben", "id": 1, "user_id": 1…},
{"complete": false, "description": "Zimmer aufräumen", "id": 2, "user_id": 1…},
{"complete": false, "description": "E-Mails schreiben", "id": 3, "user_id": 1…},
{"complete": false, "description": "Wäsche", "id": 4, "user_id": 1},
{"complete": false, "description": "Präsentation vorbereiten", "id": 5, "user_id": 1…}
]
}

***Status Code:*** 200 OK

<br>

***Request:*** `POST` {
  "description": "Neue Aufgabe erstellen",
  "completed": false
}


***Response:*** 
{
"message": "Neue To-Do erstellt"
}

***Status Code:*** 200 OK

<br>

***Request:*** `PATCH`
{
"todos":[
{"complete": false, "description": "Zimmer aufräumen von Schwester", "id": 2, "user_id": 1…},
{"complete": false, "description": "E-Mails schreiben", "id": 3, "user_id": 1…},
{"complete": false, "description": "Wäsche", "id": 4, "user_id": 1},
{"complete": false, "description": "Präsentation vorbereiten", "id": 5, "user_id": 1…},
{"complete": false, "description": "Neue Aufgabe erstellen", "id": 11, "user_id": 1…}
]
}

***Response:*** 
{
"message": "The method is not allowed for the requested URL."
}

***Status Code:*** 405 METHOD NOT ALLOWED

<br>


***Request:*** `DELETE`

***Response:*** 
{
"message": "The method is not allowed for the requested URL."
}

***Status Code:*** 405 METHOD NOT ALLOWED

<br>

---

### Route: `/todos/<int:id>`

**def():** `todo(id)`

**Purpose:** Ermöglicht das Anzeigen und Aktualisieren einer einzelnen `todo` anhand ihrer ID. Der Benutzer kann die `todo`-Beschreibung und die zugehörige Liste ändern, oder die `todo` löschen.

<br>

**Exemplare:**

***Request:*** `GET` (/todos/1)

***Response:*** 
{
"complete": false,
"description": "Hausarbeit schreiben",
"id": 1,
"user_id": 1
}

***Status Code:*** 200 OK

<br>


***Request:*** `POST` (/todos/1)

***Response:*** 
/

***Status Code:*** 405 METHOD NOT ALLOWED

<br>


***Request:*** `PATCH`
{
"complete": true,
"description": "Hausarbeit schreiben",
"id": 1,
"user_id": 1
}

***Response:*** 
{
"message": "To-Do aktualisiert"
}

***Status Code:*** 200 OK

<br>


***Request:*** `DELETE` (/todos/1)

***Response:*** 
{
"message": "To-Do gelöscht"
}

***Status Code:*** 200 OK

<br>


---