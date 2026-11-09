# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-11-09

### Added

* Branded CLI interface with a centered ASCII-art banner.
* Project description and clickable version link in CLI output.
* Rich-formatted panel for displaying the current desktop background path.
* Clickable filesystem path in the background command output.
* Formatted error reporting for background retrieval failures.
* Ruff linting and formatting configuration.
* ty static type checking configuration.
* Optional development dependency group (`dev`).

### Changed

* Replaced Setuptools with Hatchling as the package build backend.
* Migrated to dynamic package versioning using `src/getwinbg/__version__.py`.
* Centralized version management across the package, CLI, and documentation.
* Replaced plain-text CLI output with Rich terminal formatting.
* Improved project metadata, classifiers, and package configuration.
* Updated project URLs with documentation and changelog references.
* Updated Sphinx configuration to retrieve the package version dynamically.
* Updated documentation requirements to include the installable `getwinbg` package.
* Updated README examples to reflect the redesigned CLI interface.

### Removed

* Removed the previous `version.py` module.
* Removed obsolete Setuptools-specific configuration.

### Fixed

* Improved CLI failure handling by displaying descriptive error messages and returning a non-zero exit status when background retrieval fails.

## [0.1.0] - 2026-06-20

### Added

* Initial public release of `getwinbg`
* Current Windows desktop background retrieval
* Python API via `get_background()`
* Command-line interface via `getwinbg background`
* Typed package support (`py.typed`)
* Project packaging with `pyproject.toml`
* Trusted Publishing workflow for PyPI releases
* Project documentation and usage examples
* Windows desktop background retrieval using `SystemParametersInfoW`
* Background path normalization and validation
* Initial project architecture for future wallpaper providers
* Repository configuration files (`.editorconfig`, `.gitignore`)

[unreleased]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/compare/v0.1.1...HEAD

[0.1.1]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.1
[0.1.0]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.0
