# Skills d'enrichissement open source AgoraLive — v1

Trois skills scaffold pour transformer un nom de société / personne / programme de congrès en prospect qualifié dans Notion, **100% gratuit, sans aucun token à gérer**.

## Vue d'ensemble

| Skill | Rôle | Sources | Coût | Token ? |
|---|---|---|---|---|
| `enrich-societe-notion` | Complète une fiche Société (SIREN, dirigeants, NAF, effectif, site) | **API `recherche-entreprises.api.gouv.fr`** (DINUM / INSEE-INPI) + Google | 0€ | Non |
| `enrich-personne-notion` | Complète une fiche Personne (mail pro, LinkedIn, poste) | Google + DNS MX + (option Hunter free) | 0€ | Non |
| `find-prospects-congres` | Scan programme PDF de congrès → liste de prospects sponsors qualifiés dans Notion | Combine les deux ci-dessus | 0€ | Non |

Les trois skills se chaînent : `find-prospects-congres` invoque `enrich-societe-notion` puis `enrich-personne-notion` pour chaque exposant détecté.

**Pourquoi `recherche-entreprises.api.gouv.fr` plutôt que Pappers ?** C'est l'API officielle de l'État français (DINUM), alimentée par les mêmes sources INSEE/INPI que Pappers. Pas d'inscription, pas de token, pas de quota dur, et c'est même plus solide côté RGPD (source publique étatique vs republier privé). Limite : pas de comptes annuels détaillés pour les SAS/SARL non cotées — pour 99% des besoins prospection sponsor c'est sans impact.

---

## Installation (option A — directement dans le plugin local)

Pour usage immédiat dans Cowork sans passer par GitHub :

```bash
PLUGIN_SKILLS="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/d5994f1a-b6cc-4d20-81ea-429ea551c7ac/d7de8551-bc1d-4382-b260-c3269b4e4a43/rpm/plugin_01Ny8pfWnV1tMEvfexZfkppT/skills"
SRC="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/d5994f1a-b6cc-4d20-81ea-429ea551c7ac/d7de8551-bc1d-4382-b260-c3269b4e4a43/local_5e3c8c01-71d1-4427-94d1-3de860f88413/outputs/skills"

cp -r "$SRC/enrich-societe-notion"   "$PLUGIN_SKILLS/"
cp -r "$SRC/enrich-personne-notion"  "$PLUGIN_SKILLS/"
cp -r "$SRC/find-prospects-congres"  "$PLUGIN_SKILLS/"
```

Au redémarrage de Cowork, les skills apparaissent.

⚠️ Les chemins de session changent à chaque session Cowork — adapte le segment `d5994f1a-…` si tu lances le copier-coller plus tard. Plus simple : utilise l'option B.

---

## Installation (option B — via ton repo GitHub `agoralive-plugins`)

C'est ce que tu veux. Les commandes ci-dessous supposent que tu as déjà cloné le repo localement. Sinon :

```bash
cd ~/dev   # ou là où tu mets tes repos
git clone https://github.com/Yawanop/agoralive-plugins.git
cd agoralive-plugins
```

### Étape 1 — Comprendre la structure de ton repo

Avant de copier, lance ça depuis `agoralive-plugins/` et regarde la sortie :

```bash
ls -la
find . -maxdepth 3 -name "SKILL.md" | head -20
cat .claude-plugin/plugin.json 2>/dev/null || cat plugin.json 2>/dev/null || echo "(pas de plugin.json à la racine)"
cat .claude-plugin/marketplace.json 2>/dev/null || cat marketplace.json 2>/dev/null || echo "(pas de marketplace.json à la racine)"
```

Tu auras une de ces structures :

**Cas 1 — Plugin unique** : un dossier `skills/` directement à la racine du repo.
```
agoralive-plugins/
├── .claude-plugin/plugin.json
├── skills/
│   ├── agent-pauline/SKILL.md
│   ├── mail-rediger/SKILL.md
│   └── ...
```

