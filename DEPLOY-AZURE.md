# Deploying साङ्ख्य सत्संग to your Azure subscription

Two good options. **Option A (Storage static website)** is the simplest and cheapest
(typically a few rupees/month). **Option B (Azure Static Web Apps)** gives you a free
SSL custom domain and CI/CD from a Git repo (you already use Azure Repos, so B fits
nicely too).

---

## Option A — Azure Storage static website (5 minutes, az CLI)

```bash
# 1. Log in and pick your subscription
az login
az account set --subscription "<your-subscription-name-or-id>"

# 2. Create a resource group (Central India is closest to Bengaluru)
az group create --name rg-satsang --location centralindia

# 3. Create a storage account (name must be globally unique, lowercase, 3-24 chars)
az storage account create \
  --name sankhyasatsang2006 \
  --resource-group rg-satsang \
  --location centralindia \
  --sku Standard_LRS \
  --kind StorageV2

# 4. Enable the static website feature
az storage blob service-properties update \
  --account-name sankhyasatsang2006 \
  --static-website \
  --index-document index.html \
  --404-document index.html

# 5. Upload the site (run from the folder containing index.html)
az storage blob upload-batch \
  --account-name sankhyasatsang2006 \
  --destination '$web' \
  --source . \
  --overwrite

# 6. Get your live URL
az storage account show \
  --name sankhyasatsang2006 \
  --resource-group rg-satsang \
  --query "primaryEndpoints.web" -o tsv
```

The URL will look like:
`https://sankhyasatsang2006.z29.web.core.windows.net/`

**Re-deploying after edits:** just re-run step 5.

**Custom domain (optional):** add a CNAME at your DNS provider pointing to the
web endpoint, then `az storage account update --custom-domain <yourdomain>`.
For HTTPS on a custom domain with Storage, front it with Azure CDN / Front Door.

---

## Option B — Azure Static Web Apps (free tier, Git-based)

1. Push this folder to a repo (GitHub or Azure DevOps — you already use Azure Repos):
   ```bash
   git init && git add . && git commit -m "Sankhya satsang site"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
2. In the Azure Portal: **Create resource → Static Web App**
   - Plan: **Free**
   - Region: Central India (or East Asia)
   - Source: your repo, branch `main`
   - Build presets: **Custom**
   - App location: `/`   ·   Api location: *(empty)*   ·   Output location: `/`
3. Azure creates a GitHub Action / DevOps pipeline; every push redeploys automatically.
4. Free SSL + custom domain under **Static Web App → Custom domains**.

---

## Adding the satsang media later

- Small clips/audio: drop into `media/` with the filenames in `media/README.txt`
  and re-upload (Option A step 5) or `git push` (Option B).
- Full-length day videos (DVD rips can be 1–4 GB/day): don't bundle them with the
  site. Create a separate public container:
  ```bash
  az storage container create --account-name sankhyasatsang2006 \
    --name videos --public-access blob
  az storage blob upload --account-name sankhyasatsang2006 \
    --container-name videos --file day1-katha.mp4 --name day1-katha.mp4
  ```
  Then point the `<source src>` in each day page to
  `https://sankhyasatsang2006.blob.core.windows.net/videos/day1-katha.mp4`.
  (For smooth seeking/streaming of long videos, Azure Front Door or converting to
  multiple bitrates is worth considering later.)

---

## Regenerating the day pages

`build_days.py` holds all seven days' content as structured Python. Edit it
(e.g., to paste transcripts) and run `python3 build_days.py` to rebuild
`day1.html … day7.html` with consistent headers/footers.
