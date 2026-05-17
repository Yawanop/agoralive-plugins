#!/usr/bin/env bash
# AgoraLive — Installation du plugin agoralive-core
# Lance ce script depuis ton Terminal Mac pour installer automatiquement
# Claude Code + la marketplace AgoraLive + le plugin.

set -e

echo ""
echo "=================================="
echo "  🎤 AgoraLive Plugin Installer"
echo "=================================="
echo ""

# ============================
# 1. Vérification Claude Code
# ============================
if command -v claude &> /dev/null; then
  echo "✅ Claude Code CLI déjà installé."
else
  echo "❌ Claude Code CLI n'est pas installé."
  echo ""
  if command -v brew &> /dev/null; then
    echo "→ Installation via Homebrew..."
    brew install --cask claude-code
    echo "✅ Claude Code installé."
  else
    echo "Homebrew n'est pas installé. Installe-le d'abord :"
    echo '  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
    echo ""
    echo "Puis relance ce script."
    exit 1
  fi
fi

echo ""
# ============================
# 2. Ajouter la marketplace
# ============================
echo "→ Ajout de la marketplace AgoraLive..."
claude plugin marketplace add Yawanop/agoralive-plugins || {
  echo "⚠️  Échec ajout marketplace. Tu peux la faire manuellement :"
  echo "    Ouvre Claude Code (claude), puis tape :"
  echo "    /plugin marketplace add Yawanop/agoralive-plugins"
}

echo ""
# ============================
# 3. Installer le plugin
# ============================
echo "→ Installation du plugin agoralive-core..."
claude plugin install agoralive-core@agoralive-plugins || {
  echo "⚠️  Échec installation plugin. Tu peux la faire manuellement :"
  echo "    Dans Claude Code, tape :"
  echo "    /plugin install agoralive-core@agoralive-plugins"
}

echo ""
echo "=================================="
echo "✅ Plugin installé."
echo "=================================="
echo ""
echo "Prochaines étapes (à faire UNE fois, manuellement) :"
echo ""
echo "1. Ouvre Cowork (l'app desktop Claude)"
echo "2. Settings → Connectors"
echo "3. Active 2 connecteurs (OAuth, 2 clics chacun) :"
echo "     🔌 Notion (pour lire/écrire les bases AgoraLive)"
echo "     🔌 Google Drive (pour uploader les fichiers)"
echo ""
echo "4. Dans le chat Cowork, parle à TON jumeau selon qui tu es :"
echo ""
echo "   🦊 Paul     →  'Pauline brief-moi'"
echo "   🐺 Julien   →  'Julie brief-moi'"
echo "   🦁 Philippe →  'Philippine brief-moi'"
echo "   🦋 Éloïse   →  'Éloi brief-moi'"
echo "   🐘 Michel   →  'Michelle brief-moi'"
echo "   🦉 Olivier  →  'Olivia brief-moi'"
echo ""
echo "=================================="
echo "Guide complet :"
echo "https://www.notion.so/3636979fbcd181a9b371c184a0517fae"
echo "=================================="
