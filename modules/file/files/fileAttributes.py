from pydantic import BaseModel, Field
from typing import Optional
from modules.file.dirs.configDir import ConfigDir

class FileAttributes(BaseModel):
	filename: str
	content: Optional[str] = ""
	kind: Optional[ConfigDir] = Field(ConfigDir.rule, title = "Kind of file")