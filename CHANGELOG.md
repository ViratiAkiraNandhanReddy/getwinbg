# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.4] - 2026-11-27

### Added

- Added the `--copy` (`-c`) option to copy the current desktop background path to the Windows clipboard.
- Added `Background.copy()` to the public Python API.
- Added clipboard integration using the native Windows `clip` command.

### Changed

- Extended `_BackgroundManager` with clipboard functionality.
- Updated the `background` command to support copying the background path alongside the existing reveal and open operations.
- Updated the README to document the new clipboard functionality and command option.

### Improved

- Improved the `background` command with an additional way to access and reuse the current desktop background path.
- Maintained support for combining `--copy` with the existing `--reveal` (`-r`) and `--open` (`-o`) options.

## [0.1.3] - 2026-11-23

### Added

- Added the `--open` (`-o`) option to open the current desktop background with its default application.
- Added `Background.open()` to the public Python API.
- Added `Background.reveal()` to the public Python API.
- Added dedicated CLI presentation components: `CommandCLI`, `ApplicationCLI`, and `BackgroundCLI`.
- Added API, CLI, and getting-started documentation pages.
- Added Sphinx autodoc support for documenting the public Python API.

### Changed

- Extended `_BackgroundManager` with dedicated methods for opening and revealing background files.
- Refactored the `background` command to delegate display and file operations to `BackgroundCLI`.
- Centralized CLI error presentation through the shared `CommandCLI` component.
- Updated the README with the new command options, Python API usage, requirements, and development instructions.
- Expanded the Sphinx documentation with a getting-started guide, API reference, and CLI reference.
- Updated the documentation index with navigation and quick-start instructions.

### Improved

- Improved background file operation error reporting with descriptive messages.
- Improved CLI organization by separating application-level and command-specific presentation logic.
- Preserved the existing `--reveal` (`-r`) option while supporting combined `--reveal` and `--open` operations.
- Improved documentation coverage for installation, usage, API methods, and CLI options.

### Deprecated

- Marked `get_background()` as deprecated, recommending `Background().path` instead.
- Scheduled removal of `get_background()` for version `0.2.0`.

## [0.1.2] - 2026-11-16

### Added

- Added optional File Explorer integration to reveal the current desktop background and select its file.
- Added a Ruff GitHub Actions workflow to automate linting and code quality checks on pushes and pull requests.
- Added manual workflow dispatch support for running Ruff checks on demand.
- Added workflow concurrency controls to cancel outdated Ruff runs.

### Changed

- Promoted preset functionality from the `utils` package to a dedicated `presets.py` module.
- Simplified clickable background path generation by using the resolved path directly.

### Improved

- Improved File Explorer integration with descriptive CLI feedback.
- Updated Ruff workflow path filters to run checks only when relevant Python files or configuration changes are made.

### Fixed

- Improved handling of desktop background reveal operations by providing descriptive error reporting and a non-zero exit status when an error occurs.

## [0.1.1] - 2026-11-09

### Added

- Branded CLI interface with a centered ASCII-art banner.
- Project description and clickable version link in CLI output.
- Rich-formatted panel for displaying the current desktop background path.
- Clickable filesystem path in the background command output.
- Formatted error reporting for background retrieval failures.
- Ruff linting and formatting configuration.
- ty static type checking configuration.
- Optional development dependency group (`dev`).

### Changed

- Replaced Setuptools with Hatchling as the package build backend.
- Migrated to dynamic package versioning using `src/getwinbg/__version__.py`.
- Centralized version management across the package, CLI, and documentation.
- Replaced plain-text CLI output with Rich terminal formatting.
- Improved project metadata, classifiers, and package configuration.
- Updated project URLs with documentation and changelog references.
- Updated Sphinx configuration to retrieve the package version dynamically.
- Updated documentation requirements to include the installable `getwinbg` package.
- Updated README examples to reflect the redesigned CLI interface.

### Removed

- Removed the previous `version.py` module.
- Removed obsolete Setuptools-specific configuration.

### Fixed

- Improved CLI failure handling by displaying descriptive error messages and returning a non-zero exit status when background retrieval fails.

## [0.1.0] - 2026-06-20

### Added

- Initial public release of `getwinbg`.
- Current Windows desktop background retrieval.
- Python API via `get_background()`.
- Command-line interface via `getwinbg background`.
- Typed package support (`py.typed`).
- Project packaging with `pyproject.toml`.
- Trusted Publishing workflow for PyPI releases.
- Project documentation and usage examples.
- Windows desktop background retrieval using `SystemParametersInfoW`.
- Background path normalization and validation.
- Initial project architecture for future wallpaper providers.
- Repository configuration files (`.editorconfig`, `.gitignore`).

[unreleased]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/compare/v0.1.4...HEAD

[0.1.4]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.4
[0.1.3]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.3
[0.1.2]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.2
[0.1.1]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.1
[0.1.0]: https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/tag/v0.1.0

