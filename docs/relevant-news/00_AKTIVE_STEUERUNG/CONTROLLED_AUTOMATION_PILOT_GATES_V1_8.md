# Controlled Automation Pilot Gates - relevant-news V1.8

Dieses Dokument ist die technische Gate-Liste für den Controlled Automation Pilot. Es ergänzt die redaktionellen V1.8-Gates und verhindert, dass ein Import oder eine Routine alte V1.2-Automation, Versandpfade oder Rollenvermischung fortsetzt.

Diese Blockade gilt für den alten Controlled Automation Pilot, Recovery- und Legacy-Kontext. Für die drei aktuellen Scheduled-Operator-Test-Slots `scheduled_morning`, `scheduled_midday` und `scheduled_evening` gilt `TESTVERSAND_GATES_V1_8.md`; dort ist `actualSend=true` erlaubt, wenn Slot- und Send-Gates erfüllt sind.

---

## 1. Import-Gate

Import-Apply ist nur erlaubt, wenn alle Punkte erfüllt sind:

- Import-Dry-Run hat keine Errors und keine Warnings.
- Ziel-Company ist `485a2bb7-0c62-4468-97c7-d9a0a1043482`.
- Collision-Strategie für `ceo`, `cmo` und `cto` ist `skip`.
- Kein Import-Replace für bestehende Runtime-Management-Agenten.
- Projekt-Slug ist `relevant-news`, damit kein zweites Daily-Briefing-Projekt entsteht.
- Keine Secrets, API-Keys, SMTP-Daten oder Empfängerwerte im Package.
- Keine alten V1.2-Artefakte oder V1.2-Routinen werden als Grundlage übernommen.

Wenn einer dieser Punkte fehlt: kein Apply.

---

## 2. Runtime-Routinen-Gate

Vor Apply muss die bestehende Runtime geprüft werden:

- Keine aktive alte V1.2-Routine mit Schedule-Trigger.
- Keine aktive Routine mit Versandpfad, SMTP-Script oder Mailabschluss-Pfad.
- Keine Routine, die CTO als redaktionellen Ausführer/Reviewer einsetzt.
- Keine offene Routine-Execution, die alten V1.2-Kontext in neue V1.8-Arbeit trägt.

Wenn alte aktive Routinen existieren: Apply blockieren und Runtime-Audit im Laufartefakt-Ordner ablegen.

---

## 3. Pilot-Routine-Gate

Der Controlled Automation Pilot darf nur:

- ein Paperclip-Arbeitsobjekt erzeugen,
- CMO als Control Tower einsetzen,
- Spezialrollen-Handoff verlangen,
- Laufartefakte erzeugen,
- vor Versand stoppen.

Der Pilot darf nicht:

- Empfänger ableiten,
- SMTP oder Mail-Scripts ausführen,
- Reviewer-Gelb/Rot weichzeichnen,
- Source Verification überspringen,
- CTO als redaktionellen Reviewer einsetzen,
- alte V1.2-Runbooks als aktive Grundlage verwenden.

---

## 4. Versand-Gate für Pilot-/Legacy-Kontext

Versand und Testversand bleiben im alten Controlled-Automation-Pilot-, Recovery- und Legacy-Kontext blockiert, bis alle Punkte erfüllt sind:

- Source Verification ist für jede Top Story vollständig.
- Adversarial Reviewer gibt Grün.
- Kein Gelb oder Rot ist offen.
- Testempfänger sind explizit in der Runtime konfiguriert, nicht im Package.
- Ein technisches Runtime-Log liegt in `20_LAUFARTEFAKTE` vor.
- CMO bestätigt nur Prozessvollständigkeit; CEO/CTO überstimmen keine redaktionellen Gates.

Wenn ein Punkt fehlt: kein Versand, kein Testversand, keine Empfänger-Aktion.

---

## 5. Collision-Strategie

Für `ceo`, `cmo` und `cto` gilt:

```text
--collision skip
```

Grund:

- Bestehende Runtime-Agenten enthalten lokale Adapterkonfigurationen.
- Bestehende Runtime-Agenten enthalten Managed-Instruction-Pfade.
- Import-Replace könnte diese Runtime-Fidelity verlieren.

Änderungen an diesen Agenten erfolgen später gezielt über Board/API oder einen separaten, geloggten Runtime-Schritt.

---

## 6. Apply-Entscheidung

Apply ist aktuell blockiert, wenn das Runtime-Audit alte aktive Routinen findet.

Minimaler nächster sicherer Schritt:

1. Alte V1.2-Routinen pausieren oder archivieren.
2. Danach Dry-Run wiederholen.
3. Nur bei sauberem Dry-Run und erfülltem Runtime-Routinen-Gate Apply ausführen.
