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
            name="#KEYWORDS",
            type="text",
            placeholder="#KEYWORDS",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="#AUTHOR",
            type="text",
            placeholder="#AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="Sort",
            type="select",
            default=0,
            values=["updated_time", "created_time"],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="Order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="#RANDOM",
            type="toggle",
            default=False,
        ),
    ]
)

defaultUserSearch = Search(
    options=[
        # KEYWORDS
        SearchTextOption(
            query="keywords",
            name="#KEYWORDS",
            type="text",
            placeholder="#KEYWORDS",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="#AUTHOR",
            type="text",
            placeholder="#AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="Sort",
            type="select",
            default=0,
            values=["updated_time", "created_time"],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="Order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # STATUS
        SearchSelectOption(
            query="status",
            name="#CATEGORY",
            type="select",
            default=0,
            values=["any", "testing"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="#RANDOM",
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
            name="#KEYWORDS",
            type="text",
            placeholder="Search text",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="#AUTHOR",
            type="text",
            placeholder="AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="Sort",
            type="select",
            default=0,
            values=[
                "updated_time",
                "created_time",
                "bpm",
                "likes",
                "mylists",
                "notes",
                "rating",
            ],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="Order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # RATING_MIN
        SearchSliderOption(
            query="rating_min",
            name="#RATING_MINIMUM",
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
            name="#RATING_MAXIMUM",
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
            name="#GENRE",
            type="select",
            default=0,
            values=["any", "vocaloid", "jpop", "anime", "general"],
        ),
        # LENGTH
        SearchSelectOption(
            query="length",
            name="#LENGTH",
            type="select",
            default=0,
            values=["any", "short", "long", "very_short", "very_long"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="#RANDOM",
            type="toggle",
            default=False,
        ),
    ]
)

levelUserSearch = Search(
    options=[
        # KEYWORDS
        SearchTextOption(
            query="keywords",
            name="#KEYWORDS",
            type="text",
            placeholder="Search text",
        ),
        # AUTHOR
        SearchTextOption(
            query="author",
            name="#AUTHOR",
            type="text",
            placeholder="AUTHOR",
        ),
        # SORT
        SearchSelectOption(
            query="sort",
            name="Sort",
            type="select",
            default=0,
            values=[
                "updated_time",
                "created_time",
                "bpm",
                "likes",
                "notes",
                "mylists",
                "rating",
            ],
        ),
        # ORDER
        SearchSelectOption(
            query="order",
            name="Order",
            type="select",
            default=0,
            values=["desc", "asc"],
        ),
        # RATING_MIN
        SearchSliderOption(
            query="rating_min",
            name="#RATING_MINIMUM",
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
            name="#RATING_MAXIMUM",
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
            name="#GENRE",
            type="select",
            default=0,
            values=["any", "vocaloid", "jpop", "anime", "general"],
        ),
        # STATUS
        SearchSelectOption(
            query="status",
            name="#CATEGORY",
            type="select",
            default=0,
            values=["any", "testing", "played", "unplayed", "liked", "mylisted"],
        ),
        # LENGTH
        SearchSelectOption(
            query="length",
            name="#LENGTH",
            type="select",
            default=0,
            values=["any", "short", "long", "very_short", "very_long"],
        ),
        # RANDOM
        SearchToggleOption(
            query="random",
            name="#RANDOM",
            type="toggle",
            default=False,
        ),
    ]
)
