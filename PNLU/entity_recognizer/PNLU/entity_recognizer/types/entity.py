from pydantic import BaseModel, Field, validator


class Entity(BaseModel):
    token: str = Field(..., description="token from the sentence")

    @validator("token")
    def token_must_not_contain_space(cls, v):
        if " " in v:
            raise ValueError("token must not contain a space")
        return v.title()
