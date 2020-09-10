from pydantic import BaseModel, Field
from typing import Optional
from modules.file.dirs.dir import Dir

class FileAttributes(BaseModel):
	filename: str
	content: Optional[str] = ""
	kind: Optional[Dir] = Field(Dir.rule, title = "Kind of file")