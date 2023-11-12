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

| Status Code | Beschreibung                  |
|-------------|-------------------------------|
| 200         | OK - Erfolgreiche Anfrage     |
| 303         | Umleitung     |
| 400         | Schlechte Anfrage - Fehlerhaft|
| 401         | Unautorisierter Zugriff (Kein Login)|
| 403         | Keine Zugriffsberechtigung (Falscher Account)|
| 404         | Nicht gefunden                |
| 500         | Interner Serverfehler         |

<br>

## API ENDPUNKTE
---
### Route: `/index`

**def():** `index()`

**Methods:** `GET`

**Purpose:** Diese Route leitet den Benutzer zur Login-Seite weiter.

<br>

---

### Route: `/todos/`

**def():** `todos()`

**Methods:** `GET, POST`

**Purpose:** Zeigt alle `todos` des eingeloggten Benutzers an und ermöglicht das Erstellen neuer `todos` und deren Hinzufügen zur Datenbank.

<br>

---

### Route: `/todos/<int:id>`

**def():** `todo(id)`

**Methods:** `GET, POST`

**Purpose:** Ermöglicht das Anzeigen und Aktualisieren einer einzelnen `todo` anhand ihrer ID. Der Benutzer kann die `todo`-Beschreibung und die zugehörige Liste ändern, oder die `todo` löschen.

<br>

---

### Route: `/lists/`

**def():** `lists()`

**Methods:** `GET, POST`

**Purpose:** Zeigt alle `lists` des eingeloggten Benutzers an und ermöglicht das Erstellen neuer `lists` und deren Hinzufügen zur Datenbank.

<br>

---

### Route: `/lists/<int:id>`

**def():** `list(id)`

**Methods:** `GET`

**Purpose:** Zeigt die Details einer einzelnen `lists` anhand ihrer ID.


<br>

---

### Route: `/`

**def():** `home()`

**Methods:** `GET`

**Purpose:** Zeigt die Startseite an.

<br>

---

### Route: `/login`

**def():** `login()`

**Methods:** `GET, POST`

**Purpose:** Zeigt die Login-Seite an und ermöglicht Benutzern das Einloggen.

<br>

---

### Route: `/dashboard`

**def():** `dashboard()`

**Methods:** `GET, POST`

**Purpose:** Zeigt die Dashboard-Seite an, die nur eingeloggten Benutzern zugänglich ist.

<br>

---

### Route: `/logout`

**def():** `logout()`

**Methods:** `GET, POST`

**Purpose:** Ermöglicht eingeloggten Benutzern das Ausloggen.

<br>

---

### Route: `/profile`

**def():** `profile()`

**Methods:** `GET, POST`

**Purpose:** Zeigt die Profilseite des eingeloggten Benutzers an.

<br>

---

### Route: `/delete_account`

**def():** `delete_account()`

**Methods:** `GET, POST`

**Purpose:** Ermöglicht eingeloggten Benutzern das Löschen ihres Benutzerkontos. Dieser Vorgang löscht auch alle zugehörigen `todos` und `lists`.

<br>

---

### Route: `/register`

**def():** `register()`

**Methods:** `GET, POST`

**Purpose:** Zeigt die Registrierungsseite an und ermöglicht Benutzern die Registrierung in der Anwendung.

---