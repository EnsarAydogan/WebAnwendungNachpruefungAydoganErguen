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

Es wurde beschlossen, Flask-RESTful API zu verwenden, um die RESTful API-Funktionen der Webanwendung zu implementieren. Dies wurde aufgrund der folgenden Gründe entschieden:

- **Schnelle Entwicklung**: Flask-RESTful API bietet eine einfache und schnelle Möglichkeit, RESTful APIs zu entwickeln, was die Entwicklungszeit verkürzt.

- **Bewährte Technologie**: Flask-RESTful ist eine etablierte Erweiterung für Flask, die speziell für die Erstellung von RESTful APIs entwickelt wurde.

- **Dokumentation und Tutorials**: Es gibt eine Fülle von Dokumentation und Tutorials zur Verwendung von Flask-RESTful, was die Implementierung erleichtert.

- **Standardkonformität**: Flask-RESTful folgt bewährten Standards und Praktiken für RESTful APIs.

- **Einfache Integration**: Die Erweiterung lässt sich problemlos in eine vorhandene Flask-Anwendung integrieren.

### In Betracht gezogene Optionen

Alternativ zur Flask-RESTful API könnten benutzerdefinierte Implementierungen oder andere Flask-Erweiterungen zur Erstellung von RESTful APIs verwendet werden. Die Verwendung von Flask-RESTful wurde gewählt, da sie als bewährte und effiziente Lösung für die Implementierung von RESTful APIs gilt.

---
