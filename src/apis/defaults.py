from fastapi import Body, Path, Query

defaultPath = Path(None, description="")
defaultBody = Body(None, description="")
defaultLocalization = Query(
    None,
    description="It localizes response items if possible",
    min_length=1,
    max_length=50,
)
defaultPage = Query(
    1, description="It filters items for pagination if possible", ge=0, le=10000
)
defaultKeywords = Query(
    None,
    description="It filters items for search from list if possible",
    min_length=1,
    max_length=300,
)
