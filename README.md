# AgoraLive Plugins

Marketplace interne des plugins AgoraLive pour Claude Code / Cowork.

## À quoi ça sert

Ce repo centralise tous les plugins utilisés par l'équipe AgoraLive : skills métier (routing Notion, triage contrats, bugs PO, articles SFODF…), connecteurs MCP partagés, et utilitaires communs.

Chaque membre de l'équipe s'y abonne **une fois**, puis reçoit les mises à jour automatiquement.

## Comment s'abonner (à faire par chaque membre, une seule fois)

Dans Claude Code (ou via Cowork) :

```
/plugin marketplace add paulboury/agoralive-plugins
```

Puis on installe le ou les plugins selon son rôle :

```
/plugin install agoralive-core@agoralive-plugins
```

## Plugins disponibles

| Plugin | Pour qui | Contenu |
|---|---|---|
| `agoralive-core` | **Toute l'équipe** | Routing documents Notion+Drive, planification, utilitaires partagés |

D'autres plugins (rôle légal, dev, médical…) seront ajoutés au fur et à mesure.

## Maintenance

Les évolutions se font sur la branche `main`. Toute modification mergée est immédiatement disponible pour les membres abonnés (au prochain refresh marketplace).

## Contact

Paul Boury — paulboury1@gmail.com
