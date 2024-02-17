# Entwicklungsplan für SmartFitAI

## Überblick
Dieser Plan legt die Entwicklungsschritte für SmartFitAI fest, eine Kivy-basierte App, die sich auf Ernährung und Fitness konzentriert. Ziel ist es, einen iterativen und agilen Entwicklungsprozess zu nutzen, der die Integration von Supabase für Authentifizierung und später für die Datenverwaltung über PostgreSQL beinhaltet, sowie die Nutzung von GitHub und Volta für das Projektmanagement.

## Geplante Architektur der Anwendung

### App-Struktur
- **Hauptkomponenten**:
  - `main.py`: Der Startpunkt der App, wo die Hauptlogik und der Einstiegspunkt der Anwendung definiert sind.
  - `models/`: Hier befinden sich die Klassen und Datenmodelle für Nutzer, Rezepte und andere relevante Entitäten.
  - `artificial_intelligence/`: Dieses Verzeichnis ist für die KI-Integration vorgesehen, um personalisierte Empfehlungen und Funktionen zu entwickeln.
  - `database/`: Ursprünglich für die Speicherung von Daten in JSON5-Dateien genutzt, wird später die Migration zu einer Supabase PostgreSQL-Datenbank hier geplant und durchgeführt.
  - `utils/`: Eine Sammlung von Hilfsfunktionen und Werkzeugen, die quer durch die App genutzt werden können.
  - `tests/`: Enthält Testfälle für Einheits- und Integrationstests, um die Zuverlässigkeit der Anwendung zu gewährleisten.
  - `resources/`: Dieses Verzeichnis enthält statische Dateien wie Beispieldaten, Konfigurationsdateien und möglicherweise auch Multimedia-Ressourcen.
  - `pages/`: Hier werden die individuellen Bildschirmseiten der Kivy-App entwickelt. Jede Seite repräsentiert einen Teil der Benutzeroberfläche und ist verantwortlich für die Darstellung und Interaktion mit dem Benutzer.
  - `.github/`: Enthält Konfigurationen und Ressourcen für die Verwendung von GitHub, wie Workflow-Dateien für GitHub Actions und Templates für Issues und Pull Requests.

### Frontend-Entwicklung
- **Technologie**: Kivy für GUI-Entwicklung.
- **Features**:
  - Authentifizierung (Anmeldung und Registrierung).
  - Nutzerprofile (Alter, Gewicht, Geschlecht).
  - Kalorienbedarfsrechner.
  - Rezeptverwaltung und -suche.
  - Allergenwarnungen.

### Backend-Entwicklung
- **Datenmanagement**:
  - **Initiale Datenspeicherung**: Nutzung von JSON5-Dateien für Nutzer- und Rezeptdaten.
  - **Migration zu Supabase PostgreSQL**: Geplante Migration für verbesserte Skalierbarkeit und Effizienz.
- **Sicherheit**:
  - **Supabase Authentifizierung**: Implementierung von Beginn an für sichere Nutzerverifizierung.

## Technologiestack
- **Frontend**: Kivy.
- **Backend**: Python, JSON5 (initial), später Supabase PostgreSQL.
- **KI-Integration**: OpenAI API für personalisierte Empfehlungen.
- **Entwicklungswerkzeuge**: GitHub, virtuelle Python-Umgebungen, Volta für das Projektmanagement.

## Projektmanagement
- **GitHub**: Für Versionskontrolle, Milestones, Backlog Issues und Task Issues.
- **Volta**: Projektboard, synchronisiert mit GitHub, für Aufgabenverwaltung und Priorisierung.

## Geplante Sicherheit und Compliance
- **Datenschutz**: Entwicklung nach Datenschutz-Grundverordnungen (GDPR) und weiteren Bestimmungen.
- **Sicherheitspraktiken**: Einsatz von Best Practices, HTTPS für Datenübertragungen und sichere Authentifizierung über Supabase.

## Geplante Wartung und Monitoring
- **Logging und Überwachung**: Nutzung von Tools zur Leistungsüberwachung und frühzeitigen Problemerkennung.
- **Regelmäßige Updates**: Plan für Updates und Patches zur Sicherstellung der Aktualität und Sicherheit der App.

## Dokumentation und Standards
- **Code-Dokumentation**: Ausführliche Dokumentation des Codes, Architektur und Technologienutzung.
- **Coding-Standards**: Best Practices und Richtlinien für Python und Kivy, ergänzt um Supabase-spezifische Praktiken.