**Cas 2 — Marketplace multi-plugins** : un dossier par plugin (`agoralive-core/`, etc.) avec `skills/` à l'intérieur.
```
agoralive-plugins/
├── .claude-plugin/marketplace.json
├── agoralive-core/
│   ├── .claude-plugin/plugin.json
│   └── skills/
│       ├── agent-pauline/SKILL.md
│       └── ...
```

### Étape 2 — Copier les skills depuis Cowork

Garde le terminal ouvert dans `agoralive-plugins/`. Le `SRC` ci-dessous est le chemin Cowork de tes 3 skills (à adapter si la session change).

```bash
SRC="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/d5994f1a-b6cc-4d20-81ea-429ea551c7ac/d7de8551-bc1d-4382-b260-c3269b4e4a43/local_5e3c8c01-71d1-4427-94d1-3de860f88413/outputs/skills"

# Cas 1 (plugin unique à la racine)
cp -r "$SRC/enrich-societe-notion"   skills/
cp -r "$SRC/enrich-personne-notion"  skills/
cp -r "$SRC/find-prospects-congres"  skills/

# Cas 2 (marketplace, plugin agoralive-core)
cp -r "$SRC/enrich-societe-notion"   agoralive-core/skills/
cp -r "$SRC/enrich-personne-notion"  agoralive-core/skills/
cp -r "$SRC/find-prospects-congres"  agoralive-core/skills/
```

Choisis UNE des deux variantes selon ta structure.

### Étape 3 — Vérifier ce qui est ajouté

```bash
git status
git diff --stat
```

Tu dois voir trois nouveaux dossiers `enrich-societe-notion/`, `enrich-personne-notion/`, `find-prospects-congres/` chacun avec un `SKILL.md`.

### Étape 4 — Commit + push

```bash
git add skills/enrich-societe-notion skills/enrich-personne-notion skills/find-prospects-congres
#  ou pour le cas 2 :
# git add agoralive-core/skills/enrich-societe-notion agoralive-core/skills/enrich-personne-notion agoralive-core/skills/find-prospects-congres

git commit -m "feat: add 3 open-source enrichment skills (recherche-entreprises gov API, no token)"
git push origin main
```

Si ta branche par défaut n'est pas `main` (par exemple `master` ou `develop`) :

```bash
git push origin HEAD
```

### Étape 5 — Re-synchroniser le plugin local

Une fois pushé, pour que Cowork voie la version GitHub des skills, tu peux soit :
- attendre que Claude resynchronise le plugin au prochain démarrage (si configuré pour pull auto),
- soit faire un `git pull` dans le dossier du plugin local (`~/Library/Application Support/Claude/.../plugin_01Ny8pfWnV1tMEvfexZfkppT/`) — vérifie d'abord si ce dossier est lui-même un clone git :
  ```bash
  cd "$HOME/Library/Application Support/Claude/local-agent-mode-sessions/.../rpm/plugin_01Ny8pfWnV1tMEvfexZfkppT"
  git remote -v
  git pull
  ```

---

## Test POC : ADF 2024

Une fois les skills installés et reconnus par Cowork :

1. Récupère le programme officiel ADF 2024 (PDF) — disponible sur https://www.adf.asso.fr → Congrès → édition 2024.
2. Dépose le PDF dans Cowork.
3. Dis : *"Lance `find-prospects-congres` sur ce programme ADF 2024"*.
4. Le skill enchaîne automatiquement les 3 étapes (extraction PDF → enrichissement API gouv pour chaque société → identification contact commercial) et te livre une Top 10 prête pour Éloïse.

