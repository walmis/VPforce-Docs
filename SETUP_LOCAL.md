# Setting Up the Documentation Locally with Autoreloading

This guide will help you set up the VPforce Rhino Manual documentation site locally with automatic reloading whenever you make changes to the documentation files.

## Prerequisites

- **Python 3.7+** installed on your system
- **pip** (Python package manager)

## 1. Clone the Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone <repository-url>
cd vpforce-rhino-manual
```

## 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install MkDocs directly:

```bash
pip install mkdocs
```

## 4. Serve the Documentation with Autoreloading

From the `vpforce-rhino-manual` directory (where `mkdocs.yml` is located), run:

```bash
mkdocs serve --autoreload
```

This will start a local development server (usually at http://127.0.0.1:8000/). The server will automatically reload whenever you edit and save Markdown files or configuration.

## 5. Open in Your Browser

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to view the documentation. Any changes you make to the docs will be reflected automatically after saving.

## Troubleshooting

- If you get a `command not found: mkdocs` error, ensure your virtual environment is activated and MkDocs is installed.
- If you change the `mkdocs.yml` file, the server will also reload automatically.

---

For more information, see the [MkDocs documentation](https://www.mkdocs.org/).
