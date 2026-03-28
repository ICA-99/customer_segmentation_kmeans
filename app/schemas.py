from pydantic import BaseModel, Field


class CustomerInput(BaseModel):
    age: float = Field(..., example=25)
    income: float = Field(..., example=50)
    spending: float = Field(..., example=70) 