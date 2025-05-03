<div align="center">

![Image](https://github.com/user-attachments/assets/04c68e93-e88b-45d2-bfab-8060c906dd7c)

# [Codex-Workspace](https://github.com/Sunwood-ai-labs/Codex-Workspace)

<p align="center">
  <img src="https://img.shields.io/badge/OpenAI_Codex-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI Codex">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Automation-000000?style=for-the-badge&logo=robot&logoColor=white" alt="Automation">
</p>

<p align="center">
  OpenAI Codexを活用したシンプルで効率的なGitHub Actionsワークフロー集
</p>

</div>

## 🚀 概要

このリポジトリは、OpenAI Codexの強力な機能をGitHub Actions内で活用し、リポジトリの自動化を実現する軽量なワークフロー集です。重たい処理を避け、必要最小限の機能に絞ることで、シンプルさと効率性を両立しています。

## ✨ 特徴

- 💬 **Issue自動応答**: 新しいissueや更新に対して、Codexが内容を分析し適切な返信や修正を提供
- 📝 **ドキュメント品質チェック（ベータ版）**: READMEやドキュメントの品質を自動で確認し、改善提案をPRで実施
- 🔍 **コードレビュー（ベータ版）**: PRのコードを自動レビューし、改善点を提案
- 🌐 **README翻訳（ベータ版）**: README.mdを日本語に自動翻訳してPRを作成
- 📜 **リリースノート自動生成**: タグpush時にCodexでリリースノートを生成し、GitHub Releaseを作成

## 📦 セットアップ

以下の手順に従い、リポジトリを初期化し、必要な環境変数やシークレットを設定してください。

### 1. リポジトリをクローン

```bash
git clone https://github.com/<USERNAME>/<REPO>.git
cd <REPO>
```

### 2. .envファイルの作成

```bash
cp .env.example .env
```
`.env`ファイルを開き、以下の環境変数を設定してください：

* `OPENAI_API_KEY`    : OpenAI APIキー  
* `GITHUB_TOKEN`      : GitHub APIトークン（省略可、GitHub Actionsでは自動で提供されます）  
* `CODEX_QUIET_MODE`  : Codexのクワイエットモード（例: `1`）  

### 3. シークレットの設定（GitHub Actions用）

GitHubリポジトリの Settings > Secrets で以下を追加してください：

* `OPENAI_API_KEY` : OpenAI APIキー  

### 4. ワークフローの有効化

`.github/workflows/` にあるワークフローファイルが自動的に有効になります。

## 🛠️ 使用方法

### Issue自動応答

1. Issueを作成または更新
2. Codexが内容を分析し、適切な返信を投稿
3. コード修正が必要な場合は自動的にPRを作成

### ドキュメント品質チェック

1. マークダウンファイルをプッシュまたはPR作成
2. Codexが品質をチェックし、改善点を自動修正
3. 修正内容をPRとして提案

### コードレビュー

1. 新しいPRを作成
2. Codexが変更内容をレビュー
3. 改善提案をコメントとして投稿

 ### README翻訳

1. README.mdを更新
2. 自動的に日本語版を作成
 3. README.ja.mdとしてPRを作成
   
 ### リリースノート自動生成

 1. タグを `v*` の形式で push
 2. auto-release-notes ワークフローが実行され、変更差分を解析して `release_notes.md` を生成
 3. `release_notes.md` に基づいて GitHub Release を作成

## ⚙️ ワークフロー一覧

| ワークフロー | トリガー | 説明 |
|------------|--------------------|----------------------------|
| `auto-release-notes.yml` | push（タグ `v*`） | リリースノートの自動生成 |
| `issue-response-codex.yml` | Issue作成／編集、コメント投稿 | Issueへの自動応答 |
| `beta-code-review-codex.yml` | PR作成／更新 | コードレビュー (ベータ版) |
| `beta-document-quality-check.yml` | Markdownファイル変更 | ドキュメント品質チェック (ベータ版) |
| `beta-readme-translation-codex.yml` | README.md変更 | README翻訳 (ベータ版) |

※ `beta-*.yml` はベータ版です。実験的機能のため、利用時はご注意ください。

## 🔧 カスタマイズ

各ワークフローのCodexプロンプトをカスタマイズすることで、プロジェクトのニーズに合わせた動作調整が可能です。

## 📝 注意事項

- Codexは `CODEX_QUIET_MODE=1` でノイズを最小限に抑制
- `-a auto-edit` オプションで自動承認モードを有効化
- すべての処理は日本語プロンプトで実行

## 🤝 コントリビューション

改善提案やバグ報告は、Issueでお知らせください。PRも歓迎です！

## 📄 ライセンス

MIT License
