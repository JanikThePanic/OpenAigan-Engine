# OpenAigan Engine

run using `pipenv run python src/__main__.pyw`
i also run `rm -rf user/` before that during dev

go to vscode keyboard shortcuts json and just add this
runs the above with `shift+enter` and makes dev life easy

```json
[
	{
		"key": "shift+enter",
		"command": "workbench.action.terminal.sendSequence",
		"args": {
			"text": "rm -rf user/\u000Dpipenv run python src/__main__.pyw\u000D"
		}
	}
]
```

i say this again, alot of this is spgti code and a wip
