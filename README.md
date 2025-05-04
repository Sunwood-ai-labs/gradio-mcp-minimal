---
title: Gradio MCP Minimal
emoji: 🌍
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 5.26.0
app_file: app.py
pinned: false
---

<div align="center">

![Image](https://github.com/user-attachments/assets/a48bdf11-baf1-4e6d-8f4f-10bc33a68551)


# 🚀 **Gradio MCP Minimal**

<p align="center">
  <a href="https://www.python.org">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white">
  </a>
  <a href="https://www.gradio.app">
    <img alt="Gradio" src="https://img.shields.io/badge/Gradio-5.26.0-orange?logo=gradio">
  </a>
  <a href="https://github.com/makiai/gradio-mcp-minimal/blob/main/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green">
  </a>
  <a href="https://github.com/makiai/gradio-mcp-minimal/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/makiai/gradio-mcp-minimal?style=social">
  </a>
<a href="https://huggingface.co/spaces/MakiAi/gradio-mcp-minimal">
    <img alt="HF Spaces" src="https://img.shields.io/badge/Spaces-Live%20Demo-blueviolet?logo=huggingface&logoColor=white">
  </a>
</p>
</div>

## ✨ 概要
このリポジトリは **最小構成** で Gradio アプリを立ち上げ、同時に **MCP (Model Context Protocol) サーバー** として機能させるサンプルです。  
たった 1 つのファイルを実行するだけで、Web UI と MCP SSE エンドポイントの両方が手に入ります。

## 📄 ファイル構成
| ファイル / ディレクトリ | 役割 |
|------------------------|------|
| `app.py`               | Gradio UI + MCP サーバー（`letter_counter` ツール） |
| `requirements.txt`     | 依存パッケージ（`gradio[mcp]` のみ） |
| `assets/header.svg`    | README 用ヘッダー画像（任意） |

## 📦 セットアップ

### 🚀 uv を使ったクイックスタート（推奨）

```bash
# 仮想環境の作成
uv venv
# 仮想環境の有効化
source .venv/bin/activate
# 依存インストール
uv pip install -r requirements.txt
```

### 🐍 標準 pip のみで実行したい場合

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 実行
以下のコマンドを実行でローカルサーバーが起動します。
```bash
python app.py
```

- Web UI: <http://127.0.0.1:7860>  
- MCP SSE エンドポイント: <http://127.0.0.1:7860/gradio_api/mcp/sse>  
  - UI フッター → **View API** → **MCP** をクリックすると、コピペ可能な設定 JSON が表示されます。

## ⚙️ MCP クライアント設定例
Claude Desktop / Cline などで `claude_desktop_config.json` 等に追記:
```jsonc
{
  "mcpServers": {
    "gradio-local": {
      "url": "http://127.0.0.1:7860/gradio_api/mcp/sse"
    }
  }
}
```
クライアントを再起動すると `letter_counter` ツールが利用できるようになります 🎉

## 🔧 仕組み
```python
demo.launch(mcp_server=True)
```
この 1 行で Gradio アプリが SSE ベースの MCP サーバーとして動作します。  
ドキュストリングと型ヒントから自動でスキーマが生成されます。

## 🌠 拡張方法
1. `app.py` に関数を追加し、適切なドキュストリングを記述  
2. `Interface(...)` へ登録（または Blocks を使用）  
3. 再起動すれば新しい MCP ツールとして自動公開

## 🛫 🤗 Spaces へ無料デプロイ
ファイル一式を Hugging Face Spaces (Gradio テンプレート) へプッシュすると、無料の公開 MCP サーバーになります:
```
https://<your-space>.hf.space/gradio_api/mcp/sse
```
例）`https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse`

## 🔗 MCP クライアント設定例 (Spaces)

Spaces で公開したサーバーを **MCP クライアント（Claude Desktop / Cline など）** から呼び出す手順です。

1. **エンドポイント URL**
   ```
   https://<your-space>.hf.space/gradio_api/mcp/sse
   ```
   例）`https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse`

2. **config 追記例** (`claude_desktop_config.json` 等)
   ```jsonc
   {
     "mcpServers": {
       "gradio-space": {                // 任意の名前
         "url": "https://makiai-gradio-mcp-minimal.hf.space/gradio_api/mcp/sse"
       }
     }
   }
   ```

3. **動作確認**
   クライアントを再起動 → Tool Palette で `server = gradio-space` を選択 →
   `letter_counter` ツールに `text: "hello"` を送信し、`length: 5` が返れば接続完了です 🎉

## 📝 ライセンス
MIT
