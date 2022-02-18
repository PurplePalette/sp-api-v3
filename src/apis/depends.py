from fastapi import Body, Depends, Form, Path, Query
from src.database.db import get_db
from src.security_api import get_current_user, get_current_user_optional

dependsLocalization = Query(
    "ja",
    description="It localizes response items if possible",
    min_length=1,
    max_length=50,
)
dependsPage = Query(0, description="Filters contents using pagination", ge=0, le=10000)
dependsKeywords = Query(
    "",
    description="Filter contents by specified keyword, in title and description",
    min_length=1,
    max_length=300,
)
dependsSort = Query(
    "updated_time",
    description="It sorts contents using specified method",
    max_length=20,
)
dependsOrder = Query(
    "desc",
    description="It specifies sort direction",
    min_length=0,
    max_length=10,
)
dependsStatus = Query(
    "any",
    description="Filters contents using specified status",
    min_length=1,
    max_length=20,
)
dependsAuthor = Query(
    "any",
    description="Filter contents by specified author",
    min_length=0,
    max_length=100,
)
dependsRatingMin = Query(
    1, description="Filter level contents by minimum rating", ge=1, le=100
)
dependsRatingMax: int = Query(
    50, description="Filter level contents by maximum rating", ge=1, le=100
)
dependsGenre = Query(
    "any", description="Filter contents by specified genre", min_length=0, max_length=20
)
dependsLength = Query(
    "any",
    description="Filter level contents by specified length",
    min_length=0,
    max_length=10,
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
dependsPath = Path(None, description="")
dependsBody = Body(None, description="")
dependsForm = Form(None, description="")
dependsDatabase = Depends(get_db)
dependsFirebase = Depends(get_current_user)
dependsFirebaseOptional = Depends(get_current_user_optional)
