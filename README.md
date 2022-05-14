# BlogOps

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-BlogOps-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=)](https://github.com/andregri/BlogOps)
[![Actions Status](https://github.com/andregri/BlogOps/workflows/Continuous%20Integration/badge.svg)](https://github.com/andregri/BlogOps/actions)

This action uploads your Github Pages posts to other blog platforms (Medium, etc.)

## Usage

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Run action
      uses: andregri/BlogOps@master
      with:
        posts_dir: 'path/to/posts/'
        repo_name: "BlogOps"
        gh_access_token: ${{ secrets.GH_ACCESS_TOKEN }}
        medium_integration_token: ${{ secrets.MEDIUM_INTEGRATION_TOKEN }}
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `posts_dir` | The path of the folder containing the posts (_default_ is `./_posts/`) |
| `repo_name` | The name of the GitHub Pages repository |
| `gh_access_token` | Github token to read repository files |
| `medium_integration_token` | Token to use Medium API |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `myOutput` | String of posts published correctly and with errors |

## Resources

- For info on how to build your first Container action, see the [toolkit docs folder](https://github.com/actions/toolkit/blob/master/docs/container-action.md).
