# lumin/setup-pesde

[![version](https://img.shields.io/github/v/release/lumin-org/setup-pesde?style=plastic&logo=github&logoColor=FFFFFF&label=version)](https://github.com/lumin-org/setup-pesde/releases/latest)
[![test](https://img.shields.io/github/actions/workflow/status/lumin-org/setup-pesde/test.yml?style=plastic&logo=github&logoColor=FFFFFF&label=test)](https://github.com/lumin-org/setup-pesde/blob/main/.github/workflows/test.yml)
[![discord](https://img.shields.io/discord/1105688855375511642?logo=discord&logoColor=white&label=chat&color=4d3dff&style=plastic)](https://lumin-org.github.io/to/discord)

A github action that installs the Pesde CLI along with Lune 

## Prerequisites

In order to use **lumin/setup-pesde** you must be using one of the following server types:

* [`macOS`](https://en.wikipedia.org/wiki/macOS)
* [`Linux`](https://en.wikipedia.org/wiki/Linux)
* [`Windows`](https://en.wikipedia.org/wiki/Windows)
  
## Usage

Use the latest version of Pesde, with default parameters

```yaml
steps:
- uses: lumin-org/setup-pesde@v0.4.1
```

## Inputs

### `version`

The version of Pesde to install.\
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

This project was forked from [`ok-nick/setup-aftman`](https://github.com/ok-nick/setup-aftman)

## License

This project is licensed under the [MIT](https://github.com/lumin-org/setup-pesde/blob/main/LICENSE) license
