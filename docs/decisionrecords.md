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

### Entscheidung

Es wurde beschlossen, Flask-Login-Manager zu verwenden, um die Authentifizierungsfunktionen der Webanwendung zu implementieren. Dies wurde aufgrund der folgenden Gründe entschieden:

- **Einfache Integration**: Flask-Login-Manager lässt sich leicht in eine Flask-Anwendung integrieren und bietet alle erforderlichen Funktionen für die Benutzerverwaltung.

- **Bewährte Technologie**: Flask-Login-Manager ist eine bewährte Lösung in der Flask-Community und wird häufig für die Implementierung von Benutzerauthentifizierung und -verwaltung verwendet.

- **Flexibilität**: Es ermöglicht die Implementierung von Sitzungsverwaltung, Rollenbasierte Zugriffskontrolle und die Anpassung an die Anforderungen der Anwendung.

- **Aktive Community**: Flask-Login-Manager wird von einer aktiven Entwickler-Community unterstützt, was sicherstellt, dass Sicherheitsupdates und Aktualisierungen verfügbar sind.

### In Betracht gezogene Optionen

Andere Optionen zur Implementierung der Benutzerauthentifizierung wären beispielsweise das Rollen- und Berechtigungssystem von Flask oder eine benutzerdefinierte Implementierung. Die Verwendung des Flask-Login-Managers wurde gewählt, da es als robuste und benutzerfreundliche Lösung gilt.

---
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

Es wurde beschlossen, Flask-RESTful API zu verwenden, um die RESTful API-Funktionen der Webanwendung zu implementieren. Die Begründung erfolgt im nächsten Punkt.

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
