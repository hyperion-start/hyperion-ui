## [UNRELEASED] - (1.0.1)

### Fixed
- Instead of looking for `latest.log` in the component log directory the ui clients now pick the file with the most
recent file change.
- Restricted urwid version to 2.0.1 since 2.1.0 crashes because of some list widget error. See the relevant [issue](https://github.com/urwid/urwid/issues/386) on github.

### Added
- Ability to display real information in the hosts stat columns.
- In interactive cli logs are opened in an extra terminal, in case a display is
  available. The log is displayed as text widget otherwise.

## [1.0.0] - 17.06.2019

### Changed
- Moved user interfaces to external library
