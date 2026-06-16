# Security Policy

We take the security of Mocky seriously. Thank you for helping keep Mocky and its users safe.

## Supported versions

Security fixes are applied to the latest released version on the `master` branch. Please make sure you are on the latest version before reporting.

| Version | Supported |
| ------- | --------- |
| latest  | ✅        |
| older   | ❌        |

## Reporting a vulnerability

**Please do not open a public issue for security vulnerabilities.**

Instead, report privately using one of these channels:

1. **GitHub private advisory** (preferred): open a draft advisory at
   `https://github.com/raman0c17/mocky/security/advisories/new`.
2. **Email**: contact the maintainers privately and include the details below.

Please include:

- A description of the vulnerability and its potential impact
- Steps to reproduce (proof of concept if possible)
- Affected version(s) and environment (OS, architecture, Python version)
- Any suggested remediation

## What to expect

- We aim to **acknowledge** your report within **3 business days**.
- We will work with you to understand and validate the issue.
- We will keep you informed of remediation progress and coordinate a disclosure timeline.
- We are happy to credit you in the release notes once a fix ships, unless you prefer to remain anonymous.

## Scope & safe harbor

Mocky downloads images referenced in user-provided Markdown. Be mindful that converting untrusted Markdown will fetch remote URLs. We welcome reports about unsafe handling of inputs, paths, or network requests.

We consider security research conducted in good faith — including testing against your own copy of Mocky — to be authorized. We will not pursue legal action for such research as long as you respect user privacy and avoid service disruption.
