# sgsharma.github.io

Personal portfolio site built with [Hugo](https://gohugo.io/) using the [eternity-alt](./eternity-alt/) theme, hosted on GitHub Pages at [themightycomma.com](https://themightycomma.com).

## Local development

**Prerequisites:** Hugo extended v0.144+ ([install](https://gohugo.io/installation/))

```bash
# Start dev server with live reload
hugo serve -p 1313

# Build site to ./public
hugo --minify

# Build for production with explicit base URL
hugo --gc --minify --baseURL "https://themightycomma.com/"

# Create a new work post
hugo new work/2026/my-post-title.md
```

Site runs at http://localhost:1313 during local development.

## Content structure

```
content/
  work/          # Portfolio pieces, organized by year
    2026/
      *.md
  about.md
  404.md
```

Each work post lives under `content/work/<year>/<slug>.md`. Images go in `assets/images/<year>/`.

## Deployment

### Automatic (GitHub Actions)

Pushing to `master` triggers `.github/workflows/hugo.yaml`, which:
1. Installs Hugo extended
2. Checks out the repo (with submodules)
3. Builds the site with `hugo --gc --minify`
4. Uploads the `./public` artifact
5. Deploys to GitHub Pages

No manual steps needed — merge to `master` = live site.

### Manual (deploy script)

```bash
./deploy.sh
```

Requires a clean working directory. Builds the site and pushes the output to the `gh-pages` branch directly.

## Config

[`config.yaml`](./config.yaml) — key settings:

| Key | Purpose |
|-----|---------|
| `baseURL` | Production URL |
| `theme` | Theme name (`eternity-alt`) |
| `themesDir` | Set to `"."` so Hugo resolves the theme from the repo root |
| `params.homepage` | Landing redirect target (currently `/work`) |
| `params.bypassWelcomePage` | Skips splash page when `true` |
| `permalinks.work` | URL pattern for work posts (`:contentbasename/`) |
