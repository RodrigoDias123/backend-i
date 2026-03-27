from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ErrorDetail(BaseModel):
    field: str
    message: str


class ErrorResponse(BaseModel):
    error: str
    message: str
    details: list[ErrorDetail] = Field(default_factory=list)


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Human-readable item name.")
    description: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional item description.",
    )


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)

    @model_validator(mode="after")
    def validate_at_least_one_field(self) -> "ItemUpdate":
        if self.name is None and self.description is None:
            raise ValueError("At least one field must be provided.")
        return self


class Item(ItemBase):
    id: int = Field(..., ge=1, description="Unique item identifier.")