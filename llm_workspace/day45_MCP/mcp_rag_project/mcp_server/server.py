from mcp.server.fastmcp import FastMCP

from app.routers.schemas import RagRequest
from mcp_server.resources import document_catalog, runtime_config
from mcp_server.tools import (
    add_numbers as add_numbers_tool,
    ask_rag as ask_rag_tool,
    list_files as list_files_tool,
    list_mysql_knowledge as list_mysql_knowledge_tool,
    read_file as read_file_tool,
    rebuild_index as rebuild_index_tool,
    search_documents as search_documents_tool,
)

mcp = FastMCP("MCP RAG Assistant")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    return add_numbers_tool(a, b)


@mcp.tool()
def ask_rag(request: RagRequest) -> dict:
    return ask_rag_tool(request)


@mcp.tool()
def list_files() -> list[str]:
    return list_files_tool()


@mcp.tool()
def mysql_knowledge() -> list[dict]:
    return list_mysql_knowledge_tool()


@mcp.tool()
def read_file(request: FileReadRequest) -> dict:
    return read_file_tool(request)


@mcp.tool()
def rebuild_index() -> dict:
    return rebuild_index_tool()


@mcp.tool()
def search_documents(query: str) -> list[dict]:
    return search_documents_tool(query)


@mcp.resource("config://runtime")
def config_resource() -> str:
    return runtime_config()


@mcp.resource("docs://catalog")
def docs_resource() -> str:
    return document_catalog()

@mcp.prompt()
def grounded_rag_prompt(question:str) -> str:
    return (
        f"먼저 vector_search 또는 rag_question_answer Tool을 사용하세요, 검색결과에 포함된 문서만 근거로 답하세요, "
        f"확인할 수 없는 내용은 추측하지마세효, 사용자질문 {question}"
    )

if __name__ == "__main__":
    mcp.run(transport="stdio")

