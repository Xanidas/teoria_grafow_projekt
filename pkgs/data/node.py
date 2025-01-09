from pydantic import BaseModel, Field

class Node(BaseModel):
    label: str = Field(..., description="The label of the node")

    def __str__(self):
        return f"Node with label {self.label}"
