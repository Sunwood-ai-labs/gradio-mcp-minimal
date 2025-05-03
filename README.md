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

<!-- ここに SVG ヘッダーを追加する場合は assets/header.svg を用意してください -->
<!-- <img src="assets/header.svg" alt="Gradio MCP Minimal" width="80%" /> -->

# 🚀 **Gradio MCP 最小デモリポジトリ**

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
以下のコマンドを利用して実行ください。
  ```
  root 🐈 Glen in 🧶 …/gradio-mcp-minimal on 🐾 main [🗑️❓] 🐍 v3.12.3  
  😺 uv venv
  Using CPython 3.12.3 interpreter at: /usr/bin/python3
  Creating virtual environment at: .venv
  Activate with: source .venv/bin/activate
  
  root 🐈 Glen in 🧶 …/gradio-mcp-minimal on 🐾 main [🗑️📝❓] 🐍 v3.12.3  
  😺 source .venv/bin/activate
  
  root 🐈 Glen in 🧶 …/gradio-mcp-minimal on 🐾 main [🗑️📝❓] 🐍 v3.12.3 gradio-mcp-minimal 
  😺 uv pip install -r requirements.txt 
  ```
  
マニュアルに実行したい場合には下記のコマンドで実行ください。
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
