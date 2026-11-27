# Command-line interface

The `getwinbg` command displays a banner when run without a subcommand. Use
`getwinbg --help` to see the command help.

## Display the current background

```console
$ getwinbg background
```

The command prints the validated path to the current desktop background.

## Copy the background path

```console
$ getwinbg background --copy
```

Use `-c` as the short option. This copies the path as text to the Windows
clipboard; it does not copy the image file.

## Reveal the background

```console
$ getwinbg background --reveal
```

Use `-r` as the short option. This asks File Explorer to select the file.

## Open the background

```console
$ getwinbg background --open
```

Use `-o` as the short option. This opens the file with its default
application.

The options can be combined:

```console
$ getwinbg background --reveal --open --copy
```

The command displays the path first, then performs each requested operation.

## Version

```console
$ getwinbg --version
getwinbg 0.1.3
```

## Errors and exit status

When the background cannot be retrieved or an optional file operation fails,
the CLI displays a formatted error and exits with status `1`. A clipboard
failure is reported the same way.
