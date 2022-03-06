from fastapi import Body, Depends, File, Form, Header, Path, Query
from src.database.db import get_db
from src.security_api import get_current_user, get_current_user_optional

MAXIMUM_FILESIZE = 50 * 1024 * 1024  # 50 MB

dependsMaximumFileSize = Header(..., lt=MAXIMUM_FILESIZE)


async def valid_content_length(content_length: int = dependsMaximumFileSize) -> int:
    return content_length


dependsLocalization = Query(
    "ja",
    description="It localizes response items if possible",
    min_length=1,
    max_length=50,
)
dependsPage = Query(0, description="Filters contents using pagination", ge=0, le=10000)
dependsKeywords = Query(
    "any",
    description="Filter contents by specified keyword, in title and description",
    min_length=1,
    max_length=300,
)
dependsSort = Query(
    0, description="It sorts contents using specified method", ge=0, le=50
)
dependsOrder = Query(0, description="It specifies sort direction", ge=0, le=50)
dependsStatus = Query(
    0, description="Filters contents using specified status", ge=0, le=50
)
dependsAuthor = Query(
    "any",
    description="Filter contents by specified author",
    min_length=1,
    max_length=100,
)
dependsRatingMin = Query(
    1, description="Filter level contents by minimum rating", ge=1, le=100
)
dependsRatingMax: int = Query(
    50, description="Filter level contents by maximum rating", ge=1, le=100
)
dependsGenre = Query(0, description="Filter contents by specified genre", ge=0, le=50)
dependsLength = Query(
    0, description="Filter level contents by specified length", ge=0, le=50
)
dependsRandom = Query(
    0,
    description="It shuffles response list",
    ge=0,
    le=1,
)
dependsAddBackground = Body(None, description="Add background request")
dependsAddEffect = Body(None, description="Add effect request")
dependsAddParticle = Body(None, description="Add particle request")
dependsAddUser = Body(None, description="Add user request")
dependsStartSession = Body(None, description="Start session request")
dependsPath = Path(None, description="")
dependsBody = Body(None, description="")
dependsFile = File(None, description="")
dependsForm = Form(None, description="")
dependsDatabase = Depends(get_db)
dependsFirebase = Depends(get_current_user)
dependsFileSize = Depends(valid_content_length)
dependsFirebaseOptional = Depends(get_current_user_optional)