Temps attendu : 20-30 min pour ~50 sociétés (plus rapide qu'avant, l'API gouv n'a pas de quota bloquant).

Critères de succès POC :
- ≥85% des sociétés ont leur SIREN trouvé (l'API gouv couvre toutes les sociétés FR enregistrées)
- ≥60% des contacts identifiés ont un email score HIGH ou MEDIUM
- 0 fiche Notion dupliquée (dédoublonnage)
- Argument de matching utilisable tel quel sur 5+ contacts sur 10

---

## Checklist RGPD à valider par Olivia (avant industrialisation)

Avant utilisation pour de la **vraie prospection sortante**, invoque `audit-rgpd` (Olivia) sur le pipeline. Points à valider :

### Base légale
- [ ] Intérêt légitime B2B (article 6.1.f RGPD) validé pour l'usage des skills.
- [ ] Balance test intérêt légitime vs droits des personnes formalisée (template CNIL B2B).

### Sources des données
- [ ] `recherche-entreprises.api.gouv.fr` = API officielle DINUM, données INSEE/INPI publiques → ✅ légal par construction, source étatique.
- [ ] Google search publique = pas de scraping authentifié → ✅ conforme CGU.
- [ ] LinkedIn = uniquement données publiques indexées par Google → ✅ conforme CGU LinkedIn.
- [ ] DNS MX validation = standard internet → ✅ OK.
- [ ] **À valider Olivia** : SMTP probing (étape optionnelle de `enrich-personne-notion`).

### Traçabilité (article 13)
- [ ] Champ `📝 Notes enrichissement` dans Notion = trace de chaque source + date.
- [ ] Format de la mention validé par Olivia.

### Premier contact mail
- [ ] Mention "vous pouvez vous opposer au traitement de vos données" validée par Olivia + `validation-legale-message`.
- [ ] Pas de pixel tracking caché dans le 1er mail.
- [ ] Lien désinscription / mail de contact présent.

### Droits des personnes
- [ ] Process d'effacement formalisé (suppression fiche Notion + log).
- [ ] Process d'opposition formalisé (flag + arrêt relances).
- [ ] Registre des traitements à jour.

### Volumétrie
- [ ] Limiter à <100 nouveaux prospects/semaine en v1.
- [ ] Revoir à 500 prospects en base.

### Spécifique dentaire
- [ ] Si praticien individuel → flag spécifique (mélange perso/pro = base légale B2B fragile).
- [ ] `audit-code-sante-publique` pour contenus mentionnant des dispositifs médicaux.

---

## Bascule v2 (post-POC)

Une fois POC ADF 2024 validé, options pour passer en v2 :

1. **Sirene v3 INSEE** (~5 min de setup, gratuit avec token unique à demander) — alternative ou complément, pour les cas où l'API recherche-entreprises est sous tension.
2. **Pappers payant** (~50€/mois pour 10k req/mois + comptes annuels détaillés) — utile si Éloïse veut le CA précis sur des cibles Tier 1.
3. **Dropcontact** (~50-100€/mois) — bascule emails de heuristique → API RGPD-compliant FR pour gros volumes.
4. **Auto-trigger Notion** — déclenchement automatique sur création d'item (effort dev Philippe S/M).
5. **Batch mensuel** — scheduled task qui rescanne les fiches avec champs vides.

Mon avis : valide POC d'abord, puis ajoute Pappers payant UNIQUEMENT si le CA précis devient bloquant côté Éloïse pour la négo Tier 1.

---

## Fichiers livrés

```
skills/
├── README.md                         # ce fichier
├── enrich-societe-notion/
│   └── SKILL.md
├── enrich-personne-notion/
│   └── SKILL.md
└── find-prospects-congres/
    └── SKILL.md
```

Tous les skills suivent la convention AgoraLive : frontmatter YAML pour le routing intelligent, procédure étape par étape, identifiants Notion en bas, skills liés.

---

## Questions ouvertes pour Paul

1. **Mention RGPD** : tu veux que je drafte la formulation "vous pouvez vous opposer" pour le 1er mail prospection, ou tu laisses Olivia la formuler ?
2. **Process de qualification** : qui valide humainement la Top 10 (Éloïse seule ? trinôme Comm pour les 1ers envois) ?
3. **Auto-trigger v2** : on attend que Philippe ait fini le sprint en cours avant d'envisager l'automation Notion ?
4. **Volume cible** : si la prospection part fort, on doit décider du seuil où on bascule sur Pappers payant (pour le CA détaillé) — quel CA min pour qu'un sponsor justifie l'effort ?
