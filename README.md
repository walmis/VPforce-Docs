# VPforce Rhino Manual

[![Build and Deploy Documentation](https://github.com/walmis/VPforce-Docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/walmis/VPforce-Docs/actions/workflows/deploy.yml)

Complete documentation for the **VPforce Rhino FFB stick base** - a high-performance force feedback controller for flight simulation.

## 📖 About This Documentation

This documentation provides comprehensive guides for:

- Getting started with your Rhino
- Setup and configuration
- Using the VPforce TelemetryFFB application
- Game-specific force feedback settings
- Troubleshooting and maintenance
- Product information and spare parts

**Live Documentation:** [Visit the documentation site](https://docs.vpforce.eu) (when deployed)

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing typos, improving explanations, adding new sections, or creating additional resources—your help makes this documentation better for everyone.

### Ways to Contribute

- **Fix typos or grammar** - Found a mistake? Submit a quick fix
- **Improve clarity** - Reword confusing sections
- **Add examples** - Share configuration examples or setup tips
- **Report issues** - Found outdated or incorrect information? Open an issue
- **Create new sections** - Have knowledge to share? Propose new documentation

### Contributing Guidelines

1. **Fork and clone** the repository
2. Create a feature branch: `git checkout -b improve/your-improvement`
3. Make your changes
4. Test locally (see [Local Setup](#-local-setup) below)
5. Commit with clear messages: `git commit -m "Add: improved X section"`
6. Push to your fork and open a **Pull Request**

**Please follow the [style guide](.github/copilot-instructions.md)** for consistency:
- Use clear, concise language
- Keep sentences short and direct
- Use active voice
- Maintain consistent terminology
- Provide working code examples

## 🚀 Local Setup

### Prerequisites

- **Python 3.7+**
- **pip** (Python package manager)
- **Git**

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/walmis/VPforce-Docs.git
   cd VPforce-Docs
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**
   ```bash
   mkdocs serve
   ```

5. **Open in your browser**
   - Navigate to `http://localhost:8000`
   - Changes to documentation files will auto-reload in your browser

### Project Structure

```
vpforce-rhino-manual/
├── docs/                      # Documentation source files
│   ├── index.md              # Homepage
│   ├── rhino/                # Rhino manual sections
│   │   ├── index.md
│   │   ├── 2-getting-started.md
│   │   ├── 3-using-the-rhino.md
│   │   ├── 4-the-vpforce-telemffb-application.md
│   │   ├── 5-game-specific-ffb-settings-tips-and-tricks.md
│   │   ├── 6-troubleshooting-maintenance.md
│   │   ├── 7-appendix-a-known-issues.md
│   │   └── 8-appendix-b-legacy-telemffb-documentation.md
│   ├── images/               # Image assets
│   ├── media/                # Media assets
│   └── stylesheets/          # Custom CSS
├── mkdocs.yml                # MkDocs configuration
├── requirements.txt          # Python dependencies
├── SETUP_LOCAL.md           # Detailed setup instructions
└── .github/workflows/       # GitHub Actions CI/CD
```

## 📝 Editing Documentation

Documentation is written in **Markdown**. Each page corresponds to a `.md` file in the `docs/` directory.

### Adding a New Page

1. Create a new `.md` file in the appropriate `docs/` subdirectory
2. Add content using Markdown syntax
3. Update `mkdocs.yml` navigation if needed
4. Run `mkdocs serve` to preview

### Markdown Features Supported

- Headings, lists, and tables
- Code blocks with syntax highlighting
- Admonitions (notes, warnings, etc.)
- Footnotes and abbreviations
- Task lists
- Keyboard key notation
- Strikethrough and emphasis

See the [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/) for more details.

## 🔨 Building for Production

To build the static site for deployment:

```bash
mkdocs build
```

This generates the complete static website in the `site/` directory, ready for deployment.

## 🚀 Deployment

This project uses **GitHub Actions** for automated building and deployment. On every push to the `main` branch:

1. Documentation is built using MkDocs
2. The built site is deployed to the server via SSH

See `.github/workflows/deploy.yml` for the deployment configuration.

## 📜 License

This documentation is licensed under the **Creative Commons Attribution 4.0 International License** (CC-BY-4.0).

You are free to:
- ✅ Share, copy, and redistribute the documentation
- ✅ Adapt, remix, transform, and build upon the material
- ✅ Use it for any purpose, including commercial use

**Under the condition that:**
- 📝 You give appropriate credit to the VPforce project and contributors
- 🔗 Provide a link to the license
- 📌 Indicate if changes were made

For full terms, see the [LICENCE](LICENCE) file.

## 🙋 Questions or Issues?

- **Found a bug?** Open an [Issue](https://github.com/walmis/VPforce-Docs/issues)
- **Have a suggestion?** Start a [Discussion](https://github.com/walmis/VPforce-Docs/discussions)
- **Want to help?** See the [Contributing](#-contributing) section

---

**Thank you for helping improve the VPforce Rhino documentation!** 🚀
