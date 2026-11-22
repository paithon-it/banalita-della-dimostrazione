#!/usr/bin/env bash
# Salva la chiave API di Anthropic per l'esperimento, fuori dal repository, leggibile solo
# dall'utente. Da lanciare a mano (anche dall'app SSH del telefono): la chiave non passa
# dalla chat né dalla riga di comando, e non compare a schermo.
set -euo pipefail
dir="$HOME/.config/banalita-della-dimostrazione"
mkdir -p "$dir" && chmod 700 "$dir"
read -r -s -p "Chiave API di Anthropic (non viene mostrata): " key; echo
case "$key" in sk-ant-*) ;; *) echo "non sembra una chiave Anthropic (sk-ant-...): non salvo" >&2; exit 1 ;; esac
umask 077
printf 'ANTHROPIC_API_KEY=%s\n' "$key" > "$dir/chiave.env"
echo "salvata in $dir/chiave.env (permessi 600)"
