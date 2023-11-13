---
title: Decision Records on Flask extensions
nav_order: 3
---

## 01: Verwendung von Flask-Login-Manager

### Meta

Status
: Final - Beschlossen

Updated
: 15-Oct-2023

### Problemstellung

Die Webanwendung benötigt eine Authentifizierungsfunktion, um Benutzer zu verwalten, ihre Sitzungen zu speichern und den Zugriff auf bestimmte Bereiche der Anwendung zu steuern.



### In Betracht gezogene Optionen

Wir haben uns mit folgenden Flask-Erweiterungen auseinandergesetzt:

+ Flask-HTTPAuth
+ Flask-Login
+ Flask-Praetorian
+ Flask-User
---
| Kriterium | Flask-HTTPAuth | Flask-Login | Flask-Praetorian | Flask-User |
| --- | --- | --- | --- | --- |
| **Vorteile** | Einfache Integration von HTTP-Authentifizierung; Anfängerfreundlich | Ausführliche und übersichtliche Dokumentation; viele Video-Erklärungen; sehr Anfängerfreundlich, Flexibel in Authentifizierung und Datenbanknutzung| Ausführliche Dokumentation, starke Sicherheit | Anpassbare Benutzerauthentifizierung, Rolle-basierte Autorisierung und Internationalisierung  |
| **Nachteile** | Relativ kurze Dokumentation | Behandelt keine Benutzerregistrierung/ Kontowiederherstellung | geringe Auswahl bei Video-Tutorials; weniger Anfängerfreundlich | komplex für Neueinsteige |

### Entscheidung

 Wir haben uns aufgrund der guten Dokumentation, Erklärvideos und ausreichenden Funktionalitäten dazu entschieden, Flask-Login für die Implementierung der Authentifizierungsfunktionen unserer Webanwendung zu verwenden.

<br>
<br>


## 02: Verwendung von Flask-RESTful API

### Meta

Status
: Final - Beschlossen

Updated
: 22-Oct-2023

### Problemstellung

Die Webanwendung benötigt eine RESTful API, um eine Schnittstelle für den Zugriff auf Ressourcen und Daten der Anwendung bereitzustellen.

### Entscheidung

Es wurde beschlossen, Flask-RESTful API zu verwenden, um die RESTful API-Funktionen der Webanwendung zu implementieren. Die Begründung erfolgt im weiteren Verlauf.

### In Betracht gezogene Optionen
Wir haben uns mit folgenden Flask-Erweiterungen auseinandergesetzt:

+ Flask-RESTful
+ Flask-Restless-NG
+ Flask-RESTX
+ Flask-smorest

| Kriterium | Flask-RESTful | Flask-Restless-NG | Flask-RESTX | Flask-smorest |
| --- | --- | --- | --- | --- |
| **Know-how** | Erfahrung mit Flask-RESTful | - | - | - |
| **Aktive Entwicklung** | Aktiv | Nicht aktiv | Aktiv | Aktiv |
| **Flexibilität** | Moderat | Gering | Hoch | Moderat |
| **Dokumentation** | Gute Dokumentation | Gering | Gute Dokumentation | Gute Dokumentation |
| **RESTful-Features** | Basisfunktionalitäten | Begrenzt | Umfangreich | Umfangreich |

### Begründung für die Auswahl von Flask-RESTful
Nach sorgfältiger Evaluierung verschiedener Flask-Erweiterungen haben wir uns für Flask-RESTful entschieden. Die Entscheidung wurde aufgrund der folgenden Schlüsselkriterien getroffen:

1. **Know-how**: Da bereits Erfahrung mit Flask-RESTful vorhanden ist, konnte das bestehende Wissen effektiv genutzt werden.

2. **Aktive Entwicklung**: Flask-RESTful ist aktiv und wird weiterentwickelt, im Gegensatz zu Flask-Restless-NG, das nicht mehr aktiv unterstützt wird.

3. **Flexibilität**: Flask-RESTful bietet ausreichend Flexibilität, ohne die Einfachheit zu vernachlässigen.

4. **Dokumentation**: Flask-RESTful verfügt über eine gute Dokumentation, was die Entwicklung und Wartung erleichtert.

---
