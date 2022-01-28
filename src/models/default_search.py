from src.models.search import Search
from src.models.search_text_option import SearchTextOption
from src.models.search_slider_option import SearchSliderOption
from src.models.search_toggle_option import SearchToggleOption
from src.models.search_select_option import SearchSelectOption


# 譜面以外のエンドポイント
defaultSearch = Search(
    options=[
        # KEYWORDS
        SearchTextOption(
            query="keywords",
            name="text",
            type="text",
            placeholder="Search text",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="text",
            type="text",
            placeholder="AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="sort",
            type="select",
            default=0,
            values=["updatedTime", "createdTime"],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # STATUS
        SearchSelectOption(
            query="status",
            name="status",
            type="select",
            default=0,
            values=["any", "testing"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="random",
            type="toggle",
            default=False,
        ),
    ]
)

# 譜面のエンドポイント
levelSearch = Search(
    options=[
        # KEYWORDS
        SearchTextOption(
            query="keywords",
            name="text",
            type="text",
            placeholder="Search text",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="text",
            type="text",
            placeholder="AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="sort",
            type="select",
            default=0,
            values=["updatedTime", "createdTime"],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # RATING_MIN
        SearchSliderOption(
            query="rating_min",
            name="rating_min",
            type="slider",
            default=1,
            min=1,
            max=50,
            step=1,
            display="number",
        ),
        # RATING_MAX
        SearchSliderOption(
            query="rating_max",
            name="rating_max",
            type="slider",
            default=50,
            min=1,
            max=50,
            step=1,
            display="number",
        ),
        # GENRE
        SearchSelectOption(
            query="genre",
            name="genre",
            type="select",
            default=0,
            values=["any", "vocaloid", "jpop", "anime", "general"],
        ),
        # STATUS
        SearchSelectOption(
            query="status",
            name="status",
            type="select",
            default=0,
            values=["any", "testing", "played", "unplayed", "liked", "mylisted"],
        ),
        # LENGTH
        SearchSelectOption(
            query="length",
            name="length",
            type="select",
            default=0,
            values=["any", "short", "long", "very_short", "very_long"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="random",
            type="toggle",
            default=False,
        ),
    ]
)
