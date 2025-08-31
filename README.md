## 使い方
1. このテンプレートリポジトリから新規リポジトリを作成
2. 下の書き換える設定一覧に従って変更
3. streamlitのエントリーポイントとしてapp.pyを作成する。
4. actionsから手動実行するかmainへpushをすることで自動でデプロイが走ります。デプロイ先URLはgithubのabout欄に出力されます。

## 書き換える設定

#### 変数名説明 <br>
**TokenはSecretsに置いてください**
```
YOUR_ARTIFACT_REPOSITORY_NAME: 作られるArtifact Repositoryのリポジトリ名になります。
YOUR_CLOUD_RUN_SERVICE_NAME: 作られるCloud Runのサービス名になります。
GITHUB_ACESS_TOKEN: GitHub ActionsがAboutにデプロイ先URLを書き込むために使うトークン。必要なのはAdministrationへのRead/Writeです。
```

#### 1. cloudbuild.yaml
``` yaml
substitutions: 
  _REPO: YOUR_ARTIFACT_REPOSITORY_NAME
  _SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
```

#### 2. GitHub Variables
``` yaml
CLOUD_RUN_SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
```

#### 3. GitHub Secrets
``` yaml
GH_ADMIN_TOKEN: GITHUB_ACESS_TOKEN (used to update url in "About")
```


