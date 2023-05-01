from pydantic import BaseModel


class TitleBasic(BaseModel):
    id: str
    title_number: str
    title_class: str


class Title(TitleBasic):
    content: str