from pydantic import BaseModel, Field

class CustomerInput(BaseModel):
    # We use Field to add validation boundaries and examples for documentation
    recency: int = Field(
        ..., 
        description="Number of days since the customer's last purchase", 
        ge=1
    )
    frequency: int = Field(
        ..., 
        description="Total number of purchases the customer made", 
        ge=0
    )
    monetary: float = Field(
        ..., 
        description="Total amount the customer has spent", 
        gt=0.0
    )

    class Config:
        # This provides a sample payload in FastAPI's automatic documentation (Swagger UI)
        json_schema_extra = {
            "example": {
                "recency": 30,
                "frequency": 5,
                "monetary": 5000.0
            }
        }

class PredictionOutput(BaseModel):
    cluster: int
    segment_name: str