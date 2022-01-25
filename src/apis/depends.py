from fastapi import Body, Depends, Form, Path, Query
from src.database.db import get_db
from src.security_api import get_current_user

dependsLocalization = Query(
    None,
    description="It localizes response items if possible",
    min_length=1,
    max_length=50,
)
dependsPage = Query(
    1, description="It filters items for pagination if possible", ge=0, le=10000
)
dependsKeywords = Query(
    None,
    description="It filters items for search from list if possible",
    min_length=1,
    max_length=300,
)
dependsPath = Path(None, description="")
dependsBody = Body(None, description="")
dependsForm = Form(None, description="")
dependsDatabase = Depends(get_db)
dependsFirebase = Depends(get_current_user)
