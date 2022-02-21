import random
import time
from typing import Optional

import requests


class PlaceholdImageBuilder:
    ENDPOINT = "https://placehold.jp"

    def get_random_html_color(self) -> str:
        chars = "0123456789ABCDEF"
        return "".join(random.sample(chars, 6))

    def get_flip_color(self, color_str: str) -> str:
        orig_color = tuple(
            [int(color_str[i : i + 2], 16) for i in (0, 2, 4)]  # noqa: E203
        )
        flip_color = (255 - orig_color[0], 255 - orig_color[1], 255 - orig_color[2])
        color_code = "%02x%02x%02x" % flip_color
        return color_code

    def build_url(
        self,
        sizeX: int = 300,
        sizeY: int = 300,
        color_text: str = "ffffff",
        color_background: str = "000000",
        format: str = "png",
        text: Optional[str] = None,
    ) -> str:
        if format not in ["jpg", "png"]:
            raise Exception("format must be jpg or png")
        address = (
            f"{self.ENDPOINT}/{color_background}/{color_text}/{sizeX}x{sizeY}.{format}"
        )
        if text:
            address += f"?text={text}"
        return address

    def get_random_image_address(
        self,
        sizeX: int = 300,
        sizeY: int = 300,
        format: str = "png",
        text: Optional[str] = None,
    ) -> str:
        base_color = self.get_random_html_color()
        return self.build_url(
            sizeX,
            sizeY,
            base_color,
            self.get_flip_color(base_color),
            format,
            text,
        )


def main() -> None:
    import os
    import os.path

    builder = PlaceholdImageBuilder()
    folders = [
        "LevelCover",
        "LevelThumbnail",
        "BackgroundImage",
        "BackgroundThumbnail",
        "EngineThumbnail",
        "EffectThumbnail",
        "SkinThumbnail",
        "ParticleThumbnail",
    ]
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
        for i in range(1, 22):
            address = builder.get_random_image_address(text=folder)
            print(address)
            resp = requests.get(address)
            with open(f"{folder}/image{i}.png", "wb") as f:
                f.write(resp.content)
            time.sleep(1)


if __name__ == "__main__":
    main()
