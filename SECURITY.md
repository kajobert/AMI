# Security Policy

AMI is being built in public, but public does not mean unrestricted trust.

## Never commit

- API keys, passwords, tokens or private keys;
- raw personal chats/exports or sensitive archaeology evidence;
- production OpenClaw configuration containing secrets;
- private infrastructure credentials or unrestricted remote-execution paths.

## AI and external input

Pull requests, issues, comments, model output and community suggestions are untrusted input until validated. AI-generated code follows the same review and CI requirements as human-generated code.

Public GitHub workflows must not expose production credentials or execute untrusted PR code with secrets.

## Reporting

Do not publish live secrets or exploitable private infrastructure details in a public issue. Use GitHub's private vulnerability/security reporting facilities when enabled, or contact repository maintainers privately.

## Privilege principle

Grant the minimum capability required for a task. Self-improvement follows:

`observe -> propose -> isolated test -> review/approval -> apply -> verify -> rollback`

No public event should implicitly gain production shell/root authority.
