#!/usr/bin/env python
# coding=utf-8
# Copyright (c) Huawei Technologies Co., Ltd. 2024-2026. All rights reserved.
"""MkDocs hooks for copying external files referenced by Chinese docs."""

import os
import re
import shutil
import logging

logger = logging.getLogger("mkdocs.plugins.mkdocs_hooks")

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
DOCS_ZH_DIR = os.path.join(PROJECT_ROOT, "docs", "zh")

EXTERNAL_FILES = [
    ("examples/wan/parameter_config.md", "examples/wan/parameter_config.md"),
    ("examples/service", "examples/service"),
    ("examples/cache", "examples/cache"),
    ("mindiesd/compilation/mindie_sd_backend.py", "mindiesd/compilation/mindie_sd_backend.py"),
    ("OWNERS", "OWNERS"),
    ("CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.md"),
    ("docs/tech_report/RainFusion2.0.pdf", "tech_report/RainFusion2.0.pdf"),
]

LINK_FIXES = [
    ("../../examples/wan/parameter_config.md", "examples/wan/parameter_config.md"),
    ("../../examples/service", "examples/service"),
    ("../../examples/cache", "examples/cache"),
    ("../../../examples/cache/cache.py", "../../examples/cache/cache.py"),
    ("../../../OWNERS", "../OWNERS"),
    ("../../../CODE_OF_CONDUCT.md", "../CODE_OF_CONDUCT.md"),
    ("../../tech_report/RainFusion2.0.pdf", "../tech_report/RainFusion2.0.pdf"),
    ("../../../mindiesd/compilation/mindie_sd_backend.py", "../../mindiesd/compilation/mindie_sd_backend.py"),
]


def _copy_external_files():
    for src_rel, dst_rel in EXTERNAL_FILES:
        src = os.path.join(PROJECT_ROOT, src_rel)
        dst = os.path.join(DOCS_ZH_DIR, dst_rel)

        if not os.path.exists(src):
            logger.warning(f"Source does not exist, skipping: {src}")
            continue

        dst_parent = os.path.dirname(dst)
        os.makedirs(dst_parent, exist_ok=True)

        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            logger.info(f"Copied directory: {src_rel} -> {dst_rel}")
        else:
            shutil.copy2(src, dst)
            logger.info(f"Copied file: {src_rel} -> {dst_rel}")


def _strip_toctree_blocks(markdown):
    """Remove Sphinx/MyST toctree blocks so they don't render as code in MkDocs."""
    return re.sub(r"^```\s*\{toctree\}\n[\s\S]*?^```\n?", "", markdown, flags=re.MULTILINE)


def on_page_markdown(markdown, page, config, files, **kwargs):
    if page.file.src_path == "index.md":
        original = markdown
        markdown = _strip_toctree_blocks(markdown)
        if markdown != original:
            logger.info("Stripped toctree blocks from index.md")

    original = markdown
    for old_link, new_link in LINK_FIXES:
        markdown = markdown.replace(old_link, new_link)
    if markdown != original:
        logger.info(f"Fixed external links in: {page.file.src_path}")

    return markdown


def on_config(config, **kwargs):
    logger.info("Running config hook: copying external files...")
    _copy_external_files()
    logger.info("Config hook completed.")