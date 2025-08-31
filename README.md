## 使い方
1. このテンプレートリポジトリから新規リポジトリを作成
2. 下の書き換える設定一覧に従って変更
3. streamlitのエントリポイントとしてapp.pyを作成する。
4. actionsから手動実行するかmainへpushをすることで自動でデプロイが走ります。デプロイ先URLはgithubのabout欄に出力されます。

## 書き換える設定

### marubeni-streamlitにデプロイする場合
#### 変数名説明 <br>
**TokenはSecretsに置いてください**
```
YOUR_ARTIFACT_REPOSITORY_NAME: 作られるArtifact Repositoryのリポジトリ名になります。
YOUR_CLOUD_RUN_SERVICE_NAME: 作られるCloud Runのサービス名になります。
GITHUB_ACESS_TOKEN: GitHub ActionsがAboutにデプロイ先URLを書き込むために使うトークン。必要なのはAdministrationへのRead/Writeです。
```

#### 1. cloudbuild.yaml
``` yaml
serviceAccount: projects/marubeni-streamlit/serviceAccounts/cb-deployer@marubeni-streamlit.iam.gserviceaccount.com

substitutions: 
  _REGION: asia-northeast1
  _REPO: YOUR_ARTIFACT_REPOSITORY_NAME
  _SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
```

#### 2. GitHub Variables
``` yaml
CLOUD_RUN_SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
DEPLOY_SA: cb-deployer@marubeni-streamlit.iam.gserviceaccount.com
PROJECT_ID: marubeni-streamlit
PROJECT_NUMBER: 464938819289
REGION: asia-northeast1
WIF_PROVIDER: projects/464938819289/locations/global/workloadIdentityPools/github-pool/providers/github-provider
```

#### 3. GitHub Secrets
``` yaml
GH_ADMIN_TOKEN: GITHUB_ACESS_TOKEN (used to update url in "About")
```



### それ以外のGCPプロジェクトにデプロイする場合
#### 前提
サービスアカウントに対する権限付与やWIFの設定等を、streamlitと同様に事前に行う必要があります。

#### GCPプロジェクト単位
#### 1. cloudbuild.yaml
``` yaml
serviceAccount: projects/YOUR_PROJECT_ID/serviceAccounts/cb-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com

substitutions: 
  _REGION: YOUR_REGION

```


#### GitHub Repository単位
#### 1. cloudbuild.yaml
``` yaml
substitutions: 
  _REPO: YOUR_ARTIFACT_REPOSITORY_NAME
  _SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
```

#### 2. GitHub Variables
``` yaml
CLOUD_RUN_SERVICE: YOUR_CLOUD_RUN_SERVICE_NAME
DEPLOY_SA: cb-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com
PROJECT_ID: YOUR_PROJECT_ID
PROJECT_NUMBER: YOUR_PROJECT_NUMBER
REGION: YOUR_REGION
WIF_PROVIDER: projects/YOUR_PROJECT_NUMBER/locations/global/workloadIdentityPools/github-pool/providers/github-provider
```
#### 3. GitHub Secrets
``` yaml
GH_ADMIN_TOKEN: YOUR_GITHUB_ACESS_TOKEN (used to update url in "About")
```

