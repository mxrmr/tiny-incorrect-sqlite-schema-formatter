# Tiny, Incorrect SQLite Schema Formatter

You probably shouldn’t use this script. It doesn’t tokenize SQL
properly. It doesn’t format SQL properly. But if you don’t get too fancy
with your syntax, it might be helpful.

## Options

- `--spaces`: Set the number of spaces to use for indentation. If
	omitted, tabs are used for indentation.

- `--in-place`, `-i`: Edit the files in place. If omitted, the formatted
	version of each file is printed to stdout.
