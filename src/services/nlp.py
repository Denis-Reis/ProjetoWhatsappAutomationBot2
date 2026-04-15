import language_tool_python

tool = language_tool_python.LanguageTool('pt-BR')

def fix_text(texto: str) -> str:
    return tool.correct(texto)