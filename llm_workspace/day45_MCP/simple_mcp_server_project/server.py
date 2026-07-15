from __future__ import annotations
from datetime import datetime
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from pip._internal.utils import retry

BASE_DIR = Path(__file__).resolve().parent.parent
MANUAL_FILE = BASE_DIR / "data" / "manual.txt"
mcp = FastMCP("Simple MCP Server")

@mcp.tool()
def hello(name: str) -> str:
    """이름을 전달받아서 인사말을 만들어서 반환합니다.
    Args:
         name: 인사말에 포함할 사용자 이름입니다.

    Returns:
        사용자 이름이 포함된 인사말 문자열입니다.
    """
    return f"안녕하세요. {name}님!"


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    숫자 2개를 전달받아서 더하기 한 결과를 반환합니다.
    Args:
        a: 첫번째 숫자
        b: 두번째 숫자
    Returns:
        a와 b를 더한 숫자
    """
    return a + b

@mcp.tool()
def get_current_time() -> datetime:
    """
    MCP 서버가 실행중인 컴퓨터의 현재 날짜와 시간을 반환합니다.
    return:
        yyyy-mm-dd hh:mm:ss 형식
    """
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

@mcp.resource("manual://guide")
def read_manual() -> str:
    """
    data/manual.txt 파일의 내용을 읽어 mcp resource로 제공합니다 .
    :return: 사용설명서 파일의 전체 내용 문자열입니다.
    """
    if not MANUAL_FILE.exists():
        return "manual.txt 파일을 찾읈수없습니다. "

    return MANUAL_FILE.read_text(encoding="utf-8")

@mcp.resource("profile://{name}")
def get_profile(name: str) -> str:
    """
    URL에 포함된 이름으로 간단 사용자 프로필을 생성합니다.
    args:
        name: profile://url에 포함된 사용자 이름
    :return:
        이름이 포함된 간단 르포필 문자열
    """
    return (
        f"사용자이름: {name}, 학습주제: MCP SERVER"
    )

@mcp.prompt()
def summarize_document(topic: str, style:str = "쉽게") -> str:
    """
    특정 주제 topic을 요약하도록 LLM에 전달할 prompt 생성
    args:
    :param topic: 요약할 주제
    :param style: 요약 문체
    :return: LLM에 전달할 최종 prompt 문자열
    """
    return (
        f"다음주제를 {style} 설명하세요. 핵심개념, 동작과정, 간단한 예제를 포함하세요. 주제: {topic}"
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")