# ssqvid/setup-pesde

[![test](https://img.shields.io/github/actions/workflow/status/ssqvid/setup-pesde/test.yml?style=plastic&logo=github&logoColor=FFFFFF&label=test)](https://github.com/ssqvid/setup-pesde/blob/main/.github/workflows/test.yml)

A github action that installs the Pesde CLI along with Lune 

## Prerequisites

In order to use **ssqvid/setup-pesde** you must be using one of the following server types:

* [`macOS`](https://en.wikipedia.org/wiki/macOS)
* [`Linux`](https://en.wikipedia.org/wiki/Linux)
* [`Windows`](https://en.wikipedia.org/wiki/Windows)
  
## Usage

Use the latest version of Pesde, with default parameters

```yaml
steps:
- uses: ssqvid/setup-pesde@VERSION
```

## Inputs

### `version`

The version of Pesde to install. Semantic Version can be used on top of options, but pesde.toml engines field should be used over this.\
**Default:** `latest`\
**Options:**
* **'latest':** Latest release of Pesde.
* **'build':** Builds Pesde from source.

### `path`
The path of where the Pesde config file is located.\
**Default:** `.`

### `cache`
Whether or not to cache the Pesde install and packages.\
**Default:** `false`

### `token`
The security token used for publishing to the Pesde marketplace.

## Forks

This project was forked from [`axiom-co/setup-pesde`](https://github.com/axiom-co/setup-pesde)

## License

This project is licensed under the [MIT](https://github.com/ssqvid/setup-pesde/blob/main/LICENSE) license
