# Copyright (c) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# MindIE is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

import re
import urllib.parse

IMG_MD_PATTERN = re.compile(
    r"!\[(.*?)\]\((.*?)\)",
    re.MULTILINE,
)

SAFE_CHARS = "/:#?=&%"


def on_page_markdown(markdown, **kwargs):
    def encode_url(match):
        alt = match.group(1)
        url = match.group(2)

        # Skip external URLs and already-encoded URLs
        if url.startswith("http") or "%" in url:
            return match.group(0)

        encoded = urllib.parse.quote(url, safe=SAFE_CHARS)
        return f"![{alt}]({encoded})"

    return IMG_MD_PATTERN.sub(encode_url, markdown)
