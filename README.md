# Streamlit Audio Recorder

🎤 シンプルな音声録音アプリケーションです。Streamlitを使用してWebブラウザから音声を録音し、ダウンロードすることができます。

## 機能

- 🎙️ ブラウザから音声録音
- 🔊 録音した音声の再生
- 💾 録音ファイルのダウンロード（WAV形式）
- 📅 タイムスタンプ付きファイル名

## インストール

### 1. リポジトリのクローン

```bash
git clone https://github.com/yukiyamada-who-loves-yoga/streamlit-audiorec.git
cd streamlit-audiorec
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

または個別にインストールする場合：

```bash
pip install streamlit st-audiorec
```

## 実行方法

```bash
streamlit run app.py
```

アプリケーションが起動したら、ブラウザで `http://localhost:8501` にアクセスしてください。

## 使用方法

1. **録音開始**: マイクボタンをクリックして録音を開始します
2. **録音停止**: 再度ボタンをクリックして録音を停止します
3. **再生**: 録音が完了すると、自動的に再生ボタンが表示されます
4. **ダウンロード**: 「ダウンロード」ボタンをクリックして録音ファイルを保存します

## ファイル構成

```
st-audiorec/
├── app.py              # メインアプリケーションファイル
├── requirements.txt    # 依存関係ファイル
└── README.md          # このファイル
```

## 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **st-audiorec**: 音声録音コンポーネント
- **Python**: プログラミング言語

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。 