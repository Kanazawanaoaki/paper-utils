#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "使い方: $0 BASE_NAME"
  echo "例    : $0 20250417_attachment_tong_use_testx2"
  exit 1
fi

BASE="$1"

# 1) カレント直下の同名ファイルを優先的に候補に
CANDIDATES=()
[[ -f "./${BASE}.mp4" ]] && CANDIDATES+=("./${BASE}.mp4")
[[ -f "./${BASE}.MP4" ]] && CANDIDATES+=("./${BASE}.MP4")
[[ -f "./${BASE}.mov" ]] && CANDIDATES+=("./${BASE}.mov")
[[ -f "./${BASE}.MOV" ]] && CANDIDATES+=("./${BASE}.MOV")

# 2) 見つからなければ、同名ディレクトリ内を探索
if [[ ${#CANDIDATES[@]} -eq 0 && -d "./${BASE}" ]]; then
  # 同名の動画があればそれを優先
  [[ -f "./${BASE}/${BASE}.mp4" ]] && CANDIDATES+=("./${BASE}/${BASE}.mp4")
  [[ -f "./${BASE}/${BASE}.MP4" ]] && CANDIDATES+=("./${BASE}/${BASE}.MP4")
  [[ -f "./${BASE}/${BASE}.mov" ]] && CANDIDATES+=("./${BASE}/${BASE}.mov")
  [[ -f "./${BASE}/${BASE}.MOV" ]] && CANDIDATES+=("./${BASE}/${BASE}.MOV")

  # まだ無ければ任意の .mp4/.MOV を拾う（最初の1本）
  if [[ ${#CANDIDATES[@]} -eq 0 ]]; then
    mapfile -t ANY_IN_DIR < <(find "./${BASE}" -maxdepth 1 -type f \( -iname '*.mp4' -o -iname '*.mov' \) | sort)
    if [[ ${#ANY_IN_DIR[@]} -gt 0 ]]; then
      CANDIDATES+=("${ANY_IN_DIR[0]}")
    fi
  fi
fi

if [[ ${#CANDIDATES[@]} -eq 0 ]]; then
  echo "エラー: 入力動画が見つかりませんでした。以下を確認してください。"
  echo " - ./${BASE}.mp4 / .MOV が存在するか"
  echo " - または ./${BASE}/ ディレクトリ内に .mp4 / .MOV があるか"
  exit 2
fi

INPUT="${CANDIDATES[0]}"
OUTDIR="./${BASE}"
mkdir -p "${OUTDIR}"

echo "入力動画 : ${INPUT}"
echo "出力先   : ${OUTDIR}/${BASE}-%05d.jpg"

# ユーザ指定の等価コマンドで実行
ffmpeg -i "${INPUT}" -f image2 -vcodec mjpeg -qscale 1 -qmin 1 -qmax 1 "${OUTDIR}/${BASE}-%05d.jpg"
