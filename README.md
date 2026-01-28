​⚠️ Ethical & Defensive Use Disclaimer
​This tool is developed strictly for authorized defensive auditing and educational research within controlled lab environments. It is intended to help system administrators identify weak authentication patterns and test the efficacy of security controls like Fail2Ban. Unauthorized use against systems you do not own is illegal and unethical.

# Automated SSH Authentication Auditor (Termux/ARM64)

## Project Overview
This project is a modular Python-based toolkit designed to simulate and audit SSH authentication security within a sandboxed Linux environment (Termux). It consists of a targeted intelligence generator and an automated brute-force engine.

## Technical Accomplishments
* **Modular Architecture:** Developed a two-stage attack lifecycle separating reconnaissance (wordlist generation) from delivery (authentication testing).
* **Environment-Specific Optimization:** Configured the tool to handle non-standard port redirection (Port 8022) common in mobile-based Linux environments.
* **Cryptographic Implementation:** Successfully compiled and utilized `Paramiko`, `PyNaCl`, and `bcrypt` libraries for secure protocol handling on an ARM64 architecture.

## How It Works
1. **gen_wordlist.py:** Generates a targeted dictionary using iterative permutations of organizational keywords, years, and special characters.
2. **red_tool.py:** Leverages the generated wordlist to perform an automated audit against a local-loopback (127.0.0.1) SSH daemon.

## Ethical Testing Notice
This tool was developed strictly for educational and authorized auditing purposes. All testing was conducted against self-owned, local-loopback services.
