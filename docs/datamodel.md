---
title: App Data Model
nav_order: 1
---

# **app data model after extension**

![Data-Model](/static/images/datamodel_web.png)



## changes to baseline:

Im Vergleich zum Baseline-Modell, ist nun eine neue Klasse _User_ hinzugefügt worden. <br>
Die neue Klasse beinhaltet eine _ID_ als Primärschlüssel und die Attribute _username_ (String) und _password_ (String). <br>
Jedes _Todo_ und jede _List_ benötigt genau eine Zuweisung zu einem bestimmten _User_. <br>
_User_ können jedoch mehrere _Todos_ und _Listen_ erstellen und wie es auch nach dem erstmaligen Login der Fall ist, gar keine haben. <br>
Durch diese Zuweisung erforden die Klassen _Todo_ und _List_ einen Fremdschlüssel = _user_id_ (user.id), damit jeder _User_ nur seine eigenen Aktivitäten sehen und bearbeiten kann. <br>
_Todo_list_ wird dadurch ebenfalls indirekt individuell auf den _User_ angepasst. <br>