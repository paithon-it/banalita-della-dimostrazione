#!/usr/bin/env bash
# Cancella la cartella di lavoro dell'esperimento sulla macchina con la GPU, e niente altro:
# si rifiuta se il percorso non finisce in /rnd/banalita.
set -euo pipefail
RND="${RND:-$HOME/rnd/banalita}"
case "$RND" in
  */rnd/banalita) ;;
  *) echo "rifiuto: $RND non finisce in /rnd/banalita" >&2; exit 2 ;;
esac
rm -rf -- "$RND"
echo "cancellata $RND"
